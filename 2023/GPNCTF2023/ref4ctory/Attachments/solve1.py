from pwn import *
p=process(['ncat','--ssl','ref4ctory-0.chals.kitctf.de','1337'])
f=['2*2', '2*5', '2*596112', '111871*341477', '268817*922069', '458843971*921759790997', '87*43']
p.recv()
for i in f:
 j=i.split("*")
 p.sendline(j[0].encode())
 p.sendline(j[1].encode())
 p.recv()

p.recv()