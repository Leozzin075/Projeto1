import sqlite3

class DataBase():
    def __init__(self, name = "system.db"):
        self.name = name

    def conecta(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_user(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                    CREATE TABLE IF NOT EXISTS users(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                        name TEXT NO NULL,
                        user TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        access TEXT NOT NULL
                    
                    );
            
            """)
        except AttributeError:
            print('Por favor conectar')


    def insert_user(self,name, user, password, access):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                
                INSERT INTO users(name,user,password,access) VALUES(?,?,?,?)
            
            """,(name, user, password, access))
            self.connection.commit()
        except AttributeError:
            print("Faça conexao")


    def check_user(self, user, password):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT * FROM users;
            
            
            """)

            for linha in cursor.fetchall():
                if linha[2].upper() == user.upper() and linha[3] == password and linha[4] == "Administrador":
                    return "Administrador"
                elif linha[2].upper() == user.upper() and linha[3] == password and linha[4] == "User":
                    return "User"
                else:
                    print('sem acesso')

        except:
            pass


if __name__ == "__main__":
    db = DataBase()
    db.conecta()
    db.create_table_user()
    db.close_connection()