
######### Clousure
# def outter(tag):
#     def inner(content):
#         text = "<{0}>{1}</{0}>".format(tag,content)
#         return text
#     return inner

# my_tag_h1 = outter("h1")
# my_text1 = my_tag_h1("Content1")
# my_text2 = my_tag_h1("Content2")
# print(my_text1)
# print(my_text2)

# my_tag_p = outter("p")
# my_text3 = my_tag_p("P1")

# print(my_text3)

# #decorator

# def mydeco(outter_func):
#     print('outter {}'.format(outter_func.__name__))
#     b = 100
#     def wrapper(*arg, **kwg):
#         print(arg[0])
#         wrap = outter_func(*arg, **kwg)
#         print('inner {}'.format(outter_func.__name__))
#         return wrap
#     return wrapper


# @mydeco 
# def my_func(hello):
#     print(hello)

# my_func(100)


# def anotherdeco(outter_func):
#     print('decorating')
#     return outter_func

# @anotherdeco
# def my_func2(hi):
#     print(hi)

# my_func2('Hi')


class mydeco(object):
    def __init__(self, outter_func):
        super().__init__()
        self.mimic_func = outter_func

    def __call__(self, *arg, **kwg):
        print(arg[0])
        wrap = self.mimic_func(*arg, **kwg)
        print('__call__ {}'.format(self.mimic_func.__name__))



@mydeco 
def my_func(hello, world):
    print(hello, world)

my_func('Hello', 'World')