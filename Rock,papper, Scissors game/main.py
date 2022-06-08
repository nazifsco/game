import random

while True:
    player = input("Enter a choice ('R' for rock, 'P' for paper, 'S' for scissors): ")
    options = ["R", "P", "S"]
    cpu = random.choice(options)
    if player not in options:
        print("sorry Invalid Entry, Try Again")
        continue
    print(f"\nPlayer chose {player}, CPU chose {cpu}.\n")

    if player == cpu:
        print(f"Both players selected {player}. It's a tie!")
    elif cpu == "R":
        if cpu == "S":
            print("Rock beats scissors! You win!")
        else:
            print("Paper beats rock! You lose.")
    elif player == "P":
        if cpu == "R":
            print("Paper beats rock! You win!")
        else:
            print("Scissors beats paper! You lose.")
    elif player == "S":
        if cpu == "P":
            print("Scissors beats paper! You win!")
        else:
            print("Rock beats scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break