# Generator function : that generates the results
# yeild: we need to generate bunch of values and remember their values in memory stack
# yeild is also an keyword
# 
# ###

def evengenerator(limit):
    for i in range(2,limit+1,2):
        yield i


for num in evengenerator(10):
    print(num)