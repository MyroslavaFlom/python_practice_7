import pandas
def input_from_console():
    """Зчитує текст введений користувачем з консолі"""
    return input("Введіть текст: ")

def input_from_file():
    """Зчитує текст з файлу"""
    filename = "input.txt"
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def input_from_pandas_file():
    """Зчитує текст з файлу бібліотеки Pandas"""
    filename = "data.csv"
    df = pandas.read_csv(filename)
    return df
