# script.py per misurare la velocità di esecuzione di un programma
import time

def count_to_ten_million():
    for i in range(1, 10000001):
        pass

def main():
    start_time = time.time()

    count_to_ten_million()

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Tempo di esecuzione dello script: {elapsed_time:.4f} secondi")

if __name__ == "__main__":
    main()