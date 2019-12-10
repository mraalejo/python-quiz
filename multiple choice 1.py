##Quiz multiple choice

score = 0
print('''
Q1 - How many digits are in the decimal number system??
a - 10
b - 9
c - unlimited
''')
answer = input().lower()

if answer == "a":
    score = score + 2
    print(" Correct!! :) Your new score is ", score)
elif answer == "b":
    print(" The answer is incorrect :( ")
elif answer == "c":
    print(" The answer is incorrect :( ")
else:
    print(" You didn't choose a, b or c, try again next time")

