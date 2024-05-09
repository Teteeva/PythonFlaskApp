from flask import Flask, render_template, request, redirect, url_for
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


#home route
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title="Home Page")

@app.route('/about')
def about():
    return render_template('about.html',title="About Page")
    
@app.route('/create-article', methods=['POST', 'GET'])
def create_article( ):

     return render_template('create-article.html',title="Create Article  Page")

# to run the flask app
if __name__ == "__main__":
   
    app.run(debug=True)




