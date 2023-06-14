_A='backend.js'

from flask import Flask,send_file,request,redirect
import os,json,subprocess

app=Flask(__name__)

@app.route('/')
def index():return send_file('index.html')

@app.route('/logo.svg')
def logo():return send_file('logo.svg')

@app.route('/robots.txt')
def robots():return'User-agent: *\nDisallow: /source'

@app.route('/source')
def source():
	with open('app.py')as A:return A.read()

@app.route('/source/js')
def js_source():
	with open(_A)as A:return A.read()

@app.route('/3ng1n33r1ng-s4mpl3',methods=['POST'])
def flag():
	A = {A[0]:A[1]for A in request.headers.items()}
	B = request.args.to_dict()
	if subprocess.check_output(['node',_A,str(A),str(B),str(request.json)]).decode().strip()=='Valid':return os.environ.get('FLAG')
	return redirect('/')

if __name__=='__main__':app.run()