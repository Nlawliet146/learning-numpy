import numpy as np

rng = np.random.default_rng() 

# numpy generates seed itself, if you mention rng = np.random.default_rng(seed = 1), this way there only be same results

print(rng.integers(1, 7)) # Generate between 1 - 7 that is till 6
print(rng.integers(low = 1, high = 7)) # another method of what happened above
print(rng.integers(low = 1, high = 101, size = 3)) # will give array of three numbers between low and high
print(rng.integers(low = 1, high = 101, size = (3,2))) # gives 2D array of shape (3,2) filling it with random numbers

print(np.random.uniform()) # gives random float number betwenn 0 and 1
print(np.random.uniform(low = -1, high = 1)) # will give between -1 and 1
print(np.random.uniform(low = -1, high = 1, size = 3)) # we can also give size just like in rng

# if we write np.random.seed(seed = 1), then np.random.uniform() will give same result

array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array) # shuffles the array
print(array)

heros = np.array(["GOKU", "LUFFY", "ICHIGO", "NARUTO"])

hero = rng.choice(heros) # choose something 
print(hero)

hero_list = rng.choice(heros, size = 3)
print(hero_list)
