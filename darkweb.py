from time import sleep
from malloc import malloc # test lib made by me
import random
import pyautogui
# ideas: dark-mart, mine --bitc


# variables

# not needed:
# user = "John Kennedy"
# password = "fishman72"

commands_ran = 0

# Beginning 
print("\n\n\n")
print("Daniel Catarig presents...")
sleep(3)
print("""


▓█████▄  ▄▄▄       ██▀███   ██ ▄█▀    █     █░▓█████  ▄▄▄▄   
▒██▀ ██▌▒████▄    ▓██ ▒ ██▒ ██▄█▒    ▓█░ █ ░█░▓█   ▀ ▓█████▄ 
░██   █▌▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░    ▒█░ █ ░█ ▒███   ▒██▒ ▄██
░▓█▄   ▌░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄    ░█░ █ ░█ ▒▓█  ▄ ▒██░█▀  
░▒████▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄   ░░██▒██▓ ░▒████▒░▓█  ▀█▓
 ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒   ░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒
 ░ ▒  ▒   ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░     ▒ ░ ░   ░ ░  ░▒░▒   ░ 
 ░ ░  ░   ░   ▒     ░░   ░ ░ ░░ ░      ░   ░     ░    ░    ░ 
   ░          ░  ░   ░     ░  ░          ░       ░  ░ ░      
 ░                                                         ░ 
                        A DAN INC.
                           GAME

""")
sleep(2)
print("""








""")
sleep(1)
print("""








""")
sleep(1)
print("""








""")
sleep(1)
print("""












































""")
sleep(1)
print("You boot your computer up with a rush of adrenaline. You've decided to explore the decrepit depths of the Dark Web. \n Soon your monitor screen flickers on, radiating a milky white light into your otherwise pitch black room.\n\n")
sleep(8)
print("The Login Page stands before you.\n\n\n")
sleep(2)

print("8------------------------------------------------------8")
user = pyautogui.password(
    text="Enter your Password",
    title="Username Entry",
    default="",
    mask="*"
)

print("\n\nStep one complete.")
password = pyautogui.password(
    text="Login",
    title="Password Entry",
    default="",
    mask="*"
)

sleep(3)
continue0 = input(f"\n\nSuccessfully logged in. Welcome, {user}. \n\n\n\n\n\n\n\n\n")
sleep(2)
continue1 = input("""

You are smacked by another overpowering boost of adrenaline as you slowly edge your mouse cursor over to DarK_XZY, a special program 
which lets you plunge into the mysterious void that is the Dark Web.
Click! Click! You open the program.
A terminal appears. Shakily you move your cursor over to a command line. You enter in the command:

EXP10RE --DARK_WB


Your screen suddenly lights up. The fans in your pc start to whirr vigorously. Perhaps this wasn't such a good idea, but it's too late now...
The speakers start letting out rapid beeping noises, as if it was crying out from the immense strain on the computer using morse code.
Everything begins to pixelate, and odd colours start flashing randomly across the screen. And then... nothing. Your computer's CPU flatlines.
Until, suddenly, it jolts to life. Your old OS is gone. The only thing that meets your eyes is a sickly black screen with a new login page.


Some text appears on the screen. 

Press enter to continue. 
""")
print("\n\n\nLogging into DRAx Ultim...")
sleep(1)
print("[|     ] Establishing data connection...")
sleep(1)
print("[||    ] Copying IP Address...")
sleep(1)
print("[|||   ] Calculating DRAx Ultim wait times...")
sleep(1)
print("[||||  ] Sending information to servers...")
sleep(1)
print("[||||| ] Bypassing safety regulations...")
sleep(1)
print("[||||||] Finalizing actions...")
sleep(3)
print("\n\nWelcome to the Dark Web.")

print("DRAx Ultim takes no responsibility for anything that may occur on the dark web.")


# Main loop
while True:

    # starter commands for beginners. it disappears after 5 commands are ran
    while commands_ran > 6:
        print("# Starter commands: dark--mart, commands, user--hack, explore --deeper, logoff, drax-info")  #! FIX THIS!!! :(
    choice = input("> ")
    if choice == "dark--mart":
        print("\nEntering the dark mart...")

        commands_ran += 1

        
