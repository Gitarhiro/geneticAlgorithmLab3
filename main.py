from genetic_algorithm import GeneticAlgorithm
import numpy as np
import matplotlib.pyplot as plot


if __name__ == "__main__":
    # TODO Experiment 1...
    ga = GeneticAlgorithm(
        population_size=1000,
        mutation_rate=0.05,
        mutation_strength=0.12,
        crossover_rate=0.8,
        num_generations=100,
    ) # in this

    #TASK 1
    pop = [100, 200, 300, 400, 500]
    mut_r = [0.05, 0.1, 0.15, 0.2]
    mut_sc = [0.08, 0.1, 0.12, 0.14, 0.16]
    cr_rt = [0.6, 0.7, 0.8, 0.9]
    tab = []
    for p in pop:
        for mr in mut_r:
            for msc in mut_sc:
                for c in cr_rt:
                    ga.changeAll(
                        population_size=p,
                        mutation_rate=mr,
                        mutation_strength=msc,
                        crossover_rate=c,
                        num_generations=10,
                    )
                    best_solutions, best_fitness_values, _ = ga.evolve(seed = 50)
                    tab.append((p, 
                               mr, 
                               msc, 
                               c,
                               best_solutions[len(best_solutions)-1], 
                               best_fitness_values[len(best_fitness_values)-1]))
    print("Population - Mutation Rate - Mutation Strength - Crossover Rate - Best Solution - Best Fitness")
    bestOne = tab[0]
    for tab in tab:
        print(f"{tab[0]} - {tab[1]} - {tab[2]} - {tab[3]} - {tab[4]} - {tab[5]}")
        if(tab[5] > bestOne[5]):
            bestOne = tab


    #TASK 2
    seeds = [20, 40, 60, 80, 100]
    # average_fitness = []
    # print("Seeds - Best Solution - Best Fitness")
    # for i  in seeds:
    #     ga.changeAll(
    #         population_size=bestOne[0],
    #         mutation_rate=bestOne[1],
    #         mutation_strength=bestOne[2],
    #         crossover_rate=bestOne[3],
    #         num_generations=10
    #     )
        
    #     best_solutions, best_fitness_values, _ = ga.evolve(seed = i)
    #     average_fitness.append(best_fitness_values)
    #     print(f"{i} - {best_solutions[len(best_solutions)-1]} - {best_fitness_values[len(best_fitness_values)-1]}")
    # average_fitness = np.mean(average_fitness)
    # derivation = np.std(average_fitness)
    # print("Average values of fitness is: " + str(average_fitness))
    # print("Standard derivation of fitness is: " + str(derivation))

    new_pop_size = [.5, .25, .1]
    # print("New population sizes - Best Solution - Best Fitness")
    # for i in new_pop_size:
    #     ga.changeAll(population_size=int((bestOne[0])*i),
    #         mutation_rate=bestOne[1],
    #         mutation_strength=bestOne[2],
    #         crossover_rate=bestOne[3],
    #         num_generations=10
    #         )
    #     best_solutions, best_fitness_values, _ = ga.evolve(seed = 50)
    #     print(f"{i} - {best_solutions[len(best_solutions)-1]} - {best_fitness_values[len(best_fitness_values)-1]}")

    # #TASK 3 
    # meanval = []
    # bestval = []
    # for sid in seeds:
    #     for i in cr_rt:
    #         ga.changeAll(population_size=(bestOne[0]),
    #             mutation_rate=bestOne[1],
    #             mutation_strength=bestOne[2],
    #             crossover_rate=i,
    #             num_generations=10
    #             )
    #         _, best_fitness_values, mean_fitness_values = ga.evolve(seed = sid)
    #         meanval.append(mean_fitness_values)
    #         bestval.append(best_fitness_values)
    #     gens = range(10)
    #     for j , cross_rate in enumerate(cr_rt):
    #         plot.plot(gens, bestval, label = f"Crossover Rate = {cross_rate}")
    #     plot.xlabel("Generations")
    #     plot.ylabel("Fitness")
    #     plot.legend()
    #     plot.show()   
    #     bestval.clear() 
    #     # for i , cross_rate in enumerate(cr_rt):
    #     #     plot.plot(gens, meanval[i], label = f"Seed = {sid} Mean")
    #     # plot.xlabel("Generations")
    #     # plot.ylabel("Fitness")
    #     # plot.legend()
    #     # plot.show()
    #     #meanval.clear()


    #TASK 4
    meanval = []
    bestval = []
    for sid in seeds:
        for rate in mut_r:
            for str in mut_sc:
                ga.changeAll(population_size=(bestOne[0]),
                    mutation_rate=rate,
                    mutation_strength=str,
                    crossover_rate=0.8,
                    num_generations=10
                    )
                _, best_fitness_values, mean_fitness_values = ga.evolve(seed = 50)
                bestval.append(best_fitness_values)
                meanval.append(mean_fitness_values)
            gens = range(10)
            for i, str in enumerate(mut_sc):
                plot.plot(gens, bestval[i], label = f"Seed = {sid} Mutation Rate = {rate} Mutation Strength = {str}")
            plot.xlabel("Crossover Rate")
            plot.ylabel("Fitness")
            plot.legend()
            plot.show()
            bestval.clear()
            # for i, str in enumerate(mut_sc):
            #     plot.plot(gens, meanval[i], label = f"Seed = {sid} Mutation Rate = {rate} Mutation Strength = {str}")
            # plot.xlabel("Crossover Rate")
            # plot.ylabel("Fitness")
            # plot.legend()
            # plot.show()
            # meanval.clear()
        

    #print(best_fitness_values[len(best_fitness_values)-1])
    #print(best_solutions, best_fitness_values, average_fitness_values)
