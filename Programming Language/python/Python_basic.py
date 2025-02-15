# https://wikidocs.net/32
# 위 사이트를 참고해가면서 보세요. 중요한 함수만 뽑았습니다.
# 주석을 풀고 실행해본 뒤, 직접 작성해보면서 추가학습해보세요

#2. all
print('2. all')
print(all([]))
print(all(''))      #빈 요소만 있으면 True
print('='*50)

# #3. any
# print('3. any')
# print(any([1,2,0]))
# print(any([]))
# print(any(''))      #빈 요소만 있으면 False
# print('='*50)


# #4. chr: 유니코드 숫자 값을 입력받아 문자를 출력
# print('4. chr')
# print(chr(20))
# print(chr(65))
# print(chr(44040))
# print(chr(70000))
# print('='*50)


# #5. dir: 객체가 지닌 함수나 변수를 보여주는 함수
# print('5. dir')
# print(dir(list()))
# print(dir(set()))
# print('='*50)


# #7. enumerate
# print('7. enumerate')
# for i, subject in enumerate(['math','Korean','English'],start=1):
#     print(i, subject)
# print('='*50)


# #9. filter
# print('9. filter')
# lst = [-3,-2,-1,0,1,2,3]
# filtered_list = list(filter(lambda x:x>0,lst))
# print(filtered_list)
# print('='*50)


# #10. hex
# print('10. hex')
# print(hex(16))
# print(hex(17))
# print(hex(255))
# print('='*50)


# #12. input
# print('12. input')
# # a = input()
# # print(a)            #입력한 값이 출력된다
# print('='*50)

# #13. int
# print('13. int')
# print(int('3'))
# print(int(3.14))
# print('='*50)

# #14. isinstance 
# print('14. isinstance')
# print(isinstance(3, int))
# print(isinstance([1,2,3,4], list))
# print('='*50)


# #15. len
# print('15. len')
# print(len('python'))
# print(len(
#     (1,'b',[1,2,3])         # 튜플의 개수
# ))
# print('='*50)


# #16. list 
# print('16. list')
# print(list('python'))       #문자열의 각 글자를 리스트로
# print('='*50)


# #17. map: 리스트 등의 반복가능한 객체에 동일한 함수를 적용
# #모든 str형 숫자에 int 적용하기
# print('17. map')
# str_num = '12345'
# list_num = list(str_num)
# print('list_num:' , list_num)   #각각은 여전히 str이므로, 리스트의 모든 요소에 int 적용
# print(map(int, list_num))   #객체가 결과이므로, list로 풀어줌
# print(list(map(int, list_num)))
# print('='*50)



# #18. max
# print('18. max')
# print(max([1,2,3,4]))
# print(max('python'))
# print('='*50)


# #19. min
# print('19. min')
# print(min([1,2,3,4]))
# print(min('python'))
# print('='*50)


# #22. ord: 문자의 유니코드 숫자 값을 리턴
# print('22. ord')
# print(ord('a'))
# print(ord('가'))
# print('='*50)


# #23. pow: power
# print('23.pow')
# print(pow(2, 4))
# print(pow(3, 3))
# print('='*50)


# #24. range 
# print('24.range')
# print('인수가 하나')
# print(list(range(5)))

# print('인수가 둘')
# print(list(range(5,10)))

# print('인수가 셋')
# print(list(range(1,10,2)))
# print(list(range(10,1,-3)))
# print('='*50)


# #25. round
# print('25.round')
# print(round(3.14))
# print(round(7.6))
# print('='*50)

# #26. sorted
# print('26.sorted')
# lst = [3,1,2]
# print(sorted(lst))
# print(lst)      #원래 함수는 바뀌지 않는다. 바꾸려면 lst = sorted(lst)
# print(sorted("python"))     #문자열도 정렬가능
# print('='*50)


# # 27. str: 문자열로 만들기
# print('27.str')
# print(str(3))
# print('='*50)


# # 28. sum
# print('28.sum')
# print(sum([1,2,3]))
# print(sum([10,20,-3]))
# print('='*50)


# #29. tuple
# print('29. tuple')
# print(tuple('abc'))
# print(tuple([1,2,3]))
# print('='*50)


# #30. type
# print('30.type')
# print(type(3))
# print(type('3'))
# print(type([3]))
# print(type((3)))
# print('='*50)


# #31. zip: 동일한 개수의 리스트나 튜플을 묶어준다
# print('31.zip')
# lst1 = [1,2,3]
# lst2 = [4,5,6]
# print(zip(lst1,lst2))   #zip 객체가 출력되므로 list로 풀어주기
# print(list(zip(lst1,lst2)))   
# print('='*50)
