-- Print full description of the table Books from the current database
SELECT 
    column_name AS 'Column',
    column_type AS 'Type',
    is_nullable AS 'Nullable',
    column_key AS 'Key',
    column_default AS 'Default',
    extra AS 'Extra'
FROM 
    information_schema.columns
WHERE 
    table_schema = DATABASE() 
    AND table_name = 'Books';

