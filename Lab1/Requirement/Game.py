import random
from typing import Tuple, List

def guessing_game(max: int, *, attempts: int) -> Tuple[bool, Tuple[int, ...], int]: 
    """
    Generates a random number and asks the user to guess it within a limited number of attempts.
    
    Args:
        max (int): Maximum value for the random number (inclusive).
        attempts (int): Number of attempts allowed (keyword-only argument).
        
    Returns:
        Tuple[bool, Tuple[int, ...], int]: A tuple containing:
            - boolean: True if the user won, False otherwise.
            - tuple: The sequence of guesses made by the user.
            - int: The actual randomly chosen number.
    """
    chosen_int = random.randint(1, max)
    user_guesses: List[int] = []

    print(f"\nI have selected a number between 1 and {max}. You have {attempts} attempts.")

    while attempts > 0:
        val = input(f"Enter your guess ({attempts} attempts left): ")
        
        try:
            guess = int(val)
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue
        
        user_guesses.append(guess)
        
        if guess < chosen_int:
            print("Too low")
            attempts -= 1
        elif guess > chosen_int:
            print("Too high")
            attempts -= 1
        else:
            print("Correct!")
            return True, tuple(user_guesses), chosen_int

    print(f"Out of attempts. The number was {chosen_int}.")
    return False, tuple(user_guesses), chosen_int


def play_game() -> None:
    """
    The main game loop, handles win/loss logic
    """
    max_value: int = 20
    attempts: int = 5
    
    while True:
        has_won, guesses, chosen_int = guessing_game(max_value, attempts=attempts)

        if has_won:
            try:
                assert chosen_int in guesses
                print("System Check: Winning number verified in guesses.")
            except AssertionError:
                print("System Error: Winning number NOT found in guesses.")
            break
        else:
            try:
                assert chosen_int not in guesses
            except AssertionError:
                print("System Error: Winning number found in guesses despite loss.")
            
            retry = input("You lost. Would you like to play again? (yes/no): ").lower()
            if retry == "yes":
                continue
            else:
                break

if __name__ == "__main__":
    play_game()