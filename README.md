This is an application of the [genetic heuristic search algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm) that mimics the process of natural selection.
We applied it to the [Boolean Satisfiability problem](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem) (more precisely [max-sat](https://en.wikipedia.org/wiki/Maximum_satisfiability_problem)).

The main steps behind genetic algorithmes are:
1. Selection over fitness: the fittest have more chances of survival (represented in our case by cloning)
2. Crossover: is a randomly happening between randomly selected population individuals
3. Mutation: is a random change happening rarely (allows for deversification of the genes, to avoid stagnation)

###Usage
The algorithm takes as input: 

**genetic** *(clauses,nbL,k,nbIter,rate)*
- clauses:	list of clauses (list of lists). A clause being a list of literal instences.
- nbL:		number of literals.
- k:		number of individuals in the population.
- nbIter: 	number of iterations.
- rate:		mutation rate.

And returns a tuple (bestInstence, bestVal) of the best solution (literals instentiation) found, and the best satisfaction rate.

Each step is represented in the implementation as a function. The population is sorted at each iteration for better handling.

To use the algorithme:
```python
from genetic import readCnf, genetic
clauses,nbL=readCnf(filePath)
genetic(clauses,nbL,50,1000,0.2)
```

###Steps implementation
* "The survival of the fittest" rule is represented by a "cloning of the fittest" method. The individuals with the best fitness value have more chances to be cloned.
**clone** *(clauses,populat,k)*
- clauses:	Clauses set
- population:	Current population set
- k:		The number of clones to be produced


* Crosseover is done by selecting two random individuals from the population and a random *limit* value (between 0 and number\_of\_literals). New borns are produced by crossing the two individuals genes on the limit.
**pCross** *(populat,k)*
- population:	Current population set
- k:		The number of clones to be produced

* Mutation alters one random gene in a little portion (*rate*) of the population.
**mutate** *(population,rate)*
- population:	Current population set
- rate:		Mutation rate (float between 0 and 1). The number of mutated individuals vary between % and *rate*

### Helping functions:
**readCnf** *(cnfFile)*: 		reads a cnf file and returns *clauses* list of lists, and number of literals *nbL*.
- inputFile:	path to cnf file (Examples of cnf files can be downloaded from [satlib.org](http://www.satlib.org/))

**pSort** *(clauses,populat,k)* : 	Sorts population individuals following their fitness values.
- k:		length of the population

**random_sol** *(nbL)* : 		Generates a random solution
- nbL:		number of literals.

**check_all** *(clause,state)*: 	returns the number of not satisfied clauses left by *state* instentiation.
- state:	An instentation of the literals (a solution)

**fitness** *(population,clauses)* : 	returns the mean fitness value of a *population*.


***

###License:
This is published under GNU GPL Lisence.
For more informations about the terms: https://www.gnu.org/licenses/gpl.html

![Image Alt](https://www.gnu.org/graphics/gplv3-127x51.png)

