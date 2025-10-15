equation = input ("Enter the equation")
solution = "a/b*c+d-e"
if "/" in equation:
    if "/" in equation:
        for index, char in enumerate(equation):
            div = int(equation[index-1]) / int(equation[index+1])
            solution = solution.replace( "a/b" , div )
    else:
        solution = solution.replace( "a/b" , "1" )
if "*" in equation:
    if "*" in equation:
        for index, char in enumerate(equation):
            mul = int(equation[index-1]) / int(equation[index+1])
            solution = solution.replace( div*"c" , mul )
    else:
        solution = solution.replace( "b*c" , "1" )
if "+" in equation:
    if "+" in equation:
        for index, char in enumerate(equation):
            add = int(equation[index-1]) / int(equation[index+1])
            solution = solution.replace( mul+"d" , add )
    else:
        solution = solution.replace( "c+d" , "1" )        
if "-" in equation:
    if "-" in equation:
        for index, char in enumerate(equation):
            sub = int(equation[index-1]) / int(equation[index+1])
            solution = solution.replace( add - "e", sub )
    else:
        solution = solution.replace( "d-e" , "0" )        
else:
    print(f"there is a problem in equation:{equation}")        

       

# eqution= input()
# num = eqution
# for index, char in enumerate(num):
#     if char == "+":
#         print(int(num[index-1]) + int(num[index+1]))
#     elif char == "-":
#         print(int(num[index-1]) - int(num[index+1]))
#     elif char == "*":
#         print(int(num[index-1]) * int(num[index+1]))    
#     elif char == "/":
#             print(int(num[index-1]) / int(num[index+1]))    
#     else:
#          print("it contain anyother operater problem") 