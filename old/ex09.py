"""
hash table?
dict?
mess around with hash table
"""
dict = {
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}

beat = {'name':'Beat','age':23,'Fav_game':'GBFV'}
mate = {'name':'Mate','age':20,'Fav_game':'GBFV'}
people = [beat,mate]
for i in people:
    if i['name'].lower() == "mate":
        print(i['age'])