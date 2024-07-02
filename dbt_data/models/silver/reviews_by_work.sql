SELECT
    r.`id` AS `review_id`,
    b.`work_id`,
    r.`rating`
FROM {{ source('analytics', 'reviews') }} AS r
INNER JOIN {{ source('analytics', 'books') }} AS b ON r.`book_id` = b.`id`
INNER JOIN {{ source('analytics', 'works') }} AS w ON b.`work_id` = w.`id`
