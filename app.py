from flask import *
from flask_sqlalchemy import SQLAlchemy
from mail import send_mail

app = Flask(__name__)


ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/webTech'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qbkcknucomexwd:89abd25e5ff5137c9916281dd5fd2fccff9b7d3ba5d38834ddbc6f3c0bc06e7c@ec2-35-170-85-206.compute-1.amazonaws.com:5432/det872kjndmfip'

app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Contact(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    message = db.Column(db.Text)

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']

            data = Contact(name, email, message)
            db.session.add(data)
            db.session.commit()
            send_mail(name, email, message)

            return redirect(url_for('index'))

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/learn', methods=['POST'])
def learn_submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        data = Contact(name, email, message)
        db.session.add(data)
        db.session.commit()
        send_mail(name, email, message)

        return redirect(url_for('index'))

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')



if __name__ == '__main__':
    app.run(debug=True)
