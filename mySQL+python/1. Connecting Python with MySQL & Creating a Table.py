import mysql.connector as mycon  

def create_tbl_student():  
    mydb = mycon.connect(host="localhost", user="root", passwd="123")  
    mycur = mydb.cursor()  
    mycur.execute("CREATE DATABASE IF NOT EXISTS school1")  
    mycur.execute("USE school1")  
    query = '''CREATE TABLE IF NOT EXISTS student (  
        roll VARCHAR(30) PRIMARY KEY,  
        name VARCHAR(30),  
        dob VARCHAR(30),  
        att VARCHAR(30))'''  
    mycur.execute(query)  
    print('TABLE CREATED SUCCESSFULLY...')  

# MAIN  
create_tbl_student()
