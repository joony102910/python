import multiprocessing

def calc_sum(n):
    total = sum(range(1, n + 1))
    print(f"1+2+3+...+{n} = {total}")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=calc_sum, args=(1000,))
    p2 = multiprocessing.Process(target=calc_sum, args=(100000,))
    p3 = multiprocessing.Process(target=calc_sum, args=(10000000,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
