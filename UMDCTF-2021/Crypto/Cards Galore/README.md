# Cards Galore

## Challenge Author(s):
`lisichka`

## Description:
[![1.png](https://i.postimg.cc/0y9xPTQ5/1.png)](https://postimg.cc/1f7bKYwb)

The following `cards.png` image was provided:

[![cards.png](https://i.postimg.cc/j57Bzc5k/cards.png)](https://postimg.cc/9Rcx2GyG)

## Difficulty/Points: 
`707 points`

## Flag:
`UMDCTF-{thanks_for_sorting_my_cards}`
# 

# Solution

We found this [cipher](https://www.codewars.com/kata/59c2ff946bddd2a2fd00009e) based off of playing cards.

At first we tried decoding manually, noticing that decoding the first row of cards we were obtaining
`HVBOYG`, and that decoding it with ROT14 cipher we could obtain the string `THNAKS`.

After some adjustments (such as exchanging spades and diamonds in order to obtain the right order), this was the final script to decrypt the cards in the picture and obtain the flag:

```
from string import ascii_lowercase

a = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
b = ["C", "S", "H", "D"]

n = ascii_lowercase[:13]
m = ascii_lowercase[13:]

diz = {}
count = 1
for _ in b:
    v = 0
    for _1 in a:
        if count <= 2:
            diz[_1 + _] = n[v]
        else:
            diz[_1 + _] = m[v]
        v += 1
    count += 1
#print(diz)

def rot14(s, d):
    rot = ""
    for c in s:
        if c != "_":
            rot += d[c]
        else:
            rot += c
    return rot

def rotdiz():
    ret = {}
    for i in range(len(ascii_lowercase)):
        ret[ascii_lowercase[(14+i)%len(ascii_lowercase)]] = ascii_lowercase[i]
    return ret

first_row = ["8C", "9H", "2D", "2S", "QH", "7C"]
second_row = ["7H", "3S", "6C"]
third_row = ["7S", "3C", "6C", "8S", "TH", "2C", "8H"]
fourth_row = ["AC", "KS"]
fifth_row = ["4D", "2H", "6C", "5H", "7C"]
flag = ""
for _ in first_row:
    flag += diz[_]
flag += "_"
for _ in second_row:
    flag += diz[_]
flag += "_"
for _ in third_row:
    flag += diz[_]
flag += "_"
for _ in fourth_row:
    flag += diz[_]
flag += "_"
for _ in fifth_row:
    flag += diz[_]

print(flag)

d = rotdiz() 
#print(d)
print(rot14(flag, d))
```

Running this script, the result is:
```
hvobyg_tcf_gcfhwbu_am_qofrg
thanks_for_sorting_my_cards
```
