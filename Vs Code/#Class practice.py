#Class practice
class Dog():
    def __init__(self,dog_name,bread,size):
        self.dogname = dog_name
        self.bread = bread
        self.size = size
    def dogdets(self):
        print(f"hello my name is {self.dogname},\n I am a {self.size},{self.bread}")

my_dog1 = Dog("pipi ","begale ","meduim ")
my_dog1.dogdets()

