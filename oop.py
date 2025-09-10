#object orientated programming 

#construction of class
class ClassName:
    #constructor
    def __init__(self,attribute): #attrbiute passed in as paremeter during creation of object
        self.attribute = attribute

        #information hiding, restrict access to internal attributes through getters and setters
        #related to encapsulation, which involves restricting access to componets of objects
        #private attributes require getters and setters, which are methods, to access data of an object
    
        #single underscore, no practical use, just signal that attribute/ method for internal use 
        #self._attribute = attribute 
        
        #Dunder (private) attribute, which needs getters to access: 
        #self.__attribute = attribute

    #methods
        
    #getter; accessor
    def get_attribute(self):  
        print(self.attribute)

    #setter; mutator/ modifier
    def set_attribute(self, new_attribute): #pass new attribute in as parameter of setter
        self.attribute = new_attribute 

#creation of object (instance of a class)
object_name = ClassName(attribute)

#using methods
object_name.get_attribute()


#inheritence 
#legend: p means parent, c means child

#parent class is what a typical class looks like (see above)

#child class
#inherit all attributes and methods from parent  
class Child(Parent):
    def __init__(self,p_attribute, c_attribute): #p.attribute and c.attribute passed in as paremeter during creation of object
        #inheritence of attributes from parent class 
        super().__init__(p_attribute) #call constructor of parent class

        self.c_attribute = c_attribute #new attribute for child class

    #parent's methods also can use

    #define new method unique to child 
    def c_method(self): 
        print("this is a method only available to child")


#polymorphism: same method, different behaviour; override method
class Poly(Parent):
    def p_method(self):
        print("this is polymorphism")

