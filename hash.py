class HashTable:
    def __init__(self):
        self.max=100
        self.data=[None for i in range (self.max)]
    def get_hash(self,key):
        h=0
        for char in key:
            value =ord(char)  #returns ascii va;ue of character
            h+=value       #for hash function
        return(h%self.max)
    def add (self,key,value):
        h = self.get_hash(key)  #for hash function
        self.data[h]=value
        print(f"the data that is {self.data[h]} with key {key} is stored in {h}")  

    def get (self,key):
        h = self.get_hash(key)
        return (self.data[h])
    
ha = HashTable()
ha.add('kkk', 140)
print(ha.get('kkk'))


