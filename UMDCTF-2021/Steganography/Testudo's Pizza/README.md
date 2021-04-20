# Testudo's Pizza

## Challenge Author:
`sydocon`

## Description:
`My local pizzeria is trying out a new logo that is bringing in a lot of new customers. I think something fishy is going on. What are they doing?`

The following `hiddenmsg.jpg` image was provided:

![image](https://user-images.githubusercontent.com/80971089/115423534-33567000-a1fe-11eb-933b-9ca8cd341fc4.png)

## Difficulty/Points: 
`100 points`

## Flag:
`UMDCTF-{W3_ar3_th3_b3st_P1ZZ3r1a}`


# Solution
I used the following command in order to find the string `UMDCTF` and eventually the flag:

`strings hiddenmsg.jpg | grep UMDCTF`

obtaining

`\f0\fs24 \cf0 \'93UMDCTF-{W3_ar3_th3_b3st_P1ZZ3r1a}\'94}` 
