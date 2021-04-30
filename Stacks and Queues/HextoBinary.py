from data_structures import Stack

def HexToBinary(number):
    bin_holder = Stack()
    while number > 0:
        rem = number % 2
        bin_holder.push(rem)
        number = number // 2

    bin_string = ""
    while not bin_holder.isEmpty():
        bin_string = bin_string + str(bin_holder.pop())

    return bin_string

print(HexToBinary(42))
