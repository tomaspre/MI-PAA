#   Knapsack problem
#   Tomas Preucil (preucto2) @ CTU FIT
#   MI-PAA course
import time
import queue
import copy
import numpy as np
import math
#from bitarray import bitarray
import random

## Veselé VéVéce! :-) https://www.youtube.com/watch?v=aowNqlym7bc (side note Kirito+Asuna=OTP)

populationSize = 400
populations = 150
penality = 10000
mutationProbability = 7    #integer(!), probability in percent
crossoverProbability = 70   #integer(!), probability in percent
maxWithoutChange = 20

#OLD
# bfStates = 0
# dpStates = 0
# babStates = 0
# heuStates = 0

# #   Class for storing item info
class item:
    def __init__(self):
        self.value = 0
        self.size = 0
        self.relativeValue = 0
        self.present = 0 #Value for the "bit vector"

#
#
# #   Class for tree node used from second task forward
# class node():
#     level = 0
#     profit = 0
#     bound = 0.0
#     weight = 0
#
# #   Branch and bound -- global maximum variable
# globalMaxBaB = 0
#
# #   Bruteforce (yay)
# def solveKnapsackBF(capacity, itemsAvailable, items):
#     global bfStates
#     bfStates += 1
#
#     if capacity == 0 or itemsAvailable == 0:
#         return 0
#
#     if items[itemsAvailable - 1].size > capacity:
#         return solveKnapsackBF(capacity, itemsAvailable - 1, items)
#
#     return max(
#         items[itemsAvailable - 1].value + solveKnapsackBF(capacity - items[itemsAvailable - 1].size, itemsAvailable - 1,items),
#             solveKnapsackBF(capacity, itemsAvailable - 1, items))
#
# #   Bruteforce with dynamic programming by capacity -- wrapper
# def solveKnapsackDPbyCap(capacity, itemsAvailable, items):
#     decompositionArray = [[None for i in range(capacity)] for j in range(itemsAvailable)]
#
#     tmp = solveKnapsackDPworkbyCap(capacity, itemsAvailable, items, decompositionArray)
#
#     #print(counterA)
#     return tmp
#
# #   Bruteforce with dynamic programming by capacity -- function that does the work
# def solveKnapsackDPworkbyCap(capacity, itemsAvailable, items, decompositionArray):
#     global dpStates
#     dpStates += 1
#
#     if decompositionArray[itemsAvailable - 1][capacity - 1] != None:
#         return decompositionArray[itemsAvailable - 1][capacity - 1]
#
#     if capacity == 0 or itemsAvailable == 0:
#         return 0
#
#     if items[itemsAvailable - 1].size > capacity:
#         return solveKnapsackDPworkbyCap(capacity, itemsAvailable - 1, items, decompositionArray)
#
#     tmp = max(items[itemsAvailable - 1].value + solveKnapsackDPworkbyCap(capacity - items[itemsAvailable - 1].size,
#                                                                          itemsAvailable - 1, items, decompositionArray),
#                                     solveKnapsackDPworkbyCap(capacity, itemsAvailable - 1, items, decompositionArray))
#
#     decompositionArray[itemsAvailable - 1][capacity - 1] = tmp
#
#     return tmp
#
# #   FPTAS scaling function
# def scaleForFPTAS(value, FPTAS):
#     #return  value
#     return int(math.floor(float(value) / float(FPTAS)))
#
# #   Dynamic programming by value -- wrapper, FPTAS available as last parameter
# def solveKnapsackDPbyVal(capacity, itemsAvailable, items, FPTAS = 1):
#     sum = 0
#     for it in items:
#         sum += it.value
#
#     global counterB
#     counterB = 0
#     arr = [[None for i in range(scaleForFPTAS(sum, FPTAS)+1)] for j in range(itemsAvailable + 1)]
#
#     tmp = solveKnapsackDPworkbyVal(capacity, itemsAvailable, items, arr, sum, FPTAS)
#     #print(counterB)
#     return tmp
#
# #   Dynamic programming by value -- function that does the work
# def solveKnapsackDPworkbyVal(capacity, itemsAvailable, items, decompositionArray, sum, FPTAS):
#     global counterB
#     for l in range(itemsAvailable):
#         if (l == 0):
#             decompositionArray[l][scaleForFPTAS(items[l].value, FPTAS)] = items[l].size
#             continue
#
#         for m in range(scaleForFPTAS(sum, FPTAS)+1):
#             counterB += 1
#             if m == scaleForFPTAS(items[l].value, FPTAS):
#                 if decompositionArray[l][m] and decompositionArray[l][m] > items[l].size:
#                     continue
#                 else:
#                     decompositionArray[l][m] = items[l].size
#             elif decompositionArray[l - 1][m]:
#                 decompositionArray[l][m] = decompositionArray[l - 1][m]
#                 decompositionArray[l][scaleForFPTAS(items[l].value, FPTAS) + m] = decompositionArray[l - 1][m] + items[l].size
#     #np.set_printoptions(threshold=np.inf)
#     #print(np.matrix(decompositionArray))
#     max = 0
#     for l in range(scaleForFPTAS(sum, FPTAS), -1, -1):
#         # print(l)
#         if decompositionArray[itemsAvailable - 1][l] and decompositionArray[itemsAvailable - 1][l] <= capacity and \
#                 l > max:
#             max = l
#
#     return max * FPTAS
#
# #   Super simple heuristics -- just sort by size/weight ratio
# def solveKnapsackHeuristics(capacity, itemsAvailable, items):
#     result = 0
#
#     for j in items:
#         if j.value == 0:
#             break
#         j.relativeValue = j.size / j.value
#
#     items.sort(key=lambda x: x.relativeValue, reverse=False)
#
#     global heuStates
#
#     for j in items:
#
#         heuStates += 1
#         if capacity == 0:
#             break
#
#         if capacity >= j.size:
#             result += j.value
#             capacity -= j.size
#
#     return result
#
# #   Branch and bound take two -- wrapper
# def solveKnapsackBB(capacity, itemsAvailable, items):
#     potential = 0
#     current = 0
#     for i in items:
#         potential += i.value
#
#     global globalMaxBaB
#     globalMaxBaB = 0
#
#     return solveKnapsackBBwork(capacity, itemsAvailable, items, potential, current)
#
# #   Branch and bound, take two - work function
# def solveKnapsackBBwork(capacity, itemsAvailable, items, potential, current):
#     global globalMaxBaB
#     global babStates
#     babStates += 1
#
#     if current > globalMaxBaB:
#         globalMaxBaB = current
#
#     if current + potential < globalMaxBaB:
#         return 0
#
#     if capacity == 0 or itemsAvailable == 0:
#         return 0
#
#     if items[itemsAvailable - 1].size > capacity:
#         return solveKnapsackBBwork(capacity, itemsAvailable - 1, items, potential - items[itemsAvailable - 1].value, current)
#
#     return max(
#         items[itemsAvailable - 1].value + solveKnapsackBBwork(capacity - items[itemsAvailable - 1].size, itemsAvailable - 1,items, potential - items[itemsAvailable - 1].value, current + items[itemsAvailable - 1].value),
#         solveKnapsackBBwork(capacity, itemsAvailable - 1, items, potential - items[itemsAvailable - 1].value, current))


#   Main
#
#print("ID:Items:byCap:byCapTime:byValue:byValueTime:FPTAS:FPTAStime:branch:branchTime")
#print("Opt:2err:time:5err:time:10err:time:20err:time:50err:time")
#print("ID:Items:BF:BFtime:BFstates:Heu:HeuTime:HeuError:HeuStates:DPbyCap:DPbyCapTime:DPstates:BaB:BaBTime:BaBstates")


#This can stay for SAT
class chromosome:
    def __init__(self, size, items, capacity, init=0):
        self.fitness = 0
        self.arr = []
        for i in range(size):
            self.arr.append(items[i])
        self.capacity = capacity
        self.size = size

        if init == 1:
            avgValue = 0
            for i in range(size):
                avgValue += self.arr[i].value / size

            for i in range(size):
                tmp = 0
                if self.arr[i].value > avgValue and random.randint(0, 3) > 2 and self.arr[i].size <= capacity * 0.8:
                    tmp = 1

                self.arr[i].present = max(random.randint(0, 100) % 2, tmp)

        self.calcFitness()

    # This needs to be modified for SAT
    def calcFitness(self):
        global penality

        totalWeight = 0
        value = 0

        for i in range(self.size):
            totalWeight += self.arr[i].size * self.arr[i].present
            value += self.arr[i].value * self.arr[i].present

        self.fitness = value

        if totalWeight > self.capacity:
            self.fitness -= penality


    # This can stay for SAT
    def mutate(self):
        bitNumber = random.randint(0, self.size-1)
        newArray = copy.deepcopy(self.arr)
        if newArray[bitNumber].present == 1:
            newArray[bitNumber].present = 0
        else:
            newArray[bitNumber].present = 1

        newChromosome = chromosome(self.size, newArray, self.capacity)

        return newChromosome


    # This can stay for SAT
    def crossover(self, second):
        crossAt = random.randint(0, self.size)

        arrayForChildA = []
        arrayForChildB = []

        for i in range(self.size):
            if (i < crossAt):
                arrayForChildA.append(self.arr[i])
                arrayForChildB.append(second.arr[i])
            else:
                arrayForChildA.append(second.arr[i])
                arrayForChildB.append(self.arr[i])

        childA = chromosome(self.size, arrayForChildA, self.capacity)
        childB = chromosome(self.size, arrayForChildB, self.capacity)

        return childA, childB

    # This can stay for SAT
    def getFitness(self):
        return self.fitness


    def setPresentBit(self, index, value):
        self.arr[index].present = value


f = open('input.dat', 'r')
while (1):
    line = f.readline()
    if len(line) == 0:
        break
    line = line[:-1]
    arr = line.split()
    items = [None] * int(arr[1])
    numberOfThings = int(arr[1])

    for i in range(0, int(arr[1])):
        inputObject = item()
        inputObject.size = int(arr[3 + 2 * i])
        inputObject.value = int(arr[4 + 2 * i])
        items[i] = inputObject

    start = time.process_time()
    #Initialze population - random is love, random is life
    chromosomeArray = [] #Basic pop. size + all can mutate + all can cross (which yelds 2 ch.)
    for i in range(populationSize):
        chromosomeArray.append(chromosome(numberOfThings, items, int(arr[2]), 1))

    #Do the genetic stuff
    maximum = 0
    maxCount = 0
    for i in range(populations):
        currentPopulationSize = populationSize

        #Crossover
        for j in range(populationSize):
            if random.randint(0, 100) < crossoverProbability:
                crossWith = random.randint(0, populationSize-1)
                childA, childB = chromosomeArray[j].crossover(chromosomeArray[crossWith])
                chromosomeArray.append(childA)
                chromosomeArray.append(childB)
                currentPopulationSize += 2

        #Mutate
        for j in range(populationSize):
            if random.randint(0, 100) < mutationProbability:
                child = chromosomeArray[j].mutate()
                chromosomeArray.append(child)
                currentPopulationSize += 1

        #Sort
        #chromosomeArray = chromosomeArray[:currentPopulationSize-1]
        chromosomeArray.sort(key=lambda x: x.fitness, reverse=True)

        # Get rid of non surviving chromosomes
        # Well, not really needed :-)
        chromosomeArray = chromosomeArray[:populationSize]

        if chromosomeArray[0].fitness > maximum:
            maximum = chromosomeArray[0].fitness
            maxCount = 0
        else:
            maxCount += 1

        print(chromosomeArray[0].fitness, end=',')

        #if maxCount >= maxWithoutChange:
        #    break

    end = time.process_time()
    mytime = end - start

    #print(arr[0], end=',')
    #print(chromosomeArray[0].fitness, end=',')
    #print(mytime)
    print()


#OLD

    # bf = 0.0
    # bfTime = 0.0
    #
    # heu = 0.0
    # heuTime = 0.0
    #
    # dpbyVal = 0.0
    # dpTimebyVal = 0.0
    #
    # dpbyCap = 0.0
    # dpTimebyCap = 0.0
    #
    # dpFPTAS = 0.0
    # dpTimeFPTAS = 0.0
    #
    # bab = 0.0
    # babTime = 0.0
    #
    # bfStates = 0
    # dpStates = 0
    # babStates = 0
    # heuStates = 0
    #
    # # BF
    # itemsForProcessing = copy.deepcopy(items)
    # start = time.process_time()
    # bf = solveKnapsackBF(int(arr[2]), int(arr[1]), itemsForProcessing)
    # end = time.process_time()
    # bfTime = end - start
    #
    # # # Heuristics
    # itemsForProcessing = copy.deepcopy(items)
    # start = time.process_time()
    # for l in range(0, 999):
    #     heu = solveKnapsackHeuristics(int(arr[2]), int(arr[1]), itemsForProcessing)
    # end = time.process_time()
    # heuTime = (end - start) / 1000
    #
    # # # DP -- by capacity
    # start = time.process_time()
    # itemsForProcessing = copy.deepcopy(items)
    # dpbyCap = solveKnapsackDPbyCap(int(arr[2]), int(arr[1]), itemsForProcessing)
    # end = time.process_time()
    # dpTimebyCap = (end - start)
    #
    # # # DP -- by value
    # # start = time.process_time()
    # # if int(int(arr[1]) <= 15):
    # #     for i in range(100):
    # #         itemsForProcessing = copy.deepcopy(items)
    # #         dpbyVal = solveKnapsackDPbyVal(int(arr[2]), int(arr[1]), itemsForProcessing)
    # #     end = time.process_time()
    # #     dpTimebyVal = (end - start) / 100
    # # else:
    # #     itemsForProcessing = copy.deepcopy(items)
    # #     dpbyVal = solveKnapsackDPbyVal(int(arr[2]), int(arr[1]), itemsForProcessing)
    # #     end = time.process_time()
    # #     dpTimebyVal = end - start
    # #
    # # # # DP -- by value using FPTAS
    # # start = time.process_time()
    # # if int(int(arr[1]) <= 15):
    # #     for i in range(100):
    # #         itemsForProcessing = copy.deepcopy(items)
    # #         dpFPTAS = solveKnapsackDPbyVal(int(arr[2]), int(arr[1]), itemsForProcessing, 10)
    # #     end = time.process_time()
    # #     dpTimeFPTAS = (end - start) / 100
    # # else:
    # #     itemsForProcessing = copy.deepcopy(items)
    # #     dpFPTAS = solveKnapsackDPbyVal(int(arr[2]), int(arr[1]), itemsForProcessing, 5)
    # #     end = time.process_time()
    # #     dpTimeFPTAS = end - start
    #
    # # # BaB
    # start = time.process_time()
    # itemsForProcessing = copy.deepcopy(items)
    # bab = solveKnapsackBB(int(arr[2]), int(arr[1]), itemsForProcessing)
    # end = time.process_time()
    # babTime = (end - start)
    #
    # print(arr[0], end=':')
    # print(arr[1], end=':')
    # #print(counterA)
    # #print(counterB)
    # print(bf, end=':')
    # print(bfTime, end=':')
    # print(bfStates, end=':')
    # print(heu, end=':')
    # print(heuTime, end=':')
    # print((bf-heu)/bf, end=':')
    # print(heuStates, end=':')
    # print(dpbyCap, end=':')
    # print(dpTimebyCap, end=':')
    # print(dpStates, end=':')
    # # print(dpbyVal, end=':')
    # # print(dpTimebyVal, end=':')
    # # print(dpFPTAS, end=':')
    # # print(dpTimeFPTAS, end=':')
    # print(bab, end=':')
    # print(babTime, end=':')
    # print(babStates, end=':')
    # #
    # # # ( C(OPT)-C(APX) ) / C(OPT)
    # # # if int(arr[1]) <= 25:
    # # #    print((bf-heu)/bf)
    # # # else:
    # #    print("0")
    # #print("")
    # # break
    #
    # ##Measure error and time for FPTAS
    # # itemsForProcessing = copy.deepcopy(items)
    # # dpbyCap = solveKnapsackDPbyVal(int(arr[2]), int(arr[1]), itemsForProcessing, 1)
    # # print(dpbyCap, end=':')
    # #
    # # itemsForProcessing = copy.deepcopy(items)
    # # start = time.process_time()
    # # FPTAS2 = solveKnapsackDPbyVal(int(arr[2]), int(arr[1]), itemsForProcessing, 2)
    # # end = time.process_time()
    # # print((dpbyCap - FPTAS2) / dpbyCap, end=':')
    # # print(end - start, end=':')
    # #
    # # itemsForProcessing = copy.deepcopy(items)
    # # start = time.process_time()
    # # FPTAS5 = solveKnapsackDPbyVal(int(arr[2]), int(arr[1]), itemsForProcessing, 5)
    # # end = time.process_time()
    # # print((dpbyCap - FPTAS5) / dpbyCap, end=':')
    # # print(end - start, end=':')
    # #
    # # itemsForProcessing = copy.deepcopy(items)
    # # start = time.process_time()
    # # FPTAS10 = solveKnapsackDPbyVal(int(arr[2]), int(arr[1]), itemsForProcessing, 10)
    # # end = time.process_time()
    # # print((dpbyCap - FPTAS10) / dpbyCap, end=':')
    # # print(end - start, end=':')
    # #
    # # itemsForProcessing = copy.deepcopy(items)
    # # start = time.process_time()
    # # FPTAS20 = solveKnapsackDPbyVal(int(arr[2]), int(arr[1]), itemsForProcessing, 20)
    # # end = time.process_time()
    # # print((dpbyCap - FPTAS20) / dpbyCap, end=':')
    # # print(end - start, end=':')
    # #
    # # itemsForProcessing = copy.deepcopy(items)
    # # start = time.process_time()
    # # FPTAS50 = solveKnapsackDPbyVal(int(arr[2]), int(arr[1]), itemsForProcessing, 50)
    # # end = time.process_time()
    # # print((dpbyCap - FPTAS50) / dpbyCap, end=':')
    # # print(end - start)
