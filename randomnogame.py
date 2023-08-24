import random

def play_guessing_game():
    print("Welcome to the Guessing Game!")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Guess the number between 1 and 100: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

if __name__ == "__main__":
    play_guessing_game()
