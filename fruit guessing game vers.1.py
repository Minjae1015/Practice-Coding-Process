import random

def play_fruit_guessing_game():
    # List of fruit words to choose from
    fruits = ["apple", "banana", "orange", "strawberry", "watermelon", "mango", 
              "pineapple", "blueberry", "kiwi", "papaya", "peach", "raspberry",
              "grape", "lemon", "lime", "cherry", "coconut", "dragon fruit"]
    
    # Pick a random fruit
    fruit = random.choice(fruits).upper()
    fruit_length = len(fruit)
    guessed_letters = set()
    correct_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("=" * 50)
    print("🍎 FRUIT WORD GUESSING GAME! 🍌")
    print("=" * 50)
    print("Guess the fruit by entering one letter at a time.")
    print(f"You have {max_incorrect} incorrect guesses allowed.\n")
    
    # Game loop
    while incorrect_guesses < max_incorrect:
        # Display the word with guessed letters
        display_fruit = ""
        for letter in fruit:
            if letter in correct_letters:
                display_fruit += letter + " "
            else:
                display_fruit += "_ "
        
        print(f"Fruit: {display_fruit}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) or 'None'}")
        print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect}")
        print()
        
        # Check if player won
        if all(letter in correct_letters for letter in fruit):
            print("🎉 CONGRATULATIONS! You guessed the fruit:", fruit)
            print("You WIN!")
            break
        
        # Get player's guess
        guess = input("Guess a letter: ").upper()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter!\n")
            continue
        
        if guess in guessed_letters:
            print("⚠️  You already guessed that letter!\n")
            continue
        
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in fruit:
            correct_letters.add(guess)
            print(f"✅ Good! '{guess}' is in the fruit!\n")
        else:
            incorrect_guesses += 1
            print(f"❌ Sorry! '{guess}' is not in the fruit.\n")
    
    # Check if player lost
    if incorrect_guesses >= max_incorrect:
        print("=" * 50)
        print("GAME OVER! You lost!")
        print(f"The fruit was: {fruit}")
        print("=" * 50)
    
    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes" or play_again == "y":
        print("\n")
        play_fruit_guessing_game()
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    play_fruit_guessing_game()
