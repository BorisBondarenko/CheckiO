from typing import Iterable

def remove_all_before(items: list, border: int) -> Iterable:
    global tmp
    res = []
    copy_items = items

    if border == 0:
        return res
    if items[0] > items[1]:
        items.remove(items[0])
    for i in items:
        if i == border:
            tmp = True
            break
        if i != border:
            tmp = False
    if not tmp:
        return copy_items
    if tmp:
        while True:
            if items[0] == border:
                break
            else:
                items.remove(items[0])
        return items
    return items


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

# These "asserts" are used for self-checking and not for an auto-testing
assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
assert list(remove_all_before([], 0)) == []
assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
assert list(remove_all_before([10, 1, 5, 6, 7, 10], 5)) == [5, 6, 7, 10]
assert list(remove_all_before([1, 2, 6, 7, 1, 2, 4, 6, 7, 8, 3, 5, 2, 3], 6)) == [6, 7, 1, 2, 4, 6, 7, 8, 3, 5, 2, 3]

print("Coding complete? Click 'Check' to earn cool rewards!")