from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# (1) 영화제목 '매트릭스'의 평점을 가져오기
target_title = db.movies.find_one({'title':'매트릭스'})
# print(target_title['score'])

# (2) '매트릭스'의 평점과 같은 평점의 영화 제목들을 가져오기
target_score = target_title['score']

same_score_movies = list(db.movies.find({'score':target_score},{'_id':False}))
# for movie in same_score_movies:
#     print(movie['title'])

# (3) 매트릭스 영화의 평점을 0으로 만들기
db.movies.update_one({'title':'매트릭스'},{'$set':{'score':'0'}})
print(target_title['score'])
