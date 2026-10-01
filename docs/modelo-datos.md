Facturas - Sirve para visualizar los datos de las facturas.
id entero guarda el id X CLAVE PRIMARIA
proveedor_id entero guarda el id de la tabla proveedor X CLAVE FORANEA
numero texto guarda el nombre de la factura F001-A o algo así
fecha tiempo guarda la fecha de la factura
subtotal decimales guarda monto antes de impuestos
igv decimales guarda el impuesto
total decimales guarda el total despues de calcular

Proveedores - Sirve para identificar a un proveedor.
id entero guarda el id X CLAVE PRIMARIA  
ruc numero de 11 caracteres guarda el numero de ruc
razon_social texto guarda el nombre de el proveedor
