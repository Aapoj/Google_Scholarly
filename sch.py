from scholarly import scholarly

search = scholarly.search_author('Abolfazl Jalali Shahrood')
far = next(search)
scholarly.pprint(far)
print(search)
print(far)
author = scholarly.fill(far)
scholarly.pprint(author)