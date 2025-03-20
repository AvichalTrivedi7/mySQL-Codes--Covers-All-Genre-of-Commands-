import mysql.connector as mycon  

def insert_tbl_student():  
    mydb = mycon.connect(host="localhost", user="root", passwd="123", database="school1", charset="utf8")  
    mycur = mydb.cursor()  
    roll = input("Enter roll no. of the student: ")  
    name = input("Enter name of the student: ")  
    dob = input("Enter year of birth of the student: ")  
    att = input("Enter attendance of the student (P/A): ")  

    query = "INSERT INTO student VALUES('{}', '{}', '{}', '{}')".format(roll, name, dob, att)  
    mycur.execute(query)  
    mydb.commit()  
    print('DATA INSERTED SUCCESSFULLY...')  

# MAIN  
insert_tbl_student()
