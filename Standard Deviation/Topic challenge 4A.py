import math


def calculate_standard_deviation(nums):
    mean = sum(nums)/len(nums)

    mean_difference_list = []

    for num in nums:
        mean_difference_list.append(math.pow((num - mean), 2))

    mean_squared_differences = sum(mean_difference_list)/(len(mean_difference_list)-1)

    standard_deviation = math.sqrt(mean_squared_differences)

    return standard_deviation


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Avg of nums {nums} is: {calculate_standard_deviation(nums):.3f}")
