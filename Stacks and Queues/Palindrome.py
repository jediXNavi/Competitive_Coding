from data_structures import Deque

def PalindromeChecker(string):

    chardeque = Deque()

    for char in string:
        chardeque.addRear(char)

    equal = True

    while chardeque.size() > 1 and equal:
        char_rear = chardeque.removeRear()
        char_front = chardeque.removeFront()

        if char_rear != char_front:
            equal = False

    return equal

assert PalindromeChecker('radar') == True, 'Yes, it is a palindrome'
assert PalindromeChecker('malay') == False, 'No, not a palindrome'