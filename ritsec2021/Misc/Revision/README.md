# Revision
<p align="center">
  <img src=https://i.postimg.cc/tTryXsX4/1.jpg" />
</p>

#
## Solution
First you need to clone the repository through the command:
```git clone http://git.ritsec.club:7000/Revision.git```

So by running the command 
```git rev-list --objects --all | grep "flag.txt"```
inside the directory that identifies the local copy of the repository, you can see the presence of 22 files:
<p align="center">
  <img src=https://i.postimg.cc/Ls8gvZ0H/2.jpg" />
</p>
After saving the result, obtained from the previous command in a file, with the following python script

```
import subprocess

flag = ""

with open("output.txt", "r") as f:
    while "RS{" not in flag:
        subprocess_return = subprocess.run(["git", "cat-file", "-p", f.readline().split(" ")[0]], stdout=subprocess.PIPE).stdout.decode().strip()
        flag = subprocess_return + flag

print("[+] FLAG: " + flag)
```
i recovered the values corresponding to each object but, what you notice, is that the flag does not make much sense, in fact it turned out to be ``RS{Iyur1pedh3git_c0ms}``.

So I thought I'd see how many commits were referenced to the *flag.txt* file through the command: ``git log --abbrev-commit --pretty=oneline --all --full-history -- flag.txt`` and it emerged that the commits were 38. 

From this i found two important information:

1. the flag contains 38 characters;
2. there are repeated characters that, with the previous command, were not shown.

At this point the game is done as i can identify the character through the commit and i have all the commits that refer to *flag.txt*. 

After saving the result of the previous command in a file, i reprocessed the script in the following way and i recovered the correct flag.
```
import subprocess

flag = ""

f = open("all_chars_flag.txt", "r")
for line in f:
    commit = line.split()[0]
    arg1 = f"git ls-tree {commit} | grep \"flag.txt\""
    subprocess_return = subprocess.run(arg1, shell=True, stdout=subprocess.PIPE).stdout.decode().strip().split()[2]
    arg2 = f"git cat-file -p {subprocess_return}"
    subprocess_return2 = subprocess.run(arg2, shell=True, stdout=subprocess.PIPE).stdout.decode().strip()
    flag = subprocess_return2 + flag
print(f"[+] FLAG: {flag}")
f.close()
```

**FLAG:** *RS{I_h0p3_y0u_scr1pted_th0s3_git_c0ms}*
