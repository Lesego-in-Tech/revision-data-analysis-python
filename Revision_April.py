#Lesego Mongalo 56546920
incorrect_input_count = 0
def validateInput(i):
    
    global incorrect_input_count
    
    value = input(f"Enter value {i}: ")
    while value.isdigit() == False or int(value) <= 0 :
        incorrect_input_count += 1
        value = input(f"Please enter a valid numerical value.\nEnter value {i}: ")
    value = int(value)
    return value

def checkEvenOdd(highest) :
    if highest % 2 == 0:
        print("The highest value is even.")
    else:
        print("The highest value is odd.")

def displayResults(total, average, highest):
    print(f"\nIncorrect input count: {incorrect_input_count}")
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Highest: {highest}")

def main():
    total = 0
    number_1 = validateInput(1)
    total += number_1
    highest = number_1

    number_2 = validateInput(2)
    total += number_2
    if highest < number_2:
        highest = number_2

    number_3 = validateInput(3)
    total += number_3
    if highest < number_3:
        highest = number_3

    number_4 = validateInput(4)
    total += number_4
    if highest < number_4:
        highest = number_4

    number_5 = validateInput(5)
    total += number_5
    if highest < number_5:
        highest = number_5
    
    
    average = total / 5
    displayResults(total, average, highest)
    checkEvenOdd(highest)

main()

