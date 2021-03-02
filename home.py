from flask import redirect, url_for, request, render_template, session, Flask
# from flask import SQLAlchemy
#from flask_mysqldb import MySQL
#import config
#import yaml
import mysql.connector
import psycopg2

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

if __name__ == "__main__":
    app.debug = True
    app.run()


@app.route('/', methods=['GET', 'POST'])
def mainpage():
    request_method = request.method
    if request.method == 'POST':
        # -----MYSQL PART----#

        user = request.form['user']
        session["mysql_user"] = user
        pw = request.form['pw']
        session['mysql_pw'] = pw
        dbname = request.form['dbname']
        session['mysql_dbname'] = dbname
        host = request.form['host']
        session['mysql_host'] = host

        mydb = mysql.connector.connect(host=host, user=user, passwd=pw, database=dbname)

        mycursor = mydb.cursor()
        mycursor.execute("show tables;")
        data = mycursor.fetchall()
        session["mysql_data"] = data

        # -----MYSQL PART----#
        #print("data : ", data)
        #mysqldbcon(user, pw, dbname,port)
        #print("MYSQL PART : ", host, user, pw, dbname)

        #return redirect(url_for('update'))


        # -----POSTGRESQL PART----#

        user_p = request.form['user_p']
        session["posgresql_user"] = user_p
        pw_p = request.form['pw_p']
        session["posgresql_pw"] = pw_p
        dbname_p = request.form['dbname_p']
        session["posgresql_dbname"] = dbname_p
        host_p = request.form['host_p']
        session["posgresql_show"] = host_p


        return redirect((url_for('p2', data=data)))
    return render_template('mainpage.html', request_method=request_method)


@app.route('/2', methods=['GET', 'POST'])
def p2():
    #print("2222")
    request_method = request.method
    data = session["mysql_data"]
    #data_p = session["posgresql_data"]
    if request.method == 'POST':
        selected = request.form["list"]
        session["selectedtablename"] = selected
        #print("Selected Table Name :  ", selected)
        return redirect(url_for('p3'))
    return render_template("db-show.html", data=data)


@app.route('/3', methods=['GET', 'POST'])
def p3():
    request_method = request.method
    # ------MYSQL-----#

    user = session["mysql_user"]
    pw = session['mysql_pw']
    dbname = session['mysql_dbname']
    host = session['mysql_host']

    mydb = mysql.connector.connect(host=host, user=user, passwd=pw, database=dbname)
    mycursor = mydb.cursor()
    list = session["selectedtablename"]
    mycursor.execute("show columns from " + list)

    tablename=list
    columns = mycursor.fetchall()

    mycursor.execute("select * from "+tablename)
    data=mycursor.fetchall()
    #print("Selected Table Name: ", tablename)
    #print("Table Columns : ", columns)
    #print("Variables : ", data)
    cNamesQuery=''
    cNamesCreate=''
    encoding= 'utf-8'
    type=''

    for i in columns:
        cNamesQuery+=i[0]
        cNamesQuery+=','
        type+=i[0]
        type+=' '
        type+=i[1].decode(encoding)
        type+=','

    #print("Type : ",type[:-1])

    #print("names: ",cNamesQuery[:-1])

    create="DROP TABLE IF EXISTS "+tablename+"; CREATE TABLE "+tablename+" ("+type[:-1]+");"
    values=''
    for i in data:
        values+=str(i)
        values+=','



    #print("data : ", values[:-1])

    insert="INSERT INTO "+tablename+" ("+cNamesQuery[:-1]+") VALUES "+values[:-1]+";"

    #print(create)

    #print(insert)
    #print(str(data[0]))
    #mycursor.executemany(insert, data)

    # ----- POSTGRESQL-----#

    user_p = session["posgresql_user"]
    pw_p = session["posgresql_pw"]
    dbname_p = session["posgresql_dbname"]
    host_p = session["posgresql_show"]

    conn = psycopg2.connect(dbname=dbname_p, user=user_p, password=pw_p, host=host_p)
    cur = conn.cursor()

    cur.execute(create)
    conn.commit()
    #        CREATE TABLE DONE
    conn = psycopg2.connect(dbname=dbname_p, user=user_p, password=pw_p, host=host_p)
    cur = conn.cursor()
    cur.execute(insert)
    conn.commit()
    result="Seçilen "+tablename+" Tablosu "+dbname+" (Mysql) adlı databaseden başarıyla "+dbname_p+"'e (PostgreSql) aktarıldı."
    return result