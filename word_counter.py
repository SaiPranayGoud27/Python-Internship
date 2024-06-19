def count_words(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The input text to count words from.
    
    Returns:
        int: The number of words in the input text.
    """
    words = text.split()
    return len(words)

def main():
    """
    Main function to handle user input and display output.
    """
    print("Welcome to the Word Counter Program!")
    
    while True:
        # Prompt user to enter a sentence or paragraph
        user_input = input("Please enter a sentence or paragraph (type 'exit' to quit): ")

        # Check for exit condition
        if user_input.lower() == "exit":
            break

        # Check for empty input
        if not user_input:
            print("Error: Please enter some text.")
            continue

        # Count the number of words
        word_count = count_words(user_input)

        # Display the word count
        print(f"The input text contains {word_count} words.")

if __name__ == "__main__":
    main()