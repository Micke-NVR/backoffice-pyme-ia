# Modelo de datos (borrador inicial)

## Relación entre las tablas
Un proveedor tiene muchas facturas. Cada factura pertenece a un solo proveedor.
`proveedores.id` ← `facturas.proveedor_id`

---

## Tabla `proveedores`
Guarda los datos de cada proveedor que emite facturas.

| Columna | Tipo de dato | Qué guarda | Clave / Regla |
|---|---|---|---|
| `id` | entero (`INTEGER`) | Identificador único del proveedor | Primaria, automático |
| `ruc` | texto (`VARCHAR(11)`) | Número de RUC | Único, 11 caracteres |
| `razon_social` | texto (`VARCHAR(255)`) | Nombre del proveedor | Obligatorio |

---

## Tabla `facturas`
Guarda los datos de cada factura recibida.

| Columna | Tipo de dato | Qué guarda | Clave / Regla |
|---|---|---|---|
| `id` | entero (`INTEGER`) | Identificador único de la factura | Primaria, automático |
| `proveedor_id` | entero (`INTEGER`) | `id` del proveedor que emitió la factura | Foránea → `proveedores.id` |
| `numero` | texto (`VARCHAR(20)`) | Serie y correlativo, por ejemplo F001-123 | Obligatorio |
| `fecha` | fecha (`DATE`) | Fecha de emisión de la factura | Obligatorio |
| `subtotal` | decimal (`DECIMAL(10,2)`) | Monto antes de impuestos | Obligatorio |
| `igv` | decimal (`DECIMAL(10,2)`) | Impuesto (18% del subtotal) | Obligatorio |
| `total` | decimal (`DECIMAL(10,2)`) | Subtotal + IGV | Obligatorio |

---

## Reglas de la base de datos
- `id` se genera automáticamente en ambas tablas.
- `proveedores.ruc` es único y debe tener 11 caracteres.
- Todas las columnas son obligatorias (`NOT NULL`).
- Un proveedor no puede repetir el mismo `numero` de factura (`UNIQUE (proveedor_id, numero)`).
- El total no se valida en la base: se valida después para detectar excepciones.