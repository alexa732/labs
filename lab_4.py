import csv

# Объявляем класс
class Animal:

    # self — параметр, который ссылается на экземпляр класса
    # setattr функция перезаписи значения
    # Создаем конструктор для создания объекта
    def __init__(self, number, name, breed, age):
        setattr(self, '_number', number)
        setattr(self, '_name', name)
        setattr(self, '_breed', breed)
        setattr(self, '_age', age)

        # Возвращает строковое представление объекта. Например, print(repr(animal))
    def __repr__(self):
        return f"Animal(№={self._number}, Кличка='{self._name}', Порода='{self._breed}', Возраст={self._age})"

    # Метод __str__ возвращает строковое представление объекта
    def __str__(self):
        return f"{self._number}, {self._name}, {self._breed}, {self._age}"

    # Этот метод позволяет сравнивать два объекта класса Animal с использованием оператора равенства (==)
    def __eq__(self, other):
        return self._number == other._number

    # Метод __lt__ определяет поведение оператора "меньше чем" (<)
    def __lt__(self, other):
        return self._number < other._number

    # Декоратор @property позволяет вам определить методы, которые можно вызывать как атрибуты
    @property
    def number(self):
        return self._number

    @property
    def name(self):
        return self._name

    @property
    def breed(self):
        return self._breed

    @property
    def age(self):
        return self._age

    # Метод from_dict является статическим методом (@staticmethod), который принимает словарь data
    # и создает новый объект Animal, используя данные из словаря
    @staticmethod
    def from_dict(data):
        return Animal(int(data["№"]), data["Кличка"], data["Порода"], int(data["Возраст"]))


class AnimalCollection:

    # При создании объекта будет создаваться словарь.
    # Пример: collection = AnimalCollection() - print(collection) - AnimalCollection([]),
    # Такой вывод из-за __repr__
    def __init__(self):
        self._animals = []

    # Позволяет иттерировать словарь, то есть использовать цикл for
    def __iter__(self):
        return iter(self._animals)

    # Позволяет считать длину словаря
    def __len__(self):
        return len(self._animals)

    # Метод __getitem__ позволяет получить доступ к элементам коллекции по индекс
    def __getitem__(self, index):
        return self._animals[index]

    # Метод __repr__ возвращает строковое представление объекта AnimalCollection
    def __repr__(self):
        return f"AnimalCollection({self._animals})"

    # Метод add_animal добавляет новый объект Animal в коллекцию, используя метод append списка _animals.
    def add_animal(self, animal):
        self._animals.append(animal)

    # Метод sort_by_field сортирует коллекцию по указанному полю.
    # Параметр field определяет, по какому атрибуту сортировать.
    # Используется getattr для получения значения атрибута объекта Animal.
    def sort_by_field(self, field, numeric=False):
        self._animals.sort(key=lambda x: getattr(x, field), reverse=False)

    # Метод filter_by_field фильтрует коллекцию по указанному полю и значению
    def filter_by_field(self, field, value, numeric=False):
        if numeric:
            return [animal for animal in self._animals if getattr(animal, field) > value]
        else:
            return [animal for animal in self._animals if getattr(animal, field) == value]

    @staticmethod
    def read_csv(file_path):
        collection = AnimalCollection()
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                collection.add_animal(Animal.from_dict(row))
        return collection

    @staticmethod
    def write_csv(file_path, animals):
        fieldnames = ['№', 'Кличка', 'Порода', 'Возраст']
        with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for animal in animals:
                writer.writerow({
                    '№': animal.number,
                    'Кличка': animal.name,
                    'Порода': animal.breed,
                    'Возраст': animal.age
                })


class Dog(Animal):
    def __init__(self, number, name, breed, age):
        super().__init__(number, name, breed, age)
        setattr(self, '_number', number)
        setattr(self, '_name', name)
        setattr(self, '_breed', breed)
        setattr(self, '_age', age)

    def __repr__(self):
        return f"Dog(№={self._number}, Кличка='{self._name}', Порода='{self._breed}', Возраст={self._age})"

    def __iter__(self):
        yield self


def main():
    # путь к файлу
    # чтение данных из файла
    file_path = 'data1.csv'
    collection = AnimalCollection.read_csv(file_path)

    print("Исходные данные:")
    for animal in collection:
        print(animal)

    # Сортировка по строковому полю (например, "name")
    collection.sort_by_field('name')
    print("\nСортировка по Кличке:")
    for animal in collection:
        print(animal)

    # Сортировка по числовому полю (например, "age")
    collection.sort_by_field('age', numeric=True)
    print("\nСортировка по Возрасту:")
    for animal in collection:
        print(animal)

    # Фильтрация данных по критерию (например, возраст больше 3)
    filtered_animals = collection.filter_by_field('age', 3, numeric=True)
    print("\nФильтрация: Возраст больше 3")
    for animal in filtered_animals:
        print(animal)

    # Добавление новых данных
    new_animal = Animal(6, 'Снежинка', 'Британская кошка', 2)
    collection.add_animal(new_animal)

    # Сохранение данных обратно в файл
    AnimalCollection.write_csv(file_path, collection)

main()
