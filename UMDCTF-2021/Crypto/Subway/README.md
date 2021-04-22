# Subway

## Challenge Author:
`Shricubed`

## Description:
This may seem like a regular substitution cipher, but it doesn't seem to work with a regular alphabet.

It's given the following `cypher.txt` file:
```
W74 5o06 8v XP32W5-{qdw_0_vepsog_vx1vwewxwedq_w7ev_wepg}
```
## Hint:
what non-alphabetic characters does the ciphertext have?

## Difficulty/Points: 
`225 points`

## Flag:
`UMDCTF-{n0t_a_s1mpl3_subst1tut10n_th1s_t1m3}`


# Solution
It's a substitution cypher which uses letters and digits from 0 to 9. We guessed some substitutions using the known flag format, and with a bit of intuition, we recostructed the whole cypher. The following python script automatize the decrypting process :

```python
s  = '0123456789abcdefghijklmnopqrstuvwxyz {-_}'
s2 = 'abcdefghijxyz0123456789klmnopqrstuvw {-_}'
flag = 'W74 5o06 8v XP32W5-{qdw_0_vepsog_vx1vwewxwedq_w7ev_wepg}'
flag_lower = flag.lower()
res = ''
for c in flag_lower:
        res += s2[s.find(c)]
print(res)             
```

The output is:

`the flag is umdctf-{n0t_a_s1mpl3_subst1tut10n_th1s_t1m3}` 