import string

def anagram(s1, s2):
    s1_refined = s1.replace(' ', '').lower()
    s2_refined = s2.replace(' ', '').lower()
    letter_value_dict = {y:0 for y in string.ascii_lowercase}
    s1_sum = 0
    s2_sum = 0

    n = 1
    while n < 27:
        for letter in string.ascii_lowercase:
            letter_value_dict[letter] = n
            n += 1

    for letter in s1_refined:
        s1_sum += letter_value_dict[letter]

    for letter in s2_refined:
        s2_sum += letter_value_dict[letter]

    if s1_sum == s2_sum:
        return True
    else:
        return False

print(anagram('clint eastwood', 'old west action'))

