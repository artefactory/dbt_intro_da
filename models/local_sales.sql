select
    *
from {{ source("dbt_intro", "crf_hyp_sales_fr_data") }}
