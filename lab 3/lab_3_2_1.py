def reducer(arg: tuple) -> tuple :
    return tuple(map(lambda item: item / sorted(filter(lambda div: arg[0] % div == 0 and arg[1] % div == 0, list(int(i) for i in range(1, arg[0]+1))), reverse=True)[0], arg))
print(reducer((21 ,49)))