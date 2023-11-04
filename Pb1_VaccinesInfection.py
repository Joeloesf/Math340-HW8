import math
import random
import statistics as stats
import numpy as np


def f_E_of_N_given_D(infections: float):
    if (infections == 4):
        return 1/2
    elif (infections == 2) or (infections == 1/2):
        return 1/4
    else:
        return 0
    
def E_D_given_N(n):
    return ((math.e**2)*(4**n + 2*math.e**(3/2)))/(2**(3*n + 1) + (math.e**2)*4**n + math.e**(7/2))



if __name__ == "__main__":

    population_size = 100000
    population = []

    for _ in range(population_size//2):
        d = {
            "D": 0,
            "N": np.random.poisson(4)
        }
        population.append(d)

    for _ in range(population_size//4):
        d = {
            "D": 1,
            "N": np.random.poisson(2)
        }
        population.append(d)

    for _ in range(population_size//4):
        d = {
            "D": 2,
            "N": np.random.poisson(1/2)
        }
        population.append(d)

    num_samples = 10000

    sample_dic = {}

    for _ in range(num_samples):
        sample = population[random.randint(0, population_size-1)]

        if (sample["N"] in sample_dic.keys()):
            sample_dic[sample["N"]].append(sample["D"])
        else:
            sample_dic[sample["N"]] = []
            sample_dic[sample["N"]].append(sample["D"])

    for key, value in sample_dic.items():
        # print(f"Empirical E(D|N={key}) = {stats.mean(value)}")
        # print(f"Theoretical E(D|N={key}) = {E_D_given_N(key)}")
        print(f"diff = {stats.mean(value)-E_D_given_N(key)}")
        # print("\n")
