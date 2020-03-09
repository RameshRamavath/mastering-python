## **Collections in Python**

 **There are four collection data types in Python which are used to store collections of data.**
 
   **1. Lists**
        
        Mutable and can store the duplicate values
        Elements can be accessed using Indexes
        It can have any number of items and they may be of different types (integer, float, string etc.)
        
        How to create??
        
        items (elements) inside a square bracket [ ], separated by commas.
        # empty list
        my_list = []
        
        # list of integers
        my_list = [1, 2, 3]
        
        **Python List Methods**
        
        append() - Add an element to the end of the list
        extend() - Add all elements of a list to the another list
        insert() - Insert an item at the defined index
        remove() - Removes an item from the list
        pop()    - Removes and returns an element at the given index
        clear()  - Removes all items from the list
        index()  - Returns the index of the first matched item
        count()  - Returns the count of number of items passed as an argument
        sort()   - Sort items in a list in ascending order
        reverse() - Reverse the order of items in the list
        copy()   - Returns a shallow copy of the list

   
   **2. Tuples**
   
        Im-mutable and ordered in nature
        Can store the duplicate values
        Elements can be accessed using Indexes
        A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.)
        
        How to create??
        ==========
        
        By placing all the items (elements) inside parentheses ()
        
        # Empty tuple
        my_tuple = ()
        print(my_tuple)  # Output: ()
        
        # Tuple having integers
        my_tuple = (1, 2, 3)
        print(my_tuple)  # Output: (1, 2, 3) 
        
        Methods
        ==========
        count(x)  -	Returns the number of items x
        index(x)  -	Returns the index of the first item that is equal to x

   **3. Sets**
   
       A set is an unordered collection of items.
       Not indexed
       Every element is unique (no duplicates) and must be immutable. However, the set itself is mutable. We can add or remove items from it.
       
       How to create?
       
       1. Using the built-in function set()
       2. By placing all the items (elements) inside curly braces {}
          my_set = {1, 2, 3}
          
       Methods
       
        add()	            Adds an element to the set
        clear()	            Removes all elements from the set
        copy()	            Returns a copy of the set
        difference()	    Returns the difference of two or more sets as a new set
        difference_update()	Removes all elements of another set from this set
        discard()	        Removes an element from the set if it is a member. (Do nothing if the element is not in set)
        intersection()	    Returns the intersection of two sets as a new set
        intersection_update()	Updates the set with the intersection of itself and another
        isdisjoint()	    Returns True if two sets have a null intersection
        issubset()	        Returns True if another set contains this set
        issuperset()	    Returns True if this set contains another set
        pop()	            Removes and returns an arbitary set element. Raise KeyError if the set is empty
        remove()	        Removes an element from the set. If the element is not a member, raise a KeyError
        symmetric_difference()	Returns the symmetric difference of two sets as a new set
        symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
        union()	            Returns the union of sets in a new set
        update()	        Updates the set wit
   
   **4. Dictionary**
   
        Python dictionary is an unordered collection of items. 
        While other compound data types have only value as an element, a dictionary has a key: value pair
        
        Create Dict by placing items inside curly braces {} separated by comma.
        An item has a key and the corresponding value expressed as a pair, key: value
        
        # empty dictionary
          my_dict = {}
          
        # methods
        
        clear()	            Remove all items form the dictionary.
        copy()	            Return a shallow copy of the dictionary.
        fromkeys(seq[, v])	Return a new dictionary with keys from seq and value equal to v (defaults to None).
        get(key[,d])	    Return the value of key. If key doesnot exit, return d (defaults to None).
        items()	            Return a new view of the dictionary's items (key, value).
        keys()	            Return a new view of the dictionary's keys.
        pop(key[,d])	    Remove the item with key and return its value or d if key is not found. If d is not provided and key is not found, raises KeyError.
        popitem()	        Remove and return an arbitary item (key, value). Raises KeyError if the dictionary is empty.
        setdefault(key[,d])	If key is in the dictionary, return its value. If not, insert key with a value of d and return d (defaults to None).
        update([other])	    Update the dictionary with the key/value pairs from other, overwriting existing keys.
        values()	        Return a new view of the dictionary's values
        
        
 
 
   **4. Strings**
        
      A string is a sequence of characters.
      Strings are immutable.
      
      We can access individual characters using indexing and a range of characters using slicing
      
      The format() Method for Formatting Strings
      
      default_order = "{}, {} and {}".format('John','Bill','Sean')
      print('\n--- Default Order ---')



## **Collection Module in Python**

  *Collections module comes with Specialized Collection data structures of above four data types*
  
  *Alternatives for built in data types*
 
   #####1. Named Tuple
   
     Tuple with a named value for each element in the tuple
     Aceesing elements is easy and no need to remember the index of an element
     
     from collections import namedtuple
     
     Employee = namedtuple('Employee',['name','age','place'])
     emp = Employee('Ramesh',  26, 'Pune')
     
     Employee = (name:'Ramesh', age: 26, place: 'Pune')
     
     
   #####1. OrderedDict
   
      Dictionary subclass which remembers the order in which the entries were done
      
      dict = OrderedDict()
      dict['name'] = 'Ramesh'
      dict['age'] = 26
      dict['place'] = 'Pune'
      
      dict.get('name')