# lmc.py

def run_lmc(memory):
    """
    Ejecuta un programa en LMC dado un arreglo de memoria con instrucciones y datos.

    Parámetros:
    memory (list of int): Memoria con 100 celdas (0-999)

    Retorna:
    None
    """
    pc = 0
    acc = 0
    running = True

    while running:
        instr = memory[pc]
        opcode = instr // 100
        addr = instr % 100

        if opcode == 1:       # ADD
            acc += memory[addr]
        elif opcode == 2:     # SUB
            acc -= memory[addr]
        elif opcode == 3:     # STA
            memory[addr] = acc
        elif opcode == 5:     # LDA
            acc = memory[addr]
        elif opcode == 6:     # BRA
            pc = addr
            continue
        elif opcode == 7:     # BRZ
            if acc == 0:
                pc = addr
                continue
        elif instr == 901:    # IN
            acc = int(input("IN: "))
        elif instr == 902:    # OUT
            print("OUT:", acc)
        elif instr == 0:      # HLT
            running = False
        else:
            raise ValueError(f"Instrucción no válida: {instr} en PC={pc}")
        
        pc += 1
