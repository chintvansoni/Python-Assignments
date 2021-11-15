""" Standard Deviation module provides access to the MyMath class and its functions """
import math


class MyMath:
    """ MyMath class provides access to the mathematical functions """
    num_list = []

    def calculate_standard_deviation(self):
        """ Method calculates and returns standard based on list of numbers """
        mean = self.calculate_average()

        mean_difference_list = []

        for num in self.num_list:
            mean_difference_list.append(math.pow((num - mean), 2))

        mean_squared_differences = sum(mean_difference_list) / (len(mean_difference_list) - 1)
        standard_deviation = math.sqrt(mean_squared_differences)

        return standard_deviation

    def calculate_average(self):
        """ Method calculates and returns average based on list of numbers """
        return sum(self.num_list) / len(self.num_list)

    def find_max_number(self):
        """ Method finds and returns maximum number from list of numbers """
        return max(self.num_list)


if __name__ == "__main__":
    myMathObject = MyMath()
    myMathObject.num_list = \
        [int(item) for item in input("Enter the elements separated by a space: ").split()]

    print(f"Maximum of nums {myMathObject.num_list} is: {myMathObject.find_max_number()}")

    print(f"Average of nums {myMathObject.num_list} is: {myMathObject.calculate_average():.3f}")

    print(f"Standard deviation of nums {myMathObject.num_list} is: "
          f"{myMathObject.calculate_standard_deviation():.3f}")
