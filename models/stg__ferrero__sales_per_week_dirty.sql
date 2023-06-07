select
    *
from {{ source('dbt_intro', 'ferrero_sales_per_week_dirty') }}
