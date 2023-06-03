def autoresetoverdue():
    """
    Automatically reset overduedated streaks to zero and update start dates and due dates.

    - If a habit's due date is before today, the streak will be reset to zero.
    - The start date will be updated to today's date.
    - The due date will be updated based on the habit's period (daily or weekly).

    Note: This function assumes that the 'habit_db.sqlite3' database is already connected.
    """
    import sqlite3
    import datetime
    import time
    from datetime import datetime, timedelta

    sqliteConnection = sqlite3.connect('habit_db.sqlite3')
    conn = sqliteConnection.cursor()

    tmdelta = timedelta(days=-1)
    yestday = datetime.today().date() + tmdelta

    newstartdate = datetime.today().date()

    lenperiod_d = 1
    time_delta_daily = timedelta(days=1)
    newduedateday = newstartdate + time_delta_daily

    lenperiod_w = 7
    time_delta_week = timedelta(days=7)
    newduedateweek = newstartdate + time_delta_week

    Break_add = 1  # Value added to Break if overduedated

    # Add Break + 1 if Break (Overduedated)
    conn.execute('UPDATE habit_db SET Break = Break + ? WHERE Break = ? AND Due_Date <= ?', (Break_add, Break_add, yestday))

    # Reset Streak to 0 if Break (Overduedated)
    conn.execute('UPDATE habit_db SET Streak = ? WHERE Streak = ? AND Due_Date <= ?', (0, 0, yestday))

    # Replace Start_Date with today's date (for daily or weekly period it's the same)
    conn.execute('UPDATE habit_db SET Start_Date = ? WHERE Start_Date = ? AND Due_Date <= ?', (newstartdate, newstartdate, yestday))

    # Replace Daily Period Due_Date with newduedateday
    conn.execute('UPDATE habit_db SET Due_Date = ? WHERE Due_Date = ? AND Period = "Daily" AND Due_Date <= ?', (newduedateday, newduedateday, yestday))

    # Replace Weekly Period Due_Date with newduedateweek
    conn.execute('UPDATE habit_db SET Due_Date = ? WHERE Streak = Streak AND Period = "Weekly" AND Due_Date <= ?', (newduedateweek, yestday))

    sqliteConnection.commit()
    print("Reset Overdue Done")
    time.sleep(1)  # Sleep for 1 second
