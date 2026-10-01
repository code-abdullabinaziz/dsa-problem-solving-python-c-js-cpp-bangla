numbers = [10, 20, 30, 40, 50]

user_input = int(input("Enter a number to check if it is in the list: "))

if user_input % 2 == 0:
  print(f"{user_input} is in the list")
else:
  print(f"{user_input} not in the list")