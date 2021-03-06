from functools import wraps, partial, reduce, singledispatch
import time
"""
Partial :: Fit in Partial arguments and later extend to other params.
"""


def test(a, b):
    print(f'I got {a} and I got {b}')


half_fun = partial(test, a=1)
half_fun(b=2)

""" 
Single Dispatch :: Example Regardless of Integer or String the fprint function will 
behave exactly same to user. 
"""


@singledispatch
def fprint(s):
    print('Hello: ' + s)


@fprint.register(int)
def _(s):
    print('Hello: ' + str(s))


@fprint.register(set)
@fprint.register(tuple)
@fprint.register(list)
def _(s):
    print('Hello: ' + ','.join(map(str, s)))


fprint({1, 2, 3, 4, 5})
fprint([1, 2, 3, 4, 5])
fprint(10)
fprint('Hello')


"""
Use of wraps decorator within the decorator to retain the some of the properties of original functions.
Ex - Following program prints the Docstring from actual functions : _list or _tupple not wrapper.
"""

def time_it(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        This is within the wrapper !
        """
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print(f'Time Taken By {func.__name__}  is : {t2 - t1}')
        return res

    return wrapper


my_list = [1, 2, 3, 4] * 10

@time_it
def _list():
    """
    This is within the original Function.
    """
    res = list(map(lambda x: x * 10, my_list))



@time_it
def _tupple():
    my_list1 = tuple(my_list)
    res = list(map(lambda x: x * 10, my_list1))


_list()
_tupple()
print(_list.__name__)
print(_list.__doc__)   


"""
Use of reduce in aggregations such as sum, multiply etc.  
Following example gives same result as : sum(my_list)
"""

my_list = [10,10,11,12,3000,9899]
print(reduce(lambda x,y : x+y, my_list))



