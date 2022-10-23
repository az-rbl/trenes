import threading
trenA=[0,3,4]
trenB=[1,3,4]
trenC=[2,4]
#tramos=[trenA,trenB,trenC,[],[]]

class monitor:
    def __init__(self):
        self.tramos=[[],[],[],[],[]]
        self.lock= threading.Lock()
        self.cv = threading.Condition()

    def mover(self,tren,id):
        target=tren[0]
        self.tramos[target].append(tren)
        #print("se añadio")
        while self.tramos[target][0]!=tren:
            #print("esperando")
            with self.cv:
                self.cv.wait()
        tren.pop(0)
        self.tramos[target].pop(0)
        print("El tren "+str(id)+" se movió al tramo " + str(target))

def tren(mo:monitor, tren, id):
    while(tren != []):
        mo.mover(tren,id)
    print("El tren " +str(id) +" llegó a su destino")

trenes =[trenA, trenB, trenC]
t=[]
mo = monitor()

t0 =threading.Thread(target=tren, args=(mo, trenes[0],0))
t1 =threading.Thread(target=tren, args=(mo, trenes[1],1))
t2 =threading.Thread(target=tren, args=(mo, trenes[2],2))

t0.start()
t1.start()
t2.start()

t0.join()
t1.join()
t2.join()