# Corruption
<p align="center">
  <img src=https://i.postimg.cc/4y3PVp8C/1.jpg" />
</p>

## FLAG:
`RS{se3_that_wasnt_s0_bad_just_som3_git_plumbing}`
#
## Solution
The challenge was complicated from the beginning as there were various problems to be solved and few ideas from which to take inspiration.

The first problem that arose is the impossibility of cloning the git repository, in fact if you tried to do it the following error came out
```console
asd@asd:~/Scrivania/CTF/RITSECctf$ git clone git://git.ritsec.club:9418/corruption.git
Clone in 'corruption' in corso...
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
remote: aborting due to possible repository corruption on the remote side.
Ricezione degli oggetti: 100% (5/5), fatto.
fatal: EOF prematuro
fatal: index-pack non riuscito

```
So I tried to modify the git configurations with the following parameters and try to clone again, but nothing, same error!
```
git config --global pack.windowMemory "100m"
git config --global pack.packSizeLimit "100m" 
git config --global pack.threads "1"
git config --global pack.window "0"
git clone git://git.ritsec.club:9418/corruption.git
```
So you had to find a way to clone the repository, but it is the description of the challenge itself that came to my aid with the word *remote*, in fact i immediately opened the *git manual* referring to *remote* and in the *EXAMPLES* section I found the solution to the problem.
<p align="center">
  <img src=https://i.postimg.cc/SRwYJVWZ/2.jpg" />
</p>
                                               
We made it !
```console
asd@asd:~/Scrivania/CTF/RITSECctf$ mkdir corruption.git
asd@asd:~/Scrivania/CTF/RITSECctf$ cd corruption.git/
asd@asd:~/Scrivania/CTF/RITSECctf/corruption.git$ git init
suggerimento: Using 'master' as the name for the initial branch. This default branch name
suggerimento: is subject to change. To configure the initial branch name to use in all
suggerimento: of your new repositories, which will suppress this warning, call:
suggerimento: 
suggerimento:   git config --global init.defaultBranch <name>
suggerimento: 
suggerimento: Names commonly chosen instead of 'master' are 'main', 'trunk' and
suggerimento: 'development'. The just-created branch can be renamed via this command:
suggerimento: 
suggerimento:   git branch -m <name>
Inizializzato repository Git vuoto in /home/asd/Scrivania/CTF/RITSECctf/corruption.git/.git/
asd@asd:~/Scrivania/CTF/RITSECctf/corruption.git$ git remote add -f -t master -m master origin git://git.ritsec.club:9418/corruption.gitAggiornamento di origin
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
remote: aborting due to possible repository corruption on the remote side.
Decompressione degli oggetti in corso: 100% (4/4), 274 byte | 137.00 KiB/s, fatto.
fatal: early EOF
fatal: unpack-objects non riuscito                                                                                
error: Impossibile recuperare origin                                                                              
asd@asd:~/Scrivania/CTF/RITSECctf/corruption.git$ ls -al                                                          
totale 12                                                                                                         
drwxr-xr-x 3 asd asd 4096 apr 12 21:50 .                                                                          
drwxr-xr-x 6 asd asd 4096 apr 12 21:49 ..                                                                         
drwxr-xr-x 7 asd asd 4096 apr 12 21:50 .git 
```                       

Now i had to print, somehow, the contents of the objects (for more information see https://stackoverflow.com/questions/14790681/what-is-the-internal-format-of-a-git-tree-object) and looking at the *git manual* referring to *cat-file*, i found two interesting options:
1. `--batch, --batch=<format>`: *Print object information and contents for each object provided on stdin. May not be combined with any other options or arguments except --textconv or --filters, in which case the input lines also need to specify the
                                 path, separated by whitespace. See the section BATCH OUTPUT below for details.*
2. `--batch-all-objects`: *Instead of reading a list of objects on stdin, perform the requested batch operation on all objects in the repository and any alternate object stores (not just reachable objects). Requires --batch or --batch-check be
                           specified. Note that the objects are visited in order sorted by their hashes.*

So I ran the command `git cat-file --batch --batch-all-objects`, bu i didn't get the result i expected ...
```console
asd@asd:~/Scrivania/CTF/RITSECctf/corruption.git$  git cat-file --batch --batch-all-objects
59840b46d591b3dc35c0b22340ff3fb8d980b351 tree 73
100644 README.md��Ɓ���%��oO5���{k100644 flag.txt�l�c�OūMn��B
                                                             �O�
c46c1ead63e74fc5ab4d116e9695420b20aa4f8a blob 6
!flag

c517fdc681c0a2b7258691116f4f35fee6a97b6b blob 36
# Corruption

Is this git hell yet?

f7fe593ca04a5d2a835d0e72225752fa588e0685 commit 167
tree 59840b46d591b3dc35c0b22340ff3fb8d980b351
author knif3 <knif3@mail.rit.edu> 1617947351 +0000
committer knif3 <knif3@mail.rit.edu> 1617947351 +0000

Initial Commit
```

Something was missing from what i had done and so i started looking on the internet until i open a site that provides me with the part i was looking for. The site in question is https://git-scm.com/book/it/v2/Git-Basics-Working-with-Remotes in which it says that, to download the branches and/or tags (depending on the our preferences) from the remote repository, you use the command ``git fetch``.

Reading the *git manual* for *fetch* i saw the *--all* option.

So I first ran the `git fetch --all` command, then `git cat-file --batch --batch-all-objects` and **BINGO**, i got the flag !
```console
asd@asd:~/Scrivania/CTF/RITSECctf/corruption.git$ git fetch --all
Recupero di origin in corso
Da git://git.ritsec.club:9418/corruption
 * [nuovo branch]    error      -> origin/error
asd@asd:~/Scrivania/CTF/RITSECctf/corruption.git$ git cat-file --batch --batch-all-objects
59840b46d591b3dc35c0b22340ff3fb8d980b351 tree 73
100644 README.md��Ɓ���%��oO5���{k100644 flag.txt�l�c�OūMn��B
                                                             �O�
c09b32987380e63e93d93f699e1dbfeae839f8e2 blob 49
RS{se3_that_wasnt_s0_bad_just_som3_git_plumbing}

c46c1ead63e74fc5ab4d116e9695420b20aa4f8a blob 6
!flag

c517fdc681c0a2b7258691116f4f35fee6a97b6b blob 36
# Corruption

Is this git hell yet?
                                                                                                                  
f7fe593ca04a5d2a835d0e72225752fa588e0685 commit 167                                                               
tree 59840b46d591b3dc35c0b22340ff3fb8d980b351                                                                     
author knif3 <knif3@mail.rit.edu> 1617947351 +0000                                                                
committer knif3 <knif3@mail.rit.edu> 1617947351 +0000                                                             
                                                                                                                  
Initial Commit  
```
