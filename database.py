import itertools
import mysql.connector
from MySQLdb._mysql import Error
from collections import defaultdict
from operator import itemgetter

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="yourpassword"
)

def fetchData():
    try:
        conn = mydb
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM books.fictional")
        ficitional = cursor.fetchall()
        c = "Lew"
        cursor.execute("SELECT * FROM books.nonfictional where writer LIKE '%s'" % ("%" + c + "%"))
        nonfictional = cursor. fetchall()
        print("nonfict: ", nonfictional)
        books = ficitional + nonfictional
        dist = defaultdict(list)

        sortedBooks = sorted(books, key=itemgetter('writer'))

        for key, value in itertools.groupby(sortedBooks, key=itemgetter('writer')):
            for i in value:
                print(i)
                dist[key].append(i)

        print(dist)

    except Error as e:
        print(e)
    finally:
        cursor.close()

if __name__ == '__main__':
    fetchData()