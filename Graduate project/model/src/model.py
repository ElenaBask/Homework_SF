import pika
import pickle
import numpy as np
import json
try:
    with open('myfile.pkl', 'rb') as pkl_file:
        regressor = pickle.load(pkl_file)

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='Features')
    channel.queue_declare(queue='y_pred')
    def callback(ch, method, properties, body):
        print(f'Получен вектор признаков {body}')
        prediction = regressor.predict(np.array(json.loads(body)).reshape(1, -1))
        channel.basic_publish(exchange='',
                        routing_key='y_true',
                        body=json.dumps(prediction[0]))
        print(f'Предсказание {prediction[0]} отправлено в очередь y_pred')
    # Извлекаем сообщение из очереди features
    # on_message_callback показывает, какую функцию вызвать при получении сообщения
    channel.basic_consume(
        queue='features',
        on_message_callback=callback,
        auto_ack=True
    )
    print('...Ожидание сообщений, для выхода нажмите CTRL+C')
    # Запускаем режим ожидания прихода сообщений
    channel.start_consuming()
except:
    print('Не удалось подключиться к очереди')