WITH works AS (
    SELECT
        NULLIF(w.`original_title`, '') AS `title`,
        CAST(w.`work_id` AS INT64) AS `id`,
        SAFE_CAST(w.`original_publication_year` AS INT64)
            AS `publication_year`
    FROM
        {{ source('staging', 'goodreads_book_works') }} AS w
)

SELECT
    `id`,
    `title`,
    `publication_year`
FROM works
