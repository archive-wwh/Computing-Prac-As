#IMPORTANT:
#NEED HAVE self INSIDE EACH METHOD
#USE self.attribute OR self.method TO ACCESS ATTRIBUTES OR METHODS RESPECTIVELY INSIDE A CLASS (attributes can be called outside of class, depends on if attributes are private or public)


#construction of class

class ClassName:
    #constructor
    def __init__(self, attribute1, attribute2 = "value"): #attrbiutes passed in as paremeter during creation of object. attribute2 is optional parameter which will default to value if not given
        #assign attributes to memory of object
        #name of object's attribute (self.objects_attribute_name) recommended, not necessary, to follow variable name of class's parameters for better readability

        #when to do what if question never explicitly state
        #pass in as necessary parameter if question says attribute is stored
        #pass in as optional parameter if question says attribute is initalised
        
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = "fixed" #fixed attribute that do not need to be passed as a parameter. cannot be changed during creation of objecta as all new objects of same class have the same value for that attribute

        #tldr: difference between attribute2 and attribute3
        #attribute2 can be passed as parameter if object has differing value from the default one; optional parameter
        #attribute3 cannot be passed as parameter. it is a fixed value upon creation
        

        #information hiding, restrict access to internal attributes through getters and setters
        #related to encapsulation, which involves restricting access to componets of objects
        #private attributes require getters and setters, which are methods, to access data of an object
    
        #single underscore, no practical use, just signal that attribute/ method for internal use 
        #self._attribute1 = attribute1 
        
        #dunder (private) attribute, which needs getters to access (not actually private, got ways to bypass in python)
        #known as name mangling
        #self.__attribute1 = attribute1


    #methods

    #getters and setters (important to use them whenever they are present)
    #demonstrates encapsulation in python
        
    #getter; accessor to access attributes 
    def get_attribute(self):  
        print(self.attribute)

    #setter; mutator/ modifier to change attributess
    def set_attribute(self, new_attribute): #pass new attribute in as parameter of setter
        self.attribute = new_attribute 


#creation of object (instance of a class)
object_name = ClassName(attribute)

#using methods after creation of object
object_name.get_attribute()



#inheritence 
#legend: p means parent, c means child

#parent class is what a typical class looks like (see above)

#child class
#inherit all attributes and methods from parent  
class Child(Parent):
    #override __init__ when child class got additional attributes 
    def __init__(self,p_attribute, c_attribute): #p.attribute and c.attribute passed in as paremeter during creation of object
        #inheritence of attributes from parent class 
        super().__init__(p_attribute) #call constructor of parent class so do not need self.p_attribute = p_attribute

        self.c_attribute = c_attribute #new attribute for child class

    #parent's methods also can use
    #do not have to type below code:
    #def p_method(self):
        #super().p_method() this copys the method from parent class
    
    #define new method unique to child 
    def c_method(self): 
        print("this method is only available to child class")



    #polymorphism; method overriding
    #same method, different behaviour/ implementation
    #feature of inherited methods
    def p_method(self):
        print("this is polymorphism")

