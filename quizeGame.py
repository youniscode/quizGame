print("Welcome to Quize!")

playing = input("Do you want to play? ")

if playing != "yes":
  quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
  print("Correct!")
else:
  print("Incorrect!")