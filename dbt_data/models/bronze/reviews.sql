WITH reviews AS (
    SELECT
        r.`review_id` AS `id`,
        r.`user_id`,
        CAST(r.`book_id` AS INT64) AS `book_id`,
        CAST(r.`rating` AS INT64) AS `rating`,
        NULLIF(r.`started_at`, '') AS `started_at`,
        NULLIF(r.`read_at`, '') AS `read_at`
    FROM {{ source('staging', 'goodreads_reviews_dedup') }} AS r
)

SELECT
    `id`,
    `user_id`,
    `book_id`,
    `rating`,
    `started_at`,
    `read_at`
FROM reviews
