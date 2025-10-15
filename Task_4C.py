def bubble_sort_sentence():
    text = input("Enter a sentence: ")
    words = text.split()
    print(words)
    n = len(words)
    new = " "

    for i in range(n):
        for j in range(0, n - i - 1):
            if words[j] > words[j + 1]:
                words[j], words[j + 1] = words[j + 1], words[j]       

    print("Sorted sentence:",new.join(words))

bubble_sort_sentence()
