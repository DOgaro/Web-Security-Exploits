import itertools
import string

def guess_password(real):
    charsL = string.ascii_lowercase + string.digits ##for lower case (aa - 37 guesses)
    charsU = string.ascii_uppercase + string.digits ##for upper case (AA - 37 guesses )
    charsAll = string.ascii_letters + string.digits ##for both upper and lower case (aA -89 guesses, Aa - 1675 guesses)
    charsR = string.digits + string.ascii_letters
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(charsAll, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return 'password is {}. found in {} guesses.'.format(guess, attempts)

            print(guess, attempts)

#pass the password to be cracked here
print(guess_password('A1k'))