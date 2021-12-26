
from Market import db
from Model import User, Post

def init_table():
    db.drop_all()
    db.create_all()

def init_data():
    user = User(username='byunghoon', password='1234')
    db.session.add(user)
    db.session.commit()

    user_id = User.query.filter_by(username = 'byunghoon').first_or_404()
    print(user_id)
    db.session.add(Post(
        title='제습기 팔아용',
        contents='안쓰는 제습기 팝니다',
        price=350000,
        address='충북 천안시 서북구 성정동',
        image_name='eagle.jpg',
        author_id=user.id
    ))
    db.session.commit()

'''
    title = db.Column(db.String(80), nullable=False)
    contents = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image_name = db.Column(db.String(80), nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
'''