class MySuperClass:
    """Тестовий клас, зараз реалізуємо опис студента
    
    ---

    surname : str
        Прізвище студента
    
    """
    def __init__(self, surname, name, mark):
        """
        Ініціалізуємо обєкт
        - в середині конструктора створюються атрибути
        """
        print("Викликаємо __init__")
        self.surname = surname
        self.name = name
        self.mark = mark
    
    def __repr__(self):
        return "Представлення обєкту Студент, його задають: MySuperClass(surname, name, mark)"
    
    def __len__(self):
        return len(self.surname)

def function_in_module():
    pass

# Ось так нам допоміг ChatGPT зробити опис
class Students:
    """
    Клас Students для зберігання інформації про студентів.

    Attributes:
        surname (str): Прізвище студента.
        name (str): Ім'я студента.
        mark (int): Оцінка студента.
    """

    def __init__(self, surname: str, name: str, mark: int):
        """
        Ініціалізує новий екземпляр класу Students.

        Args:
            surname (str): Прізвище студента.
            name (str): Ім'я студента.
            mark (int): Оцінка студента, яка повинна бути цілим числом.
        """
        print("Викликаємо __init__")
        self.surname = surname
        self.name = name
        self.mark = mark