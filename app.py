import psycopg2

if __name__ == "__main__":
    connection = psycopg2.connect(
    host="localhost",
    database="capstone",
    user="postgres",
    password="password123"
    )
    connection.set_session(autocommit=True)
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM account')
        result = cursor.fetchone()
        print(result)