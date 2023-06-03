# HabitTracker
Habit Tracker App with python for IU onboarding course.
The program provided is a Habit Tracker App that allows users to track and manage their habits. 
1.created with python39
2.database with sqlite3

Here is an explanation of its working:

    The program begins by defining a class called Habits which serves as the main component of the app. It contains various methods for creating, editing, deleting, and analyzing habits.

    The main_page function acts as the main menu of the app. It creates an instance of the Habits class and prompts the user to choose options such as creating new habits, completing tasks, managing habits, or analyzing habits.

    Within the Habits class, several methods are defined to handle different functionalities of the app. These methods include creating a blank table, creating predefined habits, resetting streaks and due dates, creating new habits, deleting habits, editing habit titles and periods, completing tasks, and analyzing habits.

    The Habits class makes use of other modules within the Main_Package package to perform specific tasks. For example, the Predefined module handles the creation of predefined habits, the AutoResetOverDue module resets streaks and due dates, and the Analyze module provides various analysis options for habits.

    The program utilizes user input to navigate through the different functionalities. Users can input choices such as creating new habits, completing tasks, managing habits, or analyzing habits. The program responds accordingly based on the user's input.

    The program includes loops to allow users to perform multiple actions without exiting the app. For example, after completing a task or managing a habit, the program returns to the main menu to allow the user to choose another option.

    The program incorporates sleep commands (time.sleep()) to provide pauses between actions and enhance the user experience.

    The main_page function serves as the entry point of the program, and it is called at the end to start the execution of the app.

To use the Habit Tracker App, users can run the program and follow the instructions provided in the menu. They can create new habits, complete tasks, manage habits (edit, delete), and analyze their habits based on various criteria.

It's important to note that the code provided assumes the existence of additional modules and packages such as Predefined, AutoResetOverDue, CreateNew, Delete, Edit, Task, and Analyze within the Main_Package package. These modules are responsible for handling specific operations related to habits.

Overall, this Habit Tracker App allows users to effectively track and manage their habits, helping them stay organized and focused on their goals.
