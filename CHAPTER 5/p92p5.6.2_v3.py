def addToInventory(inventory,addedItems):
              dragonLoot_dict={x:dragonLoot.count(x) for x in dragonLoot}
              global combined
              combined={**dragonLoot_dict,**inv}

def displayInventory(inventory):
              print('Inventory:')
              numItem=0
              for k,v in combined.items():
                            print(str(v)+' '+k)
                            numItem=numItem+v
              print('Total number of items: '+str(numItem))
     
inv={'gold coin':42,'rope':1}
dragonLoot=['gold coin','dagger','gold coin','gold coin','ruby']
inv=addToInventory(inv,dragonLoot)

displayInventory(inv)
