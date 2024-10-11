import random

NONWORD = " "
SEED = 8


def collect_prefix(words, n):
    """ function that will return the first n prefixes of the given list

    :param words: List; of words inside the file
    :param n: Int; length of the prefix in words
    :return: List; of the n prefixes inside words
    """
    if n <= 0 or words == []:
        return []
    else:
        return [words[0]] + collect_prefix(words[1:], n - 1)
#
# def collect_prefix(words, n):
#     """ function that will return the first n prefixes of the given list
#
#     :param words: List; of words inside the file
#     :param n: Int; length of the prefix in words
#     :return: List; of the n prefixes inside words
#     """
#     return [words[i] for i in range(min(n, len(words)))]
def collect_prefixes(words, n, my_dict):
    """ Function that collects all of the prefixes of length n and puts them
        into the dictionary accordingly

    :param words: List; words inside the file
    :param n: Int; max number of words in the prefix
    :param my_dict: Dictionary refence being passed in to be modified
    :return: None; the dictionary refrence is modified via pointers
    """
    if words == [] or n >= len(words):
        return

    else:
        my_tup = tuple(collect_prefix(words, n))
        if my_tup in my_dict.keys():
            my_dict[my_tup] += [words[n]]
        else:
            my_dict[my_tup] = [words[n]]

        return collect_prefixes(words[1:], n, my_dict)
# def collect_prefixes(words, n, my_dict):
#     """ Function that collects all of the prefixes of length n and puts them
#         into the dictionary accordingly
#
#     :param words: List; words inside the file
#     :param n: Int; max number of words in the prefix
#     :param my_dict: Dictionary reference being passed in to be modified
#     :return: None; the dictionary reference is modified via pointers
#     """
#     if words == [] or n >= len(words):
#         return my_dict
#
#     for i in range(len(words) - n):
#         my_tup = tuple(words[i:i + n])
#         if my_tup in my_dict:
#             my_dict[my_tup].append(words[i + n])
#         else:
#             my_dict[my_tup] = [words[i + n]]
#
#     return my_dict



def markov(my_dict, n, words, max_n):
    """ Takes the given dictionary and creates a new list of words using
        markov chain theory

    :param my_dict: Dictionary; essential to the use of the markov algorithm
    :param n: integer; max number of words inside a prefix
    :param words: list; of words from the file
    :param max_n: Integer; the max number of words in the generated string
    :return: List; of strings created from the markov chains
    """
    random.seed(SEED)
    tlist = []
    prefix = collect_prefix(words[n:], n)
    tlist += prefix
    my_t = tuple(tlist)

    while my_dict[my_t] is not None:
        if len(tlist) >= max_n:
            break
        if len(tuple(my_dict[my_t])) == 1:
            tlist.append(my_dict[my_t][0])
            my_t = (my_t[1], my_dict[my_t][0])
        else:
            rand = random.randint(0, len(my_dict[my_t]) - 1)
            tlist.append(str(my_dict[my_t][rand]))
            my_t = (my_t[1], my_dict[my_t][rand])

    return tlist


def main():
    # file name and open
    testing = open(input(),'r')

    file = open(str(testing.readline()).rstrip(),'r')
    sample = {}

    # prefix size
    pre_n = int(str(testing.readline()).rstrip())

    # Number of words generated
    n_max = int(str(testing.readline()).rstrip())

    # The list of words inside the file
    words = []

    # Inserts the non-words into the array
    for i in range(2):
        words.insert(0, NONWORD)

    for line in file:
        temp_l = line.split()
        for word in temp_l:
            words.append(word)

    collect_prefixes(words, 2, sample)

    t = markov(sample, pre_n, words, n_max)
    count = 1
    retstr = ""
    for words in t:
        retstr += words + " "
        if count % 10 == 0:
            retstr += "\n"
        count += 1

    print(retstr)


if __name__ == '__main__':
    main()
