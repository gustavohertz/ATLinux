#include <stdio.h>
#include <omp.h>

int main() {
    long limite = 50000000;
    int array_threads[] = {1, 2, 4, 8};
    int qtd_testes = 4;
    
    printf("CPUs disponiveis: %d\n", omp_get_max_threads());
    printf("----------------------------------------\n");
    
    for (int t = 0; t < qtd_testes; t++) {
        int threads = array_threads[t];
        double step = 1.0 / (double)limite;
        double pi = 0.0;
        
        omp_set_num_threads(threads);
        double inicio = omp_get_wtime();
       
        #pragma omp parallel for schedule(static) reduction(+:pi)
        for (long i = 0; i < limite; i++) {
            double x = (i + 0.5) * step;
            pi += 4.0 / (1.0 + x * x);
        }
        
        pi = pi * step;
        double fim = omp_get_wtime();
        
        printf("Num. threads: %d | Tempo: %.4f seg | Pi: %.6f\n", threads, fim - inicio, pi);
    }
    
    return 0;
}