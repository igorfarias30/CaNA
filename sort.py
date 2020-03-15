from typing import List
import sys


def intercala(_list, p, q, r):
    n_1 = q - p + 1
    n_2 = r - q

    L = [_list[p + i - 1] for i in range(n_1)]
    R = [_list[q + j] for j in range(n_2)]
    L.append(1000)
    R.append(1000)

    i = 0; j = 0
    for k in range(p, r):
        if (L[i] <= R[j]): 
            _list[k] = L[i]; i += 1
        else: 
            _list[k] = R[j]; j += 1

    return _list

def merge_sort(_list: List[int], p: int, r: int) -> List[int]:
    if (p < r):
        q = (p + r)//2
        _list = merge_sort(_list, p, q)
        _list = merge_sort(_list, q + 1, r)
        _list = intercala(_list, p, q, r)
        return _list
    
    return _list

if __name__ == "__main__":
    
    if (len(sys.argv)):
        print(merge_sort([1, 2, 3, 5, 10], 0, 4))
    else:
        exit("too few parameters")