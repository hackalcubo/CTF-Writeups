# Cookie Clicker

## Author: awawa

## Description

I wanna reach a million cookies!

## Solution

The challenge was solved without reversing anything, there are probably multiple ways of solving it.

Opening the main executable `cookieclicker`, it presents itself with this user interface.

![](./cookie.png)

If we click the cookie we get cookies and gold, the goal is to reach a million cookies probably, we can upgrade how many cookies we get per click by going in the shop and buying the relative upgrade, but the more interesting part is the automatic workers, buying at least one of them gives us the ability to passively gain money.

Now the interesting part, if we close the program and reopen it, we get a popup saying that we get the amount of money that the workers made while the program was closed, guessing the method, it probably just checks the system time since the last time we opened the program, using an utility called `faketime` we can change the perceived application time without changing the system time, we can run it by doing `faketime -f '+2y' ./cookieclicker` in order to go forward by two yeas, by doing so the program will tell us that we made a lot of gold and cookies and then it will print the flag in stdout `bjAwYnp7WXVtbXlDMDBraWV6fQ==` the flag is base64 encoded, decoding it gets us `bjAwYnp7WXVtbXlDMDBraWV6fQ==`.

There are probably other ways of solving the challenge, in the settings there is a textbox called cheat code, we could also try to modify the savefiles.
