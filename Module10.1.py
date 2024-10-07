import threading
from time import sleep, time


def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")

def timed_write_words(word_count, file_name):
    start_time = time()
    write_words(word_count, file_name)
    end_time = time()
    print(f"Время записи в файл {file_name}: {end_time - start_time:.2f} секунд")

timed_write_words(10, 'example1.txt')
timed_write_words(30, 'example2.txt')
timed_write_words(200, 'example3.txt')
timed_write_words(100, 'example4.txt')

threads = []
thread_args = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]

for arguments in thread_args:
    thread = threading.Thread(target=timed_write_words, args=arguments)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()



