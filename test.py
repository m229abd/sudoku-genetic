import ai

instance = ai.AI()
f = open("problem.json", "r")
print(instance.solve(f.read()))