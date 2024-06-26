WITH authors AS (
    SELECT
        NULLIF(a.`name`, '') AS `name`,
        CAST(a.`author_id` AS INT64) AS `id`
    FROM
        {{ source('staging', 'goodreads_book_authors') }} AS a
)

SELECT
    `id`,
    `name`
FROM authors
