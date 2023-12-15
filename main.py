import random

# Функція для обчислення значення цільової функції
def eval_func(chromosome):
    x, y, z = chromosome
    result = 1 / (1 + (x - 2)**2 + (y + 1)**2 + (z - 1)**2)
    return (result,)

# Функція для створення випадкової хромосоми
def generate_chromosome():
    return [random.uniform(-10, 10) for _ in range(3)]

# Функція для схрещування двох хромосом
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Функція для мутації хромосоми
def mutate(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] += random.uniform(-1, 1)  # Мутація випадковим значенням з діапазону (-1, 1)
    return chromosome

# Генетичний алгоритм
def genetic_algorithm(population_size, generations, mutation_rate):
    population = [generate_chromosome() for _ in range(population_size)]

    for _ in range(generations):
        evaluated_population = [(chromosome, eval_func(chromosome)) for chromosome in population]
        evaluated_population.sort(key=lambda x: x[1][0], reverse=True)
        new_population = []

        for i in range(0, len(evaluated_population), 2):
            parent1, _ = evaluated_population[i]
            parent2, _ = evaluated_population[i+1]
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population[:population_size]  # Відбір популяції до потрібного розміру

    best_chromosome, best_fitness = max(evaluated_population, key=lambda x: x[1][0])
    return best_chromosome, best_fitness

# Параметри генетичного алгоритму
population_size = 50
generations = 100
mutation_rate = 0.1

best_chromosome, best_fitness = genetic_algorithm(population_size, generations, mutation_rate)

print(f"Найкраща хромосома: {best_chromosome}")
print(f"Найкраще значення функції: {best_fitness[0]}")
