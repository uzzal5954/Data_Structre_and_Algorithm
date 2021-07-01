
class LinearScerch:
    """Implimatation of LinearScearch"""
    def __init__(self, array, target):
        self.array = array
        self.target = target

    def traverse(self):
        self.find = 0
        for i in self.array:
            
            if i == self.target:
                self.find = 1
                break
                
        if self.find == 1:
            print("Number Found in index =", self.array.index(i))
        else:
            print("Sorry, your number not Found")
                
                


objct_01 = LinearScerch([10, 20, 30, 25, 52, 11, 13, 15 ], 13)
objct_01.traverse()