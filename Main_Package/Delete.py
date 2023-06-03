def deletehabits():
    """
    Delete habits from the database and re-index the Ids.
    """
    try:
        import sqlite3
        sqliteConnection = sqlite3.connect('habit_db.sqlite3')
        conn = sqliteConnection.cursor()
        records = conn.fetchall()
        lenrecords = len(records)

        while True:
            input_delete = input("\nDELETE Habit's ID number: ") or lenrecords + 100000000000000000000
            # In case of empty input, will delete non-existent row
            try:
                inp_delete = int(input_delete)
            except ValueError:
                print("It's not a valid Id. Try again.")
            except inp_Id > lenrecords:
                print("\nYour input is not in the list. Try again")
            else:
                break

        # Delete Id if Id exists
        command = f"DELETE FROM habit_db WHERE Id = {inp_delete} AND Id IS NOT NULL;"
        conn.execute(command)

        # Sort Ids after deleting an Id
        command = f"UPDATE habit_db SET 'Id' = (Id) - 1 WHERE Id > {inp_delete};"
        conn.execute(command)
        sqliteConnection.commit()
        conn.close()
        print("Successfully deleted habit")

    except sqlite3.Error as error:
        print("Failed to read data from SQLite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print('SQLite connection is closed')
