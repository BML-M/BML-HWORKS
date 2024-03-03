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
values_dict = {'a': 555, 'b': 44484, 'c': 4444}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ('YAHOO', 100)
print_params(*values_list_2, 42)
