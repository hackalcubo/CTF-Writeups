# PikCha

## Target:

## Objective
increment the counter 0/500 with the correct input

### Difficulty/Points
Points:`241`

# Flag
`UMASS{G0tt4_c4tch_th3m_4ll_17263548}`

# Challenge
The html it had a small form with an input, a button and above it was a picture of some pokemon.

# Solution
I tried to send a very long series of inputs that I thought were malicious.
They are actually inputs like: <script> alert (1) </script>, document.write (flag), 'or 1 = 1; - and at the end the input <? Php echo hello;?> Went well, 
it incremented me a counter from 0/500 to 1/500. I created a JS script that automated everything for me.
after i used this JS, the flag was obtained