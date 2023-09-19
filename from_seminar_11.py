from time import time

class MyString(str):
    """It is special strind to safe strind with author name and to add info. about time of creation"""
    def __new__(cls, st, author_name):
        """Creating string on base string Python class with additional params: author_name and time"""
        instance = super().__new__(cls, st)
        instance.author_name = author_name
        instance.st = st
        instance.time_ = time()
        return instance
    def __str__(self):
        return f'String "{self.st}", written by author "{self.author_name}" at {self.time_}'
    def __repr__(self):
        return f'MyString"({self.st}, "{self.author_name}", {self.time_})'

stroks = MyString('lalala', 'Nastya')
print(f'{stroks = }, "{stroks.author_name = }", {stroks.time_ = }')
print(stroks)

class Archive:
    """"This class for archiveng previous params"""
    _instance = None

    def __new__(cls, number: int, string: str):
        """Creating class on base string with list of numbers and list of strings previous data"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.numbers = []
            cls._instance.strings = []
        else:
            cls._instance.numbers.append(cls._instance.number)
            cls._instance.strings.append(cls._instance.string)
        return cls._instance

    def __init__(self, number: int, string: str):
        """Inintialasation of obj with number, string"""
        self.number = number
        self.string = string

    def __str__(self):
        """Printing method for user"""
        return f'{self.number}, {self.string} ({self.numbers}, {self.strings})'

    def __repr__(self):
        """Printing method for developer"""
        return f'Archive({self.number}, "{self.string}")'


# help(MyString)
# help(Archive)
a= Archive(4,'dfdf')
print(f'{a=}')


class Rectangle:
    """Class of Rectangle with lenght and width"""
    def __init__(self, length: float, width: float = None):
        """Instanse inintialisation with lenght(neccessary param) and width (additional param)"""
        self.length = length
        self.width = length if width is None else width

    def peri(self):
        """Calculation of rectangle perimeter"""
        return (self.width + self.length) * 2
    def area(self):
        """Calculation of rectangle Area"""
        return self.width * self.length

    def __sub__(self, other):
        """Subtraction Calculation of rectangles"""
        res = (self.peri() - other.peri())/4
        if res >=0:
            return Rectangle((self.peri() - other.peri())/4)
        else:
            raise ValueError

    def __add__(self, other):
        """Adding Calculation of rectangles"""
        if isinstance(other, Rectangle):

            return Rectangle(self.width + other.width, self.length + other.length)
        else:
            raise TypeError

    def __eq__(self, other):
        """Logic operation of equality"""
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        else:
            raise TypeError

    def __lt__(self, other):
        """Logic operation of less than"""
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            raise TypeError

    def __str__(self):
        """Printing method for user"""
        return f'Rectangle(widht = {self.width}, length = {self.length})'

    def __repr__(self):
        """Printing method for developer"""
        return f'Rectangle({self.width}, {self.length})'
rect1 = Rectangle(2)
rect2 = Rectangle(3,5)
print(rect1.peri())
print(rect1.area())
rect3= rect2 - rect1
print(rect3, f'{rect3.width = }')

print(rect3 != rect2)
print(rect1)
print(f'{rect1=}')

