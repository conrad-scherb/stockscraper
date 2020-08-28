import sqlite3

### Stores a stock into it's appropriate database

def insertStock(ticker, currTime, currPrice):
    try:
        sqliteConnection = sqlite3.connect('data/' + ticker + '.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO share
                          (currTime, currPrice)
                          VALUES (?, ?);"""

        stockTuple = (currTime, currPrice)
        cursor.execute(sqlite_insert_with_param, stockTuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into " + ticker + " table")

        cursor.close()

    except sqlite3.Error as error:
        # Does the DB not exist?
        if (' '.join(error.args)) == "no such table: share":
            # Create the table
            with open('createStock.sql', 'r') as sqliteFile:
                sqlScript = sqliteFile.read()
                cursor.executescript(sqlScript)
                print("DB dosen't exist - it was created.")
                # Recall the function (should no longer error, and will write to table)
                insertStock(ticker, currTime, currPrice)
        else: 
            print("Failed to insert Python variable into sqlite table", error)
    
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")