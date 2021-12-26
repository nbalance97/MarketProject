from flask import Flask, render_template, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Market.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
db.metadata.clear()

@app.route('/')
def index():
    from Model import Post
    return render_template('itemlist.html', posts=Post.query.all())

@app.route('/item', methods=['GET', 'POST'])
def createItem():
    from Model import Post
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        address = request.form['address']
        contents = request.form['contents']
        user_id = 1
        db.session.add(Post(
            title=title, 
            price=int(price), 
            address=address, 
            contents=contents,
            author_id=user_id
        ))
        db.session.commit()
        return render_template('itemlist.html')
    else:
        return render_template('itemadd.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploaded', filename)

if __name__ == '__main__':
    app.run(debug=True)