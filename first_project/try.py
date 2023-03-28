# def create_adder(x):
#     def adder(y):
#         print("y:", y)
#         return x+y

#     return adder


# add_15 = create_adder(15)

# print(add_15(10))


def dec(fun):
    def inner(*args, **kwargs):
        print("first")
        result = fun(*args, **kwargs)
        print("then")
        return result
    return inner


@dec
def hey(to_who):
    print(f"hey, {to_who}")
    return 1


rs = hey("you")
print(rs)
