class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        pair=[]
        for i in self.ingredients:
            for j in self.toppings:
                pair.append([i,j])
        return pair

machine = IceCreamMachine(["vanilla","chocolate"], ["chocolate sauce"])
print(machine.scoops())
machine= IceCreamMachine(["vanilla","chocolate"],["chocolate sauce","caramel sauce"])
print(machine.scoops())
