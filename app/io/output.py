def output_to_console(data):
    """Виводить текст в консоль"""
    print(data)

def output_to_file(data, filename):
    """Виводить текст в файл"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(data))
