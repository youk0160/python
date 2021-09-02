print('##########1##########')
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
students[0]['last_name']='Bryant'
sports_directory['soccer'][0]='Andres'
z[0]['y']=30
print(x)
print(students)
print(sports_directory)
print(z)

###############################################

print('\n##########2##########')
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(stud) :
    for obj in stud :
        for name in obj:
            if(name == 'first_name'):
                print(name + ' - ' + obj[name] + ', ', end='')
            else:
                print(name + ' - ' + obj[name])

# should output: (it's okay if each key-value pair ends up on 2 separate lines 
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

iterateDictionary(students)

###############################################

print('\n##########3##########')
def iterateDictionary2(key_name, some_list) :
    for obj in some_list:
        print(obj[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

################################################

print('\n##########4##########')
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict) :
    for obj in some_dict:
        print(len(some_dict[obj]),obj.upper())
        for x in range(0,len(some_dict[obj]),1):
            print(some_dict[obj][x])
        print('\n')

printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

