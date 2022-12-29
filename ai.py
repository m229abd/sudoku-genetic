import json
import numpy as np
import random
import pygad

# *** you can change everything except the name of the class, the act function and the problem_data ***

def cell_to_row(table:np.ndarray) -> np.ndarray:
    output = np.zeros(shape=(9,9))
    for i in range(0,3):
        for j in range(0,3):
            output[i*3+j,:] = np.reshape(table[i*3:(i+1)*3,j*3:(j+1)*3],newshape=(9,))
    return output

def put_in_table(values:np.ndarray, table:np.ndarray, locations:np.ndarray) -> np.ndarray:
    index = 0
    output = table.copy()
    for loc in locations:
        output[loc[0], loc[1]] = values[index]
        index += 1
    return output

def fitness(table:np.ndarray) -> int:
    fitness = 0
    table_cols = table.transpose()
    table_cells = cell_to_row(table)
    for i in range(1,10):
        for row in range(0,9):
            if (i not in table[row,:]):
                fitness -= 1
            if (i not in table_cols[row,:]):
                fitness -= 1
            if (i not in table_cells[row,:]):
                fitness -= 1
    return fitness

def initial_pop(size:int, population:int) -> np.ndarray:
    return ((np.random.random(size = (population, size))*8.9)+1).astype(int)

def mutation(offspring:np.ndarray, ga_instance: pygad.GA):
    offspring[random.randint(0,len(offspring))] += 1
    return offspring

class AI:
    # ^^^ DO NOT change the name of the class ***

    def __init__(self):
        pass

    # the solve function takes a json string as input
    # and outputs the solved version as json
    def solve(self, problem):
        # ^^^ DO NOT change the solve function above ***

        problem_data = json.loads(problem)
        # ^^^ DO NOT change the problem_data above ***

        table = np.asarray(problem_data["sudoku"])
        locations = table[table==0]
        fitness_wrapper = lambda values: fitness(put_in_table(values=values,table=table,locations=locations))
        ga_instance = pygad.GA(num_generations=500,
        initial_population=initial_pop(len(locations),100),
        num_parents_mating=94,
        fitness_func=fitness_wrapper,
        crossover_type="uniform",
        mutation_probability=1.0,
        mutation_type=mutation,
        keep_elitism = 6,
        parent_selection_type="rank",
        stop_criteria = ["reach_0", "saturate_10"]
        )
        ga_instance.run()
        finished = ga_instance.best_solution()

        # finished is the solved version
        return finished
