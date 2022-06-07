![](../assets/images/n00bzCTF_logo.png)



        
            
# So_snowy



## Challenge Author(s):
NoobMaster

## Description:

It's so snowy


## Target:

- https://ctf.n00bzunit3d.xyz/attachments/So_snowy!/enc.txt
- https://ctf.n00bzunit3d.xyz/attachments/So_snowy!/wordlists.txt

## Objective:

Show the hidden message in the `enc.txt` file, using key in `wordlists.txt` to decrypt the *snow ciphertext*. 


## Difficulty/Points: 
500 pt

## Flag:
n00bz{st3g_1s_s0_sn0wy}
# 


# Challenge
It's so snowy

# Solution

This is the *snow cipher*: http://mewbies.com/steganography/snow/how_to_conceal_a_message_in_a_text_file.htm

<code>

    import requests

    f=open('wordlists.txt','r').read()
    ff=f.split("\n")[:len(f.split("\n"))-2]

    burp0_url = "http://fog.misty.com:80/cgi/snow"
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Origin": "null", "Content-Type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate", "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7", "Connection": "close"}

    for i in ff:
        burp0_data = {"what": "decrypt", "URL": "storage.googleapis.com/static.n00bzunit3d.xyz/So_snowy!/enc.txt", "passwd": i}
        r=requests.post(burp0_url, headers=burp0_headers, data=burp0_data)
        if 'noobz' in r.text:
            print(r.text)
            break

</code>