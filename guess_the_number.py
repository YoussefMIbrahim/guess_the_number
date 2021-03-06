import random

count = 0
correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    global count
    '''get user's guess'''
    count = count + 1
    try:
        return int(input('Guess the secret number? '))
    except:
        return print('not a valid number entered')


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        if result == "you guessed correctly!":
            print(result + " It took you " + str(count) + " attempt(s)!")
        else:
            print(result)

        if result == correct:
            break


if __name__ == '__main__':
    main()
