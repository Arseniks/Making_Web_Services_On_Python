use test
set names utf8;

-- 1. Выбрать все товары (все поля)
select * from product

-- 2. Выбрать названия всех автоматизированных складов
select name from store

-- 3. Посчитать общую сумму в деньгах всех продаж
select sum(total) from sale

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
select distinct p.product_id from product as p join sale as s where p.product_id = s.product_id 

-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
select product.product_id from product natural left join sale where sale.product_id is null 

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
select name, avg(total/quantity) from sale join product using(product_id) group by product_id

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
select ANY_VALUE(name) as name from product natural join sale group by store_id having count(DISTINCT product_id)=1

-- 8. Получить названия всех складов, с которых продавался только один продукт
select ANY_VALUE(name) as name from store natural join sale group by product_id having count(DISTINCT store_id)=1

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
select * from sale where total = (select max(total) from sale)

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
select date as t from sale group by date having sum(total) = (select max(t) from (select sum(total) as t from sale group by date) as a)
