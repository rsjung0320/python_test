def say_hi(name: str, age: int) -> str:
    """
        Hi!
    """
    # your code here
    return "Hi. My name is {} and I'm {} years old".format(name, age)

if __name__ == '__main__':
    print(say_hi("Alex", 32))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"

def easy_unpack(elements):
    x = elements[0]
    y = elements[2]
    z = elements[-2]
    return x, y, z
    # return elements[0], elements[2], elements[-2]

if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')