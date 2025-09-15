import os
import json


def process_transactions(filename, threshold):
    """
    Обрабатывает транзакции из файла, возвращает список транзакций, превышающих порог.

    Args:
        filename (str): Имя файла с транзакциями в формате JSON.
        threshold (float): Порог для фильтрации транзакций.

    Returns:
        list: Список транзакций, превышающих порог.
    """
    transactions = []

    try:
        with open(filename, 'r') as f:
            data = f.read()
            transaction_data = json.loads(data)

            i = 0
            while i < len(transaction_data):
                transaction = transaction_data[i]
                amount = transaction['amount']

                if amount > threshold:
                    transactions.append(transaction)
                i = i + 1

            return transactions

    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []


def calculate_total(transactions):
    """
    Вычисляет общую сумму транзакций.

    Args:
        transactions (list): Список транзакций (словарей).

    Returns:
        float: Общая сумма транзакций.
    """
    total = 0.0

    for transaction in transactions:
        total = total + transaction['amount'] #KeyError - если нет ключа 'amount'
    return total


def save_results(data, output_file):
    """Сохраняет данные в файл."""
    with open(output_file, 'w') as file:
         file.write(str(data))

def main():
    """Основная функция."""
    file_name = "transactions.json"
    AMOUNT_THRESHOLD = 100.0

    high_value_transactions = process_transactions(file_name, AMOUNT_THRESHOLD)
    total_amount = calculate_total(high_value_transactions)

    save_results(total_amount, "results.txt")

    print("Обработка завершена.")


if __name__ == "__main__":
    main()


# Пример файла transactions.json (может быть некорректным)
# [
#   {"id": 1, "amount": 50.0},
#   {"id": 2, "amount": 150.0},
#   {"id": 3, "amount": 200.0},
#   {"id": 4, "amount": "abc"}
# ]
