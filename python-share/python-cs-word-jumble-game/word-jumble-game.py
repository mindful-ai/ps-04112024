import random

def load_words():
    # Load words from words.txt
    pass

def filter_words(words, difficulty):
    # filter words in to difficulty level: easy, medium, hard
    pass


def scramble_word(word):
    pass

def play_round(word):
    # Give three rounds: return True for correct guess or otherwise false
    pass


def game_setup():
    # Get user chocice for easy, medium, hard: return difficulty
    pass

def play_game():
    words = load_words()
    difficulty = game_setup()
    filtered_words = filter_words(words, difficulty)

    score = 0
    for word in random.sample(filtered_words, 5):  # Play with 5 words per session
        if play_round(word):
            score += 10  # Increase score for correct answer
        else:
            score -= 5   # Decrease score for incorrect

    print(f"Game Over! Your score is {score}.")

def main():
    while True:
        play_game()
        replay = input("Play again? (yes/no): ").lower()
        if replay != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
