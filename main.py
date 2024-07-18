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
import random

choices = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for rock 1 for paper and 2 for scissors: "))
computer = random.randint(0, 2)
print(f"You chose\n{choices[player]}")
print(f"Computer chose\n{choices[computer]}")

if player > 2 or player < 0:
  print("You typed an invalid number!")
elif player == 0 and computer == 2:
  print("You win!")
elif computer == 0 and player == 1:
  print("You win!")
elif computer > player:
  print("You lose!")
elif player > computer:
  print("You win!")
else:
  print("It's a draw!")






