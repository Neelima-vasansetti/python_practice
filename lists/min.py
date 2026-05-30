numbers = [3,5,8,2,4,5]
min_value = numbers[0]
for i in range(0, len(numbers)):
  if numbers[i] < min_value:
    min_value = numbers[i]
print(min_value)