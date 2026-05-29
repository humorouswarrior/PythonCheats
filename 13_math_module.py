import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

import math

print(math.sqrt(16))                  # Square root: 4.0
print(math.pow(2, 3))                 # 2^3: 8.0
print(math.factorial(5))              # 5!: 120
print(math.gcd(48, 18))               # GCD: 6
print(math.lcm(12, 8))                # LCM: 24 (Python 3.9+)
print(math.log(math.e))               # Natural log: 1.0
print(math.log10(100))                # Base 10 log: 2.0
print(math.log2(8))                   # Base 2 log: 3.0
print(math.sin(math.pi/2))            # sin(90°): 1.0
print(math.cos(0))                    # cos(0°): 1.0
print(math.degrees(math.pi))          # Radians to degrees: 180.0
print(math.radians(180))              # Degrees to radians: 3.14159...
print(math.ceil(4.3))                # Ceiling: 5
print(math.floor(4.7))                # Floor: 4
print(math.isfinite(10))              # Check if finite: True
print(math.isinf(float('inf')))       # Check if infinite: True