import sqlite3

con = sqlite3.connect("blog.sqlite",check_same_thread=False)
con.row_factory = sqlite3.Row

cur = con.cursor()

q='CREATE TABLE blog (blog_id integer primary key ,user_id integer ,blog_name varchar,blog_title varchar,blog_body varchar,blog_img blog,type varchar)'

# cur.execute(q)

import bcrypt
Password=1234
Password=Password.encode()
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(Password, salt)