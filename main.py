
import random
import time
from alu import alu
from parallel import medir_speedup
from lmc import run_lmc

def generar_datos(n):
    return [(random.randint(-2**31, 2**31 - 1), random.randint(0, 31)) for _ in range(n)]

def ejecutar_pruebas(pares):
    operaciones = ["ADD", "SUB", "AND", "OR", "XOR", "NOT", "SHL", "SHR"]
    resultados = {op: [] for op in operaciones}

    start = time.time()
    for a, b in pares:
        resultados["ADD"].append(alu("ADD", a, b))
        resultados["SUB"].append(alu("SUB", a, b))
        resultados["AND"].append(alu("AND", a, b))
        resultados["OR"].append(alu("OR", a, b))
        resultados["XOR"].append(alu("XOR", a, b))
        resultados["NOT"].append(alu("NOT", a))
        resultados["SHL"].append(alu("SHL", a, b % 32))
        resultados["SHR"].append(alu("SHR", a, b % 32))
    end = time.time()

    return end - start, resultados

def simular_pipeline(n_instrucciones, latencia=1, etapas=4):
    ciclos_sin_pipeline = n_instrucciones * etapas
    ciclos_con_pipeline = n_instrucciones + (etapas - 1)

    throughput_sin_pipeline = n_instrucciones / ciclos_sin_pipeline
    throughput_con_pipeline = n_instrucciones / ciclos_con_pipeline

    return throughput_sin_pipeline, throughput_con_pipeline

def main():
    N = 1_000_000
    pares = generar_datos(N)

    print("Ejecutando operaciones ALU...")
    tiempo, _ = ejecutar_pruebas(pares)
    print(f"Tiempo total: {tiempo:.2f} s")

    sin_pipe, con_pipe = simular_pipeline(N * 8)
    instrucciones = N * 8

    print("\n--- Comparación de throughput ---")
    print(f"Instrucciones ejecutadas: {instrucciones}")
    print(f"Tiempo real: {tiempo:.2f} s")
    print(f"Throughput real: {instrucciones / tiempo:.2f} instrucciones/seg")
    print(f"Teórico sin pipeline (CPI ≈ 4): {sin_pipe:.6f} instrucciones/ciclo")
    print(f"Teórico con pipeline ideal (CPI ≈ 1): {con_pipe:.6f} instrucciones/ciclo")

    print("\n--- Tarea 3: Paralelismo ---")
    medir_speedup()

    print("\n--- Tarea 2: LMC ---")
    programa = [0] * 100
    programa[0] = 505
    programa[1] = 306
    programa[2] = 507
    programa[3] = 308
    programa[4] = 509
    programa[5] = 309
    programa[6] = 508
    programa[7] = 106
    programa[8] = 306
    programa[9] = 508
    programa[10] = 201
    programa[11] = 713
    programa[12] = 508
    programa[13] = 105
    programa[14] = 308
    programa[15] = 606
    programa[16] = 506
    programa[17] = 902
    programa[18] = 0
    programa[5] = 0
    programa[7] = 1
    programa[9] = 10
    programa[5] = 0

    run_lmc(programa)

if __name__ == "__main__":
    main()
