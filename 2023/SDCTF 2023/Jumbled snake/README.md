# Jumbled snake
<p align="center">
  <img src="Attachments/Description.png" />
</p>

## FLAG:
`sdctf{U_unRav3led_tH3_sn3k!}`
## Solution
Analyzing the [source code](Attachments/jumble.py) provided by the challenge, we can see that the output file is the result of replacing each character, present in the `print_flag.py` file (unknown to us), with a charset found randomly from `string.printable`.

```python 
#! /usr/bin/env python3
# Need print_flag.py (secret) in the same directory as this file
import print_flag
import os
import secrets
import string

def get_rand_key(charset: str = string.printable):
    chars_left = list(charset)
    key = {}
    for char in charset:
        val = secrets.choice(chars_left)
        chars_left.remove(val)
        key[char] = val
    assert not chars_left
    return key

def subs(msg: str, key) -> str:
    return ''.join(key[c] for c in msg)

with open(os.path.join(os.path.dirname(__file__), 'print_flag.py')) as src, open('print_flag.py.enc', 'w') as dst:
    key = get_rand_key()
    print(key)
    doc = print_flag.decode_flag.__doc__
    assert doc is not None and '\n' not in doc
    dst.write(doc + '\n')
    dst.write(subs(src.read(), key))
```

However, what is interesting to note is that in the [output file](Attachments/print_flag.py.enc) a string taken directly from the `print_flag.py` file is inserted at the head. This information provides us with the starting point for solving this challenge.

The idea is to exploit the string known as a pattern to search within the output file so as to find part of the charset used. This is possible because this string, in order for it to be recognized as a `__doc__` attribute of an object, must be surrounded by triple quotes. 

So I created the following script to search for such pattern:

```python
def check_pos(v, tmp):
	value = tmp[v[0]]
	for i in range(len(tmp)):
		if tmp[i] == value and i not in v:
			return False 
	return True

def check_range(tmp, d):
	for v in d:
		if len(d[v]) != 1:
			if not check_pos(d[v], tmp):
				return False
	return True

def print_res(enc, partial_key):
	res = ""
	xx = []
	i = 0
	for x in enc:
		if x in partial_key:
			res += partial_key[x]
		else:
			res += "-"
			xx.append(i)
		i += 1
	print(res)
	if xx:
		print("\nPOSITION OF MISSING CHAR")
		print(xx)

doc = "{'the_quick_brown_fox_jumps_over_the_lazy_dog': 123456789.0, 'items':[]}"
to_be_replaced = doc.encode() + b"\n"
enc = open('print_flag.py.enc.true', 'rb').read().replace(to_be_replaced, b"")
# print(f"{enc = }")

d = {}
for i in range(len(doc)):
	if doc[i] not in d:
		d[doc[i]] = [i]
	else:
		d[doc[i]].append(i)
# print(d)

pattern = []
for i in range(len(enc) - 78):
	tmp = [x for x in enc[i:i+len(doc) + 6]]
	if tmp[0] == tmp[75] == tmp[1] == tmp[76] == tmp[2] == tmp[77]:
		if check_range(tmp[3:75], d):
			pattern = tmp
			print(f"Found pattern at index {i}: " + "".join(chr(x) for x in tmp) + "\n\n")

partial_key = {}
partial_key[pattern[0]] = '"'

for i in range(len(doc)):
	if doc[i] not in partial_key:
		partial_key[pattern[3:75][i]] = doc[i]

print("*---------------------*")
print(" PARTIAL DECODED TEXT")
print("*---------------------*")
print_res(enc, partial_key)
```

And the output produced is as follows:

```bash
└─$ python solve.py
Found pattern at index 347: 93 93 93 121 56 80 112 32 88 9 37 68 83 108 88 71 69 85 11 101 88 64 85 36 88 122 37 77 111 92 88 85 97 32 69 88 80 112 32 88 87 116 107 12 88 89 85 123 56 47 90 82 109 58 119 104 65 126 95 51 62 54 39 90 56 68 80 32 77 92 56 47 106 63 86 93 93 93


*---------------------*
 PARTIAL DECODED TEXT
*---------------------*
-- -usr-bin-env python3-import base64--coded_flag - "c2-jd--7--91bl-hdj-s---fd-gz-3-u-2shf---"--def reverse-s-:-    return "".join-reversed-s----def check--:-    """---_----_---_----_-----_---_-----_-----_---"""-    assert decode_flag.__doc__ is not -one and decode_flag.__doc__.upper--[2:45] -- reverse-check.__doc__---def decode_flag-code-:-    """{'the_quick_brown_fox_jumps_over_the_lazy_dog': 123456789.0, 'items':[]}"""-    return base64.b64decode-code-.decode----if __name__ -- "__main__":-    check---    print-decode_flag-coded_flag----

POSITION OF MISSING CHAR
[0, 1, 3, 7, 11, 23, 37, 38, 50, 55, 58, 59, 61, 62, 67, 71, 73, 74, 75, 78, 81, 83, 85, 90, 91, 92, 94, 95, 107, 109, 111, 130, 139, 141, 142, 143, 144, 154, 155, 157, 165, 166, 167, 169, 170, 171, 172, 174, 175, 176, 178, 179, 180, 181, 183, 184, 185, 186, 187, 189, 190, 191, 193, 194, 195, 196, 197, 199, 200, 201, 202, 203, 205, 206, 207, 211, 250, 284, 285, 293, 294, 303, 317, 318, 319, 335, 340, 342, 425, 453, 458, 466, 467, 468, 469, 482, 483, 496, 506, 507, 508, 518, 530, 541, 542, 543, 544]
```

But the output contains characters that do not fit into the partial charset found, for this reason those that could be known have been added by hand.

```python
partial_key[enc[0]] = "#"
partial_key[enc[1]] = "!"
partial_key[enc[3]] = "/"
partial_key[enc[23]] = "\n"
partial_key[enc[50]] = "="
partial_key[enc[107]] = "("
partial_key[enc[109]] = ")"
partial_key[enc[250]] = "N"

print("\n*---------------------*")
print(" PARTIAL DECODED TEXT")
print("*---------------------*")
print_res(enc, partial_key)
```

And the output produced is as follows:

```bash
*---------------------*
 PARTIAL DECODED TEXT
*---------------------*
#! /usr/bin/env python3
import base64

coded_flag = "c2-jd--7--91bl-hdjNs---fd-gz-3Nu-2shf-=="

def reverse(s):
    return "".join(reversed(s))

def check():
    """---_----_---_----_-----_---_N----_-----_---"""
    assert decode_flag.__doc__ is not None and decode_flag.__doc__.upper()[2:45] == reverse(check.__doc__)

def decode_flag(code):
    """{'the_quick_brown_fox_jumps_over_the_lazy_dog': 123456789.0, 'items':[]}"""
    return base64.b64decode(code).decode()

if __name__ == "__main__":
    check()
    print(decode_flag(coded_flag))
-

POSITION OF MISSING CHAR
[55, 58, 59, 61, 62, 67, 73, 74, 75, 78, 81, 85, 90, 165, 166, 167, 169, 170, 171, 172, 174, 175, 176, 178, 179, 180, 181, 183, 184, 185, 186, 187, 189, 190, 191, 194, 195, 196, 197, 199, 200, 201, 202, 203, 205, 206, 207, 544]
```

The output produced is much clearer and in fact we can see that, in the `check` method, the `reverse` method is called and part of the string previously used as a pattern is passed. So I got the last characters that were missing from the charset found up to now.

```python
def reverse(s):
    return "".join(reversed(s))

rev = doc.upper()[2:45]
check_doc = reverse(rev)
print(check_doc)

j = 0
for i in range(165, 208):
	partial_key[enc[i]] = check_doc[j]
	j += 1

print("\n*---------------------*")
print("     DECODED TEXT")
print("*---------------------*")
print_res(enc, partial_key)
```

The output produced represents the `print_flag.py` program which, once executed, gives the flag (written in base64).

```bash
REVERSED STRING: GOD_YZAL_EHT_REVO_SPMUJ_XOF_NWORB_KCIUQ_EHT

*---------------------*
     DECODED TEXT
*---------------------*
#! /usr/bin/env python3
import base64

coded_flag = "c2RjdGZ7VV91blJhdjNsZWRfdEgzX3NuM2shfQ=="

def reverse(s):
    return "".join(reversed(s))

def check():
    """GOD_YZAL_EHT_REVO_SPMUJ_XOF_NWORB_KCIUQ_EHT"""
    assert decode_flag.__doc__ is not None and decode_flag.__doc__.upper()[2:45] == reverse(check.__doc__)

def decode_flag(code):
    """{'the_quick_brown_fox_jumps_over_the_lazy_dog': 123456789.0, 'items':[]}"""
    return base64.b64decode(code).decode()

if __name__ == "__main__":
    check()
    print(decode_flag(coded_flag))
```