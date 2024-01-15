## Модуль 4.5 практика [Pentaho](https://www.hitachivantara.com/en-us/products/pentaho-plus-platform/data-integration-analytics/pentaho-community-edition.html)

### Задание звучало следующим образом  
"  
1. В качестве практики вам необходимо выявить 8-10 подсистем в ETL Pentaho DI и написать небольшой отчет, в котором вы приложите print screen компонента (ETL подсистемы) и напишите про его свойства. Результат сохраните в вашем Git.
2. Самостоятельно попробовать сделать упражнения из главы 9 книги Pentaho Data Integration Beginner's Guide - Second Edition. В книге вы найдете необходимую информацию по установки тестовой базы данных. Я сохранил все материалы для лабораторных работ в нашем git. Это достойная задача для будущего ETL разработчика или Инженера Данных.  
  
"

### Обращу внимание, что столкнулся с проблемой подключения к тренировочной базе данных.  
Для выполнения заданий книги необходимо использовать тренировочну базу данных, но по ссылкам в книге ее вы скачать не сможете.
В интернете адекватное решение для этого вы тоже найдете маловероятно.
### Как я решил данную проблему

1. Необходимая вам db представлена по следующему пути:  
путь до распакованного архива с pentaho\pdi-ce-9.4.0.0-343\data-integration\samples\db\sampledb
2. Я воспользовался database connection->Generic database, параметры на скрине ниже и в [файле](generic%20connection.txt).
![database connection params.png](png%2Fdatabase%20connection%20params.png)
Дублирую в текстовом формате параметры на скрине:  
**_Connection name:_**  
Pentaho_local_db  
**_dialect:_**  
H2  
**_URL (тут необходимо поменять путь до распакованного архива с pentaho):_**  
jdbc:h2:D:\pdi-ce-9.4.0.0-343\data-integration\samples\db\sampledb  
**_driver class name:_**  
org.h2.Driver  
**_Username:_**  
PENTAHO_ADMIN  
**_Password:_**  
PASSWORD  

### Упражнения 8 главы книги [Pentaho Data Integration Beginner’s Guide, Second Edition](https://www.programmer-books.com/pentaho-data-integration-beginners-guide-second-edition/)
1. [Запрос к базе данных 8_1_Querying a database.ktr](08%2F8_1_Querying%20a%20database.ktr)
2. [Формирование переменного запроса используя контекстные параметры 8_2_Making flexible queries using parameters.ktr](08%2F8_2_Making%20flexible%20queries%20using%20parameters.ktr)
3. [Формирование переменного запроса используя Kettle переменные 8_3_Making flexible queries by using Kettle variables.ktr](08%2F8_3_Making%20flexible%20queries%20by%20using%20Kettle%20variables.ktr)
4. [Загрузка списка производителей в таблицу базы данных 8_4_Loading a table with a list of manufacturers.ktr](08%2F8_4_Loading%20a%20table%20with%20a%20list%20of%20manufacturers.ktr)
5. [Вставка или обновление данных в базе данных испорльзуя PDI шаги 8_5_Inserting or updating data by using other PDI steps.ktr](08%2F8_5_Inserting%20or%20updating%20data%20by%20using%20other%20PDI%20steps.ktr)
6. [Удаление данных из базы данных 8_6_Eliminating data from a database.ktr](08%2F8_6_Eliminating%20data%20from%20a%20database.ktr)  

### Упражнения 9 главы книги [Pentaho Data Integration Beginner’s Guide, Second Edition](https://www.programmer-books.com/pentaho-data-integration-beginners-guide-second-edition/)
1. [Использование Лукапа для создания списка продуктов к покупке 9_1_Using a Database lookup step to create a list of products to buy.ktr](09%2F9_1_Using%20a%20Database%20lookup%20step%20to%20create%20a%20list%20of%20products%20to%20buy.ktr)
2. [Использование джоина для создания списка предложения к покупке 9_2_Using a Database join step to create a list of suggested products to buy.ktr](09%2F9_2_Using%20a%20Database%20join%20step%20to%20create%20a%20list%20of%20suggested%20products%20to%20buy.ktr)
3. [Создание dimensional таблицы с использованием лукапа 9_3_loading a region dimension with a Combination lookup_update step.ktr](09%2F9_3_loading%20a%20region%20dimension%20with%20a%20Combination%20lookup_update%20step.ktr)
4. [Создание исторических данных для отслеживания изменения состояния данных 9_4_Keeping a history of changes in products by using the Dimension lookup_update step.ktr](09%2F9_4_Keeping%20a%20history%20of%20changes%20in%20products%20by%20using%20the%20Dimension%20lookup_update%20step.ktr)