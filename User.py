class Person:
    def __init__(self,name,email_address,liscence_number):
        self.name=name
        self.email_address=email_address
        self.liscence_number=liscence_number
    def __str__(self):
        return f"Hi, my name is {self.name}, my email and liscence number are {self.email_address}, {self.liscence_number}."
    #end of class
    
esmeralda=Person('Esmeralda', 'esm@gmail.org','7TFG321')
francisco=Person('Esmeralda', 'fran@gmail.org','123qwe567')
dennis=Person('Dennis', 'den@gmail.org','1qgsd5767')

print(esmeralda)
print(francisco)
print(dennis)