#first import the logo and print it
from art import logo,vs
import random
from replit import clear
from game_data import data
print(logo)
decision =0
score=0
#print(f"You are {decision}, your current score is {score}")

def format_data(random_choice):
  """ format name in printable form"""
  random_choice_Name = random_choice["name"]
  random_choice_Description = random_choice["description"]
  random_choice_Country = random_choice["country"]

  return f"{random_choice_Name}, a {random_choice_Description}, from {random_choice_Country}" 

def check_Answer(answer,Follower_CountA,Follower_CountB):
  """Takes the user answer and follower count and returns if the user guessed it correctly or not"""
  if Follower_CountA > Follower_CountB:
    if(answer == 'a'):
      return True
    else:
      return False
  else:
    if(answer =='b'):
      return True
    else:
      return False

game_should_continue = True
random_choiceB = random.choice(data)
#do this stuff repeatidly until the user get's wrong answer
while game_should_continue:

  #generate a random number

  random_choiceA = random_choiceB
  random_choiceB = random.choice(data)
  if random_choiceA == random_choiceB:
    random_choiceB = random.choice(data)

  print(f"Compare A: {format_data(random_choiceA)}")

  #print vs
  print(vs)

  print(f"Compare B: {format_data(random_choiceB)} ")

  #Ask user for a guessA
  
  answer = input("Who has more followers. A or B. Type 'A' or 'B'\n").lower()
  
  #Check if the user is right or wrong
  #get follower count of each account
  Follower_CountA = random_choiceA["follower_count"]
  Follower_CountB = random_choiceB["follower_count"]

  is_correct = check_Answer(answer,Follower_CountA,Follower_CountB)
  #Clear the screen
  clear()
  print(logo)
  # Give user feedback on their guess
  if is_correct:
    score = score+1
    print(f"You are right, Your current score is :{score}")
   
  else:
    print(f"Sorry! that's worng, your final score is: {score}")
    game_should_continue = False





