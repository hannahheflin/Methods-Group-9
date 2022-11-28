import csv 
from customers import *
import pandas as pd



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
		f = open('Furniture.csv', 'r')
		reader = csv.reader(f, delimiter=',')
		lineCount = 0

		for row in reader:
			if lineCount == 0:
				print(f'\n\t{", ".join(row)}\n\t-----------------------------------------------------------\n')
				lineCount+=1
			else:
				if(int(row[5]) != 0):
					print(row[5])
					print(f'\t{row[0]} ||| {row[1]} ||| {row[2]}, {row[3]}, {row[4]} ||| {row[5]} |||\n')
					lineCount+=1
				else:
					lineCount+=1
		
		f.close()


	def removeItem(self, itemID=None, Quant=None):
		self.itemID = itemID
		self.quantity = Quant
		self.inFlag = 0
		self.itemDelID = []
		self.itemDelQ = []
		self.rows = []
		#print('\n',itemID, Quant,'\n')

		with open('Furniture.csv', 'r+') as inp:
			#writer = csv.writer(out, )
			reader = csv.reader(inp, delimiter=',')


			#subtract amount here 
			for row in reader:
				#print(row)
				if(row[0] == self.itemID and ((float(row[5]) - self.quantity) > 0)):
					self.inFlag = 1

					self.itemDelID.append(self.itemID)
					self.itemDelQ.append(int(float(row[5]) - self.quantity))


				elif(row[0] == self.itemID and ((float(row[5]) - self.quantity) == 0)):
					self.inFlag = 1
					self.itemDelID.append(self.itemID)
					self.itemDelQ.append(int(float(row[5]) - self.quantity))
						#print('caught2')
				elif(row[0] == self.itemID and ((float(row[5]) - self.quantity) < 0)):
					self.inFlag = 1
					print('\t** Too many items requested for current inventory\n\tItem info: {self.itemID}')

				self.rows.append(row)

			#Check that ID was found valid / else err
			if self.inFlag == 0:
	 			print("\n** Cart Item Deletion - Error **\n")

		#print(len(self.rows))
		for i in range(0, len(self.itemDelID)):
			for row in self.rows:
				if(row[0] == str(self.itemDelID[i]) and self.itemDelQ[i] >= 0):
					row[5] = str(self.itemDelQ[i])
					#print('here1\n\n')

				elif(row[0] == str(self.itemDelID[i]) and self.itemDelQ[i] < 0):
					print("\n\t** Error deleting items from stock **")
					return -1
				#	print('got xero')

			

		#print('\n')
		#print(len(self.rows))
		#print(self.rows)

		inp.close()
		with open('Furniture.csv', 'w', newline='') as out:
			wr = csv.writer(out)
			for row in self.rows:
				wr.writerow(row)

		out.close()
			
	