#importing the libraries


from enum import unique
from operator import methodcaller
from flask import Flask,render_template,request , redirect , url_for
from datetime import date, datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/yash/Documents/NSP-blog/blog1.db'
db = SQLAlchemy(app)
class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    image = db.Column(db.String(70))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)
    
    
@app.route('/')
def index():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc())
    return render_template('index.html' , posts=posts)

@app.route('/about')
def about():  
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id = post_id).one()
    return render_template('post.html' , post = post)

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/add')
def add():
    return render_template('add_html')
@app.route('/addpost' , methods = ['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']
    #a = title.split()
    #res = str(a)[1:-1]
    image = f"https://source.unsplash.com/1600x900/?{title}"
    post = Blogpost(title = title , subtitle = subtitle , author = author , date_posted = datetime.now() ,image = image, content = content)

    db.session.add(post)
    db.session.commit()
    return '<h1> Title : {} , Subtitle : {} , Author : {} , Content : {},image:{} </h1>'.format(title,subtitle,author,content,image)
if __name__ == "__main__":
    app.run(debug = True , port=8050)
