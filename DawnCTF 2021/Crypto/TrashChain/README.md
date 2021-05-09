# TrashChain
<p align="center">
  <img src=https://i.postimg.cc/zXxZyfwQ/1.jpg" />
</p>

## FLAG:
`DawgCTF{We1rd_RSA_2nd_Pre1m4g3_th1ng}`
#
## Solution
The challenge, as seen in the [source](trashchain.py), involves the creation of two chains with constraints. 
```python
 print("Welcome to TrashChain!")
 print("In this challenge, you will enter two sequences of integers which are used to compute two hashes. If the two hashes match, you get the flag!")
 print("Restrictions:")
 print("  - Integers must be greater than 1.")
 print("  - Chain 2 must be at least 3 integers longer than chain 1")
 print("  - All integers in chain 1 must be less than the smallest element in chain 2")
 print("Type \"done\" when you are finished inputting numbers for each chain.")
```
After their construction, 2 hashes are calculated through the use of modular arithmetic. 
```python
# Hash function
def H(val, prev_hash, hash_num):
    return (prev_hash * pow(val + hash_num, B, A) % A)
```

The resolution of this challenge is based on this idea as it was decided to ensure that the module was 0 used directly "A" and a multiple of its own to respect the constraints.

To do this the following python script was used.
```python
from pwn import *

if args.REMOTE:
    p = remote("umbccd.io", 3100)
else:
    p = process("./trashchain.py")

# Hash constant
A = 340282366920938460843936948965011886881

# chain 1
p.sendlineafter("> ", str(A - 1))
p.sendlineafter("> ", "done")

# chain 2
p.sendlineafter("> ", str(A*2 - 1))
p.sendlineafter("> ", str(A*2 - 1))
p.sendlineafter("> ", str(A*2 - 1))
p.sendlineafter("> ", str(A*2 - 1))
p.sendlineafter("> ", "done")

print(p.recvline().decode().strip())
print(p.recvline().decode().strip())
p.interactive()
```
