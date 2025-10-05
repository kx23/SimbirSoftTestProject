# SimbirSoft Test Project

## Требования

Для запуска тестов необходимо установить:

- **Python 3.13** или выше  

- Веб-драйверы для браузеров **Google Chrome** и **Mozilla Firefox**  

  (пути к ним должны быть добавлены в **системные переменные среды**)

  

---

## Запуск тестов

1. Перейдите в корневую папку проекта:
   ```bash
   cd ../SimbirSoftTestProject
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
3. Запустите тесты:
   ```bash
   pytest
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;или с выбором браузера:
   ```bash
   pytest --browser_name=firefox
```
   

---

## Генерация Allure отчёта
1. Запустите тесты с сохранением результатов:
   ```bash
   pytest --alluredir=allure-results
2. Сгенерируйте и откройте HTML отчёт:
   ```bash
   allure serve allure-reports
---

## Примеры тест-кейсов

### Позитивный тест-кейс:

Название: test_submit_form_with_valid_data

#### Шаги:

1. Заполнить поле Name — “Harutyunyan Artavazd”

2. Заполнить поле Password — “PassW0rd@11”

3. Выбрать напитки: “Milk” и “Coffee”

4. Выбрать цвет: “Yellow”

5. В списке Do you like automation? выбрать “yes”

6. Ввести Email — “myemail@dom.com”

7. В поле Message указать количество инструментов и инструмент с наибольшим числом символов

8. Нажать кнопку Submit

#### Ожидаемый результат:

Появляется alert с текстом: Message received!



### Негативный тест-кейс:

Название: test_submit_form_with_invalid_data

#### Шаги:

1. Оставить поле Name пустым

2. Заполнить поле Password — “PassW0rd@11”

3. Выбрать напитки: “Milk” и “Coffee”

4. Выбрать цвет: “Yellow”

5. В списке Do you like automation? выбрать “yes”

6. Ввести Email — “myemail@dom.com”

7. В поле Message указать количество инструментов и инструмент с наибольшим числом символов

8. Нажать кнопку Submit

#### Ожидаемый результат:

Форма не отправляется, alert не появляется.
