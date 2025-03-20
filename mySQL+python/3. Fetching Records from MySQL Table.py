import mysql.connector as sqltor  

def fetchRecords():  
    mconn = sqltor.connect(host="localhost", user="root", passwd="mysql", database="company", charset="utf8")  

    if mconn.is_connected():  
        print("CONNECTED SUCCESSFULLY")  
        cursor = mconn.cursor()  
        cursor.execute("SELECT * FROM dept")  

        data1 = cursor.fetchone()  
        print("FETCH ONE RECORD:", data1)  

        data2 = cursor.fetchmany(3)  
        print("FETCH THREE RECORDS:", data2)  

        data3 = cursor.fetchall()  
        print("FETCH ALL RECORDS:", data3)  

        for row in data3:  
            print(row)  

        mconn.close()  
    else:  
        print("ERROR IN CONNECTIVITY")  

# MAIN  
fetchRecords()
