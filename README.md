#Виджет банковских операций клиента 

##Описание: Проект "МойВиджет" - это приложение на Python для банковских операций клиента.

- в проекте реализована функция маскировки номера карты и номера счёта — mask_account_card
- в проекте появился новый функционал по сортировке банковских операций клиента
- в модуле widget.py создана функция mask_account_card, которая принимает строку с именем владельца и номером карты или счётом и возвращает имя владельца и замаскированный номер карты или счёт.
- в пакете src разработана функция filter_by_state, которая принимает список словарей и опционально значение для ключа state (по умолчанию «EXECUTED»). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению.
- в пакете src разработана функция sort_by_date, которая принимает список словарей и опциональное значение для ключа date (по умолчанию «CANCELED»). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ date соответствует указанному значению. Протестированы разные сценарий формата ввода и вывода. ##Установка: Для работы потребуется виртуальное окружение poetry и python версии 3.12 и выше:

##Установка:
 - Клонируйте репозиторий: git clone git@github.com:Ekaterina-RA/Project3.git
 - Установите необходимые зависимости: poetry install --group lint
