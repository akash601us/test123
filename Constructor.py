class Person():
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('Hello, my name is', self.name)

p = Person('Akash')
p.say_hello()
p1 = Person('abc')
p2 = Person('def')
p3 = Person('sdf')
p1.say_hello()
p2.say_hello()
p3.say_hello()

class A(object):
    def __init__(self, something):
        print("A int called")
        self.something  = something

class B(A):
    def __init__(self, something):
        A.__init__(self, something)
        print("B int called")
        self.something = something

obj = B("somthing")
