import time
#Introduction
print("Hello, and welcome to the Capital Quiz!")
time.sleep(2)
print("The quiz where we tell you countries/states/provinces and you tell thier capital")
time.sleep(3)
name=input("What is your name? ")
print("Nice to meet you", name, "!")
time.sleep(1)
age=int(input("How old are you? "))

if age<=11:
  print("Ok so you're a kid")
elif age in range(12, 17):
  print("Ok so you're a teenager")
elif age in range(18, 59):
  print("Ok so you're an adult")
elif age>=60:
  print("Ok so you're an elder")
else:
  int(input("Please enter your age as a number "))

#Instructions
time.sleep(1)
input("How are you feeling today? ")
print("Awesome!")
time.sleep(1)
print("Let's begin!")
time.sleep(1)
print("p.s.; when typing in the answers, please do not put any signs or periods etc. just the word. If the answer has two words, you can leave a space")
time.sleep(2)
print("You're also not allowed to use google and if you get a question wrong, we will take away one point")
#Scores
score = 0
print("Score:", score)
usa=input("What is the capital of the USA? ").lower()

#Quiz
if usa=="washington dc":
  print("Correct")
  score += 1
  print("Score", score)
else:
  print("Incorrect, it's Washington D.C.")
  score-=1
  print("Score", score)

time.sleep(1)
jamaica=input("What is the capital of Jamaica? ").lower()

if jamaica=="kingston":
  print("Correct")
  score+=1
  print("Score:", score)
else:
  print("Incorrect, it's Kingston")
  score-=1
  print("Score:", score)

time.sleep(1)
brazil=input("What is the capital of Brazil? ").lower()

if brazil=="brasilia":
  print("Correct")
  score+=1
  print("Score:", score)
else:
  print("Incorrect, it's Brasilia")
  score-=1
  print("Score:", score)

time.sleep(1)
new_york=input("What is the capital of New York? ").lower()

if new_york=="albany":
  print("Correct")
  score+=1
  print("Score:", score)
else:
  print("Incorrect, it's Albany")
  score-=1
  print("Score:", score)

time.sleep(1)
california=input("What is the capital of california? ").lower()

if california=="sacremento":
  print("Correct")
  score+=1
  print("Score:", score)
else:
  print("Incorrect, it's Sacremento")
  score-=1
  print("Score:", score)

time.sleep(1)
nigeria=input("What is the capital of Nigeria? ").lower()

if nigeria=="abuja":
  print("Correct")
  score+=1
  print("Score:", score)
else:
  print("Incorrect, it's Abuja")
  score-=1
  print("Score:", score)

time.sleep(1)
indonesia=input("What is the capital of Indonesia? ").lower()

if indonesia=="jakarta":
  print("Correct")
  score+=1
  print("Score", score)
else:
  print("Incorrect, it's Jakarta")
  score-=1
  print("Score:", score)

time.sleep(1)
poland=input("What is the capital of Poland? ").lower()

if poland=="warsaw":
  print("Correct")
  score+=1
  print("Score:", score)
else:
  print("Incorrect, it's Warsaw")
  score-=1
  print("Score:", score)

time.sleep(2)
print("You got", score ,"out of 8 in this quiz")
time.sleep(1)
print("Which means you got", (score / 8) * 100 ,"%")
time.sleep(1)
print("I hope you guys enjoyed it :)")
print("Peace!")