def max(seq, start):
    if start > len(seq):
        return \
"Number exceeds maximum elements of the sequence, try again."
    elif start == len(seq):
        return start
    else:
        return max(seq, start + 1)

seq = [1,3,5,7,9]
start = 6
test = max(seq, start)
print(test)

