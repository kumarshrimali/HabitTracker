def completetask():
    """
    Check-off a task in the 'habit_db' table.
    """
    try:
        import sqlite3
        import datetime
        import time
        from datetime import datetime, timedelta

        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        records = conn.fetchall()
        lenrecords = len(records)

        twoday = datetime.today().date()
        tmdelta = timedelta(days=-1)
        yestday = twoday + tmdelta

        twomorrow = twoday + timedelta(days=1)

        while True:
            input_Id = input("\nHabit's ID to check-off: ") or "0"  # If input is empty, then input = "0"
            # in case of empty input, will delete unexist row
            try:
                inp_Id = int(input_Id)
            except ValueError:
                print("It's not a valid Id. Try again.")
            except inp_Id > lenrecords:
                print("\nYour input is not in the list. Try again")
            else:
                break

        # Add Streak+1
        conn.execute(
            'UPDATE habit_db SET Streak = Streak+? WHERE Start_Date <=? AND Id = ? AND Due_Date > ?',
            (1, twoday, inp_Id, yestday))

        # Max_Streak = Streak if Max_Streak < Streak
        command = (f'''UPDATE habit_db SET (Max_Streak) = (Streak) WHERE (Max_Streak)<(Streak) AND Id = {inp_Id};''')
        conn.execute(command)
        sqliteConnection.commit()

        # Replace Old Due_Date become New Start_Date
        conn.execute('UPDATE habit_db SET (Start_Date)=(Due_Date) WHERE Id = ? AND Start_Date<? AND Due_Date > ?',
                     (inp_Id, twomorrow, yestday))

        newstartdate = datetime.today().date()  # new start again after Break,starting today

        # For Period = Daily
        time_delta_D = timedelta(days=2)
        newduedate_D = newstartdate + time_delta_D
        conn.execute(
            'UPDATE habit_db SET Due_Date = ? WHERE Due_Date=Due_Date AND Period=="Daily" AND Id = ? AND Due_Date > ?',
            (newduedate_D, inp_Id, yestday))

        # For Period = Weekly
        time_delta_W = timedelta(days=14)
        newduedate_W = newstartdate + time_delta_W
        conn.execute(
            'UPDATE habit_db SET Due_Date = ? WHERE Due_Date=Due_Date AND Period=="Weekly" AND Id = ? AND Due_Date > ?',
            (newduedate_W, inp_Id, yestday))

        sqliteConnection.commit()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
