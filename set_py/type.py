print("hello python")


def printHello():
    print("hello")


printHello()


def sum(a, b):
    print(a + b)


sum(3, 4)

import random
from unittest import result


def getRandomNumber():
    num = random.randint(1, 10)
    return num


print(getRandomNumber())


def add(a, b):
    result = a + b
    return result

print("sum")
print(add(5, 6))

# 자료형(리스트)
animals = ["토끼", "고양이", "강아지"]
empty = []
# 인덱스 0부터 시작됨
print(animals[2])
print(animals[-1])  # 가장 마지막 데이터
# 데이터 추가
animals.append("쿼카")
# 삭제
del animals[0]
# 할당
animals[0] = "사슴"
print(animals)
# 리스트 슬라이싱
print(animals[1:3])
print(animals[:])  # 전체
print(animals[:2])
print(animals[1:])
# 리스트 길이
print(len(animals))
# 리스트 정렬
animals.sort(reverse=True)
print(animals)

sky = ["sun", "moon", "star"]
for skye in sky:
    print("선택한 것은 ", skye, " 입니다.")

messages = "별헤는 밤"
for word in messages:
    print(word)

for i in range(1, 10, 2):  # range(시작,끝+1,단계)
    print(i)

"""
while 조건식:
    반복할 명령
    증감식
"""
k = 0
while k < 10:
    print(k, "번째 사람 선발")
    k += 2

"""
while True:  # 무한반복
    x = input("종료는 exit>>")
    if x == "exit":
        break
"""
