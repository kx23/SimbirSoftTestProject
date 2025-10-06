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
   ```
2. Сгенерируйте и откройте HTML отчёт:
   ```bash
   allure serve allure-results
   ```
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

---

## Отчет Allure

<img width="1919" height="950" alt="allure_report_screenshot_1" src="https://github.com/user-attachments/assets/75719afd-ff88-41b9-9bf8-2e2c1dc1cf0b" />

<img width="1915" height="949" alt="allure_report_screenshot_2" src="https://github.com/user-attachments/assets/c391912f-c016-4e51-9fed-77d6354e9dff" />
