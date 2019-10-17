import linda
linda.connect()

# Exemplo de arquivo que escreve e le do tuplespace

blog = linda.TupleSpace()
linda.universe._out(("MicroBlog",blog))

blog = linda.universe._rd(("MicroBlog",linda.TupleSpace))[1]

blog._out(("palmeirense","corinthians","Segue o lider"))
blog._out(("palmeirense","flamengo","Cuidado para nao perder o estadio"))
blog._out(("flamenguista","flamengo","Jaja passaremos voces"))
blog._out(("palmeirense","corinthians","Quem eh Gabigol perto de Dudu"))

t1 = blog._rd(("palmeirense","corinthians",str))
for t in t1:
    print(t)

print(t1)

blog._in(("palmeirense","corinthians","Quem eh Gabigol perto de Dudu"))
t1 = blog._rd(("palmeirense","corinthians",str))

print(t1)
# print(t2)
# print(t3)