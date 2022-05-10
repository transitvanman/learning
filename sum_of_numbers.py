class Natural_number_class(object):
    def sum_100_natural_numbers(self):
        sum = 0
        for i in range(1, 101):
            sum = sum + i
        return sum
#Create an Object
object_sum = Natural_number_class()
print(object_sum.sum_100_natural_numbers())
