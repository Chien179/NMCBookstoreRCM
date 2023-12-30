from src.helper.get_data import get_data
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.lib.logger import logger
import pandas as pd
import re


class RCMBookHelper:
    def get_coll(self, i, coll):
        return self.common_books[
            self.common_books["index"] == self.sorted_sim_books[i][0]
        ][coll].item()

    def get_coll_by_name(self, name, coll):
        return self.common_books[self.common_books["name"] == name][coll].values[0]

    def preprocessing(self):
        self.df = pd.DataFrame(get_data())
        self.df.dropna(inplace=True)
        self.df.reset_index(drop=True, inplace=True)

        self.df.drop(index=self.df[self.df["rating"] == 0].index, inplace=True)

        self.df["category"] = self.df["category"].apply(
            lambda x: re.sub("[\W_]+", " ", x).strip()
        )

        self.df["name"] = [book.replace('"', "") for book in self.df["name"].values]

    def content_based_recommender(self, name: str, size: int):
        self.preprocessing()
        name = str(name).replace('"', "")
        if name in self.df["name"].values:
            data = self.df["name"].value_counts()
            rating_counts = pd.DataFrame(data)
            rare_books = rating_counts[rating_counts.to_numpy() <= 2].index
            self.common_books = self.df[~self.df["name"].isin(rare_books)]

            if name not in rare_books:
                self.common_books = self.common_books.drop_duplicates(subset=["name"])
                self.common_books.reset_index(inplace=True)
                self.common_books["index"] = [
                    i for i in range(self.common_books.shape[0])
                ]
                target_cols = ["name", "author", "publisher", "category"]
                self.common_books["combined_features"] = [
                    " ".join(self.common_books[target_cols].iloc[i,].values)
                    for i in range(self.common_books[target_cols].shape[0])
                ]
                cv = CountVectorizer()
                count_matrix = cv.fit_transform(self.common_books["combined_features"])
                cosine_sim = cosine_similarity(count_matrix)
                index = self.common_books[self.common_books["name"] == name][
                    "index"
                ].values[0]
                sim_books = list(enumerate(cosine_sim[index]))
                self.sorted_sim_books = sorted(
                    sim_books, key=lambda x: x[1], reverse=True
                )[1:size]

                books = []
                for i in range(len(self.sorted_sim_books)):
                    book_cor = {
                        "id": self.get_coll(i, "id"),
                        "name": self.get_coll(i, "name"),
                        "price": self.get_coll(i, "price"),
                        "image": self.get_coll(i, "image"),
                        "description": self.get_coll(i, "description"),
                        "author": self.get_coll(i, "author"),
                        "publisher": self.get_coll(i, "publisher"),
                        "quantity": self.get_coll(i, "quantity"),
                        "rating": self.get_coll(i, "rating"),
                    }
                    books.append(book_cor)

                return books
        else:
            data = self.df["name"].value_counts()
            rating_counts = pd.DataFrame(data)
            rare_books = rating_counts[rating_counts.to_numpy() <= 2].index
            self.common_books = self.df[~self.df["name"].isin(rare_books)]
            
            logger.info("rare book")
            random = pd.Series(self.common_books["name"].unique()).sample(size).values
            books = []
            for book in random:
                book_cor = {
                    "id": self.get_coll_by_name(book, "id"),
                    "name": self.get_coll_by_name(book, "name"),
                    "price": self.get_coll_by_name(book, "price"),
                    "image": self.get_coll_by_name(book, "image"),
                    "description": self.get_coll_by_name(book, "description"),
                    "author": self.get_coll_by_name(book, "author"),
                    "publisher": self.get_coll_by_name(book, "publisher"),
                    "quantity": self.get_coll_by_name(book, "quantity"),
                    "rating": self.get_coll_by_name(book, "rating"),
                }
                books.append(book_cor)

            return books
