# -*- coding: utf-8 -*-
import sys , os
from copy import deepcopy
from random import randint, choice, random

#--------------------------- READ CNF FILE ----------------------------------
def readCnf(cnfFile):
	clauses=[]
	nbL=0
	with open(cnfFile) as f:
 		for clause in enumerate(f):
			c=clause[1].strip('\n').strip('\r').strip('\n').split(" ")
			c = filter(None,c)
			if 'p' in c :
				nbL=int(c[-2])
			elif not ( 'c' in c) and len(c)>1:
				clauses.append(map(int,(c[:-1])))

	return clauses,nbL


#------------------------------- CHECK --------------------------------------------------
def check_all(clause,state):
	clauses = deepcopy(clause)

	for l in state:
		i=0
		while i < len(clauses):
			if l in clauses[i]:
				clauses.remove(clauses[i])
			else:
				i=i+1
	return len(clauses)

#----------------------------- RANDOM SOLUTION -------------------------------------------
def random_sol(nbL):
	l = []
	for x in range(1,nbL+1):
		sign = randint(0,1)
		if sign:
			l.append(x)
		else :
			l.append(-x)

	return l
	
#----------------------------- POPULATION SORT ------------------------------------------

def pSort(clauses,populat,k):
	
	tmp=[0]*k
	for i in range(k):
		tmp[i]=check_all(clauses[:],populat[i])


	for i in range(k):
		for j in range(i,k):
			if tmp[i]>tmp[j]:
				tmp[i],tmp[j]=tmp[j],tmp[i]
				populat[i],populat[j]=populat[j],populat[i]



#----------------------------- RANDOM P. CROSS ------------------------------------------

def pCross(populat,k):
	newP=[0]*k
	nbL=len(populat[0])
	for i in range(k):
		limit=randint(0,nbL-1)
		newP[i]=populat[randint(0,k-1)][:limit]+populat[randint(0,k-1)][limit:]
	return newP	


#----------------------------- CLONE ---------------------------------------------------

def clone(clauses,populat,k):
	newP=[]
	chances=[]
	nbC=len(clauses)
	for i in range(k):
		chances=chances+([i]*((nbC-check_all(clauses[:],populat[i]))/10))
	
	for i in range(k):
		newP.append(populat[choice(chances)])

	return newP


#----------------------------- MUTATE P. ------------------------------------------------

def mutate(population,rate):
	nbL=len(population[0])
	rate=random()%rate		
	k=len(population)
	limit=int(len(population)*rate)
	for i in range(limit):
		r=randint(0,nbL-1)
		population[randint(2,k-1)][r]=population[i][r]*-1

#----------------------------- FITNESS P. ------------------------------------------------

def fitness(population,clauses):
	f=0.0
	nbC=len(clauses)
	for i in population:
		f=f+(nbC-check_all(clauses[:],i))/float(len(clauses))
	return f/len(population)
	
#----------------------------- GENETIC ALGORITHME ---------------------------------------

def genetic(clauses,nbL,k,nbIter,rate):
	nbC=len(clauses)
	nbIter=100
	population=[0]*k
	for i in range(k):
		population[i]=random_sol(nbL)

	count=0
	lastBest=0
	bestVal=0

	for i in range(nbIter):

		#Sort current population
		pSort(clauses,population,k)
		bestVal=(len(clauses)-check_all(clauses[:],population[0]))/float(len(clauses))


		if bestVal == 1:
			print "SOLUTION FOUND!"
			print population[0]

			print str(bestVal)
			print population[0]
			return (population[0], bestVal)
		

		print "Population fitness: "+str(fitness(population,clauses))+"\t BestVal: "+str(bestVal)

		#Clone current population
		clonedP=clone(clauses,population,k)

		#Randomly cross cloned population
		newP=pCross(clonedP,k)

		#Mutate crossed population
		mutate(newP,rate)

		pSort(clauses,newP,k)
		population=population[:int(k*0.15)+1]+newP[:int(k*0.85)]

	print str(bestVal)
	print population[0]
	return (population[0], bestVal)






