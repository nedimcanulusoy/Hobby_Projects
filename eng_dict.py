import connector_info  # this is an external library which contains personal user, password, host and db information
import mysql.connector
from mysql.connector import Error


def connect_to_db():
    try:
        conn = connector_info.connect

    except mysql.connector.Error as error:
        print('ERROR: ', error)

    finally:
        conn = connector_info.connect

        if conn.is_connected():
            conn.close()


def add_data(w, m):
    try:
        conn = connector_info.connect

        query = "INSERT INTO dict (word, meaning) VALUES (%s,%s)"
        data_query = (w, m)

        cursor = conn.cursor()
        cursor.execute(query, data_query)

        conn.commit()
        cursor.close()
        conn.close()

    except mysql.connector.Error as error:
        print("ERROR: ", error)


def query_data(word_request):
    try:
        conn = connector_info.connect
        query = "SELECT word FROM dict WHERE word = %s"

        word_request = word_request

        cursor = conn.cursor()
        cursor.execute(query, word_request)

        conn.commit()
        cursor.close()
        conn.close()

    except mysql.connector.Error as error:
        print("ERROR: ", error)


def delete_data(row_id):
    try:
        conn = connector_info.connect

        query = "DELETE FROM dict WHERE id = %s"
        request = row_id

        cursor = conn.cursor()
        cursor.execute(query, (request,))

        conn.commit()
        cursor.close()
        conn.close()

    except mysql.connector.Error as error:
        print("ERROR: ", error)


connect_to_db()
add_data('test', 'data')
delete_data(1)
query_data('test')
