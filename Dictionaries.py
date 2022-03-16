print('xxx')

thisdict={
    'brand':('ford','audi'),
    'model':'mustang',
    'year' :'1964' ,
    'speed':'190',
    'colour':['red','blue','black']


}
print(thisdict['brand'])
print(thisdict['year'])
print(thisdict.keys())
print(thisdict.values())

print(len(thisdict))    #4keysandvalues
print('\n',type(thisdict))

a=('bhanumaan')
print(type(a))

x=thisdict.get('colour')
print(x)
y=thisdict['brand']
print(y)

a=thisdict.keys()
print(a)
thisdict['owner']='raj'
print(a)

thisdict['speed']=220,240
print(thisdict.values())

p=thisdict.items()   #print whole dict
print(p)

for i in p:
    print(i)     #print all one by one

if 'model' in thisdict:
    print('yes','this key exists')
else:
    print('no , the key not found')





