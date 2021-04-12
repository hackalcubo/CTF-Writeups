# Fleshwound

# Challenge Description
```Tis but a....```

# Writeup
The challenge gave us a json file obfuscated, so first thing we did was to de-obfuscate it and read its contents. Inside we found many references to flag, various words and pieces of the real flag which starts with RS{..}.
The string ```scratch?``` caught my attention so I searched if the json file could be used in Scratch and it could, so I loaded it up. We have two sprites with some actions associated and the main stage, running it the drum sprite starts reading the flag but gets "distracted" by being sent to another "function" by the broadcast thingy.
Focusing on the drum we can change "distract me" to "finish" and we get the rest of the flag ```RS{eeee_whats_th@t_scratch?}```
![alt text](https://raw.githubusercontent.com/hackalcubo/CTF-Writeups/main/ritsec2021/revbin/fleshwound/final_stage.png)
