
from turtle import title
from flask import Flask, redirect,render_template,jsonify, url_for,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import desc
from cryptography.fernet import Fernet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['QLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Todo(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(500),nullable=False)
    password=db.Column(db.String(500))
    title=db.Column(db.String(50))
    desc=db.Column(db.String(300))
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno}&{self.title}&{self.desc}&{self.date_created}&{self.username}&{self.password}"


def searchIntoDB(id,password):
    results = db.session.query(Todo).filter_by(username=id,password=password).all()
    return results


def insertIntoDB(username,password,title,desc):
    todo=Todo(username = username, password = password, title = title, desc = desc)
    db.session.add(todo)
    db.session.commit()   

def msgEncryptor(msg):
    output_msg=""
    for e in range(0,len(msg)):
        e=msg[e]
        if(e=='a'):
            output_msg+='r'
        elif(e=='b'):
            output_msg+='x'
        elif(e=='c'):
            output_msg+='v'
        elif(e=='d'):
            output_msg+='z'
        elif(e=='e'):
            output_msg+='b'
        elif(e=='f'):
            output_msg+='s'
        elif(e=='g'):
            output_msg+='h'
        elif(e=='h'):
            output_msg+='d'
        elif(e=='i'):
            output_msg+='t'
        elif(e=='j'):
            output_msg+='y'
        elif(e=='k'):
            output_msg+='c'
        elif(e=='l'):
            output_msg+='p'
        elif(e=='m'):
            output_msg+='g'
        elif(e=='n'):
            output_msg+='u'
        elif(e=='o'):
            output_msg+='e'
        elif(e=='p'):
            output_msg+='k'
        elif(e=='q'):
            output_msg+='f'
        elif(e=='r'):
            output_msg+='q'
        elif(e=='s'):
            output_msg+='n'
        elif(e=='t'):
            output_msg+='a'
        elif(e=='u'):
            output_msg+='o'
        elif(e=='v'):
            output_msg+='j'
        elif(e=='w'):
            output_msg+='m'
        elif(e=='x'):
            output_msg+='i'
        elif(e=='y'):
            output_msg+='w'
        elif(e=='z'):
            output_msg+='l'
        elif(e=='0'):
            output_msg+='6'
        elif(e=='1'):
            output_msg+='8'
        elif(e=='2'):
            output_msg+='3'
        elif(e=='3'):
            output_msg+='0'
        elif(e=='4'):
            output_msg+='7'
        elif(e=='5'):
            output_msg+='2'
        elif(e=='6'):
            output_msg+='4'
        elif(e=='7'):
            output_msg+='9'
        elif(e=='8'):
            output_msg+='1'
        elif(e=='9'):
            output_msg+='5'
    print(output_msg)
    return output_msg

def msgDecryptor(msg):
    output_msg=""
    for e in range(0,len(msg)):
        e=msg[e]
        if(e=='r'):
            output_msg+='a'
        elif(e=='x'):
            output_msg+='b'
        elif(e=='v'):
            output_msg+='c'
        elif(e=='z'):
            output_msg+='d'
        elif(e=='b'):
            output_msg+='e'
        elif(e=='s'):
            output_msg+='f'
        elif(e=='h'):
            output_msg+='g'
        elif(e=='d'):
            output_msg+='h'
        elif(e=='t'):
            output_msg+='i'
        elif(e=='y'):
            output_msg+='j'
        elif(e=='c'):
            output_msg+='k'
        elif(e=='p'):
            output_msg+='l'
        elif(e=='g'):
            output_msg+='m'
        elif(e=='u'):
            output_msg+='n'
        elif(e=='e'):
            output_msg+='o'
        elif(e=='k'):
            output_msg+='p'
        elif(e=='f'):
            output_msg+='q'
        elif(e=='q'):
            output_msg+='r'
        elif(e=='n'):
            output_msg+='s'
        elif(e=='a'):
            output_msg+='t'
        elif(e=='o'):
            output_msg+='u'
        elif(e=='j'):
            output_msg+='v'
        elif(e=='m'):
            output_msg+='w'
        elif(e=='i'):
            output_msg+='x'
        elif(e=='w'):
            output_msg+='y'
        elif(e=='z'):
            output_msg+='l'
        elif(e=='6'):
            output_msg+='0'
        elif(e=='8'):
            output_msg+='1'
        elif(e=='3'):
            output_msg+='2'
        elif(e=='0'):
            output_msg+='3'
        elif(e=='7'):
            output_msg+='4'
        elif(e=='2'):
            output_msg+='5'
        elif(e=='4'):
            output_msg+='6'
        elif(e=='9'):
            output_msg+='7'
        elif(e=='1'):
            output_msg+='8'
        elif(e=='5'):
            output_msg+='9'

    return output_msg

def convertToUpper(msg):
    return msg.upper()

def convertToLower(msg):
    return msg.lower()

@app.route('/home/<id>&%<password>',methods=['GET','POST'])
def home(id,password):

    if(request.method=='POST'):
        title=request.form['title']
        desc=request.form['desc']
        insertIntoDB(id,password,title,desc)

    lst=searchIntoDB(id,password)
    temp=[]
    for value in lst:
        # print(type(str(value)))
        dict={}
        temp_lst=(str(value)).split('&')
        dict["id"]=temp_lst[0]
        dict["title"]=temp_lst[1]
        dict["description"]=temp_lst[2]
        dict["date"]=temp_lst[3].split(' ')[0]
        dict["username"]=temp_lst[4]
        dict["password"]=temp_lst[5]
        if(len(temp_lst[1])==0 or len(temp_lst[2])==0):
            continue
        temp.append(dict)
    # return jsonify(temp)
    allTodo=temp
    return render_template('index.html',allTodo=allTodo,id=id,password=password)
    return redirect(url_for('home',id=id,password=password))

# @app.route('/todo',methods=["GET"])
# def todo():
#     if(request.method=="GET"):
#         title = request.args['title']
#         desc = request.args['desc'] 
#         insertIntoDB("rzgtu","qeea",title,desc)


@app.route('/delete/<int:sno>&<password>&<username>')
def delete(sno,password,username):
    todo=Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home', id = username,password = password))

@app.route('/logout')
def logout():
    return redirect(url_for('auth'))

# @app.route('/')
# def temp():
#     lst=searchIntoDB("rzgtu","qeea")
#     temp=[]
#     for value in lst:
#         # print(type(str(value)))
#         dict={}
#         temp_lst=(str(value)).split('&')
#         dict["id"]=temp_lst[0]
#         dict["title"]=temp_lst[1]
#         dict["description"]=temp_lst[2]
#         dict["date"]=temp_lst[3].split(' ')[0]
#         dict["username"]=temp_lst[4]
#         dict["password"]=temp_lst[5]
#         if(len(temp_lst[1])==0 or len(temp_lst[2])==0):
#             continue
#         temp.append(dict)
#     # return jsonify(temp)
#     allTodo=temp
#     # return render_template('index.html',allTodo=allTodo,id=id,password=password)
#     return render_template('check.html',allTodo=allTodo)

@app.route('/',methods=['GET','POST'])
def auth():
    if(request.method=='POST'):
        #storing the data into database
        username=request.values.get('username')
        password=request.values.get('password')
        username=convertToLower(username)
        password=convertToLower(password)
        encUsername = msgEncryptor(username)
        encPassword = msgEncryptor(password)
        insertIntoDB(encUsername,encPassword,"","")
        return render_template('auth.html')
    else:
        return render_template('auth.html')

@app.route('/authc',methods=['GET'])
def auth_checker():
    username = request.args['username']
    password = request.args['password']
    username = convertToLower(username)
    password = convertToLower(password)
    encUsername = msgEncryptor(username)
    encPassword = msgEncryptor(password)

    lst = searchIntoDB(encUsername,encPassword)
    # lst = searchIntoDB(username,password)

    if(len(lst)>0):
        return redirect(url_for('home', id = encUsername,password = encPassword))
    else:
        return redirect(url_for('auth'))

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')
