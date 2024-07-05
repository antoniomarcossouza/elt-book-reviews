WITH works AS (
    SELECT DISTINCT
        CAST(w.`work_id` AS INT64) AS `id`,
        CASE
            WHEN
                NULLIF(w.`original_title`, '') IS NOT NULL
                THEN w.`original_title`
            ELSE b.`title_without_series`
        END AS `title`,
        SAFE_CAST(w.`original_publication_year` AS INT64)
            AS `publication_year`
    FROM
        {{ source('staging', 'goodreads_book_works') }} AS w
    INNER JOIN
        {{ source('staging', 'goodreads_books') }} AS b
        ON w.`work_id` = b.`work_id`
    WHERE NULLIF(w.`original_title`, '') IS NULL
)

SELECT
    w.`id`,
    w.`publication_year`,
    REGEXP_REPLACE(w.`title`, r' \(.*?\)', '') AS `title`
FROM works AS w
