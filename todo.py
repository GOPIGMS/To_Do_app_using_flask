from flask import Flask,request,url_for,redirect,render_template
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="todo"
mysql=MySQL(app)



@app.route("/", methods=["GET","POST"])
def home():
    if request.method=="POST":
        con=mysql.connection.cursor()
        task=request.form["taskss"]
        sql="insert into tasks values(%s)"
        con.execute(sql,[task])
        mysql.connection.commit()
        con.close()



    con=mysql.connection.cursor()
    con.execute("select * from tasks")
    res=con.fetchall()
    con.close()
    tasks = [task[0] for task in res]
    print(res)
    print(tasks)

    return render_template("todos.html",tasks=tasks)

@app.route("/edittask,<string:task>", methods=["GET","POST"])
def edittask(task):
    
    if request.method=="POST":
        con=mysql.connection.cursor()
        tasks=request.form["task"]
        sql="update tasks set task=%s where task=%s"
        con.execute(sql,[tasks,task])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))

    


    con=mysql.connection.cursor()
    sql="select  task from tasks where task=%s"
    con.execute(sql,[task])
    res=con.fetchone()
    con.close()
    print("this below is res")
    print(res)
    tasks=res[0] if  res else " "
    return render_template("edittask.html",task=tasks)
        




    
@app.route("/deletetask,<string:task>")
def deletetask(task):
    con=mysql.connection.cursor()
    sql="delete from tasks where task=%s"

    con.execute(sql,[task])
    mysql.connection.commit()
    con.close()
    return redirect(url_for(("home")))

if __name__=="__main__":
    app.run(debug=True)