WITH books AS (
    SELECT
        CAST(b.`book_id` AS INT64) AS `id`,
        CAST(b.`work_id` AS INT64) AS `work_id`,
        NULLIF(b.`title`, '') AS `title`,
        NULLIF(b.`title_without_series`, '') AS `title_without_series`,
        CAST(s[0] AS INT64) AS `series_id`,
        CAST(a[0].`author_id` AS INT64) AS `author_id`,
        NULLIF(a[0].`role`, '') AS `author_role`,
        NULLIF(b.`publisher`, '') AS `publisher`,
        SAFE_CAST(b.`num_pages` AS INT64) AS `num_pages`,
        SAFE_CAST(b.`publication_day` AS INT64) AS `publication_day`,
        SAFE_CAST(b.`publication_month` AS INT64) AS `publication_month`,
        SAFE_CAST(b.`publication_year` AS INT64) AS `publication_year`,
        NULLIF(b.`url`, '') AS `url`,
        NULLIF(b.`image_url`, '') AS `image_url`
    FROM
        {{ source('staging', 'goodreads_books') }} AS b,
        UNNEST(b.`series`.list) AS s,
        UNNEST(b.`authors`.list) AS a
)

SELECT
    `id`,
    `work_id`,
    `series_id`,
    `title`,
    `title_without_series`,
    `author_id`,
    `author_role`,
    `publisher`,
    `num_pages`,
    `publication_day`,
    `publication_month`,
    `publication_year`,
    `url`,
    `image_url`
FROM books
