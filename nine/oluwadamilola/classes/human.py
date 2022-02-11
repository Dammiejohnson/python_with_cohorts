class Human:
    def __init__(self, name, gender):
         self.name = name
         self.gender = gender
         self.age = 0
         self.height = 0
         self.complexion = "dark"
    def set_age (self, age):
        self.age = age
    def set_height (self, height):
        self.height = height
    def get_age(self):
        return self.age
    

person = Human("Dammy", "Female")
person.set_age(31)
print(person.get_age())
print(person.age)

