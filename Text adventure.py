def story_game():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself standing in front of two doors.")

    choice = input("Do you enter 'door 1' or 'door 2'? ").lower()

    if choice == 'door 1' or '1':
        print("\nYou enter door 1 and find a treasure chest!")
        print("Do you open the chest or leave it alone?")
        choice = input("Type 'open' or 'leave': ").lower()

        if choice == 'open':
            print("\nYou found a pile of gold coins! Congratulations, you're rich!")
        elif choice == 'leave':
            print("\nYou decide not to risk it and leave the treasure chest alone.")
            print("You proceed to explore further.")
        else:
            print("\nInvalid choice. You stand there undecided.")

    elif choice == 'door 2' or '2':
        print("\nYou enter door 2 and encounter a ferocious dragon!")
        print("Do you 'fight' the dragon or 'run away'?")
        choice = input("Type 'fight' or 'run away': ").lower()

        if choice == 'fight':
            print("\nYou bravely fight the dragon and defeat it!")
            print("You emerge victorious!")
        elif choice == 'run away':
            print("\nYou quickly turn around and run for your life!")
            print("You manage to escape the dragon's lair, shaken but safe.")
        else:
            print("\nInvalid choice. The dragon eyes you suspiciously.")

#stop play from making errors
    else:
        print("\nYou hesitate at the doors and decide to turn back.")
        print("The adventure awaits another day.")

# Run the game
story_game()
