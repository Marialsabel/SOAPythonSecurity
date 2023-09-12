import logging
import time
import multiprocessing
import requests

page = 'http://127.0.0.1:8090/autenticarusuario?usuario=user&clave=password'

def multiprocessing_func(page, i):
    try:
        data = requests.get(page, verify=False)
        print(f'i={i}, status={data.status_code}, time={data.elapsed.total_seconds()}')
    except Exception as e:
        print('Error:', e)

def demon(page, i):
    name = multiprocessing.current_process().name
    print(name, 'Inicio')
    multiprocessing_func(page, i)
    print(name, 'Fin')

if __name__ == '__main__':
    starttime = time.time()
    processes = []
    for i in range(10):
        p = multiprocessing.Process(target=demon, args=(page, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
