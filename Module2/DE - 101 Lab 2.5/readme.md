1. Так как AWS Cloud не дает возможности регестрироваться без применения иностранной карты, решил попробовать альтернативу этому варианту.
В качестве альтернативы выбрал Yandex Cloud. https://console.cloud.yandex.ru/cloud/b1gg6rqorlgs317npmup
2. Создал несколько db PostgresSQL и активировал публичный доступ, вот FQDN хоста rc1d-gvhkyxii714rctcc.mdb.yandexcloud.net
3. Подключился из DBeaver и DataGrip к хосту.
4. Создал схемы dw скриптом и stg путем переноса ранее созданной orders в неё.

**Ниже мини скрипт для копирвоания таблицы в схему stg.**

      create table stg.orders (like public.orders including all);
      
      insert into stg.orders
      select *
      from public.orders;
