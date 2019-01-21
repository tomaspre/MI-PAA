#   SAT problem
#   Tomas Preucil (preucto2) @ CTU FIT
#   MI-PAA course
import time
import queue
from copy import deepcopy
import numpy as np
import math
#from bitarray import bitarray
import random
import sys

populationSize = 600
populations = 400
penality = 10
mutationProbability = 40    #integer(!), probability in percent
crossoverProbability = 18   #integer(!), probability in percent
maxWithoutChange = 20
zeroCoefficient = 1
tournament = 5

#This can stay for SAT
class chromosome:
    def __init__(self, size, items, problemClass, init=0):
        self.fitness = 0
        self.arr = []
        if init == 0:
            self.arr = deepcopy(items)
        #self.restriction = restriction
        self.size = size
        self.problemClass = problemClass

        if init == 1:
            for i in range(self.problemClass.noVariables):
                self.arr.append(random.randint(0, 100) % 2)

        self.calcFitness()

    # This needs to be modified for SAT
    def calcFitness(self):
        global penality

        satisfied = 1
        #First we need to check, iof the formula is satisfied
        satisfiedClauses = 0
        for cl in range(self.problemClass.noClausules):
            for var in range(len(self.problemClass.formula[cl])):
                varTrue = self.arr[abs(self.problemClass.formula[cl][var]) - 1]
                if self.problemClass.formula[cl][var] > 0 and varTrue == 1 or self.problemClass.formula[cl][var] < 0 and varTrue == 0:
                    satisfiedClauses += 1
                    break


        if satisfiedClauses != self.problemClass.noClausules:
            self.fitness = penality * (self.problemClass.noClausules - satisfiedClauses) * (-1)
            #print(self.fitness)
            return

        value = 0

        for var in range(self.size):
            value = value + self.arr[var] * self.problemClass.weights[var]

        self.fitness = value
        #print(self.fitness)

    # This can stay for SAT
    def mutate(self):
        bitNumber = random.randint(0, self.size-1)
        newArray = deepcopy(self.arr)
        if newArray[bitNumber] == 1:
            newArray[bitNumber] = 0
        else:
            newArray[bitNumber] = 1

        newChromosome = chromosome(self.size, newArray, self.problemClass)

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

        childA = chromosome(self.size, arrayForChildA, self.problemClass)
        childB = chromosome(self.size, arrayForChildB, self.problemClass)

        return childA, childB

    # This can stay for SAT
    def getFitness(self):
        return self.fitness


    def setPresentBit(self, index, value):
        self.arr[index].present = value

class problem:
    def __init__(self, noVariables, noClausules, weights, formula):
        self.noVariables = noVariables
        self.noClausules = noClausules
        self.weights = deepcopy(weights)
        self.formula = deepcopy(formula)
        self.chromosomeArray = []

        #print(formula)
        #print(weights)

    def solve(self):
        global populationSize, maxWithoutChange, zeroCoefficient
        numGener = populations

        uselessArray = []
        uselessArray.append(0)

        for i in range(populationSize):
            self.chromosomeArray.append(chromosome(self.noVariables, uselessArray, self, 1))

        #Do the genetic stuff
        maximum = -100000000000000
        maxCount = 0
        for i in range(populations):
            #print("generation: ", end='')
            #print(i, end=',')

            if maxCount >= maxWithoutChange:
                if maximum > 0:
                    numGener = i
                    break
                else:
                    if maxCount >= maxWithoutChange * zeroCoefficient:
                        for l in range(int(populationSize-1)):
                            self.chromosomeArray[l+1] = chromosome(self.noVariables, uselessArray, self, 1)
                        maxCount = 0
                        maximum = -10000000000
                        #print("now")

            currentPopulationSize = populationSize

            global tournament

            #Crossover
            for j in range(populationSize):
                if random.randint(0, 100) < crossoverProbability:
                    id = -1
                    max = -10000000
                    for l in range(tournament):
                        crossWith = random.randint(0, populationSize - 1)
                        if self.chromosomeArray[crossWith].fitness > max:
                            max = self.chromosomeArray[crossWith].fitness
                            id = crossWith

                    childA, childB = self.chromosomeArray[j].crossover(self.chromosomeArray[id])
                    self.chromosomeArray.append(childA)
                    self.chromosomeArray.append(childB)
                    currentPopulationSize += 2

            #Mutate
            for j in range(populationSize):
                if random.randint(0, 100) < mutationProbability:
                    child = self.chromosomeArray[j].mutate()
                    self.chromosomeArray.append(child)
                    currentPopulationSize += 1

            #Sort
            #chromosomeArray = chromosomeArray[:currentPopulationSize-1]
            self.chromosomeArray.sort(key=lambda x: x.fitness, reverse=True)

            # Get rid of non surviving chromosomes
            while(currentPopulationSize != populationSize):
                rnd = random.randint(0, currentPopulationSize-1)
                if rnd < populationSize / 10:
                    continue

                del self.chromosomeArray[rnd]
                currentPopulationSize -= 1


            if self.chromosomeArray[0].fitness > maximum:
                maximum = self.chromosomeArray[0].fitness
                maxCount = 0
            else:
                maxCount += 1

            print(self.chromosomeArray[0].fitness, end=',')
            #print(self.chromosomeArray[80].fitness)

        return self.chromosomeArray[0].arr, self.chromosomeArray[0].fitness, numGener

####

f = open(sys.argv[1], 'r')
crossoverProbability = int(sys.argv[2])
mutationProbability = int(sys.argv[3])
maxWithoutChange = int(sys.argv[4])
zeroCoefficient = int(sys.argv[5])
tournament = int(sys.argv[6])
populationSize = int(sys.argv[7])
start = time.process_time()
formula = []
weights = []
noVariables = 0
noClausules = 0
#weights.append(0)
i = 0
while (1):
    line = f.readline()
    if len(line) == 0:
        break
    line = line[:-1]
    if len(line) == 0:
        continue
    arr = line.split()

    # Pokud je to komentar
    if arr[0] == 'c':
        # Pokud je to komentar s vahami
        if arr[1] == 'v':
            j = 2
            while(1):
                if int(arr[j]) == 0:
                    break
                weights.append(int(arr[j]))
                j = j + 1
        continue

    #Pokud je to specifikace formule, nahraj je
    if arr[0] == 'p':
        noVariables = int(arr[2])
        noClausules = int(arr[3])
        continue

    #Jinak
    tmpArr = []
    j = 0
    while(1):
        if int(arr[j]) == 0:
            formula.append(tmpArr)
            break
        tmpArr.append(int(arr[j]))
        j = j + 1
        i = i + 1

notAProblem = problem(noVariables, noClausules, weights, formula)
solution, solutionValue, numberOfGenerations = notAProblem.solve()

end = time.process_time()
mytime = end - start

#print(solution)
#print(weights)
#print(sys.argv[1], end=',')
#print(sys.argv[2], end=',')
#print(sys.argv[3], end=',')
#print(sys.argv[4], end=',')
#print(sys.argv[5], end=',')
#print(sys.argv[6], end=',')
#print(sys.argv[7], end=',')
print(solutionValue, end='\n')
#print(numberOfGenerations, end=',')
#print(mytime)



