import mysql.Connector


dbl=mysql.connector.connect(host='localhost', user='root', password='1234', database='user')

cur=db1.cursor()

r=int(input("Enter your rollno\n"))
n=input("Enter your name\n")
m=float(input("Enter registration number"))


s='INSERT INTO details values(%s,%s,%s)'

t=(r,n,m)

cur.execute(s,t)

db1.commit()
