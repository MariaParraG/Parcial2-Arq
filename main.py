# main.py

import random
import time
from alu import alu

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
        resultados["NOT"].append(alu("NOT", a))  # Solo requiere un operando
        resultados["SHL"].append(alu("SHL", a, b % 32))
        resultados["SHR"].append(alu("SHR", a, b % 32))
    end = time.time()

    total_time = end - start
    return total_time, resultados

def simular_pipeline(n_instrucciones, latencia=1, etapas=4):
    """
    Calcula throughput teórico en un pipeline ideal con latencia unitaria.
    """
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

    # Teórico
    sin_pipe, con_pipe = simular_pipeline(N * 8)  # 8 operaciones por par
    instrucciones = N * 8

    print("\n--- Comparación de throughput ---")
    print(f"Instrucciones ejecutadas: {instrucciones}")
    print(f"Tiempo real: {tiempo:.2f} s")
    print(f"Throughput real: {instrucciones / tiempo:.2f} instrucciones/seg")
    print(f"Teórico sin pipeline (CPI ≈ 4): {sin_pipe:.6f} instrucciones/ciclo")
    print(f"Teórico con pipeline ideal (CPI ≈ 1): {con_pipe:.6f} instrucciones/ciclo")

if __name__ == "__main__":
    main()
