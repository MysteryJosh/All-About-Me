import random

quotes = [
    ("The secret of getting ahead is getting started.", "Mark Twain"), ("The unexamined life is not worth living.", "Socrates"), ("Be yourself: everyone else is already taken.", "Oscar Wilde"), ("The way you get started is to quit talking and begin doing.", "Walt Disney"), ("If you're going through hell, keep going.", "Winston Churchill"), ("A journey of a thousand miles begins with a single step.", "Lao Tzu"), ("I have a dream.", "Martin Luther King Jr."), ("The only thing we have to fear is fear itself.", "Franklin D. Roosevelt"), ("Ask not what your country can do for you - ask what you can do for your country.", "John F. Kennedy"), ("To be or not to be, that is the question.", "William Shakespeare"),
]

quote, author = random.choice(quotes)

print(f'\n"{quote}"')
print(f"-{author}\n")




