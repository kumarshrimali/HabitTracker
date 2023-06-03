def tablecreation():
    """
    Create the 'habit_db' table in the SQLite database file.
    """
    #print("Table Creation")
        
    try:
        import sqlite3
        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        #print("Connected to SQLite")

        command = """CREATE TABLE IF NOT EXISTS 'habit_db'(
            'Id' integer NOT NULL,
            'Title' text NOT NULL,
            'Period' text NOT NULL,
            'Born' integer,
            'Start_Date' integer NOT NULL,
            'Due_Date' integer,
            'Streak' integer,
            'Max_Streak' integer,
            'Break' integer,
            PRIMARY KEY("Id" AUTOINCREMENT)
        )"""

        conn.execute(command)

        # len records of Habits exists
        records = conn.fetchall()
        #print("Total habits are:  ", len(records))
        #print("Succeed to create table")

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            #print("\n")
            #print('SQLite connection is closed')

def predefinedhabits():
    """
    Insert 5 predefined habits into the 'habit_db' table.
    """
    import sqlite3
    import datetime
    import time
    from datetime import datetime, timedelta

    sqliteConnection = sqlite3.connect('habit_db.sqlite3')
    conn = sqliteConnection.cursor()

    habits = [('Zero Sugar', 'Daily', '2023-05-01', '2023-05-21', '2023-05-23', 2, 10, 5),
              ('Workout', 'Daily', '2023-05-01', '2023-05-21', '2023-05-23', 7, 8, 9),
              ('Reading', 'Weekly', '2023-05-01', '2023-05-21', '2023-05-23', 1, 1, 1),
              ('Drink Milk', 'Daily', '2023-05-15', '2023-05-21', '2023-05-23', 4, 4, 2),
              ('Go to Church', 'Weekly', '2023-05-01', '2023-05-21', '2023-05-23', 0, 0, 2)
              ]

    conn.executemany(
        "INSERT OR REPLACE INTO habit_db ('Title','Period','Born','Start_Date','Due_Date','Streak','Max_Streak','Break') VALUES (?,?,?,?,?,?,?,?)",
        habits)

    sqliteConnection.commit()
    #print("Succeed to create 5 Predefined Habits")
