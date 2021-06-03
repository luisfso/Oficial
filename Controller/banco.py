import mysql.connector

#     usuarios cadastrados
##    hashlib.md5(b"unisa123").hexdigest()
##    hashlib.md5(b"professora123").hexdigest()
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()
try:  
   mycursor.execute("SELECT `estoque_contas`.`id`,`estoque_contas`.`username`,`estoque_contas`.`password`,`estoque_contas`.`email` FROM `estoque`.`estoque_contas`;")  
   result=mycursor.fetchall()    
   for i in result:    
      id=i[0]  
      usuario=i[1]  
      senha=i[2]
      email=i[3]  
      print(id,usuario,senha,email)  
except:
   print('Error:Nao foi possivel ler o banco.') 

'''
mycursor.execute()
lendo do banco
try:  
   mycursor.execute("SELECT `estoque_contas`.`id`,
    `estoque_contas`.`username`,
    `estoque_contas`.`password`,
    `estoque_contas`.`email`
FROM `estoque`.`estoque_contas`;")  
   result=mycursor.fetchall()    
   for i in result:    
      roll=i[0]  
      name=i[1]  
      marks=i[2]  
      print(roll,name,marks)  
except:   
   print('Error:Nao foi possivel ler o banco.') 

'''
mydb.close()
