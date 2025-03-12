
# # print("-----출력 확인선-----")
# # print()
# # print()
# # print("Hello")

# # print("""\
# # 안녕 클레오파트라
# # 세상에서 제일가는 포테이토 
# # 칩\
# # """)

# # print("안녕하세요"[1:4])

# # hello="안녕하세요"
# # print(hello[1:4])

# # hello="안녕하세요"
# # hello+="엄엄"
# # print(hello)


# # string=input("Enter the meet saying>>")
# # print(string)

# # string = input("입력>")
# # print("자료 : ",string)
# # print(type(string))

# # string_a=input("a>>")
# # int_a=int(string_a)

# # string_b=input("b>>")
# # int_b=int(string_b)

# # print("string :",string_a+string_b)
# # print("number: ", int_a + int_b)

# # output_a=str(52)
# # output_b=str(273)
# # print(type(output_a), output_a)
# # print(type(output_b), output_b)

# # str_input=input("숫자입력>>")
# # num_input=float(str_input)

# # print()
# # print(num_input, "inch")
# # print((num_input)*2.54, "cm")

# # str_input=input("원의 반지름을 입력 >>")
# # num_input=float(str_input)
# # print()
# # print("반지름 : ", num_input)
# # print("둘레: ", 2*3.14*num_input)
# # print("넓이: ",3.14*(num_input**2))

# # str1_input=input("문자열 입력> ")
# # str2_input=input("문자열 입력> ")

# # print(str1_input +" "+ str2_input)

# # str3=str1_input
# # str1_input=str2_input
# # str2_input=str3

# # print(str1_input +" "+ str2_input)

# # op="{:015.2f}".format(3.1415926383)
# # print(op)

# # op="{}".format(10,20,30,40,50).find("10")
# # print(op)

# # a=input("> 1번째 숫자: ")
# # b=input("> 2번째 숫자: ")
# # print()
# # print("{} + {} = {}".format(a, b, int(a)+int(b)))

# # x=10
# # under_20=x<20
# # print("under_20 : ",under_20)
# # print("not under_20 : ",not under_20)

# # number=input("정수입력 : ")
# # number= int(number)
# # if number > 0 :
# #     print("양수입니다.")
# # if number < 0 :
# #     print("음수입니다.")
# # if number==0 :
# #     print("0")

# # import datetime

# # now=datetime.datetime.now()

# # print("{}년 {}월 {}일 {}시 {}분 {}초".format(
# #     now.year,
# #     now.month,
# #     now.day,
# #     now.hour,
# #     now.minute,
# #     now.second
# # ))

# # import datetime

# # now = datetime.datetime.now()

# # if 1 <= now.month < 3 or now.month==12:
# #     print("이번달은 {}월로 겨울울입니다.".format(now.month))
# # if 3 <= now.month < 6 :
# #     print("이번달은 {}월로 봄입니다.".format(now.month))
# # if 

# # number = input("Enter the number >>")
# # last_number = int(number[-1])

# # if last_number == 0 \
# #     or last_number == 2 \
# #     or last_number == 4 \
# #     or last_number == 6 \
# #     or last_number == 8 :
# #     print("짝수입니다.")

# # if last_number == 1 \
# #     or last_number == 3 \
# #     or last_number == 5 \
# #     or last_number == 7\
# #     or last_number == 9 :
# #     print("홀수입니다.")


# # number = input("Enter the number >>")
# # last_number = number[-1]

# # if last_number in "02468" :
# #     print("짝수입니다.")
# # if last_number in "13579" :
# #     print("홀수입니다.")

# # number = input("Enter the number >>")
# # number = int(number)

# # if number % 2 == 0 :
# #     print("짝수입니다.")
# # else :
# #     print("홀수입니다.")

# # list_a=[1,2,3]

# # print('# 리스트 뒤에 요소 추가하기')
# # list_a.append(4)
# # list_a.append(5)
# # print(list_a)
# # print()

# # print('# 리스트 중간에 요소 추가하기')
# # list_a.insert(0, 10)
# # print(list_a)

# numbers=[273, 103, 5, 32, 65, 9, 72, 800, 99]

# # for num in numbers:
# #     if(num%2==0):
# #         print("{}는 짝수입니다.".format(num))
# #     else :
# #         print("{}는 홀수입니다.".format(num))

# # for num in numbers :
# #     if num > 100 :
# #         len_num=3
# #     elif num > 10 :
# #         len_num=2
# #     elif num > 0 :
# #         len_num=1
# #     print("{} 는 {} 자릿수입니다.".format(num, len_num))

# list_of_list = [
#     [1,2,3],
#     [4,5,6,7],
#     [8,9],
# ]

# for num in list_of_list :
#     for r_num in num :
#         print(r_num)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers :
    output[].append(number)

print(output)