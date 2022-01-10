import json

from flask import render_template, send_from_directory, request
from config import app, db
from Model import Post

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('itemlist.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def item_create():
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
        return render_template('itemlist.html', posts=Post.query.all())
    else:
        return render_template('itemadd.html')

@app.route('/item/<int:itemnumber>', methods=['GET', 'DELETE', 'UPDATE'])
def item_detail(itemnumber):
    target_post = Post.query.get(itemnumber)
    if request.method == 'GET':
        return render_template('itemdetail.html', post=target_post)
    if request.method == 'DELETE':
        db.session.delete(target_post)
        db.session.commit()
        return json.dumps({'success':True}), 200, {'ContentType': 'application/json'}


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploaded', filename)

if __name__ == '__main__':
    app.run(debug=True)