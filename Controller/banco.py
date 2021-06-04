import mysql.connector
from hashlib import md5
from Model.usuario import Usuario

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="estoque"
)
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
def inserir_novo(nome,valor,quantidade):
    global mydb
    mycursor = mydb.cursor()
    try:
        print("SELECT id,nome,valor,estoque FROM `estoque_produtos` WHERE username = \"" + str(nome) +"\";")
        mycursor.execute("SELECT id,nome,valor,estoque FROM `estoque_produtos` WHERE nome = \"" + str(nome) +"\";")
        result = mycursor.fetchmany(size=1)
        print(result)
        if result:
            print("entrou")
            return False
        else:
            print("não entrou entrou")
            query = "INSERT INTO `estoque_produtos` (`nome`, `valor`, `estoque`) VALUES ( \"<{nome: }>\", \"<{valor: }>\", \"<{estoque: }>\");"
            print(query.replace("<{nome: }>", str(nome)).replace("<{valor: }>", str(valor)).replace("<{estoque: }>",str(int(quantidade))))
            mycursor.execute(query.replace("<{nome: }>",str(nome)).replace("<{valor: }>",str(valor)).replace("<{estoque: }>",str(int(quantidade))))

    except:
        print("erro de acesso ao banco")
    mydb.commit()

def validar_usuario(username, senha):
    global mydb
    mycursor = mydb.cursor()
    user = username
    password = md5(str(senha).encode()).hexdigest()
    #print(password)
    try:
        mycursor.execute("SELECT id,username,`password`,email FROM `estoque_contas` WHERE username = \""+user+"\" AND `password` = \""+password+"\";")
        result = mycursor.fetchmany(size=1)
        if not result:
            return(False)
        """
        for i in result:
            id = i[0]
            nome = i[1]
            senha = i[2]
            email = i[3]
            print(id, nome, senha, email)
            #quemestalogado = Usuario(id,nome,senha,email)
        """
        return(result)
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
def listar_produtos():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="estoque"
    )

    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT id,nome,valor,estoque FROM `estoque_produtos`;")
        result = mycursor.fetchall()

        if not result:
            return(False)

        for i in result:
            id = i[0]
            nome = i[1]
            valor = i[2]
            estoque = i[3]
        return(list(result))
    except:
        print('Error:Nao foi possivel ler o banco.')
    mydb.close()