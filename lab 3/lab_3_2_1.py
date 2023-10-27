def reducer(arg: tuple) -> tuple:    
    dividers = list(int(i) for i in range(1, arg[0]+1))
    filtred = list(filter(lambda div: arg[0] % div == 0 and arg[1] % div == 0, dividers))    
    m, n = map(lambda item: item / sorted(filtred, reverse=True)[0], arg)
    ZeroDivisionError = m/n 
    return (m,n)

while True:
    try:
        print(reducer(tuple(int(i) for i in list(input().split()))))
    except ValueError:
        print('Несоответствие формата данных')
    except ZeroDivisionError:
        print('Деление на ноль')
    except IndexError:
        print('Неверное количество аргументов')