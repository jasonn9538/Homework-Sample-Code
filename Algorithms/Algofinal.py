import time


def hash_function(pin):
	import hashlib

	result = hashlib.md5(str(pin).encode())

	return result.hexdigest()

string = '5fd0245f6c9ddbdf3eff0f505975b6a7'
for i in range(0,9999):
	print(i, hash_function(i))
	if hash_function(i) == string:
		break
	i+= 1000

