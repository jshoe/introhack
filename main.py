def main():
    user_name = input('\nHello, and welcome to the game. Prepare for an adventure!\nLoading game...\nPlease enter your name:\n')
    print("\nHello " + user_name + "!")
    start_scene()
    return

def start_scene():
    print("You are a student at UC Berkeley, and you have just been assigned a new CS project.")
    choices = ["Start now.", "Start later."]
    choice = user_decide(choices)
    if choice == 0:
        squirrel()
    if choice == 1:
        party()

def squirrel():
    print("Great! You are on your way to Soda when sUdDenly a wild squiRrel appears!!!")
    choices = ['Feed squirrel', 'Kick squirrel.']
    choice = user_decide(choices)
    if choice == 0:
        feed_squirrel()
    if choice == 1:
        kick_squirrel() 
    
def party():
    print("Instead of working you decide to go to a party!!")
    choices = ["It's a study party for a class more important than CS...", 'Turnt up!!']
    choice = user_decide(choices)
    if choice == 0:
        study_party()
    if choice == 1:
        turn_up()

def feed_squirrel():
    print("That squirrel bites you!!")
    choices = ["Bite it back!", "Head over to the Tang Center because you forgot to waive SHIP and your health is your number one priority."]
    choice = user_decide(choices)
    if choice == 0:
        bite_back()
    if choice == 1:
        tang()

def kick_squirrel():
    print("The squirrel thinks you're rood.")
    choices = ['Continue to Soda.', 'All this squirrel kicking makes you tired. You head home for a nap.']
    choice = user_decide(choices)
    if choice == 0:
        go_to_soda()
        nap()

def study_party():
    print("What?? A class more important than CS?? HAHAHA")
    choices = ['Yeah man I was jk!', "I'm delirious and I choose to stay at the study party."]
    choice = user_decide(choices)
    if choice == 0:
        jk()
    if choice == 1:
        stay()

def turn_up():
    print("Turn up for WHATT?")
    print("Not your grades!! You failed this class.")
    user_death()

def bite_back():
    print("Yumm... squirrel!")
    print("You die of salmonella.")
    user_death()

def tang():
    print("You decide that while you're here, you're going to try to appeal your waiver. You are denied again!")
    choices = ['Flip a table.', 'Calmly accept your fate.']
    choice = user_decide(choices)
    if choice == 0:
        table()
    if choice == 1:
        fate()

def jk():
    print("You think this is a joke?!")
    print("Ded.")
    user_death()

def stay():
    print("You fail CS because you're too busy study partying.")
    print("Ded.")
    user_death()

def table():
    print("You are kicked out of Tang and die of infection.")
    print("Ded.")
    user_death()

def fate():
    print("The table flips over anyway. You are kicked out of Tang for disturbing the peace.")
    print("You leave in pieces.")
    user_death()

def go_to_soda():
    print("You thought it was due at midnight today. But it was really due midnight yesterday.")
    print("Cry.")
    print("Cry more.")
    user_death()

def nap():
    print("You oversleep and miss the deadline!")
    print("Cry.")
    print("Creys.")
    user_death() 

def user_death():
    print("You have died and failed. Goodbye.")
    return

def user_decide(choices):
    list_choices(choices)
    choice = -1
    while ((choice != 0) and (choice != 1)):
        choice = input("\nWhat do you decide to do? Enter the number of your decision:\n")
        choice = int(choice) - 1
    return choice

def list_choices(choices):
    print("1) " + choices[0])
    print("2) " + choices[1])

def user_success():
    print("You have beat the game! Congratulations! Enjoy the rest of your day.")

main()
