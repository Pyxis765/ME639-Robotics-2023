from sympy import zeros,symbols, Matrix, diff, pprint

n = int(input('Enter no. of joints = '))                           # Number of joints 
q = symbols('q1:{}'.format(n+1))                                   # Joint angles
qd = symbols('qd1:{}'.format(n+1))                                 #Joint velocity
qdd = symbols('qdd1:{}'.format(n+1))                               #Joint acceleration

D_symbols = symbols('d:{}{}'.format(n, n))

D_elements = [[(input(f'Enter element for d{i+1}{j+1}: ')) for j in range(n)] for i in range(n)]

D = Matrix(D_elements)

D1 = Matrix(zeros(n, 1))
for k in range(n):
    d=0
    for i in range(n):
        d = d + (D[i,k]*qdd[i])
    D1[k] = d


V = input('\nEnter potential term expression V(q) = ')

phi = Matrix(zeros(n, 1))
for k in range(n):
    phi[k] = diff(V, q[k])



C =  Matrix(zeros(n, 1))                                                        # Christoffel symbols
for k in range(n): 
    cijk = 0
    for i in range(n):
        for j in range(n):
            cijk = cijk +  (0.5 * (diff(D[k,j],q[i]) + diff(D[i,k],q[j]) - diff(D[i,j],q[k]))*qd[i]*qd[j])
    C[k] = cijk

tau = Matrix(zeros(n, 1))
for i in range(n):
    tau[i] = D1[i] + C[i] + phi[i]


for i in range(n):
    print(f'τ{i+1} = ')
    pprint(tau[i])
    print('\n')
