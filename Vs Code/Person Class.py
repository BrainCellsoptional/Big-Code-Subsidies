class Person():
    def __init__(self,first,last,mb,role):
        self.first = first
        self.last = last 
        self.mb = mb 
        self.role = role

p1 = Person("Marry","poppins","021567567","walker")
print(p1.first)
p1.first = "Martha"
print(p1.first)