import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

from collections import defaultdict

dd=defaultdict(int)
dd[1]="raj"
dd["striver"] = "raj"
dd["u"] = 99
dd["list"] = [1,2,3]

print(dd["list"])
print(dd[10])   #it will return 0, as it is int/list/wtv else type DEFAULTdict. never raises keyerror, just gives 0 (default value for int type)
print(dd)

