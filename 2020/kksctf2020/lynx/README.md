# lynx-writeup
`Hello! We're BluePeace organisation, and we introduce the new project - Lynx Forum!` 

This challenge gave us a link http://tasks.kksctf.ru:30070/ to a website only saying `You are not lynx, access denied`. So immediately we started googling finding about this lynx text-based web browser, instead of using it we installed a simple user-agent switcher. Reloading the page we are greeted with 
`WELCOME
Let's defend our friend - Lynx - from robots!
(C) BluePeace, 2053`

so we already knew we had to visit http://tasks.kksctf.ru:30070/robots.txt. This gave us another link to visit at http://tasks.kksctf.ru:30070/a4d81e99fda29123aee9d4bb and the flag `kks{s0m3_CLI_br0ws3rs_4r3_us3ful}` (sure they are). 
