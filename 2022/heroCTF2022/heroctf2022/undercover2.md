![](./assets/images/logo.webp)



        
            
# Undercover#2



## Challenge Author(s):
Log_s

## Description:
Now that you proved yourself, You have to assess the security of one of their developpers systems. He's a very good coder, but not that good at keeping his system safe. Could you report to us any vulnerabilities you find in his system?

The base credentials are:

    user1:password123

NB: the content of the website is not relevant, you should get a 500 anyway ;)

## Objective:
Privilege escalation to reach `dev` user, `root` and then get the flag.


## Flag:
`Hero{3w-d4ta_1s_n0t_us3l3s5}`
# 

# Solution

You are able to write into `/var/www/html` and you can also notice that `apache2` is running as `dev` user. 

So, to obtain a shell as `dev` user, you can write a `.php.` page inside this folder, which contains the code for a reverse shell. 

You can found some samples there, selecting php: https://www.revshells.com/

After uploading this php page, into your machine you've to run these commands to listen to the reverse shell:

    ngrok tcp <port>
    nc -nlvp <port>

Then, to visit the malicious web page, you have to upload `curl` into the target machine, and then run:

    curl localhost/<your-page>.php

Now, using the command `sudo -l` you can notice that `dev` user is able to run all commands as `sudo` user without any authentication required. 

    sudo /bin/bash
    cat /root/flag.txt

