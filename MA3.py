""" MA3.py

Student:
Mail:
Reviewed by:
Date reviewed:

"""
import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc
from numba import njit


# Exc1
def approximate_pi(n):
    # n is the number of points


    x=[]
    y=[]

    x_inside =[]
    y_inside=[]

    x_outside=[]
    y_outside=[]


    for i in range (n):
        x.append(random.uniform(-1, 1))
        y.append(random.uniform(-1, 1))

    count = 0
    for i in range(n):

        if x[i]**2 + y[i]**2 <= 1:
            count += 1
            x_inside.append(x[i])
            y_inside.append(y[i])

        else:
            x_outside.append(x[i])
            y_outside.append(y[i])


    pi = 4* count/n

    plt.scatter(x_inside, y_inside, color="red")
    plt.scatter(x_outside, y_outside, color="blue")

    plt.savefig(f"pi_{n}.png")
    plt.show()

    print(f"Exc 1: number of points {n}")
    print(f"Exc 1: pi estimation: {pi}")

    return pi

#approximate_pi(1000)




# Exc2, approximation
def sphere_volume(n, d):

    
    # skapar n punkter, varje punkt har d koordinater
    koords = [
        [random.uniform(-1, 1) for j in range(d)]
        for i in range(n)
    ]

   
    # för varje punkt, beräkna summan av koordinaterna i kvadrat
    squared_sums = map(
        lambda koord: sum(x**2 for x in koord),
        koords
    )

    
    # behåll bara de punkter vars kvadratsumma <= 1
    inside = filter(
        lambda summa: summa <= 1,
        squared_sums
    )

    count = len(list(inside))

    volume = (2**d) * count / n

    return volume
    

#Exc2, real value



def hypersphere_exact(n, d):

    volume = (m.pi **(d/2)) / m.gamma(d/2+1)

    
    return volume



"""
start = pc()
x=sphere_volume(10**6, 11)
end=pc()
time = end-start
print(f"sphere volume försök 1: {x}")
print(f"Tid 1 för sphere_volume: {time} sekunder")


start = pc()
x=sphere_volume(10**6, 11)
end=pc()
time = end-start
print(f"sphere volume försök 2: {x}")
print(f"Tid 2 för sphere_volume: {time} sekunder")


start = pc()
x=sphere_volume(10**6, 11)
end=pc()
time = end-start
print(f"sphere volume försök 3: {x}") 
print(f"Tid 3 för sphere_volume: {time} sekunder")

"""



@njit

#Exc3: numba version
def sphere_volume_numba(n:int, d:int)->float:

    count= 0

    for i in range(n):
        summa = 0.0

        for j in range(d):
            x = random.uniform(-1,1)
            summa += x**2

        if summa <= 1:
            count += 1

    volume = (2**d) * count/n
    return volume


"""
start = pc()
x=sphere_volume_numba(10**6, 11)
end=pc()
time = end-start
print(f"sphere volume numba försök 1: {x}")
print(f"Tid 1 för sphere_volume numba: {time} sekunder")


start = pc()
x=sphere_volume_numba(10**6, 11)
end=pc()
time = end-start
print(f"sphere volume numba försök 2: {x}")
print(f"Tid 2 för sphere_volume numba: {time} sekunder")


start = pc()
x=sphere_volume_numba(10**6, 11)
end=pc()
time = end-start
print(f"sphere volume numba försök 3: {x}") 
print(f"Tid 3 för sphere_volume numba: {time} sekunder")

"""




def sphere_count(n, d):
    count = 0

    for i in range(n):
        summa = 0.0

        for j in range(d):
            x = random.uniform(-1,1)
            summa += x**2

        if summa <= 1:
                count += 1

    return count




#Exc4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel(n, d, np=10):

    n_per_process = n// np

    works = []

    with future.ProcessPoolExecutor(max_workers = np) as executor:

        for i in range(np):
            work = executor.submit(sphere_count, n_per_process, d)
            works.append(work)

    total_count = 0

    for work in works:
        total_count += work.result()

    volume = (2**d) * total_count/n

    return volume









    
def main():
    # Exc1
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

    # Exc2
    n = 100000
    d = 2
    approx = sphere_volume(n, d)
    print(f"Approximated volume of {d} dimensional sphere = {approx}")
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")

    n = 100000
    d = 11
    approx = sphere_volume(n, d)
    print(f"Approximated volume of {d} dimensional sphere = {approx}")
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")

    # Exc3
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n, d)
    stop = pc()
    print(f"Exc3: Sequential time of {d} and {n}: {stop-start}")
    start = pc()
    sphere_volume_numba(n, d)
    stop = pc()
    print(f"Exc3: Numba time of {d} and {n}: {stop-start}")

    # Exc4
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n, d)
    stop = pc()
    print(f"Exc4: Sequential time of {d} and {n}: {stop-start}")
    start = pc()
    parallel_volume = sphere_volume_parallel(n, d, 2)
    stop = pc()
    print("What is parallel time?")
    print(f"Parallel time: {stop-start}")

    
    

if __name__ == '__main__':
	main()


"""
Hämta 
ssh niza9129@gullviva.it.uu.se
pwd
ls
git clone https://github.com/nikzam3/MA3.py.git
cd MA3.py
ls
python3 MA3.py
bash tests.sh
"""

"""
Använd
ssh niza9129@gullviva.it.uu.se
cd MA3.py
git pull --rebase origin main
python3 MA3.py
bash tests.sh
"""