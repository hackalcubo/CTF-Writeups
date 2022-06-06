# Blob
<p align="center">
  <img src=https://i.postimg.cc/T1fq0srS/Immagine.jpg" />
</p>

## FLAG:
`RS{refs_can_b3_secret_too}`
#
## Solution
First you need to clone the repository through the command:
```git clone http://git.ritsec.club:7000/blob.git```

So by running the command 
```git rev-list --objects --all```
inside the directory that identifies the local copy of the repository, you can see the presence of four files:
<p align="center">
  <img src=https://i.postimg.cc/PxVTQCv8/1.jpg" />
</p>

Then using the command
```git cat-file --batch --batch-all-objects```
i got the flag !
<p align="center">
  <img src=https://i.postimg.cc/T35zZkL1/2.jpg" />
</p>
