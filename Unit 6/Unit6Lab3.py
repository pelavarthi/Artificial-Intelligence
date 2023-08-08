import sys; args = sys.argv[1:]
import random
inp = str(args[0])

# Transfer function, basically just g(x) on the worksheet
def transfer(t_funct, input):
    #print(input)
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
                Evals[i][j] = Evals[i+1][j//(len(xv[i]))]*xv[i][j%(len(xv[i]))] * (1-xv[i][j%len(xv[i])]) * weights[i][j]# * weight    
    negative_grad = []
    for i in range(1,len(Evals)):
        li = list()
        for j in range(len(Evals[i])):

            for thing in xv[i-1]:
                li.append(thing * Evals[i][j])
        negative_grad.append(li)
    alpha = 0.3
    newWeights = updateWeights(weights, alpha, negative_grad)
    return newWeights

def updateWeights(weights, alpha, negative_grad):
    return[[weights[i][j] + alpha * negative_grad[i][j] for j in range(len(weights[i]))] for i in range(len(weights))]

def main():
    asdf = [3,12,6,4,1,1]
    print("Layer Counts: ", asdf)
    print(inp)
    temp = []
    if ">=" in inp:
        temp = inp.split("=")
    elif "<=" in inp:
        temp = inp.split("=")
    elif ">" in inp:
        temp = inp.split(">")
    else:
        temp = inp.split("<")
    
    rSquared = float(temp[1])
    print(rSquared)
    training = []
    for num in range(30000):
        tempTup = [round(random.uniform(-1.5,1.5), 2), round(random.uniform(-1.5,1.5), 2)]
        x = tempTup[0]
        y = tempTup[1]
        num = (x*x) + (y*y)
        if ">=" in inp:
            if ((x*x) + (y*y)) >= rSquared:
                tempTup.append(1.0)
            else:
                tempTup.append(0.0)
        elif "<=" in inp:
            if ((x*x) + (y*y)) <= rSquared:
                tempTup.append(1.0)
            else:
                tempTup.append(0.0)
        elif ">" in inp:
            if ((x*x) + (y*y)) > rSquared:
                tempTup.append(1.0)
            else:
                tempTup.append(0.0)
        else:
            if ((x*x) + (y*y)) < rSquared:
                tempTup.append(1.0)
            else:
                tempTup.append(0.0)
        
        training.append(tempTup)
    weights = []
    error = 10000
    for line in training:
        inputs = line[:2]
        for i in range(len(inputs)):
            inputs[i] = float(inputs[i])
        t = float(line[-1])
        inputs.append(1.0)
        layerCounts = [len(inputs),12, 6, 4,1,1]
        for i in range(len(layerCounts)-1):
            weights.append([0]*(layerCounts[i]*layerCounts[i+1]))
        for thing in weights:
            for i in range(len(thing)):
                thing[i] = round(random.uniform(-0.5,0.5), 3)
        break
    errors = []
    layerCounts = []
    count = 0
    print(training)
    for thing in training:
        inputs = thing[:2]
        for i in range(len(inputs)):
            inputs[i] = float(inputs[i])
        t = float(thing[-1])
        inputs.append(1.0)
        layerCounts = [len(inputs), 12,6,4,1,1]
        weightsCopy = []
        for li in weights:
            weightsCopy.append(li[:])
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

        weights = backProp(output, weights, t)
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

        # if error > 2:
        #     for thing in weights:
        #         for i in range(len(thing)):
        #             thing[i] = round(random.uniform(-0.5,0.5), 3)
        # print(error)
        #print(weights)

        errors.append(error)

        # for er in errors:
        #     if abs(.5-er) < 0.0001 or er > 20000:
        #         print("restarting2")
        #         for thing in weights:
        #             for i in range(len(thing)):
        #                 thing[i] = round(random.uniform(-0.5,0.5), 2)

        count+= 1
        if count%1000 == 0:
            for i in weights:
                print(i)

        # print("____________________________________________________________")`
    # if sum(errors) < 10:
    #         print("Errors:", errors)
    #         print("Layer cts:", layerCounts)
    #         print("Weights:")
    #         for thing in weights:
    #             print(thing)
    count = 0
    for thing in errors:
        if thing < 0.01:
            count += 1
    print(count)
    print(sum(errors))
            
    # if (sum(errors) > 1):
    #     #print("hi")
    #     for thing in weights:
    #         for i in range(len(thing)):
    #             thing[i] = round(random.uniform(-2,2), 2)
    # for er in errors:
    #     if abs(.5-er) < 0.0001 or er > 200:
    #         print("restarting2")
    #         for thing in weights:
    #             for i in range(len(thing)):
    #                 thing[i] = round(random.uniform(-0.5,0.5), 2)
    # for li in weights:
    #     for num in li:
    #         if abs(num) > 250 or num==0:
    #             print("restarting..")
    #             for thing in weights:
    #                 for i in range(len(thing)):
    #                     thing[i] = round(random.uniform(-0.5,0.5), 2)
    
    
    errors = []

if __name__ == '__main__': main()

# Pranav Elavarthi, 5, 2024