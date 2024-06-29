# Word Counter Program
# Function to count the number of words in a given text
def count_words(text):
    # Split the text into a list of words using spaces as delimiters
    words = text.split()
    # Return the number of words in the list
    return len(words)

# Prompt the user to enter a sentence or paragraph
user_input = input("Enter a sentence or paragraph: ")

# Check if the input is empty
if user_input.strip() == "":
    print("Error: Please enter some text.")
else:
    # Count the number of words in the input
    word_count = count_words(user_input)
    # Print the word count to the console
    print(f"Word count: {word_count}")
