SELECT
    s.`title`,
    CAST(s.`series_id` AS INT64) AS `id`
FROM {{ source('staging', 'goodreads_book_series') }} AS s
