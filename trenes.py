
trenA=[2,4]
trenB=[2,4]
trenC=[4]
tramos=[trenA,trenB,trenC,[],[]]


def mover(tren,tramos):
    target=tren[0]
    tren.pop(0)
    tramos[target]=tren


mover(trenA, tramos)
print(tramos)
print(trenA)