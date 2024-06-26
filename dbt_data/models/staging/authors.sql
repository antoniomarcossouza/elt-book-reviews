SELECT
    a.`name`,
    CAST(a.`author_id` AS INT64) AS `id`
FROM
    {{ source('staging', 'goodreads_book_authors') }} AS a
