import sys
import random 
sys.stdout = open('D:/python/new_f', 'w')
print('print start')
user_input = input()
    # with open('new_f', 'w+') as rand:
    #     # write_data = txt
    #     rand.write(txt)
    #     print(txt)
# print(write_data)

def game():
    random_number = random.randint(1,100)
    print('I create a random number, try to guess it')
    progress = True
    while progress == True:
        guess = int(input())
        if guess > random_number:
            print ('your guess > then my guess on', guess - random_number)
        if guess < random_number:
            print('your number < then my guess on', random_number - guess)
        else: 
            progress = False
    return str()
game()
sys.stdout.close()
#я пробовал сделать весь вывод из консоли в файл, и получилось, но он не принимает инпуты
