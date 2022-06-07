![](../assets/images/n00bzCTF_logo.png)



        
            
# Sneaky Png



## Challenge Author(s):
hacker_of_india

## Description:
This image is hiding something sneaky, find it! sneaky.png:/attachments/Sneaky_Png/sneaky.png

## Target:

https://ctf.n00bzunit3d.xyz/attachments/Sneaky_Png/sneaky.png

## Objective:
Found what is hidden in the given image.


## Difficulty/Points: 
500 pt

## Flag:
`n00bz{sn34ky_str1ngs_c0mm4nd5!}`
# 


# Solution
To extract hidden files in png, you can use: 

    binwalk -e sneaky.png

Then, in the folder of extracted files you can find:
- `29`
- `29.zlib`

To get the flag:

    strings 29.zlib
