# Домашнее задание МОДУЛЬ: ML-7. Оптимизация гиперпараметров
​
## Оглавление  
[1. Описание проекта]()  
[2. Какой кейс решаем?]()  
[3. Краткая информация о данных]()  
[4. Этапы работы над проектом]()  
[5. Результат]()  
[6. Выводы]()     
​
### Описание проекта    
Необходимо предсказать биологический ответ молекул (столбец 'Activity') по их химическому составу (столбцы D1-D1776)

:arrow_up:[к оглавлению]()
​
### Какой кейс решаем?    
Закрепить пройденный материал по различным способам оптимизации гиперпарамтеров моделей логистической регрессии и случайного леса

**Категории оценки**
1. Обучено две модели
2. Гипепараметры подобраны при помощи четырёх методов
3. Использована кросс-валидация
4. Сделан правильный вывод по гипотезе

**Что практикуем**     
- написание хорошего кода на Python;
- работу со встроенными и внешними модулями numpy, sklearn, hyperopt, optuna, matplotlib
- правильная оценка результатов и формулирование выводы
- размещение проекта на GitHub.
​
### Краткая информация о данных
Практика основана на соревновании [Kaggle: Predicting a Biological Response](https://www.kaggle.com/c/bioresponse) (Прогнозирование биологического ответа). Данные представлены в формате CSV. Предварительная обработка не требуется, данные уже закодированы и нормализованы. Каждая строка представляет молекулу:

- столбец Activity содержит экспериментальные данные, описывающие фактический биологический ответ [0, 1]; 
- столбцы D1-D1776 представляют собой молекулярные дескрипторы — это вычисляемые свойства, которые могут фиксировать некоторые характеристики молекулы, например размер, форму или состав элементов.


:arrow_up:[к оглавлению]()
​
​
### Этапы работы над проектом
1. Импортирование нужных библиотек
2. Нахождение метрики без оптимизации гиперпараметров
3. Постороение моделей и оптимизация их гиперпараметров методом GreadSearch
4. Постороение моделей и оптимизация их гиперпараметров методом RandomSearch
5. Постороение моделей и оптимизация их гиперпараметров методом HyperOpt
6. Постороение моделей и оптимизация их гиперпараметров методом Optuna
7. Оценка результатов

​:arrow_up:[к оглавлению]()
​
### Результат:  
   1. Построены модели
   2. Проведена оптимизация гиперпараметров
   3. Примегнена кросс-валидация
   4. Подготовлена визуализация результатов 
   5. Сделаны выводы.
​
:arrow_up:[к оглавлению]()
​
### Выводы:  
Использование ни одного из методов по оптимизации гиперпараметров не привело к к какому-либо существенному улучшению качества модели как логистиеской регресииЮ, так и случайного леса.

:arrow_up:[к оглавлению]()