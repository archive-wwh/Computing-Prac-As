#construction of class
class ClassName:
    def __init__(self,attribute): #attrbiute passed in as paremeter during creation of object
        self.attribute = attribute

        #encapsulation:
        #information hiding, restrict access to internal attributes through getters and setters

        #single underscore, no practical use, just signal attribute/ method for internal use 
        #self._attribute = attribute 
        
        #Dunder (private) attribute, which needs getters to access: 
        #self.__attribute = attribute

    #method 
    def get_attribute(self): #getter 
        print(self.attribute)

#creation of object (instance of a class)
object_name = ClassName(attribute)

#using methods
object_name.get_attribute()


#inheritence 
#legend: p means parent, c means child

#parent class is what a normal class looks like

#child class
#inherit all attributes and methods from parent  
class Child(Parent):
    def __init__(self,p_attribute, c_attribute): #p.attribute and c.attribute passed in as paremeter during creation of object
        #inheritence of attributes from parent class 
        super().__init__(p_attribute)

        self.c_attribute = c_attribute #new attribute for child class

    #parent's methods also can use

    #define new method unique to child 
    def c_method(self): 
        print("this is a method only available to child")


#polymorphism: same method, different behaviour; override method
class Poly(Parent):
    def p_method(self):
        print("this is polymorphism")
