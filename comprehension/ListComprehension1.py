#Determine if a list of numbers is odd or even.
numbers = [3, 72, 39, 11, 195, 300, 100, 41, 8];

oddOrEven = [{f"{x}": "even" if x%2==0 else "odd"} for x in numbers];
print(oddOrEven)