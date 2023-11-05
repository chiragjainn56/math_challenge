import random
import  time

OPERATORS = ["+","-","*"]
MINIMUM = 3
MAXIMUM = 12
TOTAL_PROBLEMS = 10

def problem_generator():
    left = random.randint(MINIMUM,MAXIMUM)
    right = random.randint(MINIMUM,MAXIMUM)
    operator = random.choice(OPERATORS)
    expr = str(left) + " "+ operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

input("Press enter to start!")
print("-------------")
start_time = time.time()
wrong = 0
for i in range(TOTAL_PROBLEMS):
    expr, answer = problem_generator()
    while True:
        guess = input("Problem #" + str(i+1) + " : " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1
end_time = time.time()
total_time = end_time - start_time
print("------------")
print("Congratulations! You finished in",round(total_time,2), "seconds")
