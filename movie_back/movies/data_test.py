import requests
import json
# import datetime
# from datetime import timedelta

Servicekey = '04SY8J71WZ1Q1761IC2I'
base_url = 'http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp?collection=kmdb_new2'

# 총 78394 건 수 중 Get 요청으로 접근 가능한 범위 확인
# listCount=1000, startCount=50
# 총 출력 건 수, 페이지네이션 단위
# 즉 DB에 1000건밖에 넣지 못한다는 것

# 요청인자 중 runtime 변수가 없음
# 검색을 위해서는 모든 데이터가 seeding 되어있어야 함

# 더 많은 데이터를 확보하기 위하여 년도 별로 for문을 돌리는 방법으로 접근하기로 함
# 한 해에 1000개보다 많은 영화 데이터가 존재한다면 또다시 접근 불가할테니
# 월 별로 더 쪼개보거나 하는 방법이 추가적으로 필요함

# 앞의 1000 건을 확인했을 때 가장 오래된 영화는 "prodYear":"1938"
# for year in range(1938, 2020)
# 개봉일 시작에 대한 요청인자는 releaseDts, YYYYMMDD 형식의 문자열
# 일 단위(YYYYMMDD)까지 출력하면 1000건 초과의 검색에 대한 가능성이 줄어듦
# 따라서 19390101~20200619으로 검색하자
# 날짜가 아닌 범위는 제하기 위해 import datetime
# 아니, 일자별은 API 요청 건수를 초과할지도 모르니, 년도별 월별 for문 2개로 가자
# 중간에 요청 횟수가 최과되어 데이터를 1도 못 받아올 문제 상황에 대비하여, 일단 년도별로 진행 - 오 선견지명... 다행이다... 2만 여 건은 확보함 

# import json
# json.dumps(<dict>) 사용하여 json 형태의 문자열 만들기
# json.loads(<str>) 사용하여 dict 자료형으로 만들기

# url = base_url + f'&ServiceKey={Servicekey}&listCount=1000&startCount=50'

# response = requests.get(url).json()
# print(type(requests.get(url))) # type : requests.models.Response
# print(type(response)) # type : dict

#data = json.dumps(response)
# print(data)
# print(type(data)) # type : str # json으로 변환이 되었다 !


# ** 1년 단위로 영화 정보 json 파일로 저장 **
# for year in range(1939, 2021):

#     print(year-1938) # iteration 확인 위한 프린트

#     year = str(year)
#     urltemplate = base_url + f'&createDts={year}' + f'&ServiceKey={Servicekey}&listCount=1000&startCount=50'
#     response = requests.get(urltemplate).json() # type : dict
#     # print(response)
#     with open(f'final_pjt/movie_back/movies/fixtures/kmdb_data_{year}.json', 'w', encoding='utf-8') as outfile:
#          json.dump(response, outfile, indent=2)


# 총 82번의 iteration이 돌아가야하지만 76 뿐인데, 이유는 2014년도 파일부터 JSONDecodeError가 떴기 때문. 요청횟수 초과로 생각됨.
# 하지만 개봉년도 별로 요청한 API의 데이터가 어차피 제대로 년도별로 분류된 응답을 주고있지 않고, 눈으로 확인하기에 2019년도 데이터까지 보여져
# 최근의 정보를 받아오지 못했다고 말할 수 없음. 따라서 치명적 결함은 아니라고 생각되어 다음을 진행하기로 함


# ** docid 값과 해당 객체를 딕셔너리 형태로 만들어 중복을 제거함 **
new_dict = dict()
for year in range(1939, 2014):
    year = str(year)
    with open(f'final_pjt/movie_back/movies/fixtures/before_data_cleansing/kmdb_data_{year}.json', 'r', encoding='utf-8') as f:
        read = json.load(f)
        data = read['Data'][0]
        results = data['Result']

        for result in results:
            for movie in results:
                new_dict[movie['DOCID']] = movie
                # runtime 속성이 null이면 dict에서 제외함
                if movie['runtime'] == "" or movie['posters'] == "":
                    del new_dict[movie['DOCID']]
                
# print(len(new_dict)) # 중복 id 제거 후 : 데이터 7008 건
# print(len(new_dict)) # runtime 속성 null 제외 후 : 데이터 6432 건
# print(len(new_dict)) # posters 속성 null 제외 후 : 데이터 1622 건

# ** 정제한 데이터(new_dict) json 파일로 만듦 **
# with open(f'final_pjt/movie_back/movies/fixtures/after_data_cleansing.json', 'w', encoding='utf-8') as outfile:
#     json.dump(new_dict, outfile, indent=2)

with open(f'final_pjt/movie_back/movies/fixtures/data_poster_exists.json', 'w', encoding='utf-8') as outfile:
    json.dump(new_dict, outfile, indent=2)

