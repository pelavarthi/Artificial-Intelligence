import sys; args = sys.argv[1:]
import random
infile = open(args[0])

# Transfer function, basically just g(x) on the worksheet
def transfer(t_funct, input):
    e = 2.718281828459
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

# ChatGPT W
# Does the multiplicaiotn of the weight with the value, and then adds it up
def dot_product(l1, l2):
    return sum(a * b for a, b in zip(l1, l2))

def forwardFeed(inputs, t, weights, layerCounts):
    xVals = []
    xVals.append(inputs)
    # Loops through each stage of weights except for the last one
    while len(weights) > 1:
        temp = []
        # Goes through and does the dot product
        for i in range(len(weights[0])//len(inputs)):
            temp.append(dot_product(inputs, weights[0][i*len(inputs):(i+1)*len(inputs)]))
        # Resets input_vals for the next iteration through at the next stage
        inputs = []
        for thing in temp:
            inputs.append(transfer('T3',thing))
        xVals.append(inputs)
        weights.pop(0)
    # For the last stage, there is no need for transfer
    final = []
    for i in range(len(weights[0])):
        final.append(weights[0][i]*inputs[i])
    xVals.append(final)
    return xVals

def backProp(xv, weights, t):
    # En+1 * weight * x * 1-x
    # First E = t-yfinal
    # negGrad = En+1 * x
    Evals = xv[:]
    Evals[-1][0] = (t-xv[-1][0])
    for i in range(len(Evals)-2,-1,-1):
        for j in range(len(Evals[i])):
            if i==0:
                Evals[i][j] = Evals[i][j]
            else: 
                Evals[i][j] = Evals[i+1][j//2]*xv[i][j] * (1-xv[i][j]) * weights[i][i*j]# * weight

    
    negative_grad = []
    for i in range(1,len(Evals)):
        li = list()
        for j in range(len(Evals[i])):

            for thing in xv[i-1]:
                li.append(thing * Evals[i][j])
        negative_grad.append(li)

    alpha = 0.3
    newWeights = updateWeights(weights, alpha, negative_grad)
    return newWeights, Evals

def updateWeights(weights, alpha, negative_grad):
    return[[weights[i][j] + alpha * negative_grad[i][j] for j in range(len(weights[i]))] for i in range(len(weights))]

'''
def ff(ts, xv, weights, t_funct):
   inputLength = len(ts)
   for i in range(len(weights)):
        for j in range(len(weights[i])):
            weights[i][j] = float(weights[i][j])

   while len(weights) > 1:
        res = []
        for i in range(len(weights[0])//inputLength):
            res.append(dot_product(input_vals, weights[0][i*inputLength:(i+1)*inputLength]))
        input_vals = [transfer(t_funct, x) for x in res]
        weights.pop(0)
        inputLength = len(input_vals)
   fres = []
   for i in range(len(weights[0])):
        fres.append(weights[0][i]*input_vals[i])

   err = sum([(ts[i - len(xv[-1])] - xv[-1][i])**2 for i in range(len(xv[-1]))]) / 2
   return xv, err
'''


def main():
    weights = []
    error = 10000
    for line in infile:
        lst = line.strip().split(" ")
        splitIndex = lst.index("=>")
        inputs = lst[:splitIndex]
        for i in range(len(inputs)):
            inputs[i] = float(inputs[i])
        t = float(lst[-1])
        inputs.append(1.0)
        layerCounts = [len(inputs), 2, 1, 1]
        for i in range(len(layerCounts)-1):
            weights.append([0]*(layerCounts[i]*layerCounts[i+1]))
        for thing in weights:
            for i in range(len(thing)):
                thing[i] = round(random.uniform(-2,2), 2)
        break
    brk = False
    errors = []
    layerCounts = []
    count = 0
    while True:
        fil = open(args[0])
        for line in fil:
            lst = line.strip().split(" ")
            splitIndex = lst.index("=>")
            inputs = lst[:splitIndex]
            for i in range(len(inputs)):
                inputs[i] = float(inputs[i])
            t = float(lst[-1])
            inputs.append(1.0)
            layerCounts = [len(inputs), 2, 1, 1]
            
            weightsCopy = [list(sublist) for sublist in weights]
            inputsCopy = inputs[:]
            output = forwardFeed(inputsCopy, t, weightsCopy, layerCounts)
            # print("Forward Feed Values: ")
            # print(output)
            # print()
            # print("Weights:")
            # print(weights)
            # print()
            # print("Error:")
            #error = 0.5 * ((t-output[-1][0])*(t-output[-1][0]))
            # print(error)

            weights = backProp(output, weights, t)[0]
            # print()
            # print("Better Weights: ")
            # print(weights)
            # print()
            # print("New Error:")
            weightsCopy = [list(sublist) for sublist in weights]
            newOutput = forwardFeed(inputs, t, weightsCopy, layerCounts)

            #error = abs(t-newOutput[-1][0])
            error = 0.5*((t-newOutput[-1][0])*(t-newOutput[-1][0]))
            # print(error)

            if error > 2:
                for thing in weights:
                    for i in range(len(thing)):
                        thing[i] = round(random.uniform(-2,2), 2)
            # print(error)
            #print(weights)

            errors.append(error)

            # print("____________________________________________________________")`
        if sum(errors) < 0.01:
                print("Errors:", errors)
                print("Layer cts:", layerCounts)
                print("Weights:")
                for thing in weights:
                    print(thing)

                break
        if (sum(errors) > 1):
            #print("hi")
            for thing in weights:
                for i in range(len(thing)):
                    thing[i] = round(random.uniform(-2,2), 2)
        for er in errors:
            if abs(.5-er) < 0.01:
                #print("restarting2")
                for thing in weights:
                    for i in range(len(thing)):
                        thing[i] = round(random.uniform(-2,2), 2)
        for li in weights:
            for num in li:
                if num > 250 or num==0:
                    #print("restarting..")
                    for thing in weights:
                        for i in range(len(thing)):
                            thing[i] = round(random.uniform(-2,2), 2)
        count+= 1
        if count%6250 == 0:
            for i in weights:
                print(i)
            print("Errors", errors)
            print("Weights: ", weights)
        
        errors = []

if __name__ == '__main__': main()

# Pranav Elavarthi, 5, 2024