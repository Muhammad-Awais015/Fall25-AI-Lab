equation = input("Enter the equation: ")  
solution = equation


if "/" in solution:
    for index, char in enumerate(solution):
        if char == "/":
            div = int(int(solution[index-1]) / int(solution[index+1]))
            d = (solution[index-1:index+2])
            solution = solution.replace(d, str(div))


if "*" in solution:
    for index, char in enumerate(solution):
        if char == "*":
            mul = int(solution[index-1]) * int(solution[index+1])
            m = solution[index-1:index+2]
            solution = solution.replace(m, str(mul))


if "+" in solution:
    for index, char in enumerate(solution):
        if char == "+":
            add = int(solution[index-1]) + int(solution[index+1])
            a = solution[index-1:index+2]
            solution = solution.replace(a, str(add))

if "-" in solution:
    for index, char in enumerate(solution):
        if char == "-":
            sub = int(solution[index-1]) - int(solution[index+1])
            s = solution[index-1:index+2]
            solution = solution.replace(s, str(sub))

print("Final Solution:", solution)
