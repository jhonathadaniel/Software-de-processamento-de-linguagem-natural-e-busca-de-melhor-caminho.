import pyodbc

class ConnectionDataBase:
    def __init__(self, server, database, username, password, driver='{ODBC Driver 17 for SQL Server}'):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.driver = driver
        self.connection = None

    def connect(self):
        connection_string = f'DRIVER={self.driver};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}'
        try:
            self.connection = pyodbc.connect(connection_string)
            return True
        except pyodbc.Error as e:
            print("Erro ao conectar ao banco de dados:", e)
            return False

    def execute_query(self, query):
        if not self.connection:
            print("Não há conexão ativa com o banco de dados.")
            return None

        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except pyodbc.Error as e:
            print("Erro ao executar a consulta:", e)
            return None

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            print("Conexão encerrada.")




if __name__ == '__main__':
    # Exemplo de uso da classe
    server = 'DESKTOP-IL70AD8\MSSQLSERVER001'
    database = 'treinos'
    username = 'teste1'
    password = '123456'

    db = ConnectionDataBase(server, database, username, password)

    if db.connect():
        query = "select * from produto"
        result = db.execute_query(query)

        if result:
            for row in result:
                print(row)

        db.disconnect()
