# Dictionary different from list is assigning index a meaning. 
# Therefore, for every value, it has its own special key to speicfy its location
# key should be unique and immuatable type. String and number can be used as key


data = {1:'Weiting',2:'Kevin',4:'John'}

print(data[4])

print(data.get(1))
print(data.keys())
print(data.values())

# default display for dictionary get
print(data.get(1,'Not Found'))
print(data.get(3,'Not Found'))

# Combine two list into a dictionary
keys = ['bottle','lamp','book']
values = ['transparent','bright','thick']
data2 = dict(zip(keys,values))
print(data2)
print(data2['lamp'])

# Add new key and value inside dictionary
data2['Tissue'] = 'tender'
print(data2)
# Delete  key and value inside dictionary
del data2['lamp']
print(data2)

# list and dictionart inside dictionary
prog = {'JS':'Atom', 'CS':'VS','Python':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
print(prog['Java']['JSE'])


# Extra comment on complex number. This is acutally catagorized in numeric 

comnum = complex(5,6)
print(comnum)
print(type(comnum))


# range is also specital data formulation in python

a = range(10)
print(a)
print(type(a))
print(list(a))
print(list(range(1,10,2)))