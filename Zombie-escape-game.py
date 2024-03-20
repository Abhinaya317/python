print('''
                      /\
                              /\  //\\
                       /\    //\\///\\\        /\
                      //\\  ///\////\\\\  /\  //\\
         /\          /  ^ \/^ ^/^  ^  ^ \/^ \/  ^ \
        / ^\    /\  / ^   /  ^/ ^ ^ ^   ^\ ^/  ^^  \
       /^   \  / ^\/ ^ ^   ^ / ^  ^    ^  \/ ^   ^  \       *
      /  ^ ^ \/^  ^\ ^ ^ ^   ^  ^   ^   ____  ^   ^  \     /|\
     / ^ ^  ^ \ ^  _\___________________|  |_____^ ^  \   /||o\
    / ^^  ^ ^ ^\  /______________________________\ ^ ^ \ /|o|||\
   /  ^  ^^ ^ ^  /________________________________\  ^  /|||||o|\
  /^ ^  ^ ^^  ^    ||___|___||||||||||||___|__|||      /||o||||||\       |
 / ^   ^   ^    ^  ||___|___||||||||||||___|__|||          | |           |
/ ^ ^ ^  ^  ^  ^   ||||||||||||||||||||||||||||||oooooooooo| |ooooooo  |
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
      ''')
print("Welcome to the Zombie House.")
print("Your mission is to escape from the house filled with zombies.")

choice1 = input('You\'ve entered the Zombie House. There are three doors ahead of you. Which door do you choose? "1", "2", or "3"? \n')
if choice1 == "1":
    print("You open the door and find a zombie waiting behind it. Game Over.")
elif choice1 == "2":
    print("You open the door and encounter another zombie. Game Over.")
elif choice1 == "3":
    print("You open the door and find an empty room. You notice a window. Do you try to 'open' the window or 'search' the room?")
    choice2 = input().lower()
    if choice2 == "open":
        print("You manage to open the window and escape. Congratulations! You survived!")
    elif choice2 == "search":
        print("While searching the room, you accidentally make noise and attract the attention of a zombie. Game Over.")
    else:
        print("You hesitate too long and the zombies find you. Game Over.")
else:
    print("You hesitate too long and the zombies find you. Game Over.")
