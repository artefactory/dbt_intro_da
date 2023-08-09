SELECT  grp.product_CATEGORY AS CATEGORY
        , grp.pdt_SUB_CATEGORY AS SUB_CATEGORY
        , SUM(grp.CA) AS GRP_REVENUE
        , SUM(local.LOCAL_REVENUE) AS LOCAL_REVENUE
        , SUM(grp.CA)- SUM(local.LOCAL_REVENUE) AS DIFFERENCE
FROM {{ source('dbt_intro', 'crf_sales_group_data') }}  grp  
LEFT JOIN dbt_intro_da_jamila.local_sales local
    ON grp.barcode_ean13 = local.BARCODE
    AND CAST(grp.site_key AS STRING) = local.STORE
    AND grp.DATE = local.DATE 
GROUP BY 1,2
ORDER BY 5 DESC
