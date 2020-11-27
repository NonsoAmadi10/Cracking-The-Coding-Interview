# Implement an algorithm to determine if a string has unique characters


from functools import reduce


def uniqueStrChar(strings):
    unique_set = set()

    for word in strings:
        if word in unique_set:
            return False

        unique_set.add(word)

    return True


# What if you did not need to use additional dat6a structures

def uniqueChar(data):
    for char in data:
        if data.count(char) > 1:
            return False
    return True


print(uniqueChar("lodi"))

print(uniqueStrChar('amadi'))

"""Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string
    """


def replaceSpaces(word):
    replace_with_percent = word.replace(' ', '%20')
    return replace_with_percent


print(replaceSpaces(' Mr John is mad at mr smith '))


def isPalindrome(word, word2):
    # Ensure both words are of the same length
    if len(word) != len(word2):
        return False
    # Remove whitespace
    trim_word = word.replace(' ', '')
    trim_word_2 = word2.replace(' ', '')
    new_list = []

    for i in trim_word:
        new_list.append(i)
    new_list.reverse()
    reverse_word = ''.join(new_list)

    return trim_word_2 == reverse_word


print(isPalindrome('raceca', 'racecar'))


"""Given a string, write a function to check if it is a permutation of a palin-
drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
    """


def isPalindromePerm(word):
    """
    Bear in mind - has even number counts of characters or at most just one character with an odd count. This means the string is either of even length or an odd length with just exactly one character with an odd count.
    """
    # Remove whitespaces

    trim_word = word.replace(' ', '')
    trim_word = trim_word.lower()

    list_word = [x for x in trim_word]
    odd_count = 0
    # next is to count each word in the list. I'm using python's inbuilt count library

    from collections import Counter

    counts = Counter(list_word)

    for value in counts.values():
        if value % 2 != 0:
            odd_count += 1

    return odd_count < 1


print(isPalindromePerm('never odd or even'))

"""There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
    """


def oneEdit(str1, str2):

    length_1 = len(str1)
    length_2 = len(str2)
    no_of_edits = 0

    if abs(length_2 - length_1) > 1:
        return False

    i = 0
    j = 0

    while i < length_2 and j < length_1:
        # Check if the characters in both strings match
        if str1[i] != str2[j]:
            if no_of_edits == 1:
                return False

            if length_2 > length_1:
                j += 1
            elif length_2 < length_1:
                i += 1
            else:        # If lengths of both strings is same
                i += 1
                j += 1

             # Increment no_of_edits
            no_of_edits += 1
        else:
            i += 1
            j += 1

    if i < length_2 or j < length_1:
        no_of_edits += 1

    return no_of_edits == 1


print(oneEdit('pale', 'pales'))

"""Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string a a b c c c c c a a a would become a 2 b l c 5 a 3 , If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
    """


def compressString(chars):
    count = 0
    current_word = chars[0]  # start from the first character
    result = ''

    for i in chars:
        if i == current_word:
            count += 1
        if i != current_word:
            result += current_word + str(count)
            count = 1
            current_word = i

    result += current_word + str(count)
    return result


print(compressString('aabcccccaaa'))

"""Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
    """


def rotateMatrix(arr):
    result = []
    length = len(arr)

    for i in range(0, length):
        inner = []

        for j in range(0, length):
            item = arr[j][i]
            inner.insert(0, item)
        result.append(inner)

    return result


print(rotateMatrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))


def zeroMatrix(matrix):
    # Empty matrix
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return
    row = [False] * len(matrix)
    column = [False] * len(matrix[0])
    # Record the rows and columns with element(s) being zero.
    for rowIndex in range(len(matrix)):
        for colIndex in range(len(matrix[0])):
            if matrix[rowIndex][colIndex] == 0:
                row[rowIndex] = True
                column[colIndex] = True
    # Set the qualified entire row(s) and column(s) to zero.
    for rowIndex in range(len(matrix)):
        for colIndex in range(len(matrix[0])):
            if row[rowIndex] == True or column[colIndex] == True:
                matrix[rowIndex][colIndex] = 0

    return matrix


print(zeroMatrix([
    [1, 2, 3],
    [4, 5, 0],
    [7, 8, 9]
]))

"""
Determine if a strings s1 is a rotation of another string s2, by calling only a function
Keyword arguments:
argument -- s1, s2
Return: Boolean
"""


class StringRotation:
    def __init__(self):
        pass

    def isSubstring(self, s1, s2):
        return s1 in s2

    def rotation(self, s1, s2):
        if s1 is None or s2 is None:
            return False

        s1 = s1.replace(' ', '')
        s2 = s2.replace(' ', '')
        if len(s1) != len(s2):
            return False

        return self.isSubstring(s1, s2+s2)


test = StringRotation()

print(test.rotation('waterbottle', 'erbottlewat'))


"""
Implement a reverse a string (a list of characters), in place

constraints -> can't reverse an empty string\n
            -> strings are ascii only \n
            -> return a reverse string in place\n
"""


def reverseString(data):
    if data is None:
        return None

    return data[::-1]


print(reverseString('john legend'))

"""
    Find the single different char between two strings

        ex: abbbccddde, abbbccddd -> e
            abb , bb -> a

    Keyword arguments:
    s1 -- First string
    s2 -- second string
    Return: return the difference
    """


def find_diff(s1, s2):
    if s1 is None or s2 is None:
        return None
    seen = {}
    diff = []
    for char in s1:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1

    for char in s2:
        if char in seen:
            seen[char] -= 1
        else:
            seen[char] = 1

    for key, values in seen.items():
        if values < 0:
            diff.append(key)
        if values >= 1:
            diff.append(key)
    return sorted(diff)


print(find_diff('aab', 'ab'))


def fizzBuzz(num):
    """
    constriants -> Return None on empty input or input less than  one
                -> Print fizz for numbers divisible by 3 
                -> Print buzz for numbers divisible by 5 
                -> Print fizzbuzz for numbers divisible by 3 and 5
                -> Print the number if the above cases are not covered
    """
    if num is None or num < 1:
        return ValueError('Number cannot be less than one')

    for i in range(1, num+1):
        if i % 3 == 0:
            print('fizz')
        if i % 5 == 0:
            print('buzz')
        if i % 15 == 0:
            print('fizzbuzz')

        print(i)


print(fizzBuzz(100))


def non_repeating_chars(data):
    """
    constraints -> Returns Value error on empty list 
                -> returns value error on string length less than 2
                -> returns only first non-repeating character 
    """

    if len(data) < 1:
        return ValueError('data must not be less than 1')

    """
    Algorithm -> loop through each char in the data
              -> save each char and char count in a dictionary
              -> loop through each keys and values , append values =1 to a list, return the first index of the list
    """

    dict_ = {}
    my_list = []

    for char in data:
        if char in dict_:
            dict_[char] += 1
        else:
            dict_[char] = 1

    for key, values in dict_.items():
        if values == 1:
            my_list.append(key)

    return my_list[0]


print(non_repeating_chars('chhuuul'))


def remove_char(data, char):
    """
    constraints --> Empty data should return None
                --> data length must greater than 1
                --> Char must be in the list
                --> Remove characters even with duplicates
    """
    if data is None:
        return

    result = ''

    if len(data) <= 1:
        return ValueError('length of data must be greater than 1')

    if char in data:
        for letter in char:
            result = data.replace(letter, '', data.count(letter))
            data = result
        return result
    else:
        return data


print(remove_char('calabar', 'ar'))


def int_to_string(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break
    # Adds the negative sign back if is_negative
    return ('-'if is_negative else "") + "".join(reversed(s))


print(int_to_string(12))


def two_nums(nums, target):
    if nums is None or target is None:
        raise TypeError('nums or target cannot be None')

    if not nums:
        raise ValueError(' nums cannot be empty')
    cache = {}

    for index, num in enumerate(nums):
        cache_target = target - num

        if num in cache:
            return [cache[num], index]
        else:
            cache[cache_target] = index
    return None


print(two_nums([1, 3, 2, -7, 5], 7))


def buy_and_se11_stock_once(prices):
    min_price_so_far, max_profit = float('inf'), 0.0

    for price in prices:
        max_profit_se1l_today = price - min_price_so_far

        min_price_so_far = min(min_price_so_far, price)
        max_profit = max(max_profit, max_profit_se1l_today)
    return max_profit


print(buy_and_se11_stock_once(
    [310, 310, 275, 275, 260, 260, 230, 230]))
