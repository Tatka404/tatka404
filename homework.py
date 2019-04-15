

from typing import Any
from typing import List
import string


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(a: Any, b: Any) -> bool:

    return a == b


def is_two_objects_has_same_type(a: Any, b: Any) -> bool:

    return type(a) == type(b)


def is_two_objects_is_the_same_objects(a: Any, b: Any) -> bool:

    return a is b


def multiple_ints(a: int, b: int) -> int:

    if type(a) == int and type(b) == int:
        return a * b
    else:
        raise ValueError


def multiple_ints_with_conversion(a: Any, b: Any) -> int:

    return int(a)*int(b)


def is_word_in_text(ta: str, tatka: str) -> bool:

    return ta in tatka


def some_loop_exercise() -> list:

    num_list = []
    for r in range(13):
        if r != 6 and r != 7:
            num_list.append(r)
    return num_list


def remove_from_list_all_negative_numbers(num_list: List[int]) -> list:

    r = num_list[:]
    for i in num_list:
        if i < 0:
            r.remove(i)
    return r


def alphabet() -> dict:

    #1:

    #return {k: v for k, v in zip(range(1, len(string.ascii_lowercase) + 1), string.ascii_lowercase)}


    #2:

    my_dict = {}
    letter = string.ascii_lowercase
    for number in range(1,27):
        my_dict.update({number:letter[number-1]})
    return my_dict


def simple_sort(listok: List[int]) -> List[list]:

    #1:

    #listok.sort()
    #return listok


    #2:

    """l_2 = []
    lenght = len(listok)
    r = 0
    while r < lenght:
        x = min(listok)
        l2.append(x)
        listok.remove(x)
        r +=1
    return l_2"""


    #3:

    l_2 = []
    while len(listok) > 0:
        sp = None
        for r in listok:
            if sp == None:
                sp = r
            else:
                if r < sp:
                    sp = r
        l_2.append(sp)
        listok.remove(sp)
    return l_2