import psycopg2

def table():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="sweety",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            Name TEXT,
            ID INT,
            Age INT
        );
    ''')

    print("Table created successfully")

    conn.commit()
    conn.close()


def data():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="sweety",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    name = input('Enter name: ')
    id = input('Enter id: ')
    age = input('Enter age: ')

    query = '''
        INSERT INTO employees (Name, ID, Age)
        VALUES (%s, %s, %s);
    '''

    cursor.execute(query, (name, id, age))

    print('Data added successfully')

    conn.commit()
    conn.close()



def extract():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="sweety",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM employees;
    ''')

    show = cursor.fetchone()

    print(show[2])

    conn.commit()
    conn.close()


table()
data()
extract()