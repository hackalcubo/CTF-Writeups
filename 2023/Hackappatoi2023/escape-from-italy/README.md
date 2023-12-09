# Escape from Italy
<p align="center">
  <img src="Attachments/Description.jpg" />
</p>


## FLAG:
`HCTF{1s_d1z_r34l1ty_0r_F1c710n?}`

## Solution
The challenge don't provide any source code and gave a tcp connection to use via netcat, so i have to explore the challenge to better understand how it work. As soon as I connected to the tcp port the challenge proposed this shell:

![image-20231209140619882](C:\Users\GIovanni Giordano\AppData\Roaming\Typora\typora-user-images\image-20231209140619882.png)

I wanted to figure out what kind of shell it was, and the `dir()` command confirmed that the shell was from python. Among the values shown by dir() I noticed a suspicious function:

```python
🍴🍴🍴 dir()
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'banner', 'cmd', 'readline', 'suspicious_pasta']
```

I tried to explore the function and then found that it loaded forms, loaded a shell and printed out all the files present.

```python
suspicious_pasta('os').system('sh')
```

```bash
cat *;

Yep, not the flag..., use 'guera' as the password for the real challenge at port 8889
```

I immediately logged into the challenge and found the first part of the second challenge which is shown in the description image in attachments. It was just asking me to prove that I had solved the previous step and entering "guera" took me to the second step which was a jail ruby. I used these commands to print the flag:

```python
y=" ".join([oct(ord(i))[2:] for i in """cat *"""]);pastapay(y)
```


this command I put it on my personal python shell, and it printed an octal string that went unnoticed on the jail and allowed me to execute commands using backticks `. The payload was of the type:

```ruby
`octal_string_cat_*`
```

the explanation of the steps in the final resolution is as follows:

1. octal construction of a bash string (cat * was used).
2. surround the string with backtick
3. use the final ``` `command` ```.

after this step we get flag