# fav_foods = ["lumpia", "sushi", "hummus", "salmon", "pasta"]
# print(fav_foods[1])
# print(fav_foods[-1])
# fav_foods.append("broccoli")
# # made a mistake here when i didn't use "" around the string
# print(fav_foods)
# fav_foods.insert(0, "apple")
# print(fav_foods)
# # didn't put where i wanted apple
# fav_foods.remove("sushi")
# print(fav_foods)
# len(fav_foods)

# for foods in fav_foods:
#     foods = foods.upper()
#     print(foods)

# first_and_last = fav_foods[::len(fav_foods)-1]
# print(first_and_last)



# def fav_foods(food):
#     if food == "potato":
#         print("A potato!")
#     else:
#         print("No potato!")

# # didn't put ==, only =

# numbers = range(0,21)

# def get_first_15(numbers):
#     return numbers[:15]

# def get_every_5th(step1):
#     return numbers[::5]

# def reverse_and_stride(step2):
#     return numbers[::-3]

# step1 = get_first_15(numbers)
# step2 = get_every_5th(step1)
# step3 = reverse_and_stride(step2)

# print(step3)

# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(nums[2])
# print(nums[1][1])
# nums.append([10, 11, 12])
# print(nums)

# def sum_nested(nums):
#     total = 0

#     for row in nums:
#         for number in row:
#             total += number

#     return total

# print(sum_nested(nums))

# def create_list():
#     nums = []
#     number = 1

#     for i in range(5):
#         row = []
#         for j in range(5):
#             row.append(number)
#             number += 1
#         nums.append(row)

#     return nums

# step1 = create_list()
# print(step1)

# def replace_multiples(nums):
#     for i in range(5):
#         for j in range(5):
#             if nums[i][j] % 3 == 0:
#                 nums[i][j] = "?"
#     return nums

# step2 = replace_multiples(step1)
# print(step2)

# def sum_numbers(nums):
#     total = 0

#     for row in nums:
#         for number in row:
#             if number != "?":
#                 total += number

#     return total

# step3 = sum_numbers(step2)
# print(step3)

# ages = {
#     "Katie": 30,
#     "Mariam": 42,
#     "Safia": 25,
#     "Mira": 48
# }

# print(ages["Katie"])
# ages["Mira"] = 100
# print(ages)
# ages["Milana"] = 52
# print(ages)

# del ages["Mariam"]
# print(ages)

# for key, value in ages.items():
#     print(key, value)

# didn't put .items()
# this was my favorite code