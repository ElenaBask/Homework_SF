import pika
import numpy as np
import json
from sklearn.datasets import load_diabetes
import time
from datetime import datetime

# Создаём бесконечный цикл для отправки сообщений в очередь
while True:
    try:
        # Загружаем датасет о диабете
        X, y = load_diabetes(return_X_y=True)
        # Формируем случайный индекс строки
        random_row = np.random.randint(0, X.shape[0]-1)
        # Подключение к серверу на локальном хосте:
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()
        # Создаём очередь y_true
        channel.queue_declare(queue='y_true')
        # Публикуем сообщение
        while True:
            time.sleep(10)
            message_id = datetime.timestamp(datetime.now())
            message_y_true = {
                'id': message_id,
                'body': y[random_row]
            }
            channel.basic_publish(exchange='',
                            routing_key='y_true',
                            body=json.dumps(message_y_true))
            print('Сообщение с правильным ответом отправлено в очередь')
        # Создаём очередь features
        channel.queue_declare(queue='features')
        # Публикуем сообщение
        channel.basic_publish(exchange='',
                            routing_key='features',
                            body=json.dumps(list(X[random_row])))
        print('Сообщение с вектором признаков отправлено в очередь')
        # Закрываем подключение 
        connection.close()
    except:
        print('Не удалось подключиться к очереди')