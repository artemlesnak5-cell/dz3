# Задание 1
class Wolf:
    def howl(self):
        print("Уууу!")


class Dog:
    def bark(self):
        print("Гав!")


class Werewolf(Wolf, Dog):
    def transform(self):
        print("Превращение!")


if __name__ == "__main__":
    werewolf = Werewolf()
    werewolf.howl()
    werewolf.bark()
    werewolf.transform()
    print(Werewolf.__mro__)


# Задание 2
class EatMixin:
    def eat(self):
        print("Сотрудник ест")


class SleepMixin:
    def sleep(self):
        print("Сотрудник спит")


class Worker(EatMixin, SleepMixin):
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} работает")


if __name__ == "__main__":
    worker = Worker("Иван")
    worker.eat()
    worker.work()
    worker.sleep()


# Задание 3
class A:
    def show(self):
        print("Класс A")


class B:
    def show(self):
        print("Класс B")


class C(A, B):
    def test(self):
        self.show()


if __name__ == "__main__":
    c = C()
    c.test()


class C2(B, A):
    def test(self):
        self.show()


if __name__ == "__main__":
    c2 = C2()
    c2.test()
# Задание 4
class PrintMixin:
    def print_document(self, text):
        print(text)


class SaveMixin:
    def save_document(self, text):
        print(f"Сохранено: {text}")


class Document(PrintMixin, SaveMixin):
    def create(self, content):
        self.print_document(content)
        self.save_document(content)


if __name__ == "__main__":
    doc = Document()
    doc.create("Важный документ")