--local_sales_table_creation

{{ local_sales_macro('dbt_intro','crf_hyp_sales_fr_data') }}

UNION ALL 

{{ local_sales_macro('dbt_intro','crf_sup_sales_fr_data') }}

UNION ALL 

{{ local_sales_macro('dbt_intro','crf_prx_sales_fr_data') }}


