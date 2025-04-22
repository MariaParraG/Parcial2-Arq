# parallel.py

import random
import time
from multiprocessing import Pool, cpu_count
from alu import alu

def generar_datos(n):
    return [(random.randint(-2**31, 2**31 - 1), random.randint(0, 31)) for _ in range(n)]

def operaciones_por_par(par):
    a, b = par
    return {
        "ADD": alu("ADD", a, b),
        "SUB": alu("SUB", a, b),
        "AND": alu("AND", a, b),
        "OR": alu("OR", a, b),
        "XOR": alu("XOR", a, b),
        "NOT": alu("NOT", a),
        "SHL": alu("SHL", a, b % 32),
        "SHR": alu("SHR", a, b % 32),
    }

def ejecutar_en_paralelo(pares, p):
    chunk_size = len(pares) // p
    chunks = [pares[i:i + chunk_size] for i in range(0, len(pares), chunk_size)]

    start = time.time()
    with Pool(processes=p) as pool:
        resultados = pool.map(ejecutar_chunk, chunks)
    end = time.time()

    return end - start, resultados

def ejecutar_chunk(chunk):
    return [operaciones_por_par(par) for par in chunk]

def medir_speedup(N=1_000_000):
    pares = generar_datos(N)
    resultados = []

    for p in [1, 2, 4]:
        t, _ = ejecutar_en_paralelo(pares, p)
        resultados.append((p, t))

    # Calcular speedup y eficiencia
    t1 = resultados[0][1]
    print("\n--- Resultados Paralelos ---")
    print("p\tTiempo(s)\tSpeedup\t\tEficiencia")
    for p, t in resultados:
        speedup = t1 / t
        eficiencia = speedup / p
        print(f"{p}\t{t:.2f}\t\t{speedup:.2f}\t\t{eficiencia:.2f}")
