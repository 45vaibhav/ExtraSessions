console.log("hello");
const mysql = require('mysql2')
const express = require('express')
const cors = require('cors')

const app = express()

app.use(express.json())

app.use(cors())

const db = mysql.createConnection({
    host : "localhost",
    user : "root",
    password : "Vaibhav@123",
    database : "car"
})

app.get("/getalldrivers",(req,res)=>{
    const query = "select * from driver"
    db.query(query,(err,result)=>{
        if (err) {
            console.log("errrrrrrr ghari ja bala..");
        }else{
            res.json(result)
        }
    })
})

app.get("/getallcars",(req,res)=>{
    const query = "select * from carinfo"
    db.query(query,(err,result)=>{
        if (err) {
            console.log("errrrrrrr ghari ja bala..");
        }else{
            res.json(result)
        }
    })
})

app.post("/adddriver",(req,res)=>{
        console.log(req.body);
        const query = "insert into driver(name,address,age)values(?,?,?)"
        db.query(query,[req.body.name],[req.body.address],[req.body.age],(err,result)=>{
            res.json({
                "msg":"data added"
            })
        })
       
})

app.get("/getdriverbyid",(req,res)=>{
        console.log(req.body);
        const query = "select * from students where dri_id  = ?"
        db.query(query,[req.body.dri_id ],(err,result)=>{
            res.json(result)
        })
       
})
app.listen(3000,()=>{
    console.log("serevr started");
})