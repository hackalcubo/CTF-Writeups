# Playing with xor

## Challenge Author(s):
`NoobMaster`

## Description:
Playing with xor is fun!

## FLAG:
`n00bz{pl4y1ng_w1th_x0r_m0r3_l1k3_pl4y1ng_w1th_f1r3}`
#
## Solution
After downloading the [challenge](challenge.py) file, we saw that it was simple and it was enough to obtain the key through the plain flag part and then the flag could be obtained.

The script used is the following:
```python
flag = b"n00bz{p"
enc = b"_\x03\x03U\x11\x1e\t]\x07J\x06\x05\x02&F\x02G_4\x1dICl^\x07\x19V&]\x02X\x044\x15\x15\x05J\x02Y\x0c:\x0e\x00G[h\rT\x0b\x02N"

key = bytes([a ^ b for a, b in zip(enc, flag)])
flag = "".join([chr(c ^ key[i % len(key)]) for i, c in enumerate(enc)])

print(f"[+] FLAG: {flag}")
```
