# -*-coding:utf-8-*-

from flask import Flask, render_template, redirect, request
from flaskext.mysql import MySQL

mysql = MySQL()

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'serverstudy'
app.config['MYSQL_DATABASE_PASSWORD'] = 'serverstudy!@#'
app.config['MYSQL_DATABASE_DB'] = 'serverstudy'
app.config['MYSQL_DATABASE_HOST'] = 'data.khuhacker.com'
app.config['MYSQL_CHARSET'] = 'utf-8'
mysql.init_app(app)


@app.route('/userlist/')
def showUsers():
    cur = mysql.connect().cursor()
    cur.execute("SELECT * FROM LTH_users")  # 데이터베이스에서 정보 가져오기
    data = cur.fetchall()  # 전부 받아오기
    cur.close()
    output = ""
    print data

    for user in data:
        output += "NAME:%s, STUNO:%s, DATE:%s<br>" % (user[1], user[0], user[3])
    return output


@app.route('/adduser/<name>/<number>')
def addUser(name, number):
    con = mysql.connect()
    cur = con.cursor()
    cur.execute("INSERT INTO LTH_users(stuname, stuno) VALUES(%s, %s)", (name, number))
    con.commit()
    cur.close()
    return redirect('/userlist')


@app.route('/')
def hello_world():
    return render_template('hello.html')


@app.route('/sum/<int:num1>/<int:num2>')
def sum(num1, num2):
    return str(num1 + num2)


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        write = request.form['Writer']
        content = request.form['Contents']
        con = mysql.connect()
        cur = con.cursor()
        cur.execute("INSERT INTO LTH_twitter(Writer, Contents) VALUES(%s, %s)", (write, content))
        con.commit()
        cur.close()
        con.close()

        return redirect('/guestbook')


@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        write = request.form['dw']
        content = request.form['dc']

        con = mysql.connect()
        cur = con.cursor()
        cur.execute("DELETE FROM LTH_twitter WHERE Writer = %s AND Contents = %s", (write, content))
        con.commit()

        con.close()
        cur.close()

        return redirect('/guestbook')

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        write = request.form['uw']
        content = request.form['uc']

        con = mysql.connect()
        cur = con.cursor()
        cur.execute("UPDATE LTH_twitter SET Contents = %s WHERE Writer = %s", (content, write))
        con.commit()

        con.close()
        cur.close()

        return redirect('/guestbook')
@app.route('/guestbook')
def guestbook():
    cur = mysql.connect().cursor()
    cur.execute("SELECT * FROM LTH_twitter")
    datas = cur.fetchall()
    cur.close
    return render_template('guestbook.html', datas=datas)


#@app.route('/deleteGuestbook')
#def deleGuest():
#    cur = mysql.connect().cursor()
#    cur.execute("SELECT * FROM LTH_twitter")
#    datas = cur.fetchall()
#    cur.close
#    return render_template('guestbook.html', datas=datas)
    # query = "DELETE FROM LTH_twitter WHERE Contents = %s"


if __name__ == '__main__':
    app.run()
