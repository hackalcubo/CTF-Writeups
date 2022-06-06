# Speedrun1

## Target:
`challengers.ctfd.io:30025`

## Objective
modify the cookie to get the "user 1" page

## Difficulty/Points
simple/`50`

## Flag:
`UDCTF{d0nt_r0ll_your_0wn_s3ssions}`

# Challenge
The challenge comes with a very simple textual content, it is a static html page

# Solution
this site was presented with a very simple static page with written "hello user 2" and that's it.
I started my backend analysis or I had to understand what kind of technology is behind the page.
I tried to parse the url by adding parameters like /? User = 1, / login, / home, /../flag.txt and so on.
Later out of pure curiosity I tried to open the developer console by right clicking and then inspecting and I saw that a cookie was shown in the network tab.
The cookie was obviously encoded in something weird like c81e728d9d4c2f636f067f89cc14862c
What can it be? 
The thing that helped me was checking this output in detail. It has all small letters, numbers, is about 32 characters long.
These are all elements that narrow the circle of probable algorithms used to encode it.
For more security, you can use an online tool to see how good it looks like an output from that algorithm -> https://crackstation.net/ 
and a tool to do your own string encodings -> https://gchq.github.io/CyberChef/
I found that maybe the cookie was an MD5 of character "2" and then I tried to change cookie using cyberchef to encode 1 with MD5.
I replaced the MD5 of 2 in the cookie of the page using mozilla -> developer console -> storage -> click on the cookie and I pasted MD5 of 1.
I updated the page and got the flag.