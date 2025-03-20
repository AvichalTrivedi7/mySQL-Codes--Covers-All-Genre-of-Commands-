import mysql.connector as sqlc  

conn = sqlc.connect(host="localhost", user="root", passwd="mysql", database="school_management", charset="utf8")  

if conn.is_connected():  
    print("CONNECTED SUCCESSFULLY")  
else:  
    print("NOT CONNECTED")  

def update_In_Students():  
    cursor = conn.cursor()  
    col = input("Enter the column to update: ")  
    newval = input("Enter new value: ")  
    rno = int(input("Enter roll no of student to be updated: "))  

    query = "UPDATE student SET {}='{}' WHERE rno={}".format(col, newval, rno)  
    cursor.execute(query)  
    conn.commit()  
    print("UPDATED SUCCESSFULLY....")  

# MAIN  
update_In_Students()
