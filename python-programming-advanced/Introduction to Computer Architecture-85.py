## 4. Understanding How Python Stores Data ##

import sys

my_int = 200
size_of_my_int = sys.getsizeof(my_int)

int1 = 10
int2 = 100000
str1 = "Hello"
str2 = "Hi"
int_diff = sys.getsizeof(int1) - sys.getsizeof(int2)
print(int_diff)

str_diff = sys.getsizeof(str1) - sys.getsizeof(str2)
print(str_diff)