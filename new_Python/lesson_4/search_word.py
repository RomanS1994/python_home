import re

text = "to be or not to be an idiot. BE a good coder!"

def replace(x):
    return "*"* len(x.group())

def replace_spam_words(text, spam_words):

    # pattern = re.compile(r"idiot|coder|not")
    pattern = re.compile("|".join(spam_words))
    print(pattern)
    return re.sub(pattern, replace, text)


spam_words = ["idiot", "coder", "to", "an"]
moderated_text = replace_spam_words(text, spam_words)
print(moderated_text)