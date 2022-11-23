import csv 
from customers import *



class Furniture:
	def __init__(self, product_ID=None, product_Name=None, Category=None, Designer=None, Price=None, Quantity=None):
		self.product_id = 0
		self.product_name = ""
		self.category = ""
		self.designer = ""
		self.price = ""
		self.quantity = 0

	def displayInventory(self):
		print("\t\n** Entire Stock **")
		f = open('FFurniture.csv', 'r')
		reader = csv.reader(f, delimiter=',')
		lineCount = 0

		for row in reader:
			if lineCount == 0:
				print(f'\n\t{", ".join(row)}\n\t-----------------------------------------------------------\n')
				lineCount+=1
			else:
				print(f'\t{row[0]} ||| {row[1]} ||| {row[2]}, {row[3]}, {row[4]} ||| {row[5]} |||\n')
				lineCount+=1
		
		f.close()


	def removeItem(self, itemID=None, Quant=None):
		self.itemID = itemID
		self.quantity = Quant
		self.inFlag = 0
		self.itemDel = []

		#print('\n',itemID, Quant,'\n')

		with open('Furniture.csv', 'r+') as inp:
			#writer = csv.writer(out, )
			reader = csv.reader(inp, delimiter=',')

			with open('FFurniture.csv', 'w') as out:
				writer = csv.writer(out)


			#subtract amount here 
				for row in reader:
					#print(row)
					if(row[0] == self.itemID and ((float(row[5]) - self.quantity) > 0)):
						self.inFlag = 1

						print(row[5].replace(str(row[5]), str(float(row[5]) - self.quantity)))
						#self.itemDel.append(self.itemID)
						#self.itemDel.append(float(row[5]) - self.quantity)
						#print(self.itemDel)
					elif(row[0] == self.itemID and ((float(row[5]) - self.quantity) == 0)):
						self.inFlag = 1
						self.itemDel.append(self.itemID)
						self.itemDel.append(float(row[5]) - self.quantity)
						#print('caught2')
					elif(row[0] == self.itemID and ((float(row[5]) - self.quantity) < 0)):
						print('\t** Too many items requested for current inventory\n\tItem info: {self.itemID}')

					writer.writerow(row)
			#print('test')

			#Check that ID was found valid / else err
				if self.inFlag == 0:
	 				print("\n** Cart Item Deletion - Error **\n")
