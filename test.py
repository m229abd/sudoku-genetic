import ai

instance = ai.AI()
f = open("problem.json", "r")
instance.solve(f.read())