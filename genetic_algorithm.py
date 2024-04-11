from functions import init_ranges, bukin_2d

import random

import numpy as np


def set_seed(seed: int) -> None:
    # Set fixed random seed to make the results reproducible
    random.seed(seed)
    np.random.seed(seed)


class GeneticAlgorithm:
    def __init__(
        self,
        population_size: int,
        mutation_rate: float,
        mutation_strength: float,
        crossover_rate: float,
        num_generations: int,
    ):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.mutation_strength = mutation_strength
        self.crossover_rate = crossover_rate
        self.num_generations = num_generations

    def changeAll(
        self,
        population_size: int,
        mutation_rate: float,
        mutation_strength: float,
        crossover_rate: float,
        num_generations: int,
    ):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.mutation_strength = mutation_strength
        self.crossover_rate = crossover_rate
        self.num_generations = num_generations

    def initialize_population(self) -> tuple:
        # TODO Initialize the population and return the result
        population = []
        for i in range(self.population_size):
            population.append((np.random.uniform(init_ranges[0][0], init_ranges[0][1]), np.random.uniform(init_ranges[1][0], init_ranges[1][1])))
        return population

    def evaluate_population(self, population) -> tuple:
        # TODO Evaluate the fitness of the population and return the values for each individual in the population
        reviewed_population = []
        for i in population:
            ans = bukin_2d(i[0], i[1])
            if ans == 0:
                reviewed_population.append((99999, i))
            else :
                reviewed_population.append((1/ans, i))
        return reviewed_population

    def selection(self,fitness_values, t_size, br_size) -> ...:
        # TODO Implement selection mechanism and return the selected individuals
        # TOURNAMENT SELECTION
        # T SIZE IS THE SIZE OF THE TOURNAMENT, AS OF HOW MANY ENTRIES ARE TO BE TESTED
        # B SIZE IS THE BRACKET SIZE, SO WE DIVIDE THE T SIZE/B SIZE TO KNOW WHAT % OF THE PARENTS ARE GOING FURTHER
        T = []
        B = []
        copy = fitness_values
        copy.sort()
        copy.reverse()
        for j in range(0,len(fitness_values)-t_size):
            B.append(copy[j][1])
        for i in range(t_size):
            for b in range(br_size):
                T.append(random.choice(fitness_values))
            Best = T[0][1]
            BestVal = T[0][0]
            for k in T:
                if(k[0] > BestVal):
                    Best = k[1]
            B.append(Best)
            T = []
        return B


    def crossover(self, parents) -> ...:
        # TODO Implement the crossover mechanism over the parents and return the offspring
        crossover_output = []
        while True:
            if(len(parents) <= 1):
                break
            p1 = int(np.random.uniform(0, len(parents)-1))
            p2 = int(np.random.uniform(0, len(parents)-1))
            help = np.random.random()
            if help < self.crossover_rate:
                x1, y1 = parents[p1]
                x2, y2 = parents[p2]
                alfa = np.random.random()*2 - 1
                xo = alfa * x1 + (1 - alfa) * x2
                yo = alfa * y1 + (1 - alfa) * y2
                crossover_output.append((xo,yo))
                xo = alfa * x2 + (1-alfa) * x1
                yo = alfa * y2 + (1 - alfa) * y1
                crossover_output.append((xo,yo))
            else:
                crossover_output.append(parents[p1])
                crossover_output.append(parents[p2])
            del(parents[p1])
            del(parents[p2])
        return crossover_output
            

    def mutate(self, individuals) -> ...:
        # TODO Implement mutation mechanism over the given individuals and return the results
        output = []
        for i in individuals:
            help, help1 = i
            if np.random.random() < self.mutation_rate:
                help += np.random.normal(self.mutation_strength*(-1), self.mutation_strength)*help
                help1 += np.random.normal(self.mutation_strength*(-1), self.mutation_strength)*help1
            output.append((help, help1))
        return output

    def mean_value(self, fitness_values) -> int:
        help = 0
        for i in fitness_values:
            help += i[0]
        help /= len(fitness_values)
        return help

    def evolve(self, seed: int) -> ...:
        # Run the genetic algorithm and return the lists that contain the best solution for each generation,
        #   the best fitness for each generation and average fitness for each generation
        set_seed(seed)

        population = self.initialize_population()

        best_solutions = []
        best_fitness_values = []
        average_fitness_values = []

        for generation in range(self.num_generations):
            fitness_values = self.evaluate_population(population)
            parents_for_reproduction = self.selection(fitness_values, int(len(fitness_values)/2), 3)
            offspring = self.crossover(parents_for_reproduction)
            population = self.mutate(offspring)
            #print(len(population))
        


            #ALGEBRA FOR THE OUTPUT
            fitness_values.sort()
            #print(fitness_values[len(fitness_values) - 1][0])
            best_solutions.append(fitness_values[len(fitness_values) - 1][1])
            best_fitness_values.append(fitness_values[len(fitness_values) - 1][0])
            help = self.mean_value(fitness_values)
            average_fitness_values.append(help)
            if(fitness_values[len(fitness_values) - 1][0] == 99999): break
            # TODO compute fitness of the new generation and save the best solution, best fitness and average fitness

        return best_solutions, best_fitness_values, average_fitness_values
