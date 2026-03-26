# --------------------------------------
# ROCK PAPER SCISSORS GAME
# --------------------------------------

import random

# ASCII art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]


def play_game():
    try:
        user_choice = int(input("\nType 0 for Rock, 1 for Paper, 2 for Scissors: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number (0, 1, or 2).")
        return

    if user_choice not in [0, 1, 2]:
        print("❌ Invalid choice! You lose.")
        return

    print("\nYou chose:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)

    print("Computer chose:")
    print(game_images[computer_choice])

    # Game logic
    if user_choice == computer_choice:
        print("🤝 It's a draw!")

    elif user_choice == 0 and computer_choice == 2:
        print("🎉 You win!")

    elif user_choice == 2 and computer_choice == 0:
        print("😢 You lose!")

    elif user_choice > computer_choice:
        print("🎉 You win!")

    else:
        print("😢 You lose!")


# Game loop
while True:
    play_game()
    again = input("\nDo you want to play again? (y/n): ").lower()
    if again != 'y':
        print("👋 Thanks for playing!")
        break