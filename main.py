# First, install NLTK (Natural Language Toolkit) by running: pip install nltk

import nltk
from nltk.chat.util import Chat, reflections

# Pairs of patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hey there!"]],
    [r"what is your name?", ["I am a simple chatbot.", "My name is Bot, what's yours?"]],
    [r"how are you?", ["I'm doing well, how about you?"]],
    [r"i am (.*)", ["Nice to hear you're %1!"]],
    [r"what can you do?", ["I can chat with you!"]],
    [r"bye", ["Goodbye!", "See you later!"]],
]
