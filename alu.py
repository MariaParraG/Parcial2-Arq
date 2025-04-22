# alu.py

def alu(op_code, a, b=None):
    """
    Realiza una operación de la ALU entre dos enteros de 32 bits.

    Parámetros:
    op_code (str): Código de la operación ("ADD", "SUB", "AND", "OR", "XOR", "NOT", "SHL", "SHR")
    a (int): Operando A
    b (int | None): Operando B (no requerido para NOT)

    Retorna:
    int: Resultado de la operación
    """
    if op_code == "ADD":
        return a + b
    elif op_code == "SUB":
        return a - b
    elif op_code == "AND":
        return a & b
    elif op_code == "OR":
        return a | b
    elif op_code == "XOR":
        return a ^ b
    elif op_code == "NOT":
        return ~a
    elif op_code == "SHL":
        return a << b
    elif op_code == "SHR":
        return a >> b
    else:
        raise ValueError(f"Operación desconocida: {op_code}")
