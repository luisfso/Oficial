import mysql.connector
from hashlib import md5
#     usuarios cadastrados
##    hashlib.md5(b"unisa123").hexdigest()
##    hashlib.md5(b"professora123").hexdigest()
'''class Banco():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    def validar_usuario(self,usuario,senha):
        mycursor = self.mydb.cursor()
        self.usuario = usuario
        self.senha = md5(senha.encode()).hexdigest()
        print(self.senha)
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

####
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
        
####
        self.mydb.close()
'''
def validar_usuario(usuario, senha):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    mycursor = mydb.cursor()
    user = usuario
    password = md5(str(senha).encode()).hexdigest()
    print(password)
    try:
        print("SELECT id,username,`password`,email FROM `estoque`.`estoque_contas` WHERE username = \""+user+"\" AND `password` = \""+password+"\";")
        mycursor.execute("SELECT id,username,`password`,email FROM `estoque`.`estoque_contas` WHERE username = \""+user+"\" AND `password` = \""+password+"\";")
        result = mycursor.fetchmany(size=1)
        if not result:
            return(False)

        for i in result:
            id = i[0]
            usuario = i[1]
            senha = i[2]
            email = i[3]
            print(id, usuario, senha, email)
        return(True)
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