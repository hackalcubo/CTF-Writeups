from pwn import *

r = remote('on-time-production-0.chals.kitctf.de', 7331)

server_response = r.recv()[:-1]
log.info(f"{server_response = }")

len_flag = len(server_response) // 2
log.info(f"{len_flag = }")

flag = xor(server_response[:len_flag], server_response[len_flag:]).decode()
log.success(f"{flag = }")
r.close()