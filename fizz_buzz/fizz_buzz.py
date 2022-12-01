for number in range(1, 101):
  # bug was: if number % 3 == 0 or number % 5 == 0:
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  # bug was: if number % 3 == 0:
  elif number % 3 == 0:
    print("Fizz")
  # bug was: if number % 5 == 0:
  elif number % 5 == 0:
    print("Buzz")
  else:
    # bug was: print([number])
    print(number)