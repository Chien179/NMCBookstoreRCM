from src.helper.get_data import get_data, get_amount
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.lib.logger import logger
import pandas as pd
import re
import traceback

def preprocessing():
    df = pd.DataFrame(get_data())
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)

    df.drop(index=df[df["rating"] == 0].index, inplace=True)

    df["category"] = df["category"].apply(
        lambda x: re.sub("[\W_]+", " ", x).strip()
    )

    df["name"] = [book.replace('"', "") for book in df["name"].values]
    
    return df

books = preprocessing()

class RCMBookHelper:
    def  __init__(self) -> None:
        self.df = books
        self.amount = get_amount()
    
    def get_coll(self, i, coll):
        return self.common_books[
            self.common_books["index"] == self.sorted_sim_books[i][0]
        ][coll].item()

    def get_coll_by_name(self, name, coll):
        return self.common_books[self.common_books["name"] == name][coll].values[0]   

    def content_based_recommender(self, name: str, size: int):
        if self.df.empty or get_amount() != self.amount:
            self.amount = get_amount()
            self.df = preprocessing()
        
        name = str(name).replace('"', "")
        try:
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
                            "is_deleted":self.get_coll(i, "is_deleted"),
                        }
                        books.append(book_cor)

                    return books
            
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
                    "is_deleted":self.get_coll_by_name(book, "is_deleted"),        
                }
                books.append(book_cor)

            return books
        except Exception as e:
            traceback.print_exc()