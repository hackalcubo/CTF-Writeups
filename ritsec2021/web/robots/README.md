# Robots

## Challenge Author(s):
`f1rehaz4rd`

## Description
```
Robots are taking over. Find out more.
```

## Target

`34.69.61.54:5247`

## Objective

Find the flag using the path traversal technique in order to search for the right resource that has the flag

## Difficulty/Points
simple/`100`

## Flag:
`RS{R0bots_ar3_b4d}`

# Challenge
The page have 1 picture,some description and some CSS to beautify the page.

# Solution
There aren't forms to submit data, for this reason i start to search information capture information by starting to read the html code at my disposal.
I did not find anything relevant and so I started reading well what was written and I tried to put something in the url that could be connected to the flag.
I immediately tried to insert flag.txt (http://34.69.61.54:5247/flag.txt) in the url which redirected to an encoded string that hide a message that was not the flag.
So thanks to a correct observation of a teammate of mine it was discovered that the right file to view was the robots.txt (http://34.69.61.54:5247/robots.txt) file and there is a particular encoded entry in them
`
Allow: / flag / UlN7UjBib3RzX2FyM19iNGR9
`
decoding it you get the flag -> https://www.base64decode.org/ (base64 decoding tool)