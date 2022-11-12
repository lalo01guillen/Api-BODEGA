def superQry():
    laQty = """
    ---FRESAS---
with salidita as(
select
DATE_TRUNC('day',salida.fecha_de_registro),
cat_productos.descripcion,
sum(I.cantidad*-1) as Suma
FROM inventario I
    inner join salida
    on salida.id_inventario=I.id_inventario
    inner join cat_productos
    ON cat_productos.id_producto = I.id_producto
    group by DATE_TRUNC('day',salida.fecha_de_registro),cat_productos.descripcion
    order by cat_productos.descripcion
    ),
    entradita as(
select
DATE_TRUNC('day',entrada.fecha_de_registro),
cat_productos.descripcion,
sum(I.cantidad*1) as Suma
FROM inventario I
    inner join entrada
    on entrada.id_inventario=I.id_inventario
    inner join cat_productos
    ON cat_productos.id_producto = I.id_producto
    group by DATE_TRUNC('day',entrada.fecha_de_registro),cat_productos.descripcion
    order by cat_productos.descripcion
),
FRESAS AS (
   select date_trunc, descripcion,Suma from entradita
    where descripcion='FRESAS'
    UNION
    select date_trunc, descripcion,Suma from salidita
    where descripcion='FRESAS'
),
FRESAS_2 AS (
   select date_trunc, descripcion,Sum(Suma)as Suma
   from FRESAS
    group by descripcion,date_trunc
    
)
UPDATE fresadiadia SET
suma_cantidad_dia = CASE
    WHEN (suma_cantidad_dia IS NULL) 
    THEN 0
	WHEN (fresadiadia.fecha=FRESAS_2.date_trunc) 
	THEN FRESAS_2.suma
	WHEN (fresadiadia.fecha!=FRESAS_2.date_trunc)
	THEN 0
END,
descripcion='FRESAS'
from FRESAS_2
WHERE (suma_cantidad_dia IS NULL)
  OR (fresadiadia.fecha=FRESAS_2.date_trunc) 
  OR (fresadiadia.fecha!=FRESAS_2.date_trunc);


select fecha, descripcion, suma_cantidad_dia,
SUM(suma_cantidad_dia) OVER (ORDER BY fecha) AS sumatoria
from fresadiadia
group by fecha,suma_cantidad_dia,descripcion
ORDER BY fecha;
---PERAS---
with salidita as(
select
DATE_TRUNC('day',salida.fecha_de_registro),
cat_productos.descripcion,
sum(I.cantidad*-1) as Suma
FROM inventario I
    inner join salida
    on salida.id_inventario=I.id_inventario
    inner join cat_productos
    ON cat_productos.id_producto = I.id_producto
    group by DATE_TRUNC('day',salida.fecha_de_registro),cat_productos.descripcion
    order by cat_productos.descripcion
    ),
    entradita as(
select
DATE_TRUNC('day',entrada.fecha_de_registro),
cat_productos.descripcion,
sum(I.cantidad*1) as Suma
FROM inventario I
    inner join entrada
    on entrada.id_inventario=I.id_inventario
    inner join cat_productos
    ON cat_productos.id_producto = I.id_producto
    group by DATE_TRUNC('day',entrada.fecha_de_registro),cat_productos.descripcion
    order by cat_productos.descripcion
),
PERAS AS (
   select date_trunc, descripcion,Suma from entradita
    where descripcion='PERAS'
    UNION
    select date_trunc, descripcion,Suma from salidita
    where descripcion='PERAS'
),
PERAS_2 AS (
   select date_trunc, descripcion,Sum(Suma) as Suma
   from PERAS
    group by descripcion,date_trunc
    
)
UPDATE peradiadia SET
suma_cantidad_dia = CASE
    WHEN (suma_cantidad_dia IS NULL) 
    THEN 0
	WHEN (peradiadia.fecha=PERAS_2.date_trunc) 
	THEN Peras_2.Suma
	WHEN (peradiadia.fecha!=PERAS_2.date_trunc)
	THEN 0
END,
descripcion='PERAS'
from PERAS_2
WHERE (suma_cantidad_dia IS NULL)
  OR (peradiadia.fecha=PERAS_2.date_trunc) 
  OR (peradiadia.fecha!=PERAS_2.date_trunc);

select fecha, descripcion, suma_cantidad_dia,
SUM(suma_cantidad_dia) OVER (ORDER BY fecha) AS sumatoria
from peradiadia
group by fecha,suma_cantidad_dia,descripcion
ORDER BY fecha;

---MANZANAS---
with salidita as(
select
DATE_TRUNC('day',salida.fecha_de_registro),
cat_productos.descripcion,
sum(I.cantidad*-1) as Suma
FROM inventario I
    inner join salida
    on salida.id_inventario=I.id_inventario
    inner join cat_productos
    ON cat_productos.id_producto = I.id_producto
    group by DATE_TRUNC('day',salida.fecha_de_registro),cat_productos.descripcion
    order by cat_productos.descripcion
    ),
    entradita as(
select
DATE_TRUNC('day',entrada.fecha_de_registro),
cat_productos.descripcion,
sum(I.cantidad*1) as Suma
FROM inventario I
    inner join entrada
    on entrada.id_inventario=I.id_inventario
    inner join cat_productos
    ON cat_productos.id_producto = I.id_producto
    group by DATE_TRUNC('day',entrada.fecha_de_registro),cat_productos.descripcion
    order by cat_productos.descripcion
),
MANZANAS AS (
   select date_trunc, descripcion,Suma from entradita
    where descripcion='MANZANAS'
    UNION
    select date_trunc, descripcion,Suma from salidita
    where descripcion='MANZANAS'
),
MANZANAS_2 AS (
   select date_trunc, descripcion,Sum(Suma) as Suma
   from MANZANAS
    group by descripcion,date_trunc
    
)
UPDATE manzanadiadia SET
suma_cantidad_dia = CASE
    WHEN (suma_cantidad_dia IS NULL) 
    THEN 0
	WHEN (manzanadiadia.fecha=MANZANAS_2.date_trunc) 
	THEN MANZANAS_2.Suma
	WHEN (manzanadiadia.fecha!=MANZANAS_2.date_trunc)
	THEN 0
END,
descripcion='MANZANAS'
from MANZANAS_2
WHERE (suma_cantidad_dia IS NULL)
  OR (manzanadiadia.fecha=MANZANAS_2.date_trunc) 
  OR (manzanadiadia.fecha!=MANZANAS_2.date_trunc);


select fecha, descripcion, suma_cantidad_dia,
SUM(suma_cantidad_dia) OVER (ORDER BY fecha) AS sumatoria
from manzanadiadia
group by fecha,suma_cantidad_dia,descripcion
ORDER BY fecha;

---COCOS---
with salidita as(
select
DATE_TRUNC('day',salida.fecha_de_registro),
cat_productos.descripcion,
sum(I.cantidad*-1) as Suma
FROM inventario I
    inner join salida
    on salida.id_inventario=I.id_inventario
    inner join cat_productos
    ON cat_productos.id_producto = I.id_producto
    group by DATE_TRUNC('day',salida.fecha_de_registro),cat_productos.descripcion
    order by cat_productos.descripcion
    ),
    entradita as(
select
DATE_TRUNC('day',entrada.fecha_de_registro),
cat_productos.descripcion,
sum(I.cantidad*1) as Suma
FROM inventario I
    inner join entrada
    on entrada.id_inventario=I.id_inventario
    inner join cat_productos
    ON cat_productos.id_producto = I.id_producto
    group by DATE_TRUNC('day',entrada.fecha_de_registro),cat_productos.descripcion
    order by cat_productos.descripcion
),
COCOS AS (
   select date_trunc, descripcion,Suma from entradita
    where descripcion='COCOS'
    UNION
    select date_trunc, descripcion,Suma from salidita
    where descripcion='COCOS'
),
COCOS_2 AS (
   select date_trunc, descripcion,Sum(Suma) as Suma  
   from COCOS
   group by descripcion,date_trunc
    
)
UPDATE cocodiadia SET
suma_cantidad_dia = CASE
    WHEN (suma_cantidad_dia IS NULL) 
    THEN 0
	WHEN (cocodiadia.fecha=COCOS_2.date_trunc) 
	THEN COCOS_2.Suma
	WHEN (cocodiadia.fecha!=COCOS_2.date_trunc)
	THEN 0
END,
descripcion='COCOS'
from COCOS_2
WHERE (suma_cantidad_dia IS NULL)
  OR (cocodiadia.fecha=COCOS_2.date_trunc) 
  OR (COCOdiadia.fecha!=COCOS_2.date_trunc);
  


select fecha, descripcion, suma_cantidad_dia,
SUM(suma_cantidad_dia) OVER (ORDER BY fecha) AS sumatoria
from cocodiadia
group by fecha,suma_cantidad_dia,descripcion
ORDER BY fecha;

select 
cocos.fecha, cocos.descripcion, 
SUM(cocos.suma_cantidad_dia) OVER (ORDER BY cocos.fecha) AS CajasdeCoco,
manzanas.descripcion,
SUM(manzanas.suma_cantidad_dia) OVER (ORDER BY manzanas.fecha) AS CajasdeManzana,
peras.descripcion,
SUM(peras.suma_cantidad_dia) OVER (ORDER BY peras.fecha) AS CajasdePera,
fresas.descripcion,
SUM(fresas.suma_cantidad_dia) OVER (ORDER BY fresas.fecha) AS CajasdeFresa

from cocodiadia cocos

right join manzanadiadia manzanas
on manzanas.fecha = cocos.fecha

right join peradiadia peras
on peras.fecha = cocos.fecha

right join fresadiadia fresas
on fresas.fecha = cocos.fecha
where cocos.fecha between '2022-10-29 00:00:00' and '2022-11-29 00:00:00'
group by cocos.fecha,cocos.suma_cantidad_dia,cocos.descripcion,
		 manzanas.fecha,manzanas.suma_cantidad_dia,manzanas.descripcion,
		 peras.fecha,peras.suma_cantidad_dia,peras.descripcion,
		 fresas.fecha,fresas.suma_cantidad_dia,fresas.descripcion
ORDER BY cocos.fecha;
   """

    return laQty