import json

from flask import render_template, send_from_directory, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from config import app, db, login_manager
from Model import Post, User

@login_manager.user_loader
def load_user(user):
    return User.query.get(user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print(request.form)
        id = request.form['id']
        pw = request.form['pw']
        user = User.query.filter_by(username=id).first()
        if not user:
            db.session.add(User(
                username = id,
                password = pw
            ))
            db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html')


@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('itemlist.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
@login_required
def item_create():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        address = request.form['address']
        contents = request.form['contents']
        user_id = current_user.id
        db.session.add(Post(
            title=title, 
            price=int(price), 
            address=address, 
            contents=contents,
            author_id=user_id
        ))
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('itemadd.html')

@app.route('/item/<int:itemnumber>', methods=['GET', 'DELETE', 'UPDATE'])
def item_detail(itemnumber):
    target_post = Post.query.get(itemnumber)
    if request.method == 'GET':
        return render_template('itemdetail.html', post=target_post)
    if request.method == 'DELETE':
        if target_post.author != current_user:
            return json.dumps({'success':False}), 401, {'ContentType': 'application/json'}
        db.session.delete(target_post)
        db.session.commit()
        return json.dumps({'success':True}), 200, {'ContentType': 'application/json'}


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']
        user = User.query.filter_by(username=id, password=pw).first()
        if user:
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    return render_template('itemsearchresult.html', posts=Post.query.filter(Post.title.contains(query)).all())


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploaded', filename)


if __name__ == '__main__':
    app.run(debug=True)