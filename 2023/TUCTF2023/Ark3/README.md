# Ark3 challenge
<p align="center">
  <img src="Attachments/Description.jpg" />
</p>


## FLAG:
`TUCTF{k3YCh41ns_AR3_sUp3r_c00L}`

## Solution

the first thing I did was to use `file meow` to figure out what I was up against. meow is an Keychain file, and my goal is to find a password stored in this file. I listened to the challenge suggestion, got from rockyou.txt all the words that have meow as a substring with grep and then used john the ripper to crack the hash generated by keychain2john. I found on github a tool that work with keychain file and i used this tool to recover the password with the flag.

```bash
keychain2john meow > meow_hash
cat rockyou.txt | grep meow > meow2
john -w=meow2 meow_hash
git clone https://github.com/n0fate/chainbreaker
cd chainbreaker
pip install -r requirements.txt
python3 -m chainbreaker m --dump-all --password coolcatmeow
```

