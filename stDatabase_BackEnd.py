import sqlite3
#backend
def studentData():
    con=sqlite3.connect("student.db")
    con.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, StdID text, firstname text,surname text,DoB text,\
                Age text,Gender text,Address text,Mobile text)")
    con.commit()
    con.close()
def addStRec(stid,firstname,surname,dob,age,gender,address,mobile):
     con=sqlite3.connect("student.db")
     cur=con.cursor()
     #cur.execute("INSERT INTO student VALUES(NULL,?,?,?,?,?,?,?,?,?)",(stid,firstname,surname,dob,age,gender,address,mobile ))    
     cur.execute("INSERT INTO student VALUES(NULL,?,?,?,?,?,?,?,?)",(stid.get(), firstname.get(), surname.get(), dob.get(), age.get(), gender.get(), address.get(), mobile.get()))
     con.commit()
     con.close()

def viewDate():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM student")
    row=cur.fetchall()
    con.close()
    return row
def deleteRec(id):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("DELETE FROM student WHERE id=?",(id))
    con.commit()
    con.close()
def searchData(stdid="",firstname="",surname="",dob="",age="",gender="",address="",mobile=""):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM student WHERE stdid=? OR firstname=? OR surname=? Or dob=? OR age=? OR gender=? OR address=? OR\
                mobile=?",(stdid,firstname,surname,dob,age,gender,address,mobile))         
    rows=cur.fetchall()
    con.close()
    return rows
def dataUpdate(stdid="",firstname="",surname="",dob="",age="",gender="",address="",mobile=""):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("UPDATE student SET stdid=?,firstname=?,dob=?,age=?,address=?,mobile=?,WHERE id=?,\
                ",(stdid,firstname,surname,dob,age,gender,address,mobile))
    
    con.commit()
    con.close()



studentData()