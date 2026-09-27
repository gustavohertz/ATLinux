import multiprocessing
import time
import os

TAMANHO = 50_000_000
TESTES_PROCESSOS = [1, 2, 4, 8]

def calcular_pi_parcial_mp(inicio, fim, step, fila):
    soma_parcial = 0.0
    for i in range(inicio, fim):
        x = (i + 0.5) * step
        soma_parcial += 4.0 / (1.0 + x * x)
    fila.put(soma_parcial)

if __name__ == "__main__":
    print("Número de CPUs:", multiprocessing.cpu_count())
    print("-" * 40)
    
    step = 1.0 / TAMANHO
    
    for num_processos in TESTES_PROCESSOS:
        fila = multiprocessing.Queue()
        processos = []
        tamanho_parte = TAMANHO // num_processos
        
        inicio_tempo = time.perf_counter()
        
        for i in range(num_processos):
            inicio_lista = i * tamanho_parte
            if i == num_processos - 1:
                fim_lista = TAMANHO
            else:
                fim_lista = inicio_lista + tamanho_parte
                
            processo = multiprocessing.Process(
                target=calcular_pi_parcial_mp, 
                args=(inicio_lista, fim_lista, step, fila)
            )
            processos.append(processo)
            processo.start()
            
        for processo in processos:
            processo.join()
            
        soma_total = 0.0
        while not fila.empty():
            soma_total += fila.get()
            
        pi_total = soma_total * step
        fim_tempo = time.perf_counter()
        
        print(f"Num. processos: {num_processos:2d} | Tempo: {fim_tempo - inicio_tempo:.4f}s | Pi: {pi_total:.6f}")