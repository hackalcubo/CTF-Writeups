# Task

![image](https://user-images.githubusercontent.com/80971089/114400371-2d2f1680-9ba2-11eb-994b-5918ea72b9a6.png)

![image](https://user-images.githubusercontent.com/80971089/114400387-30c29d80-9ba2-11eb-84e1-1afd22bdc3d0.png)

# Solution

This challenge is also about this suspicious girl (read [previous chall writeup](https://github.com/hackalcubo/CTF-Writeups/blob/main/ritsec2021/Intel/Music%20Signs/README.md)). I spent some time digging through her social media, music tastes, without realising I had the best piece of information right in front of my eyes since the beginning:

![image](https://user-images.githubusercontent.com/80971089/114400695-85feaf00-9ba2-11eb-950e-31c31205261a.png)

In the previous challenge, I focused on her Twitter bio with the Spotify link but I didn’t investigate what was the string below it. At first, I also didn’t notice the “money” emoji right there, that’s kind of suspicious.
So I googled that string obtaining 1 result:

![image](https://user-images.githubusercontent.com/80971089/114400843-aaf32200-9ba2-11eb-9248-591296f07b21.png)

That's a bitcoin wallet! Opening this link, we can find that Claire’s wallet exchanged money with another wallet:

![image](https://user-images.githubusercontent.com/80971089/114400926-be9e8880-9ba2-11eb-9df4-1ea40d58273d.png)

Googling the wallet on the right `1FsXnPtqRtWs89YtDhFdoZpyt2LUWJDfW1`, we can find an interesting result:

![image](https://user-images.githubusercontent.com/80971089/114401459-3a98d080-9ba3-11eb-8075-ffc607f37f6e.png)

The third [result](https://finance.ackaria.xyz/) seems interesting, let's find out more:

![image](https://user-images.githubusercontent.com/80971089/114401643-687e1500-9ba3-11eb-9452-3851b428d035.png)

![image](https://user-images.githubusercontent.com/80971089/114401663-6f0c8c80-9ba3-11eb-8ef3-c1f258956b1c.png)

This means she’s definitely interacting with the *Republic of Ackaria*, since the flag:

`RS{Ackaria}`
