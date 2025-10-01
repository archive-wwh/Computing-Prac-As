#IMPORTANT:

#NEED HAVE self INSIDE EACH METHOD
#USE self.attribute OR self.method TO ACCESS ATTRIBUTES OR METHODS RESPECTIVELY INSIDE A CLASS (attributes can be called outside of class, depends on if attributes are private or public)


#construction of class

class ClassName:
    #constructor
    def __init__(self, attribute1, attribute2 = "value", attribute4:str): #attrbiutes passed in as paremeter during creation of object
        #assign attributes to memory of object
        #name of object's attribute (self.objects_attribute_name) recommended, not necessary, to follow variable name of class's parameters for better readability

        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = "fixed_attribute"
        self.attribute4 = attribute4
        

        '''
        different types of attributes
        when to use what attribute depends on what question explicitly states or context


        attribute1
        compulsory parameter passed in during creation of object
        usually when question says attribute is stored


        attribute2
        optional parameter that will be default to value provided if parameter not passed in  during creation of object
        can be modified when object's attribute has differing value from default
        usually when question says attribute is initialised
        

        attribute3
        fixed attribute not passed as a parameter
        all new objects of same class have the same value for that attribute as said attribute cannot be changed during creation of object
        

        attribute4 (not as useful in h2 computing)
        fixing the data type so that only accept parameters of specified data type (str, int, float, bool, etc)
              
        
        information hiding, restrict access to internal attributes through getters and setters
        related to encapsulation, which involves restricting access to componets of objects


        demonstration of encapsulation:
        private attributes require getters and setters, which are methods, to access and modify data of an object outside of class

    
        single underscore, no practical use, just signal that attribute/ method for internal use 
        self._attribute1 = attribute1 

        
        dunder (private) attribute, which needs getters to access (not actually private, got ways to bypass in python)
        known as name mangling
        self.__attribute1 = attribute1
        '''

    #methods

    #getters and setters (important to use them whenever they are present)
        
    #getter; accessor to access attributes 
    def get_attribute(self):  
        print(self.attribute)

    #setter; mutator/ modifier to change attributess
    def set_attribute(self, new_attribute): #pass new attribute in as parameter of setter
        self.attribute = new_attribute 


#creation of object (instance of class)
object_name = ClassName(attribute)


#using methods after creation of object
object_name.get_attribute()



#inheritence 
#legend: p means parent, c means child

#parent class is what a typical class looks like (see above)

#child class inherits all attributes and methods from parent class
class Child(Parent):
    #additional attributes for child class

    #override __init__ of parent class
    def __init__(self,p_attribute, c_attribute): #p.attribute and c.attribute passed in as paremeter during creation of object
        #inheritence of attributes from parent class 
        super().__init__(p_attribute) #call constructor of parent class so do not need self.p_attribute = p_attribute

        self.c_attribute = c_attribute #new attribute for child class

    
    #no additional attributes for child class
    #above __init__ s (def __init__ () ) and super().__init__() ) are redundant
    #super().__init__() automatically called for child class if def __init__ () not redefined


    #parent's methods also can use
    #so do not have to type below code:
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

