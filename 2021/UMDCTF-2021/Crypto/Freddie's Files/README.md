# Freddie's Files
<p align="center">
  <img src=https://i.postimg.cc/yYgF2Jqm/b.jpg" />
</p>

## FLAG:
`UMDCTF-{pHR3dd13_m3RcURY_w0uld_83_pR0uD}`
#
## Solution
After downloading the FreddiesFiles.zip file, we had to crack it as it was password protected. This was done thanks to [John The Ripper](https://github.com/openwall/john) with the following commands:
```console
asd@asd:~/Scrivania/UMDCTF$ zip2john FreddiesFiles.zip > tocrack
ver 2.0 efh 5455 efh 7875 FreddiesFiles.zip/ciphertext.txt PKZIP Encr: 2b chk, TS_chk, cmplen=91, decmplen=319, crc=293BF639
ver 1.0 efh 5455 efh 7875 FreddiesFiles.zip/key.txt PKZIP Encr: 2b chk, TS_chk, cmplen=44, decmplen=32, crc=9BC81710
ver 2.0 efh 5455 efh 7875 FreddiesFiles.zip/queen.txt PKZIP Encr: 2b chk, TS_chk, cmplen=6588, decmplen=16538, crc=2D86B827
NOTE: It is assumed that all files in each archive have the same password.
If that is not the case, the hash may be uncrackable. To avoid this, use
option -o to pick a file at a time.
asd@asd:~/Scrivania/UMDCTF$ john --wordlist=rockyou.txt tocrack
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
No password hashes left to crack (see FAQ)
asd@asd:~/Scrivania/UMDCTF$ john --show tocrack
FreddiesFiles.zip:qfreddie78::FreddiesFiles.zip:key.txt, ciphertext.txt, queen.txt:FreddiesFiles.zip

1 password hash cracked, 0 left
```

After recovering the password (*qfreddie78*) and unpacking the zip file, we extracted 3 files: [ciphertext.txt](FreddiesFiles/ciphertext.txt), [key.txt](FreddiesFiles/key.txt) and [queen.txt](FreddiesFiles/queen.txt).

We started to think what could be done with these 3 files and looking at the *key* we noticed that it was an MD5, so, at first, we saw if it was a known hash and we did not arrive at a result, then seeing the *queen* file we tried to crack the *key* (always with John The Ripper) using the *queen.txt* file as wordlist and we had a result.
```console
asd@asd:~/Scrivania/UMDCTF/FreddiesFiles$ john --wordlist=queen.txt key.txt --format=Raw-MD5
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 256/256 AVX2 8x3])
No password hashes left to crack (see FAQ)
asd@asd:~/Scrivania/UMDCTF/FreddiesFiles$ john --show --format=Raw-MD5 key.txt 
?:Buddy, you're a boy, make a big noise

1 password hash cracked, 0 left
```

At this point, doing the [xor](http://xor.pw/#) of the key with the ciphertext you get the flag!
<p align="center">
  <img src=https://i.postimg.cc/nLXXVGQR/c.jpg" />
</p>
