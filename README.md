# AI CHATBOT WITH NLP

# AI CHATBOT WITH NLP

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: KOLLURI BHANUTEJA

*INTERN ID*: CT08DF855

*DOMAIN*: PYTHON

*DURATION*: 8 WEEKS

*MENTOR*: NEELA SANTOSH

##In this project, I created a simple chatbot using Python and the Natural Language Toolkit (NLTK) library. The purpose of this chatbot is to understand some basic user inputs and respond accordingly. This was my first experience working with Natural Language Processing (NLP), and it helped me understand how machines can process and understand human language in a basic way.

First, I installed the NLTK library using pip. NLTK is a popular library in Python used for working with human language data. It provides tools for tokenization, lemmatization, and other text-processing functions. I also downloaded the necessary NLTK data, such as wordnet and omw-1.4, which are needed for lemmatization.

In my chatbot, I defined some simple categories of user inputs, also known as intents. For example, if a user says “hello” or “hi”, the chatbot recognizes that as a greeting intent. Other intents I included were goodbye, thanks, name, help, weather, and creator. Each intent has a few example phrases that the bot checks against when someone types a message.

To process the text, I used a tokenizer called TreebankWordTokenizer. This breaks the input sentence into individual words or tokens. Then I used a lemmatizer to convert words to their root form. For example, "running" becomes "run", which helps the bot understand variations of words.

I wrote a function called predict_intent() which checks what the user said and tries to match it to one of the known intents. It does this by comparing the tokens from the user input with the tokens from the example phrases. If it finds a match, it returns the intent. If nothing matches, it returns "unknown", and the chatbot replies with a message saying it doesn’t understand.

In the main part of the program, I created a chat loop where the bot keeps asking for user input until the user types "bye", "exit", or "quit". Based on the intent detected, the bot picks a random reply from a list of possible responses. This makes the chatbot feel more natural.

This project helped me understand how basic chatbot systems work. It is not connected to the internet or any AI model, so it can only understand the few patterns that I gave it. However, it was a great introduction to how NLP works. I now understand what tokenization and lemmatization mean, and how intent matching can be done using simple logic.

In the future, I would like to improve this chatbot by connecting it to more advanced NLP tools like spaCy or even a trained machine learning model. I might also add a GUI using tkinter or a web interface using Flask. But for now, this simple chatbot works well in both Jupyter Notebook and VS Code, and I am happy with how it turned out as a beginner project.


#OUTPUT

<img width="1092" height="354" alt="Image" src="https://github.com/user-attachments/assets/88683a57-ae2a-483f-981c-85aa2b59a34f" />
