print("""
 __          __  _                            _        
 \ \        / / | |                          | |       
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___  
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \ 
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/ 
                                                       
                                                       
  _______                                  _____     _                 _ 
 |__   __|                                |_   _|   | |               | |
    | |_ __ ___  __ _ ___ _   _ _ __ ___    | |  ___| | __ _ _ __   __| |
    | | '__/ _ \/ _` / __| | | | '__/ _ \   | | / __| |/ _` | '_ \ / _` |
    | | | |  __/ (_| \__ \ |_| | | |  __/  _| |_\__ \ | (_| | | | | (_| |
    |_|_|  \___|\__,_|___/\__,_|_|  \___| |_____|___/_|\__,_|_| |_|\__,_|
                                                                         """)
user_won = False
print("Your mission is to find the treasure!")

user_choice = input("You're at a cross road. Where do you want to go? Left or right? ").lower()
if user_choice.startswith('r'):
    user_choice = input("You turn right and begin to walk forward coming to a lake, do you want to wait for the boat "
                        "to cross, or try and swim? ")
    if user_choice.startswith('w'):
        user_choice = input("You wait for the boat and when it arrives you get on. You see something in the "
                            "distance.... it's an island. as you get closer, you can feel the excitement,you've made "
                            "it nothing can stop you now! You arrive at the island and there are three doors, red, "
                            "green and blue, which door do you pick? ")
        if user_choice.startswith('g'):
            print("You open the door and there it is, the treasure you've been looking for! GAME OVER.")
            user_won = True
        else:
            print("You open the door and you see nothing, you step inside and the door begins to shut on you, "
                  "in the distance you see two eyes staring at you. GAME OVER.")
    else:
        print("You jump into to lake and as you're swimming across, you're attacked by a crocodile. GAME OVER!")
else:
    print("As you begin to go left, you're struck by a car, GAME OVER!")


if user_won:
    print("Congratulations on getting the treasure, and thank you for playing.")
else:
    print("Better luck next time. Thank you for playing.")
