-- Borra las tablas si existen (facturas primero, porque depende de proveedores)
DROP TABLE IF EXISTS facturas;
DROP TABLE IF EXISTS proveedores;

CREATE TABLE proveedores (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,   -- se numera solo
    ruc VARCHAR(11) NOT NULL UNIQUE CHECK (length(ruc) = 11),
    razon_social VARCHAR(255) NOT NULL
);

CREATE TABLE facturas (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,   -- se numera solo
    proveedor_id INTEGER NOT NULL,
    numero VARCHAR(20) NOT NULL,
    fecha DATE NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    igv DECIMAL(10,2) NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (proveedor_id) REFERENCES proveedores(id),
    UNIQUE (proveedor_id, numero)                          -- evita facturas duplicadas
);