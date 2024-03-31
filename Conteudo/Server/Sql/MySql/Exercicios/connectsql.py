import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="barbeariapatocksx"
)

cursor = conexao.cursor()

comandos_sql = [
    "CREATE TABLE IF NOT EXISTS user (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), email VARCHAR(255))",
    "CREATE TABLE IF NOT EXISTS agendados (id INT AUTO_INCREMENT PRIMARY KEY, cliente_id INT, produto VARCHAR(255), quantidade INT)",
    "CREATE TABLE IF NOT EXISTS vagas (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), preço DECIMAL(10,2))"
]

for comando in comandos_sql:
    cursor.execute(comando)


conexao.commit()

cursor.close()
conexao.close()

print("Tabelas criadas com sucesso!")

