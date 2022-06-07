![](./assets/images/logo.webp)



        
            
# Heist



## Challenge Author(s):
Log_s

## Description:
This new online bank is supposely unbreakable. They want us to prove it to the world. Here is the source code. It's messy, but simple. I can feel something's wrong, but I am not sure what.
Help me out will you ?

## Target:
   prog.heroctf.fr 7001

## Objective:
Buy the flag.


## Flag:
`Hero{ch3ck_4_n3g4t1v3s}`
# 

# Solution

If we passed it a negative number, the check that the entered value shouldn't be greater than the money available on the account is passed. 

So, let's pass `-100` and then you can buy the flag!