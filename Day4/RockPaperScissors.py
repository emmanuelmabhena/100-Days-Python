import random

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
---'   ____)____
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

choices = ["rock", "paper", "scissors"]
computer_choice_text = random.choice(choices)

player_choice_text = input("Enter rock, paper, or scissors: ").lower()

if player_choice_text not in choices:
    print("Invalid choice. Please enter rock, paper, or scissors.")
else:
    player_choice_index = choices.index(player_choice_text)
    computer_choice_index = choices.index(computer_choice_text)

    player_choice_art = [rock, paper, scissors][player_choice_index]
    computer_choice_art = [rock, paper, scissors][computer_choice_index]

    print(f"\nYou chose:\n{player_choice_art}")
    print(f"\nComputer chose:\n{computer_choice_art}")

    if player_choice_text == computer_choice_text:
        print("It's a draw!")
    elif (player_choice_text == "rock" and computer_choice_text == "scissors") or \
         (player_choice_text == "paper" and computer_choice_text == "rock") or \
         (player_choice_text == "scissors" and computer_choice_text == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
