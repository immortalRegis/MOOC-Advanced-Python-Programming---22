# Write your solution here:
class Series:
    def __init__(self, title:str, number_of_seasons:int, genre_list:list):
        self.title = title
        self.number_of_seasons = number_of_seasons
        self.genre_list = genre_list
        self.ratings = []
    
    def __str__(self):
        str_genre = ", ".join(self.genre_list)
        if len(self.ratings) > 0:
            mean_rating = 0
            for num in self.ratings:
                mean_rating += num
            mean_rating = float(mean_rating)/len(self.ratings)
            return f"{self.title} ({self.number_of_seasons} seasons) \ngenres: {str_genre}\n{len(self.ratings)} ratings, average {mean_rating:.1f} points"
        else:
            return f"{self.title} ({self.number_of_seasons} seasons) \ngenres: {str_genre} \nno ratings"
    
    def rate(self, rating: int):
        self.ratings.append(rating)
    
    
def minimum_grade(rating: float, series_list: list):
    met_criteria = []
    for seasonal in series_list:
        for val in seasonal.ratings:
            if val >= rating:
                met_criteria.append(seasonal)
                break
    
    return met_criteria

def includes_genre(genre: str, series_list: list):
    met_criteria = []
    for seasonal in series_list:
        for aspect in seasonal.genre_list:
            if aspect == genre:
                met_criteria.append(seasonal)
                break
    
    return met_criteria



if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)
    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)
    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)
    series = [s1, s2, s3]

    vastaus = includes_genre("Crime", series)
    print(vastaus)