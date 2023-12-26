1. Нарисовал модель данных Superstore используя SqlDBM. Ниже представлено его изображение.
![schema of SqlDBM.png](schema%20of%20SqlDBM.png)  
2. Создал таблицы в локальной db, попутно отловил проблему Null postal_code для города Burlington.  
Решил ее следующим запросом перед созданием таблицы geography.  

         UPDATE orders
         SET postal_code = '05401'
         WHERE city = 'Burlington' AND postal_code IS NULL;  
Полный вариант DDL скрипта для создания таблиц представлен в [SQL_for_Lab_2_4.sql](SQL_for_Lab_2_4.sql)