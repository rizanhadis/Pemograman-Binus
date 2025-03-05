# a = int(input())
# for i in range(1, a + 1):
#     if i % 15 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# total = 0
# while True:
#     num = int(input())
#     if num < 0:
#         break
#     total += num
# print(total)

text = input().strip()
count = 0
for char in text:
    if char == 'a':
        count += 1
print(count)