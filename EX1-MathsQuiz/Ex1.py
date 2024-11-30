import random

def displayMenu():
    print("\n===============================")
    print("LEVELS OF CHALLENGE")
    print("===============================")
    print("\n===============================")
    print("1. Easy")
    print("\n===============================")
    print("2. Intermediate")
    print("\n===============================")
    print("3. Expert")
    print("===============================\n")

def decideOperation():
    return random.choice(['+', '-'])

def randomInt(level):
    ranges = {1: (0, 9), 2: (10, 99), 3: (1000, 9999)}
    return random.randint(*ranges[level])

def displayProblem(first, second, op):
    return int(input(f"\nSolve: {first} {op} {second}\nYour Answer: "))

def isCorrect(answer, correct):
    return answer == correct

def displayResults(score):
    print("\n===============================")
    print(f"Your final score is: {score}/100")
    if score >= 90:
        print("Grade: A+")
    elif score >= 80:
        print("Grade: A")
    elif score >= 70:
        print("Grade: B")
    elif score >= 60:
        print("Grade: C")
    else:
        print("Grade: F")
    print("===============================\n")

while True:
    displayMenu()
    level = int(input("Enter challenge level (1, 2, or 3): "))
    total = 0

    for i in range(1, 11):
        first, second, op = randomInt(level), randomInt(level), decideOperation()
        correct = eval(f"{first}{op}{second}")

        print(f"\nProblem {i}:")
        answer = displayProblem(first, second, op)

        if isCorrect(answer, correct):
            print("Correct!")
            total += 10
        else:
            print("Incorrect, Please try again!")
            retry = int(input(f"Retry: {first} {op} {second} = "))
            if isCorrect(retry, correct):
                print("Correct on second attempt!")
                total += 5
            else:
                print(f"Still wrong! The correct answer was {correct}.")

    displayResults(total)

    if input("Would you like to play again? (yes/no): ").strip().lower() != "yes":
        print("\nThanks for playing! Have a great day!")
        break
