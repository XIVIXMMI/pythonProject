# dictionary = A changeable, unordered collection of unique key: Value pairs
#              Fast because they use hashing, allow us to access a value quickly

#create a dictionary
capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijng',
            'Russia':'Moscow',
            'Vietnam':'Ha Noi'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')#remove
capitals.clear()

#print(capitals['Germany'])
#print(capitals.get('Germany'))#safer
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key, value in capitals.items():
    print(key, value)