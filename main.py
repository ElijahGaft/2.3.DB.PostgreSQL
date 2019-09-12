import psycopg2
from contextlib import closing

def create_db(): # создает таблицы
    with conn.cursor() as cur:
        cur.execute("""CREATE TABLE student (
            id serial PRIMARY KEY,
            name varchar(100),
            gpa numeric(10,2),
            birth timestamp with time zone);
            """)
        cur.execute("""CREATE TABLE course (
                    id serial PRIMARY KEY,
                    name varchar(100));
                    """)


def get_students(): # возвращает студентов
    with conn.cursor() as cur:
        cur.execute("select * from student ")
        records = cur.fetchall()
        return records


def add_students(name, gpa): # создает студентов и
                                       # записывает их на курс
    with conn.cursor() as cur:
        name_s = name
        gpa_s = gpa
        cur.execute("insert into student (name, gpa) values (%s, %s)", (name_s, gpa_s))
        cur.execute("select * from student")
        cur.execute("insert into course (name) values (%s)", (name_s))
        cur.execute("select * from student")
        print('студента добавили на курс')
    return

def get_student(students_id):
    with conn.cursor() as cur:
        id = students_id
        cur.execute("select * from student where id = (%s)", (id))
        records = cur.fetchall()
        return records


def add_student(name, gpa): # просто создает студента
    with conn.cursor() as cur:
        name_s = name
        gpa_s = gpa
        cur.execute("insert into student (name, gpa) values (%s, %s)", (name_s, gpa_s))
        cur.execute("select * from student")
        print('студента добавили')
    return


if __name__ == '__main__':
    # Создаем соединение с нашей базой данных
    with closing(psycopg2.connect(dbname='homework', user='postgres', password='Scientist98')) as conn:
        print("Database opened successfully")
        # create_db()
        # add_student('Петр Джаваскриптов', '10')
        # get_students('1')
        # add_students('1', 'Петр Джаваскриптов', '10')
        # get_students()
