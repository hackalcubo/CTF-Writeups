# go2win
## DESCRIPTION: 
`One of the easiest pwn in this ctf, should be an easy go!`

[Dowload binary here](https://we.tl/t-RVhmBMETdp)
[Or Here](https://drive.google.com/file/d/18BU8bbWeTHZ9SM5FNsRxCG215-okxTTX/view?usp=sharing)

`nc 92.246.89.201 10003`

### Author: 
`@fracchetto`

## FLAG:
`hctf{g0_pWn_theM-4ll}`

## Solution
After downloading the [file](Attachments/go2win) and decompiling (using [Ghidra](https://ghidra-sre.org/)), let's analyze the `main`.

```c
void main.main(void)

{
  undefined8 local_10;
  
  while (&stack0x00000000 <= CURRENT_G.stackguard0) {
    runtime.morestack_noctxt.abi0();
  }
  local_10 = 0x4141414141414141;
  runtime.makeslice(&uint8___runtime._type,0x200,0x200);
  bufio.(*Reader).Read(main.reader,&local_10,0x200,0x200);
  if ((char)local_10 == '*') {
    main.win();
  }
  return;
}
```

What you notice is that you just need to send `*` to get the flag. 

```bash
└─$ nc 92.246.89.201 10003
*
hctf{g0_pWn_theM-4ll}
```