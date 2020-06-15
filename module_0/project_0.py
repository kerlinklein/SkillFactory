#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
count = 0                            # счетчик попыток
number = np.random.randint(1, 101)    # загадали число
print("Загадано число от 1 до 100")

while True:                        # бесконечный цикл
    predict = int(input())         # предполагаемое число
    count += 1                     # плюсуем попытку
    if number == predict:
        break    # выход из цикла, если угадали
    elif number > predict:
        print(f"Угадываемое число больше {predict} ")
    elif number < predict:
        print(f"Угадываемое число меньше {predict} ")

print(f"Вы угадали число {number} за {count} попыток.")


# In[2]:


number = np.random.randint(1,101)    # загадали число
print ("Загадано число от 1 до 100")
for count in range(1,101):         # более компактный вариант счетчика
    if number == count: break    # выход из цикла, если угадали      
print (f"Вы угадали число {number} за {count} попыток.")


# In[3]:


def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1,101) # предполагаемое число
        if number == predict: 
            return(count) # выход из цикла, если угадали
        
        


# In[21]:


import numpy as np

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    number = np.random.randint(1,101)
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадали

score_game(game_core_v2)


# In[59]:


import numpy as np

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток",count_ls)
    return(score)

def game_core_my(number):
    '''Для увеличения скорости сходимости будем идти к искомому числу с шагом половины разницы между этими числами'''
    count = 1
    predict =  50 # берем среднее чесло между 1 и 100
    
    while number != predict:
        count+=1
        if number > predict: # проверка, если наше число больше, чем угадываемое,
            predict += int((number - predict)/2) # то увеличиваем наше число на среднее значение между искомым и нашим числом
            if number - predict == 1: # когда мы подошли уже на единицу к искомому числу, то чтобы избежать зацикливания (int от 1/2 всегда 0) 
                if count >= 3: # проверка на "длительность" поиска (если изначально искомое число отличается от нашего меньше, чем на 2)
                    return(count+1) # выходим из цикла
                else:
                    return(count) # если загаданное число отличается от нашего на единицу - мы всегда угадываем его за 2 попытки
        elif number < predict: # проверка, если наше число больше, чем угадываемое,
            predict -= int((predict - number)/2)# то уменьшаем наше число на среднее значение между искомым и нашим числом
            if predict - number == 1: # когда мы подошли уже на единицу к искомому числу, то чтобы избежать зацикливания (int от 1/2 всегда 0) 
                if count >= 3:
                    return(count+1) # выходим из цикла
                else:
                    return(count) # если загаданное число отличается от нашего на единицу - мы всегда угадываем его за 2 попытки
    return(count) # выход из цикла, если угадали

score_game(game_core_my)


# In[1]:


import numpy as np


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


def game_core_my(number):
    '''Для увеличения скорости сходимости будем идти к искомому числу с шагом половины разницы между этими числами'''
    count = 1
    predict = 50  # "наше" число - берем среднее число между 1 и 100

    while number != predict:
        count += 1
        if number > predict:                     # Проверка, если наше число больше, чем искомое,
            predict += int((number - predict)/2) # то увеличиваем наше число на среднее значение между искомым
                                                 # и нашим числом.
            if number - predict == 1:            # Когда мы подошли уже на единицу к искомому числу, то чтобы избежать
                                                 # зацикливания (int от 1/2 всегда 0),
                if count >= 3:                   # при условии проверки на "длительность" поиска (если изначально искомое
                                                 # число отличается от нашего меньше, чем на 2) -
                    return(count+1)              # выходим из цикла, добавляя еще одну попытку.
                else:
                    return(count)                # Если загаданное число отличается от нашего на единицу -
                                                 # мы всегда угадываем его за 2 попытки.
        elif number < predict:                   # Проверка, если наше число больше, чем искомое,
            predict -= int((predict - number)/2) # то уменьшаем наше число на среднее значение между искомым
                                                 # и нашим числом.
            if predict - number == 1:            # Когда мы подошли уже на единицу к искомому числу, то чтобы избежать
                                                 # зацикливания (int от 1/2 всегда 0),
                if count >= 3:                   # при условии проверки на "длительность" поиска (если изначально искомое
                                                 # число отличается от нашего меньше, чем на 2) -
                    return(count+1)              # выходим из цикла, добавляя еще одну попытку.
                    
                else:                            # если загаданное число отличается от нашего на единицу -
                    return(count)                # мы всегда угадываем его за 2 попытки
                    
    return(count)                                # выход из цикла, если угадали число с первого раза (number = 50)


score_game(game_core_my)


# In[62]:


def int_r(num):
    ''' Из-за отсутсвия функции математического округления в Python 3 - пишем соответствующую функцию вручную'''
    num = int(num + (0.5 if num > 0 else -0.5))
    return num

print(int_r(0.49))


# In[ ]:




