# this creates a new map with 256 buckets inside of it
def new(num_buckets = 256):
	"""Initializes a Map with the given number of buckets."""
	# this initializes the aMap variable
	aMap = []
	# this walks through the entire map and appends an empty list to each bucket
	for i in range(0, num_buckets):
		aMap.append([])
	return aMap
	
# this takes in the map and a key to return a hash
def hash_key(aMap, key):
	""" Given a key this will create a number and then convert it 
	to an index for the aMap's buckets."""
	# this converts a string into a number and then modulos it by the length of the map
	return hash(key) % len(aMap)
	
# this finds a bucket where the given key could go based a passed in key
def get_bucket(aMap, key):
	"""Given a key, find the bucket where it would go."""
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]
	
# this rolls through the list of values in the bucket found in get_bucket until it finds 
# 	what it is looking for
def get_slot(aMap, key, default = None):
	"""
	Returns the index, key, and value of a slot found in a bucket.
	Returns -1, key, and default (None if not set) when not found.
	"""
	# this runs the get_bucket function to find which bucket the passed in value is in
	bucket = get_bucket(aMap, key)
	
	# this runs through the bucket and finds the value that was passed in
	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			return i, k, v
			
	return -1, key, default
	
# this runs the get_slot function, but only returns the value and not the location
def get(aMap, key, default = None):
	"""Gets the value in a bucket for the given key, or the default."""
	i, k, v = get_slot(aMap, key, default = default)
	return v
	
# this assigns a key and value to the passed in location and replaces anything that is in there
def set(aMap, key, value):
	"""Sets the key to value, replacing any existing value."""
	bucket = get_bucket(aMap, key)
	i, k, v = get_slot(aMap, key)
	
	if i >= 0:
		# the key exists, replace it
		bucket[i] = (key, value)
	else:
		# the key does not, append to create it
		bucket.append((key, value))
		
# this deletes a key/value pair
def delete(aMap, key):
	"""Deletes the given key from the Map."""
	bucket = get_bucket(aMap, key)
	
	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break

# this function prints out all items in the map			
def list(aMap):
	"""Prints out what's in the map."""
	for bucket in aMap:
		if bucket:
			for k, v, in bucket:
				print k, v