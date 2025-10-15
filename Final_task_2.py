# MiniProject 2:
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
def show_movies():
    print("\nMovies in the list:")
    for name, budget in movies:
        print(f"- {name}: {budget}")

def new_movie():
    num = int(input("How many movies do you want to add? "))
    for i in range(num):
        name = input("Enter movie name: ")
        budget = int(input("Enter movie budget: "))
        movies.append((name, budget))
    
def high_budget_movies():
    total_budget = 0
    for movie in movies:
        total_budget += movie[1]
    average_budget = total_budget / len(movies)
    print("\nAverage Budget:", average_budget)    
    count = 0
    for movie in movies:
        if movie[1] > average_budget:
            extra = movie[1] - average_budget
            print(movie[0], "is higher than average by", extra)
            count += 1
    print("\nNumber of movies above average:", count)    
    
def main():
    while True:
        num = int(input("\nChoose an option:\n 1) Show all movies\n 2) Add new movies\n 3) Show high budget movies\n 4) Exit"))
        if num == 1:
            show_movies()
        elif num == 2:
            new_movie()
        elif num == 3:
            high_budget_movies()
        elif num == 4:
            print("System is going down")
            break
        else:
            print("Invalid choice!")       
                    
main()



# MiniProject 1:
def show_rules():
    print("Welcome to FizzBuzz!")
    print("Rules:")
    print("- Say 'Fizz' for numbers divisible by 3")
    print("- Say 'Buzz' for numbers divisible by 5")
    print("- Say 'Fizz Buzz' for numbers divisible by both 3 and 5")
    print("- Otherwise, just type the number itself")
    

def fizz_buzz_game():
    print("The Game is started: ")
    print("To exit the game type exit: ")
    for i in range(1, 101):
        answer = input(f"{i}: ")

        if answer.lower() == "exit":
            print("Exiting the game.")
            return  

        if i % 3 == 0 and i % 5 == 0:
            correct = "Fizz Buzz"
        elif i % 3 == 0:
            correct = "Fizz"
        elif i % 5 == 0:
            correct = "Buzz"
        else:
            correct = str(i)

        if answer != correct:
            print(f"Wrong! The correct answer was: {correct}")
            print("Game Over!")
            return  

    print("Congratulations! You completed 100 rounds without mistakes!")

def main():
    show_rules()
    while True:
        choice = input("\nChoose an option \n 1) Start Game\n 2) Exit \n ")
        if choice == "1":
            fizz_buzz_game()
        elif choice == "2":
            print("System is going down.")
            break
        else:
            print("Invalid choice! Please try again.")

main()

