# Import required libraries
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TreebankWordTokenizer
import random

# Download required data from NLTK (only once)
nltk.download('wordnet')      # For lemmatization
nltk.download('omw-1.4')      # Optional, improves lemmatization

# Create tokenizer and lemmatizer objects
tokenizer = TreebankWordTokenizer()
lemmatizer = WordNetLemmatizer()

# Define some simple question types (intents)
intents = {
    "greeting": ["hi", "hello", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "see you", "goodbye"],
    "thanks": ["thanks", "thank you"],
    "name": ["what is your name", "who are you"],
    "help": ["help", "what can you do", "how to use this bot"],
    "weather": ["how is the weather", "is it raining", "weather update"],
    "creator": ["who created you", "who made you", "your creator"]
}

# Define what the bot should reply for each type
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!"],
    "name": ["I'm a chatbot made using Python and NLTK.", "Call me ChatBot!"],
    "help": ["I can answer simple questions like 'hi', 'who are you', or 'what can you do'."],
    "weather": ["I'm not connected to weather data, but it looks fine to me!"],
    "creator": ["I was created by a beginner using Python and NLTK."]
}

# Function to understand what the user said
def predict_intent(user_input):
    user_input = user_input.lower()  # make input lowercase
    tokens = tokenizer.tokenize(user_input)  # break input into words
    lemmatized = [lemmatizer.lemmatize(token) for token in tokens]  # convert to base words

    # Check if the input matches any known pattern
    for intent, patterns in intents.items():
        for pattern in patterns:
            pattern_tokens = tokenizer.tokenize(pattern)
            pattern_lemmatized = [lemmatizer.lemmatize(token) for token in pattern_tokens]
            if set(pattern_lemmatized).issubset(set(lemmatized)):
                return intent
    return "unknown"  # if nothing matches

# The main chat loop
def chat():
    print("ChatBot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("ChatBot: Goodbye!")
            break
        intent = predict_intent(user_input)  # figure out the intent
        if intent in responses:
            print("ChatBot:", random.choice(responses[intent]))
        else:
            print("ChatBot: I don't understand that. Can you ask differently?")

# Start the chatbot
chat()
