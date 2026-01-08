#  flask api for little applications
# CRUD operations
# this operations is checked by thunderclient
from flask import Flask , jsonify , request
import mysql.connector
app=Flask(__name__)

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vaibhav@123",
    database="car"
)
cursor=db.cursor(dictionary=True)
# GET_API
@app.route("/getallowner", methods=["GET"])
def get_allowner():
    query="select * from owner"
    cursor.execute(query)
    result=cursor.fetchall()
    return jsonify(result)
    
# ADD_API
@app.route("/addowner", methods=["POST"])
def add_owner():
    data=request.json
    id=data["id"]
    name=data["name"]
    address=data["address"]
    age=data["age"] 
    query="insert into owner (id , name , address , age)values(%s,%s,%s,%s)"
    cursor.execute(query,(id,name,address,age))
    db.commit()
    return jsonify({
        "msg":"data added"
    })
#   DELETE_API  
@app.route("/deleteowner", methods=["DELETE"])
def del_owner():
    data=request.json
    id=data["id"]
    query="delete from owner where id = %s"
    cursor.execute(query,(id,))
    db.commit()
    return jsonify({
        "msg":"owner deleted"
    })
# UPDATE_API
@app.route("/updateowner",methods=["PUT"])
def update_owner():
    data=request.json
    id=data["id"]
    name=data["name"]
    address=data["address"]
    age=data["age"] 
    query="update owner set name=%s,address=%s,age=%s where id=%s"
    cursor.execute(query,(name,id))
    db.commit()
    return jsonify({
        "msg":"owner upadted"
    })
    
app.run()
