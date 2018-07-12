import sqlite3
conn=sqlite3.connect('stock.db')
cursor=conn.cursor()
# CREATE TABLE inventory (
#  Item_id INTEGER,
#  Item_name VARCHAR,
# );
print "1.add items\t2.delete item\t3.edit item details\t4.display"
opt=input()
if opt==1:
	cursor.execute('select * from inventory_manage')
	all_list_items=cursor.fetchall()
	Item_id=raw_input("enter the item Id (Id must begin with a character. eg:I201):\t")
	id_list=[]
	Item_flag=0
	for data in all_list_items:
		id_list.append(data[0])
	for i in range(0,len(id_list)):
		if Item_id==id_list[i]:
			Item_flag=1
	if Item_flag==0:
		print Item_id," is not in the item list so it is a new item"
		Item_name=raw_input("enter the item name :\t")
		Item_cost=raw_input("enter the item cost :\t")
		Item_quantity=raw_input("enter the item quantity:\t")
		Item_tax=raw_input("enter the item tax:\t")
		perishable=raw_input("If the Item is perishable enter 1....else....0:\t")
		Item_exp_date=raw_input("enter the item expiry date(DD/MM/YYYY):\t")
		sql="INSERT INTO inventory_manage(Item_id,Item_name,Item_cost,Item_quantity,Item_tax,perishable,Item_exp_date)values(?,?,?,?,?,?,?)"
		cursor.execute(sql,(Item_id,Item_name,Item_cost,Item_quantity,Item_tax,perishable,Item_exp_date))
	else:
		print Item_id, " is in the item list"
		Item_cost=raw_input("enter the item cost :\t")
		Item_quantity=raw_input("enter the item quantity:\t")
		Item_tax=raw_input("enter the item tax:\t")
		Item_exp_date=raw_input("enter the item expiry date (DD/MM/YYYY):\t")
		sql="UPDATE inventory_manage SET Item_cost=?,Item_quantity=?,Item_tax=?,Item_exp_date=?"
		cursor.execute(sql,(Item_cost,Item_quantity,Item_tax,Item_exp_date))
	print Item_id," is inserted to the stock"
conn.commit()
#conn.close()
if opt==2:
	cursor.execute('select * from inventory_manage')
	all_list_items=cursor.fetchall()
	Item_id=raw_input("enter the item Id (Item_id must begin with a character. eg:I201:\t")
	id_list=[]
	Item_flag=0
	for data in all_list_items:
		id_list.append(data[0])
	for i in range(0,len(id_list)):
		if Item_id==id_list[i]:
			Item_flag=1
	if Item_flag==0:
		print Item_id, " is not in the item list so it cannot be deleted"
	else :
		print Item_id, " is in the item list"
		sql="DELETE FROM inventory_manage WHERE Item_id=?"
		cursor.execute(sql,(Item_id,))
		dele=cursor.execute('select * from inventory_manage')
		print "\n\n",Item_id," IS SUCCESSFULLY DELETED"
conn.commit()
if opt==3:
	cursor.execute('select * from inventory_manage')
	all_list_items=cursor.fetchall()
	print all_list_items
	Item_id=raw_input("enter the item Id to be edited (Id must begin with a character. eg:I201):\t")
	id_list=[]
	Item_flag=0
	for data in all_list_items:
		id_list.append(data[0])
	for i in range(0,len(id_list)):
		if Item_id==id_list[i]:
			Item_flag=1
	if Item_flag==0:
		print Item_id, " is not in the item list so it is a new item"
	else:
		print Item_id, " is in the item list"
		edit_flag=1
		while edit_flag==1:
			print "What do you like to edit\n1.Item name\n2.Item cost\n3.Item tax\n4.Item quantity\n5.Item expiry date\npress 6 to exit"
			choice=input()
			if choice==1:
				Item_name=raw_input("enter the item name :\t")
				sql="UPDATE inventory_manage SET Item_name=? WHERE Item_id=?"
				cursor.execute(sql,(Item_name,Item_id))
				#print "The name of the Item with Id ",Item_id," is edited to ",Item_name
				cursor.execute('select * from inventory_manage')
				all_list_items=cursor.fetchall()
				print all_list_items
			elif choice==2:
				Item_cost=raw_input("enter the item cost :\t")
				sql="UPDATE inventory_manage SET Item_cost=? WHERE Item_id=?"
				cursor.execute(sql,(Item_cost,Item_id))
				cursor.execute('select * from inventory_manage')
				all_list_items=cursor.fetchall()
				print all_list_items
				#print "The cost of the Item with Id ",Item_id," is edited to ",Item_cost 
			elif choice==3:
				Item_tax=raw_input("enter the item tax :\t")
				sql="UPDATE inventory_manage SET Item_tax=? WHERE Item_id=?"
				cursor.execute(sql,(Item_tax,Item_id))
				cursor.execute('select * from inventory_manage')
				all_list_items=cursor.fetchall()
				print all_list_items
				#print "The tax of the Item with Id ",Item_id," is edited to ",Item_tax
			elif choice==4:
				Item_quantity=raw_input("enter the item quantity :\t")
				sql="UPDATE inventory_manage SET Item_quantity=? WHERE Item_id=?"
				cursor.execute(sql,(Item_quantity,Item_id))
				cursor.execute('select * from inventory_manage')
				all_list_items=cursor.fetchall()
				print all_list_items
				#print "The quantity of the Item with Id ",Item_id," is edited to ",Item_quantity
			elif choice==5:
				Item_exp_date=raw_input("enter the item expiry date (DD/MM/YYYY):\t")
				sql="UPDATE inventory_manage SET Item_exp_date=? WHERE Item_id=?"
				cursor.execute(sql,(Item_exp_date,Item_id))
				cursor.execute('select * from inventory_manage')
				all_list_items=cursor.fetchall()
				print all_list_items
				#print "The expiry date of the Item with Id ",Item_id," is edited to ",Item_exp_date
			else:
				edit_flag=0
conn.commit()
if opt==4:
	cursor.execute('select * from inventory_manage')
	all_list_items=cursor.fetchall()
	print "Item_id\t\tItem_name\tItem_cost\tItem_quantity\tItem_tax\tperishable\tItem_exp_date"
	for data in all_list_items:
		print data[0],"\t\t",data[1],"\t\t",data[2],"\t\t",data[3],"\t\t",data[4],"\t\t",data[5]

conn.commit()
conn.close()
