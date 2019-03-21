class MyClass(object):
    i = 123
    def __init__(self,name):
        self.name = name

    def f(self):
        return 'hello ,' + self.name

use_class = MyClass('mazhao')

print('diaoyong',use_class.i)
print('wwwwwwww',use_class.f())