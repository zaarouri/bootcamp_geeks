from game import Game

def get_user_menu_choice():
    print("Menu:")
    print("1 - Play a new game")
    print("2 - Show scores")
    print("x - Exit")
    choice = input("Enter your choice: ").lower()
    if choice in ['1', '2', 'x']:
        return choice
    else:
        print("Invalid choice.")
        return None

def print_results(results):
    print("Game Results Summary:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("Thank you for playing!")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    while True:
        choice = get_user_menu_choice()
        if choice == '1':
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == '2':
            print_results(results)
        elif choice == 'x':
            print_results(results)
            break

if __name__ == "__main__":
    main()
