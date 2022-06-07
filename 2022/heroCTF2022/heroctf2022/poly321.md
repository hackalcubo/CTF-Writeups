![](./assets/images/logo.webp)



        
            
# Poly321



## Challenge Author(s):
xanhacks

## Description:
An unskilled mathematician has created an encryption function. Can you decrypt the message ?

## File:
    #!/usr/bin/env python3

    FLAG = "****************************"

    enc = []
    for c in FLAG:
        v = ord(c)

        enc.append(
            v + pow(v, 2) + pow(v, 3)
        )

    print(enc)

    """
    $ python3 encrypt.py
    [378504, 1040603, 1494654, 1380063, 1876119, 1574468, 1135784, 1168755, 1534215, 866495, 1168755, 1534215, 866495, 1657074, 1040603, 1494654, 1786323, 866495, 1699439, 1040603, 922179, 1236599, 866495, 1040603, 1343210, 980199, 1494654, 1786323, 1417584, 1574468, 1168755, 1380063, 1343210, 866495, 188499, 127550, 178808, 135303, 151739, 127550, 112944, 178808, 1968875]
    """


## Objective:
Decrypt the message using bruteforce.


## Flag:
`Hero{this_is_very_weak_encryption_92835208}`
# 

# Solution
<code>

    import string

    enc = [378504, 1040603, 1494654, 1380063, 1876119, 1574468, 1135784, 1168755, 1534215, 866495, 1168755, 1534215, 866495, 1657074, 1040603, 1494654, 1786323, 866495, 1699439, 1040603, 922179, 1236599, 866495, 1040603, 1343210, 980199, 1494654, 1786323, 1417584, 1574468, 1168755, 1380063, 1343210, 866495, 188499, 127550, 178808, 135303, 151739, 127550, 112944, 178808, 1968875]


    for e in enc:
        for c in string.printable:
            v = ord(c)
            test = v + pow(v, 2) + pow(v, 3)
            if test == e:
                print(c, end='')
                break
</code>