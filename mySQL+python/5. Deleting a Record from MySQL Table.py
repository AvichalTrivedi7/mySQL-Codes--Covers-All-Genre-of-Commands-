import mysql.connector as sqlc  

conn = sqlc.connect(host="localhost", user="root", passwd="mysql", database="school_management", charset="utf8")  

if conn.is_connected():  
    print("CONNECTED SUCCESSFULLY")  
else:  
    print("NOT CONNECTED")  

def delete_Students():  
    cursor = conn.cursor()  
    rno = int(input("Enter roll no of student to delete: "))  

    query = "DELETE FROM student WHERE rno={}".format(rno)  
    cursor.execute(query)  
    conn.commit()  
    print("DELETED SUCCESSFULLY....")  

# MAIN  
delete_Students()
