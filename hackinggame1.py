#import pygame



#start of program degug mode is indicated on the first line#
# second line is atepmts made _
debuging_mode = True

password_list = ['PROVIDE',
  'SETTING',
  'CANTINA',
  'CUTTING',
  'HUNTERS',
  'SURVIVE',
  'HEARING',
  'HUNTING',
  'REALIZE',
  'NOTHING',
  'OVERLAP',
  'FINDING',
  'PUTTING']

def password_display():
    #for displaying tje list to the header function
    for pw in password_list:
        print(pw.upper())
    print()

def header_display():
    #print debuging_mode
    if debuging_mode == True:
        print(f"DEBUG MODE")
    #print attemps with a varible to change the number of attemps later
    attemps_left = 1
    print(attemps_left," ATTEPMT(S) LEFT","\n")
    password_display()
    

def user_guess_prompt():
    #for prompting user to enter the password guess
    user_guess = input(f"Enter Pasword > ")
    return user_guess

def fail_exit_prompt():
    print("LOGIN FAILURE - TERMINAL LOCKED", "\n")

    print("PLEASE CONTACT AN ADMINISTRATOR","\n")    
    exit_prompt = input("PRESS ENTER TO EXIT")



if __name__ == '__main__':
    header_display()
    user_guess_prompt()
    fail_exit_prompt()
