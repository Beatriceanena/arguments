def multiply_and_greetings(*integers,**student):
   product=1
   for num in integers:
      product*=num
   print(product)
   print(f"hello {student}")

