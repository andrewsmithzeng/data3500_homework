print('Hello, world!')

# for i in range(100000000):
#   print(i**2)


print(-7//2.1)
print(-7/2.1)

print("andy" * 3)

print(int(3.1415))

age = 0
while(age < 1001):
  print("your age is: ", age)
  age += 1

fav_colors = ["aggie blue", "fighting white", "red"]

for color in fav_colors:
    print(color)
    
for num in range(1000):
    print("num: ", num, sep="---")
    
    
def say_hi(name):
    print("hi ", name)
    
    return None
    
def add_two_nums(num1, num2):
    result = num1 + num2
    # return result
    return None
    
print(add_two_nums(3,4))

print('ending program')

    
print(fav_colors[0:2]) # "aggie blue", "fighting white"
print(fav_colors[0:1]) # just "aggie blue"

print(fav_colors[2]) # red
print(fav_colors[-1]) # red

print(fav_colors[-1:-3:-1])
 
s = "racecar"
print(s == s[::-1]) # True palindrome


def isPalindrom(s):
    return s == s[::-1]
    
print(isPalindrom("amanaplanacanalpanama"))
print(isPalindrom("ratsliveonnoevilstar"))

fav_colors = ["aggie blue", "fighting white", "red"]
fav_colors.insert(1, "orange")
print(fav_colors)


a=input(1)# in console, output 1 and then wait for user input
print(a)# print the user input

num = 3.1415926
print(f"{num:.2f}")  # 输出: 3.14

def x(a=1, b=2):
    p = print(a + b)
    return p 

a = x(3, 4)
print(a)

