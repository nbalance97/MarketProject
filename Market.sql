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
    price INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES USER(id)
);