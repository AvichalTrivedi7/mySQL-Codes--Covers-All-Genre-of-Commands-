#CONNECTIVITY CODE
import mysql.connector as con

mydb=con.connect(host="localhost",user="root",passwd="root",database="box")
mycursor=mydb.cursor()                     #CURSOR CREATED

                                        #CREATING THE TABLE

sql="create table if not exists record(RNO int(10), SNAME varchar(20), STIPEND int(10), SUBJECT varchar(20), AVERAGE int(3));"
mycursor.execute(sql)
mydb.commit()

                                 #INSERTING VALUES INSIDE THE TABLE

for i in range(5):
    rno=int(input("Enter the rno: "))
    sname=input("Enter the name: ")
    stipend=int(input("Enter the stipend: "))
    subject=input("Enter the subject: ")
    average=int(input("Enter the average: "))
    sql="insert into record values({},{},{},{},{});".format(rno,sname,stipend,subject,average)
    mycursor.execute(sql)
    mydb.commit()

                              #SHOWING THE RECORDS IN THE TABLE "RECORD"

sql="select * from record;"
mycursor.execute(sql)
rows=mycursor.fetchall()
print("rno \t sname \t stipend \t subject \t average")
for y in rows:
    for x in y:
        print(y," \t ")

                                             #FINISHING
mycursor.close()


