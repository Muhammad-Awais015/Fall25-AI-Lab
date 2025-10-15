def remove_punctuations():
    text = input("Enter a string: ")
    punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
    result = ""
    for char in text:
        if char not in punctuations:
            result += char
    print("String without punctuations:", result)

remove_punctuations()
