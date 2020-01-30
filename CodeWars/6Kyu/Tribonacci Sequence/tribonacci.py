
# Check https://www.codewars.com/kata/tribonacci-sequence/train/python
# for specification.


def tribonacci(signature, n):
    seq = [] + signature
    for i in range(n-3):
        seq.append(sum(seq[-3:]))
    return seq[:n]
