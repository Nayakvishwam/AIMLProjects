WITH pk AS (
    SELECT
        kcu.table_schema,
        kcu.table_name,
        kcu.column_name
    FROM information_schema.table_constraints tc
    JOIN information_schema.key_column_usage kcu
        ON tc.constraint_name = kcu.constraint_name
       AND tc.table_schema = kcu.table_schema
    WHERE tc.constraint_type = 'PRIMARY KEY'
),
fk AS (
    SELECT
        kcu.table_schema,
        kcu.table_name,
        kcu.column_name,
        ccu.table_name AS ref_table,
        ccu.column_name AS ref_column
    FROM information_schema.table_constraints tc
    JOIN information_schema.key_column_usage kcu
        ON tc.constraint_name = kcu.constraint_name
    JOIN information_schema.constraint_column_usage ccu
        ON tc.constraint_name = ccu.constraint_name
    WHERE tc.constraint_type = 'FOREIGN KEY'
),
uk AS (
    SELECT
        kcu.table_schema,
        kcu.table_name,
        kcu.column_name
    FROM information_schema.table_constraints tc
    JOIN information_schema.key_column_usage kcu
        ON tc.constraint_name = kcu.constraint_name
    WHERE tc.constraint_type = 'UNIQUE'
)
SELECT
    c.table_schema,
    c.table_name,
    c.ordinal_position,
    c.column_name,

    c.data_type,
    c.udt_name,

    c.character_maximum_length,
    c.numeric_precision,
    c.numeric_scale,

    c.is_nullable,
    c.column_default,

    c.is_identity,
    c.identity_generation,

    CASE
        WHEN pk.column_name IS NOT NULL
        THEN 'PRIMARY KEY'
    END AS primary_key,

    CASE
        WHEN fk.column_name IS NOT NULL
        THEN 'FOREIGN KEY'
    END AS foreign_key,

    CASE
        WHEN uk.column_name IS NOT NULL
        THEN 'UNIQUE'
    END AS unique_key,

    fk.ref_table,
    fk.ref_column

FROM information_schema.columns c

LEFT JOIN pk
ON c.table_schema = pk.table_schema
AND c.table_name = pk.table_name
AND c.column_name = pk.column_name

LEFT JOIN fk
ON c.table_schema = fk.table_schema
AND c.table_name = fk.table_name
AND c.column_name = fk.column_name

LEFT JOIN uk
ON c.table_schema = uk.table_schema
AND c.table_name = uk.table_name
AND c.column_name = uk.column_name

WHERE c.table_schema NOT IN
(
    'information_schema',
    'pg_catalog'
)

ORDER BY
    c.table_name,
    c.ordinal_position;