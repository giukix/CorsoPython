class Animal: 
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def walk(self):
       print("walking...")

class Cat(Animal): #subclass
    def purr(self):
        print("Purr...")
        
class Dog(Animal):
    def bark(self):
        print("Woof!")
    def walk(self):
        super().walk()
        print("...ma so anche correre...")
    

animale = Animal("Bobby", "white")
print("Colore dell'animale -> " + animale.color)

fido = Dog("Fido", "brown")
fido.bark()
fido.walk()

###########

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  #regular method
  def describe_book(self):
    print(self.title, 'by', self.author)

  #class method
  @classmethod
  def books_in_series(cls, series_name, number_of_books):
    print('There are', number_of_books, 'books in the', series_name, 'series')

# Creating an instance of Book
my_book = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")

# Using the instance method to describe the book
my_book.describe_book()

# Using the class method to display information about the series
Book.books_in_series("Harry Potter", 7)


#### PROTECTED ATTRIBUTES WITH UNDERSCORE ####
class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'protected'
    self._odometer = odometer  

  def describe_car(self):
    print(self.year, self.model)

  def read_odometer(self):
    print("Odometer:", self._odometer, "miles")

my_car = Car('Audi', 2020, 15000)

#accessing the protected attribute
print(my_car._odometer)



######### PRIVATE ATTRIBUTE WITH TWO UNDERSCORES #########
class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'private'
    self.__odometer = odometer  

  def describe_car(self):
    print(self.year, self.model)

  def read_odometer(self):
    print("Odometer:", self.__odometer, "miles")

my_car = Car('Audi', 2020, 15000)

#accessing the attribute within method
my_car.read_odometer()

#error
print(my_car.__odometer)

#accesing using name mangling (pratica non consigliata)
print(my_car._Car__odometer)


########## Anche i metodi possono diventare protected e privati
class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'private'
    self.__odometer = odometer  

  def _describe_car(self):  # Making the describe_car method 'protected'
    print(self.year, self.model)

  def __read_odometer(self):  # Making the read_odometer method 'private'
    print("Odometer:", self.__odometer, "miles")


my_car = Car('Audi', 2020, 15000)

#accessing protected method
my_car._describe_car()

#error when accessing a privete method
my_car.__read_odometer()
