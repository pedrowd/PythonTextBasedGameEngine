def steal(victim, robber, index):
    robber.append(victim[index])
    victim.pop(index)


def trade(trader1, trader2, index):
    placeholder1 = trader1[index]
    placeholder2 = trader2[index]
    trader1[index] = placeholder2
    trader2[index] = placeholder1


def sep_sum(list1, list2):
    return_list = []
    for a in range(min(len(list1), len(list2))):
        return_list.append(list1[a] + list2[a])
    return return_list


def sep_mul(list1, list2):
    return_list = []
    if list2 is list:
        for a in range(min(len(list1), len(list2))):
            return_list.append(list1[a] * list2[a])
    elif list2 is int or list2 is float:
        for a in range(len(list1)):
            return_list.append(list1[a] * list2)
    return return_list


def get_index(target_list, thing):
    r = -1
    for _ in range(len(target_list)):
        r += 1
        if target_list[r] == thing:
            return r
    return None


def semi_equal(list1, list2):
    if len(list1) == len(list2):
        result = 0
        for index in range(len(list1)):
            if list1[index] in list2:
                result += 1
        if result == len(list2):
            return True
    return False


def crown(x):
    """Basically an interpretation of the 3x+1 problem as a function."""
    result = 0
    infinity_tester = 0
    infinity_barrier = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    infinity_barrier **= infinity_barrier
    infinity_barrier **= infinity_barrier
    infinity_barrier **= infinity_barrier
    while x != 1:
        infinity_tester += 1
        result += 1
        if x % 2 == 0:
            x /= 2
        else:
            x *= 3
            x += 1
        if infinity_tester > infinity_barrier:
            print("INFINITY!!!")
            break
    return result + 1  # The "+ 1" is there because Python counts starting from 0.


def lonely(group):
    """I really wanted to create a new function,
    so this is what I came up with:

    The variable "group" is supposed to be a list,
    one containing ONLY NUMBERS (floats or ints).

    All the numbers in it are divided by the number
    at the opposite end of the variable.

    Then, this function returns the sum of all
    that."""
    result_group = []
    placeholder1 = 0
    placeholder2 = 0
    for x in range(len(group)):
        placeholder1 = group[x]
        placeholder2 = group[-x]
        result_group.append(placeholder1 / placeholder2)
    return sum(result_group)


def powerful(x):
    "You know factorial? This is factorial, but it's x to the power of y instead of x times y."
    r = 1
    for a in range(x):
        r **= (a + 1)
    return r


def list_to_int(target_list, base):
    multiplier = base ** (len(target_list) - 1)
    result = 0
    for x in range(len(target_list)):
        result += target_list[x] * multiplier
        multiplier /= base
    return result


def str_to_int(target_str, base):
    return list_to_int(str(target_str), base)


def str_numberize(target_str, base):
    for index in range(len(list(target_str))):
        target_str[index] = str_to_int(target_str[index], base)


def etisoppo(number, base):
    """Alright, the name might seem weird, but this function does the following:

    1: Returns the number divided by the number backwards.

    2: That's it"""
    return number / str_to_int(str(number)[::-1], base)


def grammar(word):
    word = list(word.lower())
    word[0] = word[0].upper()
    return "".join(word)


def anti_grammar(word):
    word = list(word.upper())
    word[0] = word[0].lower()
    return "".join(word)


def custom_grammar(word, upper_list):
    word = list(word.lower())
    for x in range(len(word)):
        if word[x] in upper_list:
            word[x] = word[x].upper()
    return "".join(word)


class MultiDictionary:
    def __init__(self, language_amount):
        self.languages = []
        for _ in range(language_amount):
            self.languages.append([])

    def get(self, word, start_lang, end_lang):
        start_lang = self.languages[start_lang]
        end_lang = self.languages[end_lang]
        index = get_index(start_lang, word)
        return end_lang[index]

    def add(self, thing_list):
        for index in range(len(self.languages)):
            self.languages[index].append(thing_list[index])

    def set(self, index, thing_list):
        for x in range(len(self.languages)):
            self.languages[x][index] = thing_list[x]

    def remove(self, index):
        for x in range(len(self.languages)):
            self.languages[x].pop(index)

    def __str__(self):
        return str(self.languages)

    def __len__(self):
        return len(self.languages) * len(self.languages[0])

    def __getitem__(self, items):
        return self.languages[items[0]][items[1]]

    def __setitem__(self, key, value):
        self.languages[key[0]][key[1]] = value

