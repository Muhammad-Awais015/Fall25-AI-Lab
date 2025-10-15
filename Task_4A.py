def LUHN_Algorithm():
    card = input("Enter the card number: ")
    digits = [int(d) for d in card]
    check_digit = digits.pop()
    digits.reverse()
    total = 0
    for i in range(len(digits)):
        if i % 2 == 0:
            doubled = digits[i] * 2
            if doubled > 9:
                doubled -= 9
            total += doubled
        else:
            total += digits[i]
    total += check_digit
    if total % 10 == 0:
        print("It is a valid number ")
    else:
        print("It is an invalid number ")

LUHN_Algorithm()
