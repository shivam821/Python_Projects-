import random
import time

operators = ["+","-","*"]

min_operand = 3
max_operand = 12 

total_problems = 10

start_time = time.time()

def generate_problems() :
    left = random.randint(min_operand,max_operand)
    right = random.randint(min_operand,max_operand)
    operator = random.choice(operators)

    expression = str(left) + " " + operator + " " + str(right)

    # eval() is a built-in function that allows us to evaluate the Python expression as a 'string' and return the value as an integer.
    answer = eval(expression)
    return expression, answer

for i in range(total_problems) : 
    expression,answer = generate_problems()
    while True : 
        guess = input("Problem " + str(i+1) + ": " + str(expression) + " = ")
        if guess == str(answer) : 
            break

end_time = time.time()
total_time = round(end_time - start_time, 2)

print('Total Time : ', total_time + "seconds")
