# Day 13 - Debugging: How to Find and Fix Errors in Your Code  

## 1. Describe the Problem

Clearly state what the code should do vs. what it's actually doing.  

```python
# Incorrect:
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")

my_function()

# Corrected:
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

my_function()
```

## 2. Reproduce the Bug

Make the bug happen consistently so you can understand it better.  

```python
# Incorrect:
dice_imgs = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

# Corrected:
dice_imgs = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
```

## 3. Play Computer

Go through the code line by line as if you were the computer.  

```python
# Incorrect:
year = int(input("What's your year of birth? "))

if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# Corrected:
year = int(input("What's your year of birth? "))

if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")
```

## 4. Fix Errors and Watch for Red Underlines

Pay attention to syntax and data types.  

```python
# Incorrect:
age = input("How old are you? ")
if age > 18:
    print("You can drive at age {age}.")

# Corrected:
try:
    age = int(input("How old are you? "))

except ValueError:
    print("Invalid input. Please enter a number.")

if age > 18:
    print(f"You can drive at age {age}.")
```

## 5. Squash Bugs with print()

Add print statements to check variable values.  

```python
# Incorrect:
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))

total_words = pages * word_per_page
print(total_words)

# Corrected:
word_per_page = int(input("Number of words per page: "))
pages = int(input("Number of pages: "))

total_words = pages * word_per_page
print(total_words)
```

## 6. Use a Debugger

Sometimes manual debugging is not enough, so use a built-in debugger.  

```python
import random
import maths

# Incorrect:
def mutate(a_list):
    b_list = []
    new_item = 0

    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)

    b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])

# Corrected:
def mutate(a_list):
    b_list = []

    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)

    print(b_list)

mutate([1, 2, 3, 5, 8, 13])
```