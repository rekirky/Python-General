import time
start_time = time.time()
for i in range(1,101,1):
  output = ""
  if i%3 == 0: output += 'Fizz'
  if i%5 == 0: output += 'Buzz'
  if output == "": output += str(i)
  print(output)
