def square(x:int) ->int:
    """
    Docstring - this function blah blah
    """
    result = x**2
    return result

a = square(5)
print(a)

# %%
def addition(a, b=5) :
    return a + b

print(addition(10),addition(10,2))
# %%
def func(*args) :
    return args[0]

print(func(1,2))

# %%
def func(**kwargs) :
    return kwargs["length"]/kwargs["time"]

velocity = func(length = 100, time = 10)
print(velocity)
# %%
class Animal :
    name:str=None
    weight:float=None

    def weight_in_grams(self) :
        msg=f'{self.name} weighs {self.weight*1000}'
        return msg

blah = Animal()
print(type(blah))    
# %%
blah.name="Alice"
blah.weight=2.5
blah.weight_in_grams()
# %%
class Dog(Animal) :
    breed:str=None

    def bark(self) :
        return "woof"
    
my_dog = Dog()

my_dog.bark()
# %%
