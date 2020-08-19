# use json module to work with JSON

import json

person_string = '''
{
"people": [
    {
        "name" : "Ramesh",
        "phone" : "8187085549",
        "emails" : ["test@gmail.com", "abc@gmail.com"],
        "has_licence" : true
    },
    {
        "name" : "Suresh",
        "phone" : "8187085550",
        "emails" : null,
        "has_licence" : false
    }
  ]
}
'''

# convert this string to Python object (dict)  - use loads method

data = json.loads(person_string)
print( type(data))  # dict
print( type(data['people']))  # list -- JSON array converted to Python list


'''
JSON decoders

JSON      Python
----------------
Object      dict
Array       list
String      str
number(int)  int
number(real)  float
true        True
false       False
null        None
'''

# loop through the people

for person in data['people']:
    print( person['name'])
    print( person['phone'])


# create new JSON string by modifying the python object

for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)
# print( new_string)


#################

''' 

Working with JSON file - Use load method to work with JSON file locations

'''

with open('states.json', 'r') as json_data:
    # print( json_data.read()['states']) # TypeError: string indices must be integers, not str
    data = json.load(json_data)
    # print( type(data))
    # print( data['states'])

for state in data['states']:
    pass
    # print( state['name'], state['abbreviation'])

# modify data and write to file

for state in data['states']:
    del state['area_codes']


# open a file and dump data to it

with open('new_states.json','w') as f:
    json.dump(data, f, indent=2)   # object and file , indent for beautifying it
