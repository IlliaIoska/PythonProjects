numOfTests = int(input("Number of Test: "))
while(numOfTests > 0):
    numOfTests -= 1
    num1 = int(input("First num: "))
    num2 = int(input("Second num: "))
    sum = num1 + num2
    match_num = 0
    while(sum > 0):
        remainder = sum % 10
        if (remainder == 0):
            match_num += 6
        elif (remainder == 1):
            match_num += 2
        elif (remainder == 2):
            match_num += 5
        elif (remainder == 3):
            match_num += 5
        elif (remainder == 4):
            match_num += 4
        elif (remainder == 5):
            match_num += 5
        elif (remainder == 6):
            match_num += 5
        elif (remainder == 7):
            match_num += 3
        elif (remainder == 8):
            match_num += 7
        elif (remainder == 9):
            match_num += 6
        
        sum = int(sum/10)
    print(match_num)