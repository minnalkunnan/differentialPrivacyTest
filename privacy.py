from numpy import random
import pymongo
from random import randint
from pymongo import MongoClient

class User(object):
    pass

def db_average(db, n):
	cursor = db.users.find()

	count = 0
	for i in range(0, n):
		if cursor[i]['bit'] == 1:
			count += 1
	print(count)

	return(float(count)/n)

def initial_insert_users(db):
	users = []
	for i in range(1, 1001):
		print(i)
		user = User()
		user.id = i
		
		prob = random.uniform(0, 1)

		if prob < .01:
			bit = 1
		else:
			bit = 0

		user.sensitive_bit = bit
		users.append(user)

	for user in users:
		print(user.sensitive_bit)
		result = db.users.insert_one(
			{
				"id":user.id,
				"bit":user.sensitive_bit
			}
		)
		print(result)



def main():
	client = MongoClient()
	db = client.hw3_db

	result = db_average(db, 500)
	print ("Result " + str(result))

if __name__ == "__main__":
    main()








