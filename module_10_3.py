from threading import Thread, Lock
from time import sleep
from random import randint


class Bank(Thread):
    def __init__(self, balance=0):
        super().__init__()
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        for _ in range(101):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += randint(50, 500)
            print(f'Пополнение:{randint(50, 500)}. Баланс:{self.balance}')
            sleep(0.001)


    def take(self):
        for _ in range(101):
            print(f'Запрос на {randint(50, 500)} ')
            if randint(50, 500) <= self.balance:
                self.balance -= randint(50, 500)
                print(f'Снятие :{randint(50, 500)}. Баланс : {self.balance}')
            else:
                print(f'Недостаточно средств на счету')
                self.lock.acquire()
            sleep(0.001)





if __name__ == '__main__':
    bk = Bank()
    tk1 = Thread(target=Bank.deposit, args=(bk,))
    tk2 = Thread(target=Bank.take, args=(bk,))

    tk1.start()
    tk2.start()
    tk1.join()
    tk2.join()
    print(f'Итоговый баланс: {bk.balance}')
