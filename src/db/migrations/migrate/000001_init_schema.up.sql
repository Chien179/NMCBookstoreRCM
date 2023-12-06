CREATE TABLE "users" (
  "username" varchar PRIMARY KEY NOT NULL,
  "full_name" varchar NOT NULL,
  "email" varchar UNIQUE NOT NULL,
  "password" varchar NOT NULL,
  "image" varchar NOT NULL,
  "phone_number" varchar NOT NULL,
  "age" int NOT NULL,
  "sex" varchar NOT NULL,
  "role" varchar NOT NULL DEFAULT 'user',
  "is_deleted" boolean NOT NULL DEFAULT false,
  "password_changed_at" timestamptz NOT NULL DEFAULT '0001-01-01 00:00:00Z',
  "created_at" timestamptz NOT NULL DEFAULT 'now()'
);

CREATE TABLE "books" (
  "id" BIGSERIAL PRIMARY KEY,
  "name" varchar NOT NULL,
  "price" float NOT NULL,
  "image" varchar [] NOT NULL,
  "description" varchar NOT NULL,
  "author" varchar NOT NULL,
  "publisher" varchar NOT NULL,
  "publication_date" varchar NOT NULL,
  "page" varchar NOT NULL,
  "product_dimensions" varchar NOT NULL,
  "quantity" int NOT NULL,
  "is_deleted" boolean NOT NULL DEFAULT false,
  "created_at" timestamptz NOT NULL DEFAULT 'now()'
);
CREATE TABLE "genres" (
  "id" BIGSERIAL PRIMARY KEY,
  "name" varchar NOT NULL,
  "is_deleted" boolean NOT NULL DEFAULT false,
  "created_at" timestamptz NOT NULL DEFAULT 'now()'
);

CREATE TABLE "books_genres" (
  "id" BIGSERIAL PRIMARY KEY,
  "books_id" bigserial NOT NULL,
  "genres_id" bigserial NOT NULL,
  "created_at" timestamptz NOT NULL DEFAULT 'now()'
);

CREATE TABLE "reviews" (
  "id" BIGSERIAL PRIMARY KEY,
  "username" varchar NOT NULL,
  "books_id" bigserial NOT NULL,
  "liked" int NOT NULL DEFAULT 0,
  "disliked" int NOT NULL DEFAULT 0,
  "reported" boolean NOT NULL DEFAULT false,
  "comments" varchar NOT NULL,
  "is_deleted" boolean NOT NULL DEFAULT false,
  "rating" int NOT NULL DEFAULT 0,
  "created_at" timestamptz NOT NULL DEFAULT 'now()'
);

CREATE INDEX ON "books_genres" ("books_id");
CREATE INDEX ON "books_genres" ("genres_id");
CREATE INDEX ON "books_genres" ("books_id", "genres_id");
ALTER TABLE "books_genres"
ADD FOREIGN KEY ("books_id") REFERENCES "books" ("id");
ALTER TABLE "books_genres"
ADD FOREIGN KEY ("genres_id") REFERENCES "genres" ("id");