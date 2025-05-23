import ttg

x = ttg.Truths(['p', 'q'], ['(~p or q) and p and ~q'], ints=False)
print(x)
print(x.valuation())