## Знакомство с [Pentaho](https://www.hitachivantara.com/en-us/products/pentaho-plus-platform/data-integration-analytics/pentaho-community-edition.html)

### Практику я начал с видео по следующей [ссылке](https://www.youtube.com/watch?v=K3X9wIC0jO8).  
В результате чего выполнил план практики

- Скачаем sample-superstore.xls из 1 модуля. (1 job)  
[job_download_samplestore.kjb](sources%2Fintroduction_pentaho%2Fmy_files%2Fjob_download_samplestore.kjb)  
![job_download_samplestore.png](sources%2Fjpg%2Fjob_download_samplestore.png)
- Объединим данные из 3 таблиц в одну. (1 transformation)  
  [transformation_general.ktr](sources%2Fintroduction_pentaho%2Fmy_files%2Ftransformation_general.ktr)  
  ![transformation_general.png](sources%2Fjpg%2Ftransformation_general.png)
- Разобьем данные на разные форматы   (2 transformation)
  - Информацию по продуктам сохраним в JSON формате
  - Информацию о возвратах сохраним в формате XML
  - Информацию о заказах разобьем по регионам:
    - CENTRAL – Одним файлом в формате Excel (xls)
    - WEST -  Несколько  файлов разбитых по штатам в csv
    - SOUTH – Один файл формата csv в zip архиве
    - EAST – текстовый файл с расширением .dat  
[transformation_for_task.ktr](sources%2Fintroduction_pentaho%2Fmy_files%2Ftransformation_for_task.ktr)  
![transformation_for_task.png](sources%2Fjpg%2Ftransformation_for_task.png)  
- Добавляем “ошибки” для большего реализма :D (3 transformation)
    - WEST – разные названия страны (US, United States, USA), лишние символы в поле City
    - EAST – добавляем опечатки в названиях городов (сложно прогнозируемые для ручного исправления)
    - SOUTH – добавляем дубли заказов  
[transformation_add_errors.ktr](sources%2Fintroduction_pentaho%2Fmy_files%2Ftransformation_add_errors.ktr)  
![transformation_add_errors.png](sources%2Fjpg%2Ftransformation_add_errors.png)
- Финальный джоб  
[final_job.kjb](sources%2Fintroduction_pentaho%2Fmy_files%2Ffinal_job.kjb)  
![final_job.png](sources%2Fjpg%2Ffinal_job.png)
### Результаты практики представлены ниже:
[файлы pentaho]([my_files](sources%2Fintroduction_pentaho%2Fmy_files))    
[файлы созданные в результате работы пайплайна]([temp](sources%2Ftemp))

### Через "Планировщик задач" запускал финальный job следующей командой в [.bat файле]([sheduling_job.bat](sources%2Fintroduction_pentaho%2Fmy_files%2Fsheduling_job.bat))  

    "D:\pdi-ce-9.4.0.0-343\data-integration\Kitchen.bat" /file:"D:\Module4\introduction_pentaho\my_files\final_job.kjb" /level:Basic