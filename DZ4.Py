#Вычислить число c заданной точностью d
#Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


#k = 1
#d = 0
#for k in range(1, 1000000):
    #d = d+4*((-1)**(k+1))/(2*k-1)
#print(round(d,4))



#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

#num = int(input("Введите число: "))
#i = 2 
#lst = []
#old  = num
#while i <= num:
    #if num % i== 0:
        #lst.append(i)
        #num  //= i
        #i  = 2
    #else:
        #i += 1
#print("Простые множители числа  приведены в списке: {}".format(lst))



#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
#  исходной последовательности.

from random import randint
 
print('Введите натуральную степень k:')
k = int(input())
 
def write_file(st):
    with open('Task04.txt', 'w') as data:
        data.write(st)

 
def create_list(k):
    list = []
    for i in range(k + 1):
        list.append(randint(0, 101))    
    return list
    
def create_str(sp):
    list = sp[::-1]
    wr = ''
    if len(list) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                wr += '{}x^{}-i-1'.format (list[i], len(list))
                if list [i + 1] != 0:
                    wr += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                wr += '{}x'.format (list[i])
                if list[i + 1] != 0:
                    wr += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                wr += '{}=0'.format (list[i]) 
            elif i == len(list) - 1 and list[i] == 0:
                wr += ' = 0'
    return wr
 
koef = create_list(k)
write_file(create_str(koef))