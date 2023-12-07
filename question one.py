# calculating the area that takes the radius of acircle as aparameter and returns the area of a circle
# Test the function with a radius of 5
def calculate_area(radius):
    function = 3.14
    area = function * radius **2
    return area
radius_number = 5


print(f"The area of a circle with radius {radius_number} is {function:.2f}")

# (ii) write arecursive function to calculate the sum of natural numbers
def sum_of_natural_numbers(n):
    if n ==0:
        return 0
    else:
        return n + sum_of_natural_numbers(n-1)
# Test the function with n=4
n = 4
output =sum_of_natural_numbers(n)
print(f"The sum of natural numbers up to {n} is:" {output})

# removing the element at index 2
numbers =[1,3,5,7,9]
del numbers[2]
# inserting the values
numbers.append(10)
# list
print(numbers)


# A new list containing only even numbers.
numbers = [1, 3, 7, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# update the value of age to 25 and add
person_info = { 'city': 'Newyork'}

# Update the value of 'age' to 25
person_info['age'] = 25

# Add a new key-value pair ('city', 'New York')
person_info['city'] = 'New York'

# Print the updated dictionary
print(person_info)

# creating a new dictionary with only key-value pairs 
original_dict = {'a': 3, 'b': 8, 'c': 2, 'd': 7}
new_dict = {key: value for key, value in original_dict.items() if value > 5}

print(new_dict)

    
