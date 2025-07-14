import random

class Gene:
    def __init__(self):
        self.value = random.choice([0, 1])

    def mutate(self):
        self.value = 1 - self.value

    def __str__(self):
        return str(self.value)


class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]

    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.5:
                gene.mutate()

    def is_all_ones(self):
        return all(gene.value == 1 for gene in self.genes)

    def __str__(self):
        return ''.join(str(gene) for gene in self.genes)


class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]

    def mutate(self):
        for chromosome in self.chromosomes:
            chromosome.mutate()

    def is_perfect(self):
        return all(chromosome.is_all_ones() for chromosome in self.chromosomes)

    def __str__(self):
        return '\n'.join(str(chrom) for chrom in self.chromosomes)


class Organism:
    def __init__(self, environment_chance):
        self.dna = DNA()
        self.environment_chance = environment_chance

    def mutate(self):
        if random.random() < self.environment_chance:
            self.dna.mutate()

    def is_perfect(self):
        return self.dna.is_perfect()
# Let’s simulate natural selection:
def simulate_evolution(environment_chance=0.2):
    organism = Organism(environment_chance)
    generations = 0

    while not organism.is_perfect():
        organism.mutate()
        generations += 1
        if generations % 1000 == 0:
            print(f"Generation {generations}... still evolving.")

    print(f"Perfect DNA evolved in {generations} generations!")
    print("Final DNA:")
    print(organism.dna)

simulate_evolution()