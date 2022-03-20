#dictionary

#리스트와 비슷하나 순서를 따지지 않음
#키와 값이 pair가 원소가 된다

fruits = {'apple':'사과','watermelon':'수박'}
print(fruits['watermelon'])
fruits['kiwi'] = '키위' #삽입
print(fruits)

empty ={}
print(type(fruits), type(empty))

test = [['python',3],['english',2],['dance',1]]
print(test[1][0])
print(dict(test)) #dict함수 리스트에서 딕셔너리로 변환 시켜줌

test1 = ['ab','cd','ef']
print(test1[1][0])
print(dict(test1)) #리스트에서 붙어있는 문자열 2개까지만 딕셔너리 변환가능하고 , 변환시 a : b 이런식으로 변환

test2 = ['ab','cd','ef']
print(test2[1][0])
print(dict(test2)) #dict함수 리스트에서 딕셔너리로 변환 시켜줌


#update()
fruits = {'apple':'사과','watermelon':'수박'}
others = {'strawberry':'딸기','kiwi':'딸기'} #others 딕셔너리를 fruits에 결합하는 update 함수
fruits.update(others)
print(fruits)

#del
del fruits['apple'] #apple 키워드를 딕셔너리에서 삭제하는 del 키워드 apple 딕셔너리가 삭제됨
print(fruits)

#clear함수
# fruits.clear() #딕셔너리는 유지되며 들어있던 원소만 전체 삭제
# print(fruits)

#keys() 딕셔너리 키값을 출력 하는 함수
# print(fruits.keys())

# #items() 딕셔너리에 키, 벨류 값을 출력하는 함수
# print(fruits.items())

#for문으로 딕셔너리 key 값 출력하기
for k in fruits.keys():
    print(k)

#for문에서 items를 이용하여 key값과 value값을 출력
for k, v in fruits.items():
    print(k)
    print(v)

#음식 추천 프로그램 v0.1



