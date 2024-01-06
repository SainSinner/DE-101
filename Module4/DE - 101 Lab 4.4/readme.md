## Модуль 4.4 практика [Pentaho](https://www.hitachivantara.com/en-us/products/pentaho-plus-platform/data-integration-analytics/pentaho-community-edition.html)

### Задание звучало следующим образом  
"Скачать и запустить Pentaho DI.  
Скачать мои примеры Pentaho jobs для Staging и Dimension Tables и доделать их, чтобы получить такой же результат, как в модуле 2.  
Создайте еще одну трансформацию, в которой вы создадите sales_fact таблицу."

В результате выполнения сформировал следующие файлы:
- [staging orders.ktr](staging%20orders.ktr)  - трансформация, которая загружает данные из файлы Superstore в Postgres  
![staging orders.png](png%2Fstaging%20orders.png)
- [dim_tables.ktr](dim_tables.ktr) - трансформация, которая трансформирует данные (T в ETL) внутри нашей базы данных (красным отмечено потому что делал скрин когда отключил кластер с БД в облаке)  
![dim_tables.png](png%2Fdim_tables.png)
- [create sales_fact.ktr](create%20sales_fact.ktr) - трансформация, которая создает объединяющую таблицу sales_fact  
![create sales_fact.png](png%2Fcreate%20sales_fact.png)
- [Pentaho Job.kjb](Pentaho%20Job.kjb) - главный job, который выполняет последовательность трансформаций (оркестрирует нашим data pipeline)  
![Pentaho Job.png](png%2FPentaho%20Job.png)