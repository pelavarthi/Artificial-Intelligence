import sys; args = sys.argv[1:]
file = open(args[0])
import math # didnt really use this lol
e = 2.718281828459

# Transfer function, basically just g(x) on the worksheet
def transfer(t_funct, input):
   input = float(input)
   # T1
   if (t_funct == "T1"):
      return input
   # T2
   if (t_funct == "T2"):
      if input > 0:
         return input
      else:
         return 0
   # T3
   if (t_funct == "T3"):
      return 1/(1+(e**(-input)))
   # T4
   if (t_funct == "T4"):
      return (2/(1+(e**(-input))))-1
   else:
      return 0

# def dot_product(input, weights, stage):

# ChatGPT W
# Does the multiplicaiotn of the weight with the value, and then adds it up
def dot_product(l1, l2):
    return sum(a * b for a, b in zip(l1, l2))

# Goes through each level and then calls the dot product and transfer to go to the next stage
def evaluate(file, input_vals, t_funct):
   # Initial setup of weights, reading in the file
   weights = []
   for line in file:
      weights.append(line.strip().split())
   for i in range(len(weights)):
      for j in range(len(weights[i])):
         weights[i][j] = float(weights[i][j])

   # Loops through each stage of weights except for the last one
   while len(weights) > 1:
      temp = []
      # Goes through and does the dot product
      for i in range(len(weights[0])//len(input_vals)):
         temp.append(dot_product(input_vals, weights[0][i*len(input_vals):(i+1)*len(input_vals)]))
      # Resets input_vals for the next iteration through at the next stage
      input_vals = []
      for thing in temp:
         input_vals.append(transfer(t_funct,thing))
      print(input_vals)
      weights.pop(0)
   # For the last stage, there is no need for transfer
   final = []
   for i in range(len(weights[0])):
      final.append(weights[0][i]*input_vals[i])
   return final
   # stage = 1
   # for i in range(len(file)):
   #    line = file[i]
   #    line = line.strip()
   #    weights = line.split() 
   #    for thing in range(len(weights)):
   #       weights[thing] = float(weights[thing])
   #    temp = dot_product(input_vals, weights, stage)
   #    input_vals = []
   #    for i in range(len(temp)):
   #       input_vals.append(transfer(t_funct, temp[i]))
   #    stage += 1
   # return input_vals

def main():
   inputs, t_funct, transfer_found = [], 'T1', False
   for arg in args[1:]:
      if not transfer_found:
         t_funct, transfer_found = arg, True
      else:
         inputs.append(float(arg))
   li =(evaluate(file, inputs, t_funct)) #ff
   for x in li:
      print (x, end=' ') # final outputs
   print()

if __name__ == '__main__': main()

# Pranav Elavarthi, Period 5, 2024