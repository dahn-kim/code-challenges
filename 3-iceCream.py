class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
         # YOUR CODE GOES HERE
        pair=[]
        for i in range(0,len(self.ingredients)):
            for j in range(0,len(self.toppings)):
                pair.append([self.ingredients[i],self.toppings[j]])
        return pair

machine = IceCreamMachine(["vanilla","chocolate"], ["chocolate sauce"])
print(machine.scoops())
machine= IceCreamMachine(["vanilla","chocolate"],["chocolate sauce","caramel sauce"])
print(machine.scoops())
