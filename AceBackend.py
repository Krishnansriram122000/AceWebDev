from flask import *
import re
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
	mail=0
	ph=0
	local=[]
	global u
	if request.method == 'POST':
		a=request.form['krish']
		local.append(a)
		x = re.search(".*@.*", a)
		if x:
			print('match')
		else:
			mail=1
			print('not a match')
		b=request.form['krish2']
		local.append(b)
		if not b.isdecimal():
			ph=1
			print('only numbers are allowed')
		elif len(b)<10 or len(b)>10:
			ph=2
			print('10 no needed')
		else:
			print('ph crt')

		print(a,b)	
		
		local.append(request.form['fullname'])
		local.append(request.form['address'])
		local.append(request.form['city'])
		local.append(request.form['country'])
		local.append(request.form['pc'])
		if mail==0 and ph==0:
			u=local
			return redirect('/index1')
		else:
			return render_template('index.html',tasks=[mail,ph])
	else:
		mail=0
		ph=0
		u=[]
		return render_template('index.html',tasks=[mail,ph])

@app.route('/index1', methods=['POST', 'GET'])
def index1():
	global u
	return render_template('index1.html',tasks=u)

if __name__ == "__main__":
	u=[]
	app.run(debug=True)