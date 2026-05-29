import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


s = "Hello World"                       
print(s.upper())                # Uppercase: "HELLO WORLD"      
print(s.lower())                # Lowercase: "hello world"
print(s.capitalize())           # First letter capital: "Hello world"
print(s.title())                # Title case: "Hello World"
print("  hello  ".strip())             # Remove whitespace: "hello"
print(s.split())                       # Split by space: ['Hello', 'World']
s.split('l')                    # Split by 'l': ['He', '', 'o Wor', 'd']
print("-".join(['a', 'b', 'c']))       # Join: "a-b-c"
print(s.replace('World', 'Python'))    # Replace: "Hello Python"
print(s.find('World'))                 # Find index: 6
print(s.find('xyz'))                  # Not found: -1
print(s.index('World'))                # Find index: 6
# s.index('xyz')                 # ValueError (not found)
print(s.startswith('Hello'))        # Check prefix: True
print(s.endswith('World'))            # Check suffix: True
print(s.count('l'))                   # Count occurrences: 3
print("abc".isalpha())                 # All alphabetic: True
print("123".isdigit())                 # All digits: True
print("abc123".isalnum())              # Alphanumeric: True


s = "Hello"
print(s[1:4])                         # Slice: "ell"
print(s[:3])                         # From start: "Hel"
print(s[2:])                         # To end: "llo"
print(s[::-1])                         # Reverse: "olleH"
print(s[::2])                         # Every 2nd char: "Hlo"