## Ok so i was able to knock this up after alot of research.
## Its not how I thought id do it but Im sure this has fewer
## lines of code than I would have originally wrote.

class number(object):
    def sum_100_numbers(self):
        sum = 0
        for i in range(1, 101):
            sum = sum + i
        return sum
#Create an Object
object_sum = number()
print(object_sum.sum_100_numbers())
