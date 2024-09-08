import logging
from collections import Counter

logging.basicConfig(level=logging.DEBUG)

def is_palindrome(word: str) -> bool:
    str_len = len(word)
    if str_len < 2:
        return True
    i1 = 0
    i2 = str_len -1
    for i in range(int(str_len/2 + 0.5)): # str_len = 4 -> 2, str_len = 5 -> 3
        if word[i1] != word[i2]:
            return False
        i1+=1
        i2-=1
    return True

def max_product(numbers: list) -> float | int:
    """
    Take in a list of integers and return the maximum product of any two numbers in the list

    :param numbers: list of numbers
    :return product: float or an integer representing the maximum product from two numbers in the list
    """
    
    p1 = 0
    p2 = 0
    n1 = 0
    n2 = 0

    for num in numbers:
        if num > p1:
            p2 = p1
            p1 = num
        elif num < n1:
            n2 = n1
            n1 = num
    
    if len(numbers) < 2:
        raise ValueError("The list does not contain 2 numbers, therefore we can't create a product.")
    elif len(numbers) == 2:
        return p1 * n1
    else:
        if p1 * p2 > n1 * n2:
            return p1 * p2 
        else:
            return n1 * n2

def is_anagram(s1: str, s2: str) -> bool:
    s1_counter = Counter(s1)
    s2_counter = Counter(s2)

    if s1_counter == s2_counter:
        return True
    else:
        return False
    
def longest_substring(s: str) -> str:
    """ 
    Return the longest substring of a string

    :param s: string
    :return sub_s: sub-string of s

    """
    for i, c in enumerate(s):
        
    


if __name__ == "__main__":
    # examples = ["racecar", "Austin", "yoyo", "hannah"]
    # print(is_palindrome(examples[0]))
    # print(is_palindrome(examples[1]))
    # print(is_palindrome(examples[2])) 
    # print(is_palindrome(examples[3]))

    # num_list = [1, 5, 9, -5, -11, 14, 15]
    # logging.debug(max_product(num_list))

    examples = [("listen", "silent"), ("ham", "ahm"), ("slam", "lamb")]
    logging.debug([is_anagram(example[0], example[1]) for example in examples])
    

