import mysql.connector  
   
 def mysqlsearch(name): 
        mydb = mysql.connector.connect( 
        host= "192.168.27.36", 
        user="projectyt", 
        password="Pranavsai@2003" 
        database="Attendanceyt" 
  
 
 ) 
  
 
        a = mydb.cursor() 
        sql1=a.execute("SELECT * from UserAttendance WHERE USERNAME = %(name)s", 
{'name': name}) 
  
 
        a.execute(sql1) 
        checkUsername = a.fetchall() 
        print(*checkUsername, sep = "\n") 
  
 
        mydb.commit() 
        mydb.close() 
  
 
 name=input("Enter UserName:-") 
 mysqlsearch(name)