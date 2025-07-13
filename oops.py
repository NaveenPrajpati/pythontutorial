class Student:
    name='naveen'
    roll=123
    language='hindi'

    def __init__(self,name,roll,language): ## dunder method
        self.name=name
        self.roll=roll
        self.language=language
        print('calling class')

    def printlanguage(self):
        print(f'this is language {self.language}')

    @staticmethod
    def greet():
        print('hello ')


# st= Student()
# print(st.name)
# st.printlanguage()
# st.greet()
st2=Student('rohan',34,'english')
print(st2.name)