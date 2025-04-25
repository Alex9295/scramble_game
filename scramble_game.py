# Import the random module to shuffle words and make random selections
import random

def scramble_word(word):
    """Scramble the letters of a word randomly"""
    # Convert the word into a list of characters for shuffling
    word_list = list(word)
    # Shuffle the letters randomly
    random.shuffle(word_list)
    # Join the shuffled letters back into a string
    return ''.join(word_list)

def play_game():
    # List of words that will be used in the game
    word_list = ["python", "developer", "programming", "algorithm", 
                "function", "variable", "debugging", "compiler", 
                "codechef", "machine", "bitcoin", "operation"]

    # Main game loop - continues until player chooses to exit
    while True:
        # Randomly select a word from the list
        original_word = random.choice(word_list)
        # Scramble the selected word
        scrambled = scramble_word(original_word)

        # Display game header and the scrambled word
        print("\nWelcome to the Word Scramble Game!")
        print(f"Scrambled word: {scrambled}")

        # Initialize attempts counter (3 tries per word)
        attempts = 3

        # Guessing loop for the current word
        while attempts > 0:
            # Get player's guess and convert to lowercase
            guess = input("Guess the word (or type 'exit' to quit): ").lower()

            # Check if player wants to exit
            if guess == "exit":
                print("Thanks for playing! Goodbye!")
                return  # Exit the game completely

            # Check if guess is correct
            if guess == original_word:
                print("Correct! You guessed it!\n")
                break  # Exit the guessing loop for this word
            else:
                # Decrement attempts and show remaining tries
                attempts -= 1
                print(f"Wrong guess. Attempts left: {attempts}")

        # If player used all attempts without guessing correctly
        if attempts == 0:
            print(f"Sorry, you ran out of attempts. The correct word was: {original_word}\n")

        # Ask if player wants to continue with another word
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break  # Exit the main game loop

# Standard Python idiom to check if this script is being run directly
if __name__ == "__main__":
    # Start the game
    play_game()
