class HashMap ():
    def __init__(self, size):
        self.size = size
        self.map = [None] * self.size

    def get_hash_value(self, key):
        return sum ([ord (p) for p in key]) % self.size

    def add(self, key, value):
        hash_value = self.get_hash_value(key)
        key_value_pair = [key, value]

        if (self.map[hash_value] is None):
            self.map[hash_value] = [key_value_pair]
        else:
            self.map[hash_value].append (key_value_pair)

    def get_value(self, key):
        hash_value = self.get_hash_value (key)

        if (self.map[hash_value] is None):
            return None
        else:
            for i in range (0, len (self.map[hash_value])):
                if (self.map[hash_value][i][0] == key):
                    return self.map[hash_value][i][1]


        return None


    def delete(self, key):
        hash_value = self.get_hash_value (key)

        if (self.map[hash_value] is None):
            return None
        else:
            for i in range (0, len (self.map[hash_value])):
                if (self.map[hash_value][i][0] == key):
                    return self.map[hash_value].pop (i)

        return None


    def print(self):
        for index, key in enumerate (self.map):
            if (key != None):
                print (key)


h = HashMap(5)
h.add('Bob', '567-8888')
h.add('Ming', '293-6753')
h.add('Ming', '333-8233')
h.add('Ankit', '293-8625')
h.add('Aditya', '852-6551')
h.add('Alicia', '632-4123')
h.add('Mike', '567-2188')
h.add('Aditya', '777-8888')
h.print()
h.delete('Bob')
h.print()
print('Ming: ' + h.get_value('Ming'))
