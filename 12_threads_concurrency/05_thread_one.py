import threading
import time

def boil_milk():
    print(f"Boiling milk...")
    time.sleep(2)
    print(f"Milk Boiled...")

def toast_bun():
    print(f"Toasting bun...")
    time.sleep(3)
    print(f"Done with bun toast...")

start = time.time()

thread1 = threading.Thread(target= boil_milk)
thread2 = threading.Thread(target= toast_bun)


thread1.start()
thread2.start()
thread1.join()
thread2.join()

end = time.time()

print(f" Breadkfast is read in {end - start:.2f}")


