import sys, time, os, threading

TAMANHO = 50_000_000
TESTES_THREADS = [1, 2, 4, 8]

def calcular_pi_parcial(inicio, fim, step, resultados, indice):
    soma_parcial = 0.0
    for i in range(inicio, fim):
        x = (i + 0.5) * step
        soma_parcial += 4.0 / (1.0 + x * x)
    resultados[indice] = soma_parcial

print("Python:", sys.version.split(" ")[0])
print("GIL está habilitado:", getattr(sys, '_is_gil_enabled', lambda: True)())
print("CPUs disponíveis:", os.cpu_count())
print("-" * 40)

step = 1.0 / TAMANHO

for num_threads in TESTES_THREADS:
    resultados = [0.0] * num_threads
    threads = []
    tamanho_parte = TAMANHO // num_threads
    
    inicio_tempo = time.perf_counter()
    
    for i in range(num_threads):
        inicio_lista = i * tamanho_parte
        if i == num_threads - 1:
            fim_lista = TAMANHO
        else:
            fim_lista = inicio_lista + tamanho_parte
            
        thread = threading.Thread(target=calcular_pi_parcial, 
                                  args=(inicio_lista, fim_lista, step, resultados, i))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
        
    pi_total = sum(resultados) * step
    fim_tempo = time.perf_counter()
    
    print(f"Num. threads: {num_threads:2d} | Tempo: {fim_tempo - inicio_tempo:.4f}s | Pi: {pi_total:.6f}")