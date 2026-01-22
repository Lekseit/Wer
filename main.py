import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
def print_hi(name):
    logging.info(f'Вызов функции print_hi с аргументом: {name}')
    if name:
        print(f'Hi, {name}')
        logging.info(f'Сообщение успешно создано: hi, {name}')
    else:
        logging.warning('Аргумент name не передан или пуст')

if __name__ == '__main__':
    logging.info('Запуск программыыыыыыыыы')
    try:

        print_hi(name=input("Введите свое имя: "))
    except Exception as e:
        logging.error(f'Произошла ошибка: {e}')
    logging.info('Завершение программы')

