def odd_sum(number):
    sum =0
    for x in range(1,number+1):
      if x%2 != 0:
         sum+=x
    return sum
def even_average(number):
    sum =0
    count = 0
    for x in range(1,number+1):
        if x%2 == 0:
           sum+=x
           count+=1
           average = sum/count
    return average
intp =int(input("enter a number:\n"))
print(odd_sum(intp))
print(even_average(intp))



