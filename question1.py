import typing
def main(numbers: typing.List[int], target_sum: int):
    # START WRITING CODE HERE
    result = set()
    hash_table = {}
    numbers.sort()
    for i,each in enumerate(numbers):
        hash_table[each] = i
    for i,a in enumerate(numbers):
        if i != 0 and numbers[i] == numbers[i-1]:
            continue
        for j,b in enumerate(numbers[i+1:]):
            c = -(a+b)
            if c in hash_table and hash_table[c] > i and hash_table[c] > j+i+1:
                result.add((a,b,c))
                return True
            return False
if __name__ == "__main__":
    assert (main([5, 4, 10, 7, 1, 9], 13) is True), "Triplet exists"
    assert (main([4, 2, 5, 9, 11, 23], 9) is False), "Triple does not exist"
