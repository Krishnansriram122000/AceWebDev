from flask import *
import re
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
	email = db.Column(db.String(200), primary_key=True)
	phone= db.Column(db.String(200))
	fullname= db.Column(db.String(200))
	address=db.Column(db.String(200))
	city=db.Column(db.String(200))
	country=db.Column(db.String(200))
	pincode=db.Column(db.String(200))
	def givelist(self):
	    return [self.email,self.phone,self.fullname,self.address,self.city,self.country,self.pincode]


@app.route('/', methods=['POST', 'GET'])
def index():
	mail=0
	ph=0
	global u
	if request.method == 'POST':
		a=request.form['krish']
		x = re.search(".*@.*", a)
		if x:
			print('match')
		else:
			mail=1
			print('not a match')
		b=request.form['krish2']
		if not b.isdecimal():
			ph=1
			print('only numbers are allowed')
		elif len(b)<10 or len(b)>10:
			ph=2
			print('10 no needed')
		else:
			print('ph crt')

		print(a,b)	
		u=a
		c=request.form['fullname']
		d=request.form['address']
		e=request.form['city']
		f=request.form['country']
		g=request.form['pc']
		if mail==0 and ph==0:
			
			Data=Todo(email=a,phone=b,fullname=c,address=d,city=e,country=f,pincode=g)
			try:
			    db.session.add(Data)
			    db.session.commit()
			    return redirect('/index1')
			except:
			    return 'There was an issue adding your task'

			
		else:
			return render_template('index.html',tasks=[mail,ph])
	else:
		mail=0
		ph=0
		return render_template('index.html',tasks=[mail,ph])

@app.route('/index1', methods=['POST', 'GET'])
def index1():
	global u
	data = Todo.query.get_or_404(u)
	task=data.givelist()
	return render_template('index1.html',tasks=task)

if __name__ == "__main__":
	u=0
	app.run(debug=True)