from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['cse01']
info = db.cse
student1 = {"Reg Num":"210003001","Name":"PFSD"}
student2 = [
    {"Reg Num":"210003301","Name":"hFSD"},
    {"Reg Num":"210003201","Name":"tFSD"},
    {"Reg Num":"210003101","Name":"rFSD"},
    {"Reg Num":"210003501","Name":"eFSD"}

]

studentData = db.student
studentData.insert_one(student1)


