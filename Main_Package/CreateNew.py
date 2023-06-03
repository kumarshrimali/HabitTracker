def newhabits():
    """
    Create new habits based on user inputs.
    """
    print("User inputs for new habits creation")
    try:
        # Return list of all currently tracked habits
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        print("Connected to SQLite")

        command = """SELECT * FROM habit_db"""
        conn.execute(command)
        records = conn.fetchall()
        print("Total habits are:  ")
        lenrecords = len(records)
        print(lenrecords)

        # Print each row
        for row in records:
            print(row)

        # User input for new habits
        do_next = True
        while do_next:
            inp_continue = input("\nCreate New Habit? Y/N: ")

            if inp_continue.upper() == 'Y':
                inp_Id = lenrecords + 1
                print(f'New Habit Id is : {inp_Id}')

                streak = 0

                inp_Title = input("\nNew Habit Name: ")
                ############ if it's not exist
                print(inp_Title)

                born = datetime.today().date()
                creation_start = datetime.today().date()
                print(f'Habit created on: {creation_start}')

                lenrecords = lenrecords + 1

                inp_Period = input("\nPeriod is Daily? Y/N: ")

                # New Daily Habit Creation
                doing = True
                while doing:
                    if inp_Period.upper() == 'Y':
                        inp_Period = 'Daily'
                        print(f'Habit Period: {inp_Period}')

                        due_date = creation_start + timedelta(days=1)
                        print(f'Due date to check off: {due_date}')

                        doing = False

                    # New Weekly Habit Creation
                    elif inp_Period.upper() == 'N':
                        inp_Period = 'Weekly'
                        print(f'Habit Period: {inp_Period}')

                        due_date = creation_start + timedelta(days=7)
                        print(f'Due date to check off: {due_date}')

                        doing = False

                    else:
                        print("\nYour input is not Y or N. Try again")
                        inp_Period = input("\nPeriod is Daily? Y/N: ")

                # Insert into habit_db
                habits = [
                    (lenrecords, inp_Title, inp_Period, born, creation_start, due_date, 0, 0, 0)
                ]

                conn.executemany("INSERT OR REPLACE INTO habit_db VALUES(?,?,?,?,?,?,?,?,?)", habits)
                print("Succeeded to insert into")

                sqliteConnection.commit()
                # Insert into habit_db ended

            elif inp_continue.upper() == 'N':
                conn.close()
                print("Bye-Bye")
                do_next = False

                # If "N" then Go to Main Menu
            else:
                print("\nYour input is not Y or N. Try again")
                inp_continue = input("\nCreate New Habit? Y/N: ")


    except sqlite3.Error as error:
        print("Failed to read data from SQLite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            #print('SQLite connection is closed')
