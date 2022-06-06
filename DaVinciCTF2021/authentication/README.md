# Authentication


## Description
```
Can you find a way to authenticate as admin?
```

## Target

`http://challs.dvc.tf:1337/`

## Objective

Login as admin and search for flag

## Difficulty/Points
simple/`10`

## Flag:
`dvCTF{!th4t_w4s_34sy!}`

# Challenge
We had a simple login form. We doesn't know anything

# Solution
We had to make the login condition true in order to log in.
Usually the correct credentials are entered to log into an account and a user must find the "right" ones.
if the condition consists of:
A and B
we can decompose it into
A = (a' or b') and B = (a'' or b'') with b 'and b' 'tautologies
if conditions b' and b'' are true then the whole expression A and B is true.
But we can do even better if we only use A, without the use of B trying to obscure it from the condition itself.
I tried to make a sql inection or in the form instead of the user I put admin and the password I put 'or 1 = 1; --
this strange syntax means character by character: we immediately close the password field with a quote making its content empty, then we add an OR and add something that is always true.
The rest is all closed and commented on because it is not needed. So the query being something like:

```
SELECT * FROM accounts WHERE username = '{username}' AND password = '{password}' 
```

let's substitute the user with admin and pass with the exact string 'or 1 = 1; - I make the query become

```
SELECT * FROM accounts WHERE username = 'admin' AND password = '' OR 1 = 1
```

once logged in as admin just inspect the html code and the flag is returned