def findPairThatAddsToSum(listOfNums, sum):
    hashset = set()
    for num in listOfNums:
        diff = sum - num
        if diff in hashset:
            return num, diff
        else:
            hashset.add(num)
    return None

def findThreesNumbersThatAddUpToSum(listOfNums, sum):
    for i in range(len(listOfNums)):
        diff = sum - listOfNums[i]
        pair = findPairThatAddsToSum(listOfNums[i+1:], diff)
        if pair is not None:
            num1, num2 = pair
            return listOfNums[i], num1, num2




