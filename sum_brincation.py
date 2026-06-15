# This is a sum of scores from a student. If the student scores more than 10, they pass. 
# If they score between 7 and 9 they receive another chance.
# If they score below 7 they fail.

input_receiver = input("Enter a sequence of numbers, separated by commas: ")

# def check_errors(input_receiver):
#     if not isdigit(input_receiver): 
#         Print("Burro do caralho, coloca um número") 

# check_errors(input_receiver)

numbers = input_receiver.split(",")

numbers = [int(number) for number in numbers]

# total = sum(numbers)

print(numbers)

print(type(numbers))

for number in numbers:
    print(type(number))

sum_numbers = 0
for number in numbers:
    sum_numbers += number

# print(sum_numbers)

score = sum_numbers

def pass_or_fail (score):
    if score >= 10:
        return "Congratulations, you passed! 🚀"
    if score < 7:
        return "You suck 🤡"
    else:
        return "You'll get another chance"
    
print(pass_or_fail(score))







