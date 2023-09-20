import threading
import random
import time

tam_fila = 30

semaforo_caixas = threading.Semaphore(3)

def atender_cliente(cliente):
    global tam_fila

    tempo_atendimento = random.randint(3, 10)
    
    with semaforo_caixas:
        if tam_fila > 0:
            print(f"Cliente {cliente} está sendo atendido por {tempo_atendimento} segundos.")
            tam_fila -= 1
            time.sleep(tempo_atendimento)
            print(f"Cliente {cliente} foi atendido e saiu.")
        else:
            print(f"Cliente {cliente} chegou, mas a fila está cheia. Saindo.")

if __name__ == "__main__":
    threads_clientes = []
    for i in range(1, 31):
        cliente_thread = threading.Thread(target=atender_cliente, args=(i,))
        threads_clientes.append(cliente_thread)

    for cliente_thread in threads_clientes:
        cliente_thread.start()

    for cliente_thread in threads_clientes:
        cliente_thread.join()

    print("Todos os clientes foram atendidos.")
