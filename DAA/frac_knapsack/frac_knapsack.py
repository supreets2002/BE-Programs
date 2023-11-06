class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(W, arr):
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)
    finalvalue = 0.0

    for item in arr:
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.profit
        else:
            finalvalue += item.profit * W / item.weight
            break

    return finalvalue

if __name__ == "__main__":
    num_items = int(input("Enter the number of items: "))
    arr = []
    for i in range(num_items):
        profit = int(input("Enter the profit for item {}:".format(i + 1)))
        weight = int(input("Enter the weight for item {}:".format(i + 1)))
        arr.append(Item(profit, weight))

    W = int(input("Enter the maximum weight limit (W): "))

    max_val = fractionalKnapsack(W, arr)
    print("The maximum value that can be obtained is:", max_val)
