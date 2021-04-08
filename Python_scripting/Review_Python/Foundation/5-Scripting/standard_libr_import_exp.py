import random

# create a password generator 

word_list = ['Canada', 'euphoria', 'vogmod']
def generator_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)
  