# El problema

## Situación

Una pyme recibe cada mes decenas o cientos de facturas de sus proveedores, en PDF o foto. Una persona las lee una por una y copia a mano los datos (RUC, fecha, importe, IGV, total) a un Excel. A fin de mes también revisa el extracto del banco, movimiento por movimiento, para saber qué facturas ya se pagaron.

## Quién lo sufre

La persona que lleva la contabilidad o la administración de la pyme. Muchas veces es una sola persona que además hace otras tareas.

## Qué sale mal

- Errores de digitación: un RUC con un dígito de menos, un total mal copiado.
- IGV mal calculado o totales que no suman.
- Facturas duplicadas, que se pagan o registran dos veces.
- Pagos que no se encuentran en el banco, o movimientos del banco que no se sabe a qué factura corresponden.
- Los errores se descubren tarde, cuando ya hay que cerrar el mes.

## Cuánto tiempo se pierde (supuestos, no datos reales)

- 200 facturas al mes x 5 minutos cada una = 1,000 minutos, unas 17 horas.
- Conciliar con el banco: 200 movimientos x 2 minutos = unas 7 horas.
- Total aproximado: **24 horas al mes**, más el tiempo de corregir errores.

## Qué propone este proyecto

Un sistema que lee las facturas con IA, valida los datos con reglas claras (RUC de 11 dígitos, IGV 18%, suma de totales, duplicados), los compara con el extracto bancario y muestra en un dashboard solo las **excepciones**, es decir, lo que una persona sí debe revisar.

Nota: todas las facturas, clientes y datos del proyecto son ficticios.
