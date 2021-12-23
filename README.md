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

``` SQL
DROP TABLE IF EXISTS USER;
DROP TABLE IF EXISTS GOODS;

CREATE TABLE USER (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE ITEMPOST (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    contents TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES USER(id)
);
```

# 구현사항 작성
1. 상품 리스트 보기 
2. 상품 등록
3. 상품 수정
4. 상품 삭제
5. 로그인 / 회원가입
