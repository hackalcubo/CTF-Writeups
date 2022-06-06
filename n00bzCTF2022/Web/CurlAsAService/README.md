# Curl as a Service


## Author: NoobMaster

## Description

Curl as a Service. Note flag is not in flag.txt, https://challs.n00bzunit3d.xyz:30533/


## Solution

The provided program is a bit misleading at first, there is a blacklist function, which is never used, it seems to hint a [SSTI](https://portswigger.net/web-security/server-side-template-injection), but `render_template_string` is not used.

The program basically goes to whatever url we put inside, in order to do this it uses `urllib.request.urlopen(f'{inp})`, trying a bit of things with it I noticed that `urlopen` allows using `file://` urls, so we can gain access to every file on the machine, assuming we know the full path. After a bit of thinking, I tried to enumerate all the running processes doing requests on `file:///proc/PID/cmdline` but only one process was found, with PID 1, which was the flask application. In the proc filesystem there is a link to the current working directory where the process was spawned, we can now take a guess on some files, using `file:///proc/1/cwd/challenge.py` we can get back the app real source code.

```py
from flask import Flask, request, render_template, render_template_string, redirect
import subprocess
import urllib
app = Flask(__name__)
def blacklist(inp):
    blacklist = ['{{','}}','import','os','system','[','_',']']
    for b in blacklist:
    inp = inp.replace(b, '')
    return inp
@app.route('/')
def main():
    return redirect('/curl')

@app.route('/curl',methods=['GET','POST'])
def curl():
    if request.method == 'GET':
    return render_template('curl.html')
    elif request.method == 'POST':
    inp = request.values['curl']
    #print(inp)

    #p = subprocess.Popen([python3, admin.py], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #print('a')
    def admin():
        return inp
    print(admin())
    webUrl = urllib.request.urlopen(f'{inp}')
    data = webUrl.read()
    #print(data)
    #data = data.replace(b'',b'')
    return f'Am Admin, Going to visit {inp} fingers crossed, Result:{data}'

@app.route('/such_a_1337_flag_file_th4t_n0_one_c4n_defnitely_f1nd_hahahaha_lollll_nooob_xDDDDDDd.txt')
def flag():
    return render_template('such_a_1337_flag_file_th4t_n0_one_c4n_defnitely_f1nd_hahahaha_lollll_nooob_xDDDDDDd.txt')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
```

Now we can go on that page and get the flag `n00bz{4rb1t4ry_f1le_re4d_us1ng_curl_ftw!}`
