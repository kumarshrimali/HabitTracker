"""This is Main Habit Tracker App"""

class Habits():
    """This is Habits class"""

    def __init__(self):
        print('HABIT TRACKER')


    def mytablecreation(self):
        """This Will Create Blank Table """
        from Main_Package import Predefined
        Predefined.tablecreation()


    def mypredefinedhabits(self):
        """This will create 5 Predefined habits"""
        from Main_Package import Predefined
        Predefined.predefinedhabits()


    def userautoresetoverdue(self):
        """Reset Streak=0, NewDueDate if OverDueDated"""
        from Main_Package import AutoResetOverDue
        AutoResetOverDue.autoresetoverdue()


    def usercreation(self):
        """For For User to  to create new habits"""
        from Main_Package import CreateNew
        CreateNew.newhabits()


    def userdeletion(self):
        """For For User to  to delete habits"""
        from Main_Package import Delete
        Delete.deletehabits()


    def useredittitle(self):
        """For User to  edit habit's title"""
        from Main_Package import Edit
        Edit.edittitle()


    def useredittodaily(self):
        """For User to  edit Period to Daily"""
        from Main_Package import Edit
        Edit.edittodaily()


    def useredittoweekly(self):
        """For User to  edit Period to Daily"""
        from Main_Package import Edit
        Edit.edittoweekly()


    def usercheckoff(self):
        """For User to  complete task"""
        from Main_Package import Task
        Task.completetask()


    def useranalyze1(self):
        """To Display  all habits"""
        from Main_Package import Analyze
        Analyze.allhabitlist()


    def useranalyze2(self):
        """To Display  all daily habits"""
        from Main_Package import Analyze
        Analyze.dailyhabitlist()


    def useranalyze3(self):
        """To Display  all weekly habits"""
        from Main_Package import Analyze
        Analyze.weeklyhabitlist()


    def useranalyze4(self):
        """To Display  longest streak habits"""
        from Main_Package import Analyze
        Analyze.longstreakhabits()


    def useranalyze5(self):
        """To Display  longest streak Daily habits"""
        from Main_Package import Analyze
        Analyze.longstreakdailyhabits()


    def useranalyze6(self):
        """To Display  longest streak Weekly habits"""
        from Main_Package import Analyze
        Analyze.longstreakweeklyhabits()


    def useranalyze7(self):
        """To Display  longest streak of given habit"""
        from Main_Package import Analyze
        Analyze.longstreakgivenhabit()


    def useranalyze8(self):
        """To Display  shortest streak from all habits"""
        from Main_Package import Analyze
        Analyze.shortstreakhabits()


#This Will Be Automatically started from beginning

#This is the Habit Main Page
import time

def main_page():
    """Main menu Function"""
    myhabits = Habits()
    myhabits.mytablecreation()
    #myhabits.mypredefinedhabits()
    #myhabits.userautoresetoverdue()

    #START OPTIONS : Either Fresh OR With Predefined Habits
    freshyesno = True
    while freshyesno == True:
        predef = input("\nUSE PREDEFINED HABITS? Y/N :  ")
        #Use Predefined Habits
        if predef.upper() == 'Y':
            myhabits.mypredefinedhabits()
            freshyesno = False
        #Start Fresh Without Predefined Habits
        elif predef.upper() == 'N':
            break
        else:
            print("\nYour input is not Y or N. Try again")
            ffreshyesno = True

    choice = ''
    # Keep looping until user input 'Quit'.
    while choice.lower() != 'q':

        print("\n[1] Enter 1 to CREATE NEW HABIT.")
        print("[2] Enter 2 to COMPLETE TASKS.")
        print("[3] Enter 3 to MANAGE (EDIT/ DELETE) HABIT.")
        print("[4] Enter 4 to ANALYSE YOUR HABIT.")
        print("[Q] Enter q to quit.")

        # Asking user to input his/her choice.
        choice = input("\nYOUR CHOICE :  ")

        # Reset Streak = 0 and modify to New Due_Date for Overdue dated
        myhabits.userautoresetoverdue()

        # Respond to the user's choice.
        if choice == '1':  # Create new habits
            print("\nCreate New Habit\n")
            myhabits.useranalyze1() # To Display  all habits before add new habits
            myhabits.usercreation()
            myhabits.useranalyze1() # To Display  all habits after new habits created
            time.sleep(1)  # sleep 1 secs
            print("\nGO TO MAIN PAGE\n")

        elif choice == '2':  # complete tasks(checkoff)
            print("\nComplete Tasks\n")
            myhabits.useranalyze1() # To Display  all habits before check
            myhabits.usercheckoff() # """Complete task, checkoff"""
            myhabits.useranalyze1() # To Display  all habits after checkoff
            time.sleep(1)  # sleep 1 sec
            print("\nGO TO MAIN PAGE\n")

        elif choice == '3':  # manage habits
            print("\nEdit/Delete Habit\n")

            manage_choice = ''
            while manage_choice.lower() != 'x':
                print("\n[1] Enter 1 to DELETE HABIT")
                print("[2] Enter 2 to EDIT HABIT'S TITLE")
                print("[3] Enter 3 to EDIT HABIT'S PERIOD TO DAILY")
                print("[4] Enter 4 to EDIT HABIT'S PERIOD TO WEEKLY")
                print("[X] Enter X to EXIT")

                # Asking user to input his/her choice.
                manage_choice = input("\nYOUR CHOICE :  ")
                # Respond to the user's choice.

                if manage_choice == '1':  # DELETE HABIT
                    print("\nDELETE HABIT\n")
                    myhabits.useranalyze1()  # To Display  all habits before deletion
                    myhabits.userdeletion()  # Delete Habit
                    myhabits.useranalyze1()  # To Display  all habits after deletion
                    time.sleep(3)  # sleep 2 sec
                    print("\nGO TO MANAGE PAGE\n")

                elif manage_choice == '2':  # EDIT HABIT'S TITLE
                    print("\nEDIT HABIT'S TITLE\n")
                    myhabits.useranalyze1()  # To Display  all habits before edit
                    myhabits.useredittitle()  # Edit Habit
                    myhabits.useranalyze1()  # To Display  all habits after edited
                    time.sleep(3)  # sleep 1 sec
                    print("\nGO TO MANAGE PAGE\n")

                elif manage_choice == '3':  # EDIT HABIT'S PERIOD TO DAILY
                    print("\nEDIT HABIT'S PERIOD TO DAILY\n")
                    myhabits.useranalyze1()  # To Display  all habits before edit
                    myhabits.useredittodaily()  # Edit Period to Daily
                    myhabits.useranalyze1()  # To Display  all habits after edited
                    time.sleep(3)  # sleep 3 sec
                    print("\nGO TO MANAGE PAGE\n")

                elif manage_choice == '4':  # EDIT HABIT'S PERIOD TO WEEKLY
                    print("\nEDIT HABIT'S PERIOD TO DAILY\n")
                    myhabits.useranalyze1()  # To Display  all habits before edit
                    myhabits.useredittoweekly()  # Edit Period to Weekly
                    myhabits.useranalyze1()  # To Display  all habits after edited
                    time.sleep(2)  # sleep 2 sec
                    print("\nGO TO MANAGE PAGE\n")

                elif manage_choice.lower() == 'x':  # Go to main page
                    print("\nTHANK YOU !!!!!!!.\n")

                else:
                    print("\n PLEASE INPUT CORRECT OPTION.\n")

        elif choice == '4':  # analyze habits
            print("\nAnalyse Habit\n")
            # To Display  Analyze Page

            analyze_choice = ''
            while analyze_choice.lower() != 'x':

                print("\n[1] Enter 1 to DISPLAY ALL HABITS")
                print("[2] Enter 2 to DISPLAY ALL DAILY HABITS")
                print("[3] Enter 3 to DISPLAY ALL WEEKLY HABITS.")
                print("[4] Enter 4 to DISPLAY LONGEST STREAK HABITS.")
                print("[5] Enter 5 to DISPLAY LONGEST STREAK OF DAILY HABIT.")
                print("[6] Enter 6 to DISPLAY LONGEST STREAK OF WEEKLY HABIT.")
                print("[7] Enter 7 to DISPLAY LONGEST STREAK OF A GIVEN HABIT.")
                print("[8] Enter 8 to DISPLAY HABIT YOU STRUGGLED THE MOST.")
                print("[X] Enter X to EXIT.")

                # Asking user to input his/her choice.
                analyze_choice = input("\nYOUR CHOICE :  ")
                # Respond to the user's choice.

                if analyze_choice == '1':  # DISPLAY ALL HABITS
                    print("\nDISPLAY ALL HABITS\n")
                    myhabits.useranalyze1() #To Display  all habits
                    time.sleep(1)  # sleep 1 sec
                    print("\nGO TO ANALYZE PAGE\n")

                elif analyze_choice == '2':  # DISPLAY ALL DAILY HABITS
                    print("\nDISPLAY ALL DAILY HABITS\n")
                    myhabits.useranalyze2()
                    time.sleep(1)  # sleep 1 sec
                    print("\nGO TO ANALYZE PAGE\n")

                elif analyze_choice == '3':  # DISPLAY ALL WEEKLY HABITS
                    print("\nDISPLAY ALL WEEKLY HABITS\n")
                    myhabits.useranalyze3()
                    time.sleep(1)  # sleep 1 sec
                    print("\nGO TO ANALYZE PAGE\n")

                elif analyze_choice == '4':  # DISPLAY LONGEST STREAK HABITS
                    print("\nDISPLAY LONGEST STREAK HABITS\n")
                    myhabits.useranalyze4()
                    time.sleep(1)  # sleep 1 sec
                    print("\nGO TO ANALYZE PAGE\n")

                elif analyze_choice == '5':  # LONGEST STREAK OF A DAILY HABIT
                    print("\nDISPLAY LONGEST STREAK A GIVEN HABIT\n")
                    myhabits.useranalyze5()
                    time.sleep(1)  # sleep 1 sec
                    print("\nGO TO ANALYZE PAGE\n")

                elif analyze_choice == '6':  # LONGEST STREAK OF A WEEKLY HABIT
                    print("\nDISPLAY HABIT YOU STRUGGLED THE MOST\n")
                    myhabits.useranalyze6()
                    time.sleep(1)  # sleep 1 sec
                    print("\nGO TO ANALYZE PAGE\n")

                elif analyze_choice == '7':  # LONGEST STREAK OF A GIVEN HABIT
                    print("\nDISPLAY LONGEST STREAK A GIVEN HABIT\n")
                    myhabits.useranalyze7()
                    time.sleep(1)  # sleep 1 sec
                    print("\nGO TO ANALYZE PAGE\n")

                elif analyze_choice == '8':  # SHORTEST STREAK OF ALL HABITS
                    print("\nDISPLAY HABIT YOU STRUGGLED THE MOST\n")
                    myhabits.useranalyze8()
                    time.sleep(1)  # sleep 1 sec
                    print("\nGO TO ANALYZE PAGE\n")

                elif analyze_choice.lower() == 'x':  # Go to main page
                    print("\n THANK YOU !!!!!!!.\n")

                else:
                    print("\n PLEASE INPUT CORRECT OPTION.\n")

        elif str(choice.lower()) == 'q':
            print("\n THANK YOU !!!!!!!.\n")

        else:
            print("\n PLEASE INPUT CORRECT OPTION.\n")

main_page()
