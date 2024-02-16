import queue
import time
import threading
import random

# Створити чергу заявок
request_queue = queue.Queue()

# Створити нову заявку, додати заявку до черги
def generate_request():
    while True:
        request_id = random.randint(1, 1000)
        request_queue.put(request_id)
        print(f"Заявка {request_id} додана до черги")
        time.sleep(random.uniform(0.5, 2))

# Якщо черга не пуста: Видалити заявку з черги, Обробити заявку, Інакше: Вивести повідомлення, що черга пуста
def process_request():
    while True:
        if not request_queue.empty():
            request_id = request_queue.get()
            print(f"Заявка {request_id} обробляється")
            time.sleep(random.uniform(1, 3)) 
        else:
            print("Черга пуста.")
            time.sleep(1)

# Поїхали
generator_thread = threading.Thread(target=generate_request)
processor_thread = threading.Thread(target=process_request)

generator_thread.start()
processor_thread.start()