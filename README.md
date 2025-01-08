#Виджет банковских операций клиента 

##Описание: Проект "МойВиджет" - это приложение на Python для банковских операций клиента.

- в проекте появился  функционал по сортировке банковских операций клиента
- в модуле widget.py создана функция mask_account_card, которая принимает строку с именем владельца и номером карты или счётом и возвращает имя владельца и замаскированный номер карты или счёт.
- в пакете src разработана функция filter_by_state, которая принимает список словарей и опционально значение для ключа state (по умолчанию «EXECUTED»). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению.
- в пакете src разработана функция sort_by_date, которая принимает список словарей и опциональное значение для ключа date (по умолчанию «CANCELED»). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ date соответствует указанному значению. Протестированы разные сценарий формата ввода и вывода. 

##Установка:
 - Клонируйте репозиторий: git clone git@github.com:Ekaterina-RA/Homework_10.1.git
 - Установите необходимые зависимости: poetry install --group lint
##Тестирование функций: 
- get_mask_card_number, 
- get_mask_account,
- mask_account_card,
- get_date, 
- filter_by_state, 
- sort_by_date

