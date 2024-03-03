from typing import Set


def print_params(a=1, b='строка', c=True):
    print(print_params)
    print(a)
    print(b)
    print(c)


print_params()
# noinspection PyTypeChecker
print_params(b=25)
# noinspection PyTypeChecker
print_params(c=[1, 2, 3])

values_list = ('to me', 45, 'years old')
values_dict = {1, 'строка',True}
print_params(*values_list,**values_dict)


