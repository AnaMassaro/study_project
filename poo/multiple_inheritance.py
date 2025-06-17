# Classe Person - Define as informações pessoais
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        return f"Name: {self.name}, Age: {self.age}"

# Classe Job - Define informações sobre o trabalho
class Job:
    def __init__(self, job_title, salary):
        self.job_title = job_title
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.10  # Bônus de 10%

# Classe Employee - Herda de Person e Job
class Employee(Person, Job):
    def __init__(self, name, age, job_title, salary):
        # Chama os construtores das classes pai
        Person.__init__(self, name, age)
        Job.__init__(self, job_title, salary)

    def print_all_details(self):
        personal_details = self.print_details()
        bonus = self.calculate_bonus()
        return f"{personal_details}\nJob Title: {self.job_title}, Salary: {self.salary}, Bonus: {bonus}"

employee = Employee("Ana", 30, "Developer", 5000)

print(employee.print_all_details())

"""
Herança Múltipla e Ambiguidade: Quando se utiliza herança múltipla, como no caso da classe Employee herdar de Person e Job, 
existe o risco de ambiguidade se as classes base tiverem métodos ou atributos com o mesmo nome.
Por exemplo, se ambas as classes Person e Job tivessem um método chamado `print_details()`, 
a classe Employee não saberia qual método utilizar, e isso poderia levar a erros inesperados.
Para resolver essa ambiguidade, é importante entender a ordem de resolução de métodos (Method Resolution Order - MRO) do Python,
que define qual classe será usada quando o método é chamado.
"""
