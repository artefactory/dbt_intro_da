
--local_sales_macro

{% macro local_sales_macro(dataset,dataset_table) -%}

SELECT 
    CAST ( barcode_ean13  AS STRING) AS BARCODE
    , CAST( site_key AS STRING) AS STORE
    ,  product_CATEGORY AS CATEGORY
    ,  pdt_SUB_CATEGORY AS SUB_CATEGORY
    ,  DATE 
    ,  CA AS LOCAL_REVENUE
FROM {{ source(dataset,dataset_table ) }}

{%- endmacro %}