
# Snek

### Challenge Description
Points: `100`
Descr: `No step on snek`

### Writeup
First of all I have executed `file snek` and it returned `python 3.7 byte-compiled`
So i've used [decompyle3](https://github.com/rocky/python-decompile3) in order to retrieve the source code.
Reading the decompiled source file I've found this:

```
self.decrypt = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 95, 82, 83, 123, 97, 108, 108, 95, 104, 105, 36, 36, 95, 97, 110, 100, 95, 110, 48, 95, 98, 105, 116, 51, 125]
```

We can instantly notice that this array contains numbers that seem to represent characters in ASCII so we can just print all of this in char using 
`for x in self.decrypt: print(chr(x))` 
and at the end of string generated we have the flag:
`RS{all_hi$$_and_n0_bit3}`
