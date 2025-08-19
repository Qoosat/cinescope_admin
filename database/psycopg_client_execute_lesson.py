import psycopg2
from psycopg2 import extras
from resources.db_creds import MoviesDbCreds


def execute():
    """Функция для подключения к PostgreSQL базе данных"""
    connection = None
    cursor = None

    try:
        # Подключение к базе данных
        connection = psycopg2.connect(
            dbname=MoviesDbCreds.DATABASE_NAME,
            user=MoviesDbCreds.USERNAME,
            password=MoviesDbCreds.PASSWORD,
            host=MoviesDbCreds.HOST,
            port=MoviesDbCreds.PORT
        )

        print("Подключение успешно установлено")

        # Создание курсора
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # Выполнение SQL-запроса
        cursor.execute('''
            DELETE from genres 
            where name = %s;
        ''', ('фантастический боевик',))
        affected_rows = cursor.rowcount
        print(f"Количество обновленных строк: {affected_rows}")

        connection.commit()

    except Exception as error:
        print("Ошибка при работе с PostgreSQL:", error)
        if connection:
            connection.rollback()
            print('роллбекаемся')

    finally:
        # Закрытие соединения с базой данных
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("Соединение с PostgreSQL закрыто")


if __name__ == "__main__":
    execute()
