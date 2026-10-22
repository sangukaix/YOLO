score=72
if score >= 90:
    grade='A'
elif score >= 80:
    grade= 'B'
else:
    grade='C'
print('학점:', grade)

#반복문
for n in range(1,6): #1~5까지 반복
    if n==3:
        continue
    print(n)

count=0
while count<3:
    print(count)
    count += 1

# (중요) 리스트[], 튜플(), 딕셔너리{key:value}, Set{}, 컴프리헨션
fruits= ["사과","바나나","사과"] #순서대로 저장. 수정 가능. 중복데이터 허용
print(fruits)
fruits.append('포도')
print(fruits)
fruits[1]="오렌지"
print(fruits)

point=(10,20) #튜플 - 요소 수정 불가
print(point, point[0], point[1])
#point.append() 존재하지 않는 기능
#point[0]=100 #error

student= {"name":"sam","score":80} #key:value pair
print(student)
student['score']=90
print(student['score'], student.get('nam','없음'))

#중복 데이터를 허용하지 않는 Set 타입
unique_fruits= set(fruits) #list ==> set 으로 변경.
print(unique_fruits) #순서는 보장 안됨. 중복 허용 안함.

#리스트 컴프리헨션
#1~5의 제곱값을 저장하는 리스트 생성
squars= [n*n for n in range(1,6)]
print(squars)

passing= [n for n in [65,90,73,82] if n>=80] #시험 패스 조건 통과점수들.
print(passing)
print()

#5. 함수, lambda
def greet(person, greeting='안녕하세요'):
    return f"{greeting}, {person}님!"

print( greet('영희') )
print( greet('철수','반가워요.') )

def average(numbers):
    return sum(numbers) / len(numbers) #총합/개수 = 평균 (sum, len 내장함수)
print("평균:", average([80,90,75]))

#제곱해주는 기능 함수 --람다 함수로
#def square(x):
#    return x*x
square= lambda x: x*x
print(square(5))

#내장 함수 중에서 자주 사용
print('정렬:', sorted([3,1,5,2]))
print( min(3,1,5), max(3,1,5) )

#6. 파일 입출력 기능함수
#현재 파일이 있는 폴더에 결과 txt 문서를 저장
from pathlib import Path
BASE_DIR= Path(__file__).resolve().parent
#D:\mbca_home\YOLO
file_path= BASE_DIR / "aaa.txt"

file= open(file_path, "w", encoding='utf-8')
file.write('파이썬 복습\n파일 입출력 예제\n')
file.close()

with open(file_path, "r", encoding="utf-8") as file:
    print('파일 내용:', file.read())

#예외처리 (예외가 발생해도 다운되지 않도록..)
try:
    number= int("80abc")
    print(number+10)
except ValueError as error:
    print("예외발생:", error)
finally:
    print("예외여부와 상관없이 무조건 실행")
