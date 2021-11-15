""" Standard Deviation module provides access to the MyMath class and its functions """
import math


class MyMath:
    """ MyMath class provides access to the mathematical functions """

    def __init__(self):
        """ Method initializes list of number """
        try:
            self.num_list = []
        except Exception as init_err:
            print(init_err)

    def calculate_standard_deviation(self):
        """ Method calculates and returns standard based on list of numbers """
        try:
            mean = self.calculate_average()

            mean_difference_list = []

            try:
                for num in self.num_list:
                    mean_difference_list.append(math.pow((num - mean), 2))
            except ValueError as stddev_value_err:
                print(stddev_value_err)

            mean_squared_differences = sum(mean_difference_list) / (len(mean_difference_list) - 1)
            standard_deviation = math.sqrt(mean_squared_differences)

            return standard_deviation

        except Exception as stddev_err:
            print(stddev_err)

    def calculate_average(self):
        """ Method calculates and returns average based on list of numbers """
        try:
            average = 0

            try:
                for num in self.num_list:
                    average += num
            except ValueError as average_value_err:
                print(average_value_err)

            return average / len(self.num_list)
        except Exception as average_err:
            print(average_err)

    def find_max_number(self):
        """ Method finds and returns maximum number from list of numbers """
        try:
            max_num = self.num_list[0]
            try:
                for num in self.num_list:
                    if max_num < num:
                        max_num = num
            except ValueError as max_value_err:
                print(max_value_err)
            return max_num
        except Exception as max_err:
            print(max_err)


if __name__ == "__main__":
    try:
        myMathObject = MyMath()

        try:
            myMathObject.num_list = \
                [int(item) for item in input("Enter the elements separated by a space: ").split()]
        except ValueError as value_err:
            print(value_err)

        print(f"Maximum of nums {myMathObject.num_list} is: {myMathObject.find_max_number()}")

        print(f"Average of nums {myMathObject.num_list} is: {myMathObject.calculate_average():.3f}")

        print(f"Standard deviation of nums {myMathObject.num_list} is: "
              f"{myMathObject.calculate_standard_deviation():.3f}")
    except Exception as exception_err:
        print(exception_err)
