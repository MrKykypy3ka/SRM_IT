# CRM для сервисного центра техники
### Формы и элементы управления
* Запустив программу отображается форма авторизации
  * Текстовое поле - "Логин"
  * Текстовое поле - "Пароль"
  * Кнопка - "Войти"
* После авторизации пользователь попадет на главную форму программы:
  * Кнопка - "Создать запись" - отобразится окно для добавления новой записи в базу данных.
  * Кнопка - "Редактировать запись" - отобразится окно для редактирования выделенной записи в базе данных.
  * Кнопка - "Удались запись" - удаляет запись из базы данных.
  * Кнопка - "Просмотреть запись" - отображает окно для просмотра выделенной записи.
  * Кнопка - "Добавить пользователя" - отобразится окно для добавления нового пользователя в базу данных.
  * Поле - "Учётная запись" - TODO.
  * Поле - "Список заказов" - поле для отображения всех заказов хранящихся в базе данных.
  * Поле - "Календарь заказов" - TODO.
  * Кнопка - "Руководство пользователя" - отобразится окно, в котором можно ознакомится с руководством пользователя.
  * Кнопка - "Режим для слабовидящих" - TODO.
* Из главной формы можно попасть на формы Создания/радктировани/просмотра заказа, который все похоже по структуре.
  * Числовое поле - Номер заказа.
  * Текстовое поле - Заказчик.
  * Текстовое поле - Специалист.
  * Текстовое поле - Дата приёмки.
  * Текстовое поле - Дата сдачи.
  * Текстовое поле - Отметка о выполнении.
  * Числовое поле - Стоимость.
  * Текстовое поле - Примечания.
  * Кнопка - Добавить/Сохранить/Закрыть.
* Из главной формы можно попасть на форму добавления нового сотрудника.
  * Текстовое поле - Фамилия.
  * Текстовое поле - Имя.
  * Текстовое поле - Должность.
  * Текстовое поле - Логин.
  * Текстовое поле - Пароль.
  * Текстовое поле - Подтверждение пароля.
  * Кнопка - Добавить.
  
### Особенности
* Реализованна авторизация пользователей
* Отображение названий кнопок в нижней части экрана при наведении
* Подсветка полей для ввода данных при отсутствии данных/неправильных данных
* 

### Структура файлов

      |- main.py - программный код приложения (входная точка)

      |- identifier.sqlite - база данных

      |- forms - папка с формами

      |- images - папка с файлами изображений

      |- info - текстовый файл, руководство пользователя

### Иерархия классов
* Классы: ***addForm***, ***editForm***, ***mainForm***, ***userForm***, ***viewForm***
  * Классы вёрстки
* Класс ***UiA*** наследник ***autoresationForm***.
  * Описывает форму авторизации.
* Класс ***UiM*** наследник ***mainForm***.
  * Описывает главную форму.
* Класс ***UiD*** наследник ***addForm***.
  * Описывает форму добавления заказа.
* Класс ***UiE*** наследник ***editForm***.
  * Описывает форму редактирования заказа.
* Класс ***UiU*** наследник ***userForm***.
  * Описывает форму добавления нового работника.
* Класс ***UiV*** наследник ***viewForm***.
  * Описывает форму отображения заказа.


### Функции
* main(scr)
  * Основная функция игры.

### Требования
Все требования в requirements.txt

### Запуск
Запустить файл main.py, или SRM_IT.exe

Ввести логин и пароль пользователя из таблицы ниже.

![img.png](image/PU/A.png)
![img.png](image/PU/L.png)

Нажать кнопку "Войти"

На главном экране пользователь увидит список всех заказов.
Сверху имеется ряд кнопок для работы с данными.


![i2.png](image/PU/M.png)

* ***Добавить запись***

Для открытия окна необходимо нажать на кнопку с листком+

Для добавления новой записи необходимо заполнить все полня и назвать на кнопку "Добавить".

При вводе некорректных данных поле подсвечивается красным цветом(например стоимость должна быть просто число).

![i3.png](image/PU/D.png)

* ***Редактировать запись***

Для начала редактирования записи, пользователю необходимо выбрать нужную ему запись из списка и нажать на кнопку с карандашиком

![i3.png](image/PU/E.png)


![i3.png](image/PU/R.png)


![i3.png](image/PU/V.png)


![i3.png](image/PU/U.png)

### TODO
* Аватар пользователя
* Режим для слабовидящих
* Отображение заказов в календаре
