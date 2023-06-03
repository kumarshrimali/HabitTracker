def allhabitlist():
    """Display all habits in the habit_db table."""
    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()

        # Fetch all habits from the habit_db table
        command = """SELECT * FROM habit_db"""
        conn.execute(command)
        records = conn.fetchall()
        print("Total habits are:  ", len(records))
        print("\n")

        # Print each row in the records
        for row in records:
            print(row)

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data from the sqlite table:", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()


def dailyhabitlist():
    """Return a list of all habits with the same periodicity: Daily"""
    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()

        # Fetch habits with the periodicity 'Daily'
        command = """SELECT * FROM habit_db WHERE Period = 'Daily'"""
        conn.execute(command)
        records = conn.fetchall()
        print("Total habits are:  ", len(records))
        print("\n")

        # Print each row in the records
        for row in records:
            print(row)

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data from the sqlite table:", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("\n")


def weeklyhabitlist():
    """Return a list of all habits with the same periodicity: Weekly"""
    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()

        # Fetch habits with the periodicity 'Weekly'
        command = """SELECT * FROM habit_db WHERE Period = 'Weekly'"""
        conn.execute(command)
        records = conn.fetchall()
        print("Total habits are:  ", len(records))

        # Print each row in the records
        for row in records:
            print(row)

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data from the sqlite table:", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("\n")


def longstreakhabits():
    """Return the longest run streak of all defined habits"""
    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()

        # Find the habit with the longest run streak among all habits
        command = """SELECT Title, MAX(Max_Streak) FROM habit_db"""
        conn.execute(command)
        records = conn.fetchall()

        # Print the habit with the longest run streak
        for row in records:
            print(f"The longest run streak among all habits is: {row}")

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data from the sqlite table:", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("\n")


import sqlite3
import datetime
import time
from datetime import datetime, timedelta

def longstreakdailyhabits():
    """Return the longest run streak of all daily habits"""
    try:
        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()

        # Find the habit with the longest run streak among daily habits
        command = """SELECT Title, MAX(Max_Streak) FROM habit_db WHERE Period = 'Daily'"""
        conn.execute(command)
        records = conn.fetchall()

        # Print the habit with the longest run streak
        for row in records:
            print(f"The longest run streak among all daily habits is: {row}")

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data from the sqlite table:", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("\n")


def longstreakweeklyhabits():
    """Return the longest run streak of all weekly habits"""
    try:
        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()

        # Find the habit with the longest run streak among weekly habits
        command = """SELECT Title, MAX(Max_Streak) FROM habit_db WHERE Period = 'Weekly'"""
        conn.execute(command)
        records = conn.fetchall()

        # Print the habit with the longest run streak
        for row in records:
            print(f"The longest run streak among all weekly habits is: {row}")

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data from the sqlite table:", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("\n")


def longstreakgivenhabit():
    """Return the longest run streak for a given habit"""
    try:
        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()

        # Fetch all habits from the habit_db table
        command = """SELECT * FROM habit_db"""
        conn.execute(command)
        records = conn.fetchall()
        print("Total habits are:  ")

        # Print each row in the records
        for row in records:
            print(row)

        # Input habit title while habitId is exist
        lenrecords = int(len(records))

        do_next = True
        while do_next:
            input_Id = input("\nDisplay longest streak of habit # (eg. 1, 2, 3, 4, 5, etc.): ") or "0"
            # If input is empty, it will default to zero and will not cause an error
            try:
                inp_Id = int(input_Id)

                if inp_Id in range(lenrecords):
                    do_next = False
                else:
                    print("\nYour input is not in the list. Try again")
                    do_next = True
            except ValueError:
                print("It's not a valid Id. Try again.")
            else:
                break

        command = f'''SELECT Title, MAX(Max_Streak) FROM habit_db WHERE Id = {inp_Id} ;'''
        conn.execute(command)
        records = conn.fetchall()

        # Print the habit with the longest run streak
        for row in records:
            print(f"The longest run streak of the given habit is: {row}")

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data from the sqlite table:", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("\n")


def shortstreakhabits():
    """Return the habit with the shortest run streak among all defined habits"""
    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()

        # Find the habit with the shortest run streak among all habits
        command = """SELECT Title, MIN(Max_Streak) FROM habit_db"""
        conn.execute(command)
        records = conn.fetchall()

        # Print the habit with the shortest run streak
        for row in records:
            print(f"The habit you struggled the most with is: {row}")

        sqliteConnection.commit()
        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data from the sqlite table:", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("\n")




