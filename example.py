import linda
linda.connect()

# Exemplo de arquivo que escreve e le do tuplespace

blog = linda.TupleSpace()
linda.universe._out(("MicroBlog",blog))

blog = linda.universe._rd(("MicroBlog",linda.TupleSpace))[1]

blog._out(("palmeirense","corinthiano","Segue o lider"))
blog._out(("palmeirense","flamenguista","Cuidado para nao perder o estadio"))
blog._out(("palmeirense","flamenguista","Jaja passaremos voces"))
blog._out(("palmeirense","corinthiano","Quem eh Gabigol perto de Dudu"))

t1 = blog._rd(("palmeirense","corinthiano",str))
# t2 = blog._rd(("alice","gtcn",str))
# t3 = blog._rd(("bob","gtcn",str))
print(t1)

blog._in(("palmeirense","flamenguista","Quem eh Gabigol perto de Dudu"))
t1 = blog._rd(("palmeirense","flamenguista",str))


print(t1)
# print(t2)
# print(t3)