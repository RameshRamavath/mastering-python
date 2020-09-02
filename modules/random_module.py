import random

# get random value b/w 0, 1[exclusive]

value = random.random()
print(value)


# get random integers b/w two values

ran = random.randint(1, 10)
print(ran) # any value b/w 1, 10


# get random floating b/w two values

ran_uniform = random.uniform(1, 10)
print(ran_uniform) # any value b/w 1, 10

# pickup a random value from the list

greetings = ['Hi', 'Hello', 'Welcome', 'How are you?']
ran_greet = random.choice(greetings)
print(ran_greet + ", Ramesh")

# simulate data using existing list

colors = ['Red', 'Blue', 'Green']
results = random.choices(colors, k=15, weights=[15, 15, 5])  # Red is 15/35 likely to get
print(results)

