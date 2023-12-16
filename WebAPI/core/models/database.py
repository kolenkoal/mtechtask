import psycopg2


def get_db_connection():
    """
    Настроить соединение с базой данных.
    :return:
    """
    return psycopg2.connect(
        dbname="mtekhtest",
        user="user",
        password="password",
        host="db"
    )


def execute_query(query, params=None):
    """
    Запустить запрос для взаимодействия с базой данных.
    :param query:
    :param params:
    :return:
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    return cursor
