# Modelo de datos (borrador inicial)

## Relación entre las tablas
Un proveedor tiene muchas facturas. Cada factura pertenece a un solo proveedor.
`proveedores.id` ← `facturas.proveedor_id`

---

## Tabla `proveedores`
Guarda los datos de cada proveedor que emite facturas.

| Columna | Tipo de dato | Qué guarda | Clave |
|---|---|---|---|
| `id` | entero (`INTEGER`) | Identificador único del proveedor | Primaria |
| `ruc` | texto de 11 caracteres (`CHAR(11)`) | Número de RUC | |
| `razon_social` | texto (`VARCHAR`) | Nombre del proveedor | |

---

## Tabla `facturas`
Guarda los datos de cada factura recibida.

| Columna | Tipo de dato | Qué guarda | Clave |
|---|---|---|---|
| `id` | entero (`INTEGER`) | Identificador único de la factura | Primaria |
| `proveedor_id` | entero (`INTEGER`) | `id` del proveedor que emitió la factura | Foránea → `proveedores.id` |
| `numero` | texto (`VARCHAR`) | Serie y correlativo, por ejemplo F001-123 | |
| `fecha` | fecha (`DATE`) | Fecha de emisión de la factura | |
| `subtotal` | decimal (`NUMERIC(12,2)`) | Monto antes de impuestos | |
| `igv` | decimal (`NUMERIC(12,2)`) | Impuesto (18% del subtotal) | |
| `total` | decimal (`NUMERIC(12,2)`) | Subtotal + IGV | |