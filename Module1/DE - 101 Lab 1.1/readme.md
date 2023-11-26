## Изначальное задание было опробовать навыки в EXCEL, но так как с EXCEL я знаком давно, мне показалось, что будет инетереснее понять отличие стандартного EXCEL от Power BI. Результаты прикладываю после описания задания ниже.

### Архитектура Аналитического Решения
Необходимо нарисовать верхнеуровневую архитектуру аналитического решения по примеру теоретического видео, где я рассказывал об архитектуре ламоды. Необходимо использовать:
- Source Layer - слой источников данных
- Storage Layer - слой хранения данных 
- Business Layer - слой для доступа к данным бизнес пользователей

Необходимо использовать draw.io, Microsoft Visio Studio, Power Point или инструмент на выбор. 

Здесь вы можете найти [инструкции по установке draw.io](https://github.com/Data-Learn/data-engineering/blob/master/how-to/How%20to%20install%20drawio.md).

### Аналитика в Excel

Используя данные Sample - Superstore.xls сделать:
- Использовать Lookup
- Построить Сводную таблицу
- Построить примеры отчетов
- Создать дашборд
- И другая функциональность Excel на ваш выбор.

Идеи для создания дашборда отчета:
1. Overview (обзор ключевых метрик)
  - Total Sales 
  - Total Profit
  - Profit Ratio
  - Profit per Order
  - Sales per Customer
  - Avg. Discount
  - Monthly Sales by Segment ( табличка и график)
  - Monthly Sales by Product Category (табличка и график)
 2. Product Dashboard (Продуктовые метрики)
  - Sales by Product Category over time (Продажи по категориям)
 3. Customer Analysis
  - Sales and Profit by Customer
  - Customer Ranking
  - Sales per region


**Значения атрибутов в Sample - Superstore.xls**
| Название столбца | Значение                          |
|------------------|-----------------------------------|
| Row ID           | Идентификатор строки (уникальный) |
| Order ID         | Идентификатор заказа              |
| Order Date       | Дата заказа                       |
| Ship Date        | Дата доставки                     |
| Ship Mode        | Класс доставки                    |
| Customer ID      | Идентификатор покупателя          |
| Customer Name    | Имя и фамилия покупателя          |
| Segment          | Сегмент покупателя                |
| Country          | Страна                            |
| City             | Город                             |
| State            | Штат                              |
| Postal Code      | Почтовый индекс                   |
| Region           | Регион                            |
| Product ID       | Идентификатор товара              |
| Category         | Категория                         |
| Sub-Category     | Подкатегория                      |
| Product Name     | Название товара                   |
| Sales            | Продажи (Доход)                   |
| Quantity         | Количество                        |
| Discount         | Скидка в %                        |
| Profit           | Прибыль                           |
| Person           | Региональный менеджер             |
| Returned         | Возвраты товара                   |


## В результате у меня получилось 3 dashboards

### Overview (обзор ключевых метрик)

![Overview](DE-101\Module1\DE - 101 Lab 1.1\Overview.jpg "Overview")

### Product Dashboard (Продуктовые метрики)

![Product_Dashboard](DE-101\Module1\DE - 101 Lab 1.1\Product_Dashboard.jpg "Product_Dashboard")

### Customer Analysis

![Customer_Analysis](DE-101\Module1\DE - 101 Lab 1.1\Customer_Analysis.jpg "Customer_Analysis")

### Полезные материалы
* [Алгоритм проектирования дашборда](https://youtu.be/xSp5ykKcQho) - общие правила проектирования высококачественных дашбордов
* [Обзор дашборда|Гайд по BI](https://youtu.be/rxu8jmsvw98) - гайд по проектированию интерактивных отчетов в Excel (пример для superstore). 
* [Пример отчета](https://github.com/Data-Learn/data-engineering/blob/master/DE-101%20Modules/Module01/DE%20-%20101%20Lab%201.1/Sample%20-%20Superstore%20-%20Dashboard.xlsx)
* [Пошаговая инструкция](https://github.com/Data-Learn/data-engineering/blob/master/DE-101%20Modules/Module01/DE%20-%20101%20Lab%201.1/build_steps_dashboard.md)
