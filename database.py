import sqlite3
import json

con = sqlite3.connect("blog.sqlite",check_same_thread=False)
con.row_factory = sqlite3.Row

cur = con.cursor()

def check_email(signup_email):
    emails=[]
    q1="SELECT email FROM user;"
    for email in cur.execute(q1):
        emails.append(email[0])
    if signup_email in emails:
        return True
    else :
        return False
    
# print(check_email('abhiseknanda11@gmail.com'))

def login(login_email,password):
    if check_email(login_email)==True:
        q='SELECT password from user WHERE email=?'
        data=cur.execute(q,(login_email,)).fetchall()
        con.commit()
        
        if str(data[0][0])==password:
            q='SELECT * from user WHERE email=?'
            login_data=cur.execute(q,(login_email,)).fetchall()
            con.commit()
            l=[]
            for i in login_data[0] :
                l.append(i)
            # import json
            # return json.dumps({"user_id":l[0],"Firstname":l[1],"Lastname":l[2],"email":l[3],"Phone":l[5]})
            return ["login",l[0],l[1]]
        else:
            return "Invalid Password"
    else:
        return "Invalid Email"
    
# print(login('abhiseknanda11@gmail.com','1234'))

def blog_data(user_id):
    q='SELECT * from blog WHERE user_id=?'
    data=cur.execute(q,(user_id,)).fetchall()
    con.commit()
    data_json = json.dumps([dict(ix) for ix in data ],separators=(',', ':'))
    return data_json

def type1():
    type='type1'
    q='SELECT * from blog WHERE type=? and blog_id=?'
    data=cur.execute(q,(type,1)).fetchall()
    con.commit()
    new=data[0][3:6]
    
    return [new[0],new[1],new[2]]

def blog_data_id(blog_id):
    type='type1'
    q='SELECT * from blog WHERE type=? and blog_id=?'
    data=cur.execute(q,(type,blog_id)).fetchall()
    con.commit()
    new=[data[0][0],data[0][3],data[0][4],data[0][5],data[0][6]]
    
    return new

print(blog_data_id(1))