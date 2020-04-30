
######### Clousure
def outter(tag):
    def inner(content):
        text = "<{0}>{1}</{0}>".format(tag,content)
        return text
    return inner

my_tag_h1 = outter("h1")
my_text1 = my_tag_h1("Content1")
my_text2 = my_tag_h1("Content2")
print(my_text1)
print(my_text2)

my_tag_p = outter("p")
my_text3 = my_tag_p("P1")

print(my_text3)

#decorator

def mydeco(outter_func):
    print('decorating')
    def wrapper(a):
        print('wrapping')
        return outter_func(a)
    return wrapper


@mydeco
def my_func(hello):
    print(hello)

my_func("Hello world")


def anotherdeco(outter_func):
    print('decorating')
    return outter_func

@anotherdeco
def my_func2(hi):
    print(hi)

my_func2('Hi')