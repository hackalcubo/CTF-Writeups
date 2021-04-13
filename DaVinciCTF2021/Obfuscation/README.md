# Obfuscation

## Description
```
My password is my secret. You will never find it...
To validate this chall, please enter the secret code as the flag.
```

## Target

`http://challs.dvc.tf:5555/`

## Objective

Decrypt the strange JS and get the flag

## Difficulty/Points
simple/`10`

## Flag:
`dvCTF{1t_is_n0t_4_secr3t_4nym0r3}`

# Challenge
a web page with html, js, css code is provided which can be inspected by browser

# Solution
inspecting the source code of the web page (right click -> inspect/analyze element) there was a strange JS.
If you pay attention to the source there was a string URIencoded like %01%02%03.
This style of encoding is adopted by browsers to encode special characters.
If you use ```decodeURI("%64%76%43%54%46%7b%31%74%5f%69%73%5f%6e%30%74%5f%34%5f%73%65%63%72%33%74%5f%34%6e%79%6d%30%72%33%7d")``` you get the flag.
if you want to do more, i can suggest you these two tools to de-obfuscate the JS -> https://beautifier.io/ and https://www.dcode.fr/javascript-unobfuscator
you can simply pasted the code into this 2 tool and the JS 