##Simple Score - True or False

#set score to 0
score = 0

##Question 1
print("Gold is expensive, true or false? ")
answer = input()

if answer == "true":
    score = score + 1
    print("Score = ", score)
else:
    score = score + 0
    print("New Score = ", score)

##Question 2
print("Obama is the UK Prime Minister, true or false?")
answer = input()

if answer == "false":
    score = score + 1
    print("New Score = ", score)
else:
    score = score + 0
    print("New Score = ", score)

##Question 3
print("There are 26 letters in English Alphabet, true or false? ")
answer = input()

if answer == "true":
    score = score + 1
    print("New Score = ", score)
else:
    score = score + 0
    print("New Score = ", score)

##Question 4
print("Binary numbers are only 1 and 0, true or false? ")
answer = input()

if answer == "true":
    score = score + 1
    print("New Score = ", score)
else:
    score = score + 0
    print("New Score = ", score)

##Question 5
print("Lithium has the atomic number 17, true or false? ")
answer = input()

if answer == "false":
    score = score + 1
    print("New Score = ", score)
else:
    score = score + 0
    print("New Score = ", score)


print("Thank you for playing! Your final score is", score, "out of 5")
