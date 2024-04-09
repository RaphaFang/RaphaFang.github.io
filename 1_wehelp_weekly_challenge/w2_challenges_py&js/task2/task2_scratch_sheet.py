programming_languages = [
{'language':'Python','year':1991},
{'language':'Swift','year':2014},
{'language':'Java', 'year':1995},
{'language':'C++','year':1985},
{'language':'Go','year':2007},
{'language':'Rust','year':2010},
]

def get_year(element):
    return element['year']

programming_languages.sort(key=get_year)

print(programming_languages)