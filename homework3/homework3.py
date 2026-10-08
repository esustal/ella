name = "Ella"

def say_goodbye(name):
    print("Goodbye,", name)

say_goodbye(name)

radius = 7

def area(radius):
    print(3.14 * radius * radius)

area(radius)

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

readings = [80, 63, 76, 69, 64]

def outfits(num):
    return (min(num), max(num))

print(outfits(readings))

days = [1, 2, 3, 4, 5, 6, 7]

def weekends(day):
    if day == 6 or day == 7:
        return True
    else:
        return False

print(weekends(6))


def fuel_efficiency(distance, fuel_used):
    return distance / fuel_used


def astrophysics_data(number):
    if number < 10:
        return number

    lastint = number % 10
    restints = number // 10

    multiplier = 1
    countdown = restints
    while countdown > 0:
        multiplier *= countdown
        countdown -= 1

    return (lastint * multiplier) + restints

secretcode = 12345
print(astrophysics_data(secretcode))

def power(x, y):
    base = x
    for i in range(y-1):
        base*=x
    return base

        

numbers = [1, 2, 3, 4, 5, 6, 7]

def minimum(values):
    min_value = values[0]
    for item in values[1:]:
        if item < min_value:
            min_value = item
    return min_value


def maximum(values):
    max_value = values[0]
    for item in values[1:]:
        if item > max_value:
            max_value = item
    return max_value


def minimum_while(values):
    counter = 0
    min_value = values[0]
    while counter < len(values):
        if values[counter] < min_value:
            min_value = values[counter]
        counter += 1
    return min_value

print(minimum_while(numbers))

numbers = [1, 2, 3, 4, 5, 6, 7]

def sum_list(values):
    total = 0
    for item in values:
        total += item
    return total

print(sum_list(numbers))

# favorite function is sum
