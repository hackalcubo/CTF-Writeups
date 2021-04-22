## Challenge Author:
`itsecgary`
            
# Chungus Bot

## Description:

>  I wonder if ChungusBot has the flag.
>
>  Make sure to join the discord for the challenge!
>
>  https://discord.gg/dDnQncKqzV

## Points: 
`337`

## Flag:
`UMDCTF-{I_th1nk_y0u_4r3_th3_b0t_n0w_sh3333333333sh}`


# Challenge
We have a Chungus Bot on UMDCTF's Discord. First of all, get some help in private message.


```
>help
```

What we get:

> ```
> ChungusBot Help
> >help
> display this help page
> >flag
> idk see what you get ;)
> ```

Ok, let's try

`>flag`

Answer:

`Invalid command. Run ``>help flag`` for information on flag commands.`

Seems not working. Let's try

`>help flag`

Answer:

`lol no info for you dawg`

Ok, probably all commands are troll, so change way. There's a strange status on Chungus Bot saying:

`Is playing: Check out my code`

Searching on GitHub "ChungusBot" I found [this](https://github.com/itsecgary/ChungusBot). 



![image-20210421174430824](https://i.imgur.com/ho2ctVL.png)

Removed flag commit on cogs, go and see what in there.

![image-20210421174512200](https://i.imgur.com/M0j5vvs.png)

chungusboi.py:

```
import discord
from discord.ext import commands, tasks
import string
import json
import requests
import sys
import time
import help_info

def in_dms():
    async def tocheck(ctx):
        # A check for ctf context specific commands
        if str(ctx.channel.type) == "private":
            return True
        else:
            await ctx.send("This command is only available over DM!")
            return False

    return commands.check(tocheck)

def in_channel():
    async def tocheck(ctx):
        # A check for ctf context specific commands
        if not str(ctx.channel.type) == "private":
            return True
        else:
            await ctx.send("This command is not available over DM!")
            return False

    return commands.check(tocheck)

class Chungusboi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def chungusboi(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.channel.send("Invalid command. Run `>help chungusboi` for information on **chungusboi** commands.")

    @chungusboi.command()
    @in_dms()
    async def kyle(self, ctx):
        tic = time.perf_counter()
        with open(f'userfiles/{ctx.author.name}_time', 'w') as f:
            f.write(f'{tic}\n')

#################################### SETUP #####################################
def setup(bot):
    bot.add_cog(Chungusboi(bot))
```

How we can see, there's a command named chungusboi

`@chungusboi.command()` tagged as `in_dms()`

and a subcommand `kyle` that open and create a folder named `userfiles/{ctx.author.name}_time` and start a counter too:

`tic = time.perf_counter()` and write a `{tic}\n` value in ``userfiles/{ctx.author.name}_time``

The first command so it's `>chungusboi kyle`

Let's see flag.py code:

```
import discord
from discord.ext import commands, tasks
import string
import json
import requests
import sys
import time
import help_info

def in_dms():
    async def tocheck(ctx):
        # A check for ctf context specific commands
        if str(ctx.channel.type) == "private":
            return True
        else:
            await ctx.send("This command is only available over DM!")
            return False

    return commands.check(tocheck)

def in_channel():
    async def tocheck(ctx):
        # A check for ctf context specific commands
        if not str(ctx.channel.type) == "private":
            return True
        else:
            await ctx.send("This command is not available over DM!")
            return False

    return commands.check(tocheck)

class Flag(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def flag(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.channel.send("Invalid command. Run `>help flag` for information on **flag** commands.")

    @flag.command()
    @in_channel()
    async def printflag(self, ctx):
        await ctx.channel.send("chungus is dissapointed")

    @flag.command()
    @in_channel()
    async def rr(self, ctx):
        await ctx.channel.send("<https://bit.ly/1NbiVPe>")

    @flag.command()
    @in_dms()
    async def yeeee(self, ctx):
        tic = time.perf_counter()
        try:
            f = open(f'userfiles/{ctx.author.name}_time', 'r')
            stuff = f.read()
            count = len(stuff.split('\n'))

            if count == 2:
                f = open(f'userfiles/{ctx.author.name}_time', 'a')
                f.write(f'{tic}\n')
            else:
                await ctx.channel.send("Uh ohhh (count not 2)")
        except:
            await ctx.channel.send("Uh ohhh (no file)")

#################################### SETUP #####################################
def setup(bot):
    bot.add_cog(Flag(bot))
```

We can see the ``flag`` command and a `yeeee` subcommand tagged as `in_dms()`. This one split the file's content for `\n` and check if there are exactly 2 items and add an other `{tic}`. So this is the second command to do.

`>flag yeeee`

Let's check now chungy.py:

```
import discord
from discord.ext import commands, tasks
import string
import json
import requests
import sys
import time
import help_info
import subprocess

def in_dms():
    async def tocheck(ctx):
        # A check for ctf context specific commands
        if str(ctx.channel.type) == "private":
            return True
        else:
            await ctx.send("This command is only available over DM!")
            return False

    return commands.check(tocheck)

def in_channel():
    async def tocheck(ctx):
        # A check for ctf context specific commands
        if not str(ctx.channel.type) == "private":
            return True
        else:
            await ctx.send("This command is not available over DM!")
            return False

    return commands.check(tocheck)

class Chungy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def chungy(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.channel.send("Invalid command. Run `>help chungy` for information on **chungy** commands.")

    @chungy.command()
    @in_dms()
    async def mcchungus(self, ctx):
        tic = time.perf_counter()
        try:
            f = open(f'userfiles/{ctx.author.name}_time', 'r')
            stuff = f.read()
            count = len(stuff.split('\n'))

            if count == 3:
                f = open(f'userfiles/{ctx.author.name}_time', 'a')
                f.write(f'{tic}\n')
            else:
                await ctx.channel.send("Uh ohhh (count not 3)")
        except:
            await ctx.channel.send("Uh ohhh (no file)")

#################################### SETUP #####################################
def setup(bot):
    bot.add_cog(Chungy(bot))
```

`chunghy` command and `mcchungus` subcommand here tagged as `in_dms()`. Ok, this one check for 3 `{tic}\n` and add another one, so the next command is:

`>chungy mcchungus`

Now check last python file, gagagaga.py:

```
import discord
from discord.ext import commands, tasks
import string
import json
import requests
import sys
import time
import help_info
from config_vars import *

def in_dms():
    async def tocheck(ctx):
        # A check for ctf context specific commands
        if str(ctx.channel.type) == "private":
            return True
        else:
            await ctx.send("This command is only available over DM!")
            return False

    return commands.check(tocheck)

def in_channel():
    async def tocheck(ctx):
        # A check for ctf context specific commands
        if not str(ctx.channel.type) == "private":
            return True
        else:
            await ctx.send("This command is not available over DM!")
            return False

    return commands.check(tocheck)

class Gagagaga(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def gagagaga(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.channel.send("Invalid command. Run `>help gagagaga` for information on **gagagaga** commands.")

    @gagagaga.command()
    @in_dms()
    async def giveittome(self, ctx):
        try:
            f = open(f'userfiles/{ctx.author.name}_time', 'r')
            stuff = f.read()
            head = stuff.split('\n')[0]
            tail = stuff.split('\n')[3]

            if float(tail) - float(head) < 15:
                await ctx.channel.send('`' + flag + '`')
                await ctx.channel.send(file=discord.File("morris.PNG"))
                f = open(f'userfiles/{ctx.author.name}_time', 'w')
                f.write("")
        except:
            await ctx.channel.send("Uh ohhh (no file)")

    @gagagaga.command()
    @in_channel()
    async def chunga(self, ctx):
        await ctx.channel.send("chungachungachungachungachungachungachunga")

    @gagagaga.command()
    @in_dms()
    async def chungusisgod(self, ctx):
        tic = time.perf_counter()
        try:
            f = open(f'userfiles/{ctx.author.name}_time', 'r')
            stuff = f.read()
            count = len(stuff.split('\n'))

            if count == 4:
                f = open(f'userfiles/{ctx.author.name}_time', 'a')
                f.write(f'{tic}\n')
            else:
                await ctx.channel.send("Uh ohhh (count not 4)")
        except:
            await ctx.channel.send("Uh ohhh (no file)")

#################################### SETUP #####################################
def setup(bot):
    bot.add_cog(Gagagaga(bot))
```

This one has a `gagagaga` command and two subcommands: `chungusisgod` and `giveittome`. The first one check for the last `{tic}\n` and add an other. Next command is

`>gagagaga chungusisgod`

The other subcommand, `giveittome` opens the `userfiles/{ctx.author.name}_time` file in read-only and check if 

`if float(tail) - float(head) < 15:`

So, the last command is:

`>gagagaga giveittome`

What we recieve:

![image-20210421180405431](https://i.imgur.com/3TSna2s.png)