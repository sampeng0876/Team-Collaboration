import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import nltk
from nltk.chat.util import Chat, reflections

# Read the patterns and responses from the Excel file
df = pd.read_excel('QA.xlsx')
patterns = df['Pattern'].values.tolist()
responses = df['Response'].values.tolist()

# Preprocess patterns for fuzzy matching
processed_patterns = [pattern.lower() for pattern in patterns]

# Create a chatbot instance
chatbot = Chat([], reflections)

# Function to find the best pattern match
def find_best_match(user_input):
    best_score = 0
    best_match = None

    for pattern, response in zip(processed_patterns, responses):
        score = fuzz.ratio(user_input.lower(), pattern)
        if score > best_score:
            best_score = score
            best_match = response

    return best_match

# Run the chatbot
while True:
    user_input = input("> ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break

    response = find_best_match(user_input)
    if response:
        print("Chatbot:", response)
    else:
        print("Chatbot: Sorry, I couldn't understand your question.")
