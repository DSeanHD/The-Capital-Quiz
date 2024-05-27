import time

# Countries for the quiz
countries = [
  "the United States of America", "Jamaica", "Brazil", "New York", "California", "Nigeria", "Indonesia", 
  "Poland"
]

# Answers for each country
capitals = [
  "washington dc", "kingston", "brasilia", "albany", "sacramento", "abuja", "jakarta", "warsaw"
]

# Introduction
print("Hello, and welcome to the Capital Quiz!")
time.sleep(1)
print("The quiz where we tell you countries/states/provinces and you tell thier capital")
time.sleep(2)
name=input("What is your name? ")
print("Nice to meet you", name + "!")
time.sleep(1)

while True:
  try:
    age = int(input("How old are you? "))
    break
  except ValueError:
    print("Please enter a number")

if age <= 12:
  print("Ok so you're a kid")
elif age in range(13, 20):
  print("Ok so you're a teenager")
elif age in range(20, 60):
  print("Ok so you're an adult")
elif age >= 60:
  print("Ok so you're an elder")

#Instructions
time.sleep(1)
input("How are you feeling today? ")
print("Awesome!")
time.sleep(1)
print("Let's begin!")
time.sleep(1)
print("p.s.; when typing in the answers, please do not put any signs or periods etc. just the word. If the answer has two words, you can leave a space\n")

# Initialize the score
score = 0

# Keep track of index for the countries array
index = 0

# Display questions dynamically
for x in capitals:
  user_answer = input(f"What is the capital of {countries[index]}? ")

  if user_answer == x:
    print("Correct!")
    score += 1
  else:
    print("Incorrect, it's", x)
  
  index += 1

#Total Score
time.sleep(1)
print("You got", score ,"out of 8 in this quiz")
time.sleep(1)

percent = int((score / len(countries)) * 100)

print("Which means you got " + str(percent) + "%")
time.sleep(1)
print("I hope you guys enjoyed it :)")
print("Peace!")
