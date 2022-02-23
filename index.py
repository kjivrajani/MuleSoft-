from mimetypes import init
import sqlite3
class Moviesdb:
    db = sqlite3.Connection("MoviesDatabase.db") #create Database
    print("Database is Created")

    db.execute("Create Table if not exists Movies(id int primary key Not Null,name varchar(20) Not Null,actor varchar(20) not null,actress varchar(20)not null,director varchar(20)not null,year int not null)") #Create Table 
    print("Table is created")
 
    # User Insert Value in Database
    def insert(self):
     id = int(input("Enter Id := "))   
     name = input("Enter Name := ")
     actor = input("Enter actor Name:= ")
     actress = input("Enter actress Name:= ")
     director = input("Enter director Name:= ")
     year = int(input("Enter year of release := "))
     self.db.execute("insert into Movies(id,name,actor,actress,director,year)Values(?,?,?,?,?,?)",(id,name,actor,actress,director,year))   #Insert Value
     self.db.commit()     #Commit Value
     print("Value is Inserted")
    
    def update(self):
     id = int(input("Enter Id := "))   
     name = input("Enter Name := ")
     actor = input("Enter actor Name:= ")
     actress = input("Enter actress Name:= ")
     director = input("Enter director Name:= ")
     year = int(input("Enter year of release := "))
     self.db.execute("Update Movies set name = ?,actor = ?, actress = ?,director = ? ,year = ? where id = ?" ,(id,name,actor,actress,director,year))
     print("Value is Updated")
    
    def deleted(self):
     id = int(input("Enter Id := "))  
     self.db.execute("Delete from Movies where id = ? ",(id))
     print("Data is Deleted")
    def display(self):
      data = self.db.execute("Select * from Movies")
      for row in data:
        print("ID : {},Name : {} , actor : {},actress : {},director :{},year : {}".format(row[0],row[1],row[2],row[3],row[4],row[5]))

con = Moviesdb()

con.()

con.()

while(True):
    print("1 insert Value")
    print("2 Update Value")
    print("3 Delete Value")
    print("4 Display Value")

    choices = int(input("Choice from 1 - 4"))

    if(choices == 1):
        con.insert()
    elif(choices == 2):
        con.update()
    elif(choices == 3):
        con.deleted()
    elif(choices == 4):
        con.display()
    else:
        print("Invalid Choice")
        exit()