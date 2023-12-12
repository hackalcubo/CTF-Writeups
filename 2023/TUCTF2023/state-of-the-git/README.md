# State of the Git challenge
<p align="center">
  <img src="Attachments/Description.jpg" />
</p>


## FLAG:
`TUCTF{73rr4f0rm_S7A73-1y_53cr375}`

## Solution

the challenge looks like a mixture of lots of files. As soon as I did a printout of all the files to see them 1 by 1 I noticed a password field encoded in base64. Double equals suggested it to me at the end. Of course I could not be certain of this claim, so it is obvious that I had to try the base64 decoding command first to see if what I thought was a correct assumption. I eventually found that I was right, and the flag was indeed this password decoded by base64.

```
cat *;
echo  VFVDVEZ7NzNycjRmMHJtX1M3QTczLTF5XzUzY3IzNzV9Cg== | base64 -d;
```

