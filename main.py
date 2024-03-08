def test_Muxa(*args):
    print('test_Muxa')
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print(i, arg)


test_Muxa('привет', 'я думаю', ' если я все правильно понял', 2, 2444, 5.6, 3.5, 188)


def test_Muxa_2(n):
    if n == 1:
        return 1
    test_Muxa_3 = test_Muxa_2(n=n - 1)
    return n * test_Muxa_3


print(test_Muxa_2(45))
