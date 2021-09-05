import random
def game():
    progress = True
    word = ['orange', 'limon', 'potato']
    lifes = 3
    word_in_play = get_word (word)
    transform = start_transform (word_in_play)
    welcome_speech(list_to_string_convert(transform))
    while progress:
        user_guess = user_input()
        transform = build_transform(transform, word_in_play, user_guess)
        guessed = list_to_string_convert(transform)
        print_result(guessed)
        progress = check_win(guessed)

        if not check_mistake(word_in_play, user_guess):
            print(f'Remain {lifes} attemmpts')
            lifes = check_attempt(lifes)
        
        if lifes ==0:
            lose_speech()
            break
        if not progress:
            win_speech()
        

def get_word(w):
    # random.choice - выбирает в делимом объекте случайный объект
    # random.shuffle - изменяет делимый и изменяемый объект случайным образом перемешивая значения
    return random.choice(w)

def start_transform(w):
    t = []
    for l in w:
        t.append('_')
    return t

def welcome_speech(t):
    print(f'''
    welcome to hangman {t} pls guess the word
    ''')

def list_to_string_convert(t):
    s = ''
    return s.join(t)

def user_input():
    letter = input('print letter ')
    return letter

def build_transform(t,w,g=''):
    if g in w:
        for i in range(len(w)):
            let = w[i]
            if let == g:
                t[i] = let
    return t                       

def print_result(g):
    print('result =', g)

def check_win(g):
    if '_' in g:
        return True
    else: 
        return False

def check_mistake(w,g):
    if g not in w:
        return False
    else: 
        return True

def check_attempt(life):
    life -= 1
    return life
def lose_speech():
    print(f'loser, game over')
def win_speech():
    print(f'very good, you win')


game()
