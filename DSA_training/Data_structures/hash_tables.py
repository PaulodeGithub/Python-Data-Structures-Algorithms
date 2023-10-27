class HashTable:
    def __init__(self, size = 7) -> None:
        self.data_map = [None] * size # creating a list for tebale entry ie 7

    def __hash(self, key):  #0(1)
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
    # ord() is getting the aski value of each letter in the key and * it my 23(prime no)
    # % len(self.data_map) is dividing up the the hash for each entry on our table. 0-6(7 spaces)
        return my_hash
    
    def print_table(self):
        for i, val in  enumerate(self.data_map): # because its key: value table/dic
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
        

        

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

print(my_hash_table.keys())