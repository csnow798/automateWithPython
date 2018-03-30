#i = ['apple','red','apple','red','red','pear']
#d = {x:i.count(x) for x in i}
#print(d)


dragonLoot=['gold coin','dagger','gold coin','gold coin','ruby']
dragonLoot_dict={x:dragonLoot.count(x) for x in dragonLoot}
print(dragonLoot_dict)

dragonLoot_dict={'gold coin': 3, 'dagger': 1, 'ruby': 1}
inv={'gold coin':42,'rope':1}
combined={**dragonLoot_dict,**inv}
print(combined)

for k,v in combined.items():
              print(str(v)+' '+k)
              item_total=item_total+v
              print('')
              print('Total number of items: '+str(item_total))
