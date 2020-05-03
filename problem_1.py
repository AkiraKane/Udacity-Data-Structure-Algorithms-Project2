from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 

        if key not in self.cache:
            return -1
        
        # if we found the key, then move the key to the end to show that it is recently used.
        self.cache.move_to_end(key)
        return self.cache[key]
        

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 

        if self.capacity == 0:
            print("Error: Capacity cannot be 0")
            return 
        
        # remove the least recently used item if ordereddict is at capacity
        if len(self.cache) ==  self.capacity:
            self.cache.popitem(last=False)
        
        # add/update the key, and move the key to the end to show that it is recently used
        self.cache[key] = value
        self.cache.move_to_end(key)

our_cache = LRU_Cache(5)

############################## Test1 - at capacity ################################################################

# set values and get values within the capacity
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4); 
print(our_cache.get(1))    # returns 1
print(our_cache.get(2))    # returns 2
print(our_cache.get(9))    # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)        # move 5 to the end  
our_cache.set(6, 6)        # exceed the capacity, remove the left-most key, which is 3. then move 6 to the end
print(our_cache.get(3))    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(6))    # return 6 since it was recently used

################################ Test2 - update key ####################################################################
# update the existing key 
our_cache.set(4,10)
print(our_cache.get(4))    # return 10

# update the non-existing key
our_cache.set(3,20)
print(our_cache.get(3))    # return 20

################################## Test 3 - no-keys & no-capacity ########################################################
# initialize a cache without setting any keys/values
our_cache_no_keys = LRU_Cache(3)
print(our_cache_no_keys.get(1))   # return -1 since no key found in the cache

our_cache_no_capacity = LRU_Cache(0)
our_cache_no_capacity.set(1, 1)   # print out the error message
print(our_cache_no_capacity.get(1)) # return -1 

