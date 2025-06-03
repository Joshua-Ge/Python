"""Basic practice using lists and the other functionality that python provides"""

temperatures = [23, 25, 19, 22, 26, 21, 24]
total = 0
length = len(temperatures)
warmest = max(temperatures)
coldest = min(temperatures)
above_average = []

for i in temperatures:
    total += i


average = total / length
average = round(average, 2)

for i in temperatures:
    if i > average:
        above_average.append(i)


print(total)
print(length)
print(f"The average temperature over the days was {average} degrees C")
print(f"The Warmest was {warmest} degrees C")
print(f"The Coldest was {coldest} degrees C")
print(f"The above average temperatures are {above_average}")