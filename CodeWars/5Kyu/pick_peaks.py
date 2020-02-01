
# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python


def is_peak(arr, ind):
    if ind == 0:
        return False
    try:
        if arr[ind] > arr[ind-1] and arr[ind] > arr[ind+1]:
            return True
        elif arr[ind] > arr[ind-1] and arr[ind] == arr[ind+1]:
            i = 2
            while i < len(arr):
                if arr[ind+i] < arr[ind]:
                    return True
                elif arr[ind+i] > arr[ind]:
                    return False
                i += 1
        elif arr[ind] == arr[ind-1]:
            return False
    except IndexError:
        pass
    return False


def pick_peaks(arr):
    output = {
        'pos': [],
        'peaks': [],
    }

    for ind, val in enumerate(arr):
        if is_peak(arr, ind):
            output['pos'].append(ind)
            output['peaks'].append(val)
    return output


assert pick_peaks([1,2,3,6,4,1,2,3,2,1]) == {"pos":[3,7], "peaks":[6,3]}
assert pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]) == {"pos":[3,7], "peaks":[6,3]}
assert pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]) == {"pos":[3,7,10], "peaks":[6,3,2]}
assert pick_peaks([2,1,3,1,2,2,2,2]) == {"pos":[2], "peaks":[3]}
assert pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]) == {"pos":[2,7,14,20], "peaks":[5,6,5,5]}

