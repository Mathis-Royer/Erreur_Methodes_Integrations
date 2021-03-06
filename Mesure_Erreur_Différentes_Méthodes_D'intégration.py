import math as m
import matplotlib.pyplot as plt
#----------------------#    Définitions de la fonction et de la valeur de l'intégrale (X).
def f(x):
    return x*m.log(x)
X=(3*m.exp(4)+1)/4
#----------------------#    Méthode d'intégrations.
def rectG(a,b,f,n):
    h=(b-a)/n
    S=0
    for k in range(n):
        ak=a+k*h
        S=S+f(ak)
    return h*S
    
def point_milieu(a,b,f,n):
    h=(b-a)/n
    h2=h/2
    S=0
    for k in range(n):
        ak=a+k*h
        S=S+f(ak+h2)
    return h*S
    
def trapezes(a,b,f,n):
    h=(b-a)/n
    S=0
    for k in range(n):
        ak=a+k*h
        ak1=a+(k+1)*h
        S=S+(f(ak)+f(ak1))/2
    return h*S

def simpson(a,b,f,n):
    assert a<b, "a<b"
    h=(b-a)/n
    S=0
    for k in range(n):
        ak=a+k*h
        ak1=a+(k+1)*h
        S=S+(h/6)*(f(ak)+4*f((ak+ak1)/2)+f(ak1))
    return S
#----------------------#
La=[10**2,10**3,10**4,10**5,10**6,10**7]    #Liste abscisses représentant différents ordres de grandeur de la subdivision

Lo_Simpson=[]
Lo_Rectangles=[]
Lo_Points_Milieux=[]
Lo_Trapèze=[]

for i in range(len(La)):    #Mesure de l'erreur des différentes méthodes d'intégration pour différentes subdivisions
    Lo_Simpson.append(abs(X-simpson(1,m.exp(2),f,La[i])))
    Lo_Rectangles.append(abs(X-rectG(1,m.exp(2),f,La[i])))
    Lo_Points_Milieux.append(abs(X-point_milieu(1,m.exp(2),f,La[i])))
    Lo_Trapèze.append(abs(X-trapezes(1,m.exp(2),f,La[i])))
#----------------------#    Affichage des résultats
plt.figure()
plt.loglog(La,Lo_Points_Milieux,La,Lo_Simpson,La,Lo_Rectangles,La,Lo_Trapèze)
plt.grid()
plt.show()

