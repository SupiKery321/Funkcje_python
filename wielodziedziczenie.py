class Film:
    def __init__(self, title, the_year_of_publishment, type, number_of_plays,):
        self.title = title
        self.the_year_of_publishment = the_year_of_publishment
        self.type = type
        self.number_of_plays = number_of_plays
    
    def play(self):
        for a in lista:
         number_of_plays = a.number_of_plays + 1
         print(number_of_plays)

    def film(self): 
         self.title = input("Nazwa filmu:")
         for a in lista:
            if self.title == a.title:
             return(f"{self.title}({self.the_year_of_publishment})")     

class Series(Film):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number
    
    def serie(self):
        self.title = input("Nazwa serialu:")
        for a in lista:
           if self.title == a.title:
            return(f"{self.title} S{self.season_number}E{self.episode_number}")

lista = [] 
lista.append(Series(title = "Narcos", the_year_of_publishment = "2015", type = "Crime TV genre", number_of_plays = 15000000, episode_number = "07", season_number = "01"))
lista.append(Film(title = "Creed", the_year_of_publishment = "2015", type = "Sport film", number_of_plays = 71323581))
lista.append(Series(title = "Punisher", the_year_of_publishment = "2017", type = "Conspiracy fiction", number_of_plays = 4214125, episode_number = "02", season_number = "04"))
lista.append(Film(title = "Sniper", the_year_of_publishment = "2014", type = "Action", number_of_plays = 9124531))


rodzaj = input("Film czy Serial:")
for a in lista: 
    if rodzaj =="serial" and type(a)== Series:
      print(a.serie())
      break
    elif rodzaj == "film" and type(a)== Film:
      print(a.film())
      break
    

        

 

        



