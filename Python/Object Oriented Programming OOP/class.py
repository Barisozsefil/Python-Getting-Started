# Class                                => Person adında bir class tanımladık
class Person:
    # class attributes
    address = 'no information'

    # constructor (yapıcı metod)
    def __init__(self, name, year):    #=> Person Classımızın name ve yaş özellikleri olsun
        # object attributes
        self.name = name
        self.year = year


    # methods ekstra methods yazmadık bu yapıda..


# object (instance)
person1 = Person(name='ali', year= 1990)          #=> Person1 diye bir obje oluşturalım ve Person clasımızın özellikleriyle doldurduk burada 
person2 = Person(name ='yağmur', year = 1995)     #=> Person2 diye bir obje oluşturalım ve Person clasımızın özellikleriyle doldurduk burada 

# # updating
# person1.name = 'ahmet'
# person1.address = 'kocaeli' 

# accessing object attributes
print(f'person1 :name: {person1.name} year: {person1.year} address: {person1.address}')
print(f'person2 :name: {person2.name} year: {person2.year} address: {person2.address}')

print(person1)
print(person2)


