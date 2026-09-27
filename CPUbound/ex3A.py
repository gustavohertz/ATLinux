import time

TAMANHO = 50_000_000 

def calcular_pi_sequencial(num_steps):
    step = 1.0 / num_steps
    pi = 0.0
    for i in range(num_steps):
        x = (i + 0.5) * step
        pi += 4.0 / (1.0 + x * x)
    return pi * step

if __name__ == "__main__":
    print(f"--- Iniciando Teste Sequencial ---")
    print(f"Passos (N): {TAMANHO:,}".replace(",", "."))
    
    inicio = time.perf_counter()
    resultado = calcular_pi_sequencial(TAMANHO)
    fim = time.perf_counter()
    
    print(f"Pi: {resultado:.10f}")
    print(f"Tempo Sequencial: {fim - inicio:.4f}s")
