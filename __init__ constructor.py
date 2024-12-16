class Dog:
    colour = "Black"

    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

    def info(self):
        return f"This is my Dog And its name is {self.name}, and its breed is {self.breed}"

dog1 = Dog("Buddy" , "bulldog")
dog2 = Dog("Max", "Golden Retriever")

print (dog1.info())
print (dog2.info())
print (Dog.colour)