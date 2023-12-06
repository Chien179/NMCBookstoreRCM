-- name: GetBooksRCM :many
select u.username,
    b.id,
    r.rating,
    b.name,
    b.price,
    b.author,
    b.publisher,
    b.image,
    b.quantity,
    b.description,
    string_agg(distinct g.name, ',') as category
from books as b
    inner join reviews as r on b.id = r.books_id
    INNER JOIN users as u ON r.username = u.username
    INNER JOIN books_genres as bg ON b.id = bg.books_id
    inner join genres as g on bg.genres_id = g.id
group by u.username,
    b.id,
    r.rating,
    b.name,
    b.price,
    b.author,
    b.publisher,
    b.quantity,
    b.image,
    b.description;