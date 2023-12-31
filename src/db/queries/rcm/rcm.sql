-- name: GetBooksRCM :many
SELECT u.username,
    b.id,
    r.rating,
    b.name,
    b.price,
    b.author,
    b.publisher,
    b.image,
    b.quantity,
    b.description,
    b.is_deleted,
    string_agg(DISTINCT g.name, ',') AS category
FROM books AS b
    INNER JOIN reviews AS r ON b.id = r.books_id
    INNER JOIN users AS u ON r.username = u.username
    INNER JOIN books_genres AS bg ON b.id = bg.books_id
    INNER JOIN genres AS g ON bg.genres_id = g.id
GROUP BY u.username,
    b.id,
    r.rating,
    b.name,
    b.price,
    b.author,
    b.publisher,
    b.quantity,
    b.image,
    b.description,
    b.is_deleted;

-- name: GetReviewsAmount :one
SELECT COUNT(*) AS amount
FROM books AS b
INNER JOIN reviews AS r ON r.books_id = b.id;