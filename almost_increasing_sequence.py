def almostIncreasingSequence(sequence):
    droppped = False
    last = prev = min(sequence) - 1
    print(prev)
    for elm in sequence:
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True

    # return new_list
print(almostIncreasingSequence([1,2,3,2,2,2]))