# MarketProject

# 개발 도구
- VSCODE
- Python 3.7
- Flask 2.0.2

# Model
1. User
    - 유저 ID / 비밀번호 저장
2. ItemPost
    - 게시된 물건명, 내용, 저자 정보 저장

- Flask의 SQLAlchemy 활용하여 ORM 설정

### Model.py
``` python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class ItemPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    contents = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
```

# 구현사항 작성

1. 상품 리스트 보기 ✔️
2. 상품 등록 ✔️
3. 상품 상세 페이지 ✔️
4. 상품 수정 
5. 상품 삭제 ✔️
6. 로그인 / 회원가입
