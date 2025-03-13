# dict_a = { }
# dict_a["name"]="구름"
# print(dict_a)
# del dict_a["name"]
# print(dict_a)

# pets = [
#     {"name":"구름","age" : 5},
#     {"name":"초코","age" : 3},
#     {"name":"아지","age" : 1},
#     {"name":"호랑이","age" : 1}
# ]

# print("# 우리 동네 애완 동물들")
# for i in range(4) :
    
#     input_a=str(pets[i]["age"])+"살"
#     print(pets[i]["name"], input_a)
# #이게 왜 돌아가는지 모르겠음음
# numbers=[1,3,2,5,7,8,4,6,4,3,5,7,9,1,9]
# counter = {}

# for number in numbers:
#     array=0
#     for i in range(len(numbers)):
#         if numbers[i]==number:
#             array=array+1
#     counter[number]=array
        
# print(counter)

# character = {
#     "name" : "기사",
#     "level" : 12,
#     "items" : {
#         "sward" : "불꽃의 검",
#         "armor" : "풀플레이트"
#     },
#     "skill" : ["베기", "세게 베기", "아주 세게 베기"]
#     }

# for key in character :
#     if type(character[key]) is str :
#         print("name",":",character[key])
#     elif type(character[key]) is int :
#         print("level",":",character[key])
#     elif type(character[key]) is list :
#         for skills in character[key] :
#             print(key,":",skills)
#     elif type(character[key]) is dict :
#         for items in character[key] :
#             print(key,":",items)

# import time

# number = 0

# target_tick = time.time() + 5
# while time.time() < target_tick :
#     number+=1

# print("5초동안 {}번 반복했습니다.".format(number))

# key_list = ["name","hp","mp","level"]
# value_list = ["기사", 200, 30, 5]
# character = {}
# for i in range(len(key_list)) :
#     character[key_list[i]]=value_list[i]

# print(character)

# limit = 10000
# i = 1
# sum_value = 0
# while sum_value < limit :
#     sum_value += i
#     i += 1

# print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i-1,limit,sum_value))

# max_value = 033
# a = 0
# b = 0

# for i in range(1, 100+1) :
#     j=100 - i

#     first_value = i * j
#     if max_value <= first_value :
#         max_value = first_value
#         a = i
#         b = j
#         print("{}".format(max_value))

# print("최대가 되는 경우 : {} * {} = {} ".format(a,b,max_value))        

# ex_list=["요소A", "요소B", "요소C"]

# print(ex_list)

# print(enumerate(ex_list))

# print(list(enumerate(ex_list)))

# for i, value in enumerate(ex_list) :
#     print("{}번째 요소는 {}입니다.".format(i,value))

# ex_dict = {
#     "키Q" : "값Q",
#     "키W" : "값W",
#     "키E" : "값E",
# }

# print("items() : ", ex_dict.items())

# for key, element in ex_dict.items() :
#     print("dictionary[{}] : {}".format(key, element))

# number = int(input("정수입력>"))

# if number % 2 == 0 :
#     print((
#             "입력한 문자열은 {}입니다.\n"
#             "{}은 짝수입니다.".format(number,number)
#         )
#     )

# else :
#     print((
#             "입력한 문자열은 {}입니다.\n"
#             "{}은 홀수입니다.".format(number,number)
#         )
#     )

# output=[i for i in range(1,100+1) if "{:b}".format(i).count('0')==1]

# for i in output :
#     print("{} : {}".format(i,"{:b}".format(i)))

# print("합계 : ", sum(output))

# def f(x) :
#     return 2*x + 1

# print(f(10))

# def f(x) :
#     return x**2 + 2*x + 1

# print(f(10))

# def mul(*values) :
#     num = 0
#     for value in values :
#         if num == 0 :
#             num = value
#         else :
#             num *= value
    
#     return num

# print(mul(5, 7, 9, 10))

# def flatten(data) :
#     first_data=[]
#     for num in data :
#         if type(num)==list :
#             first_data+=flatten(num)
#         else :
#             first_data.append(num)
#     return first_data
                


# example = [[1,2,3],[4,[5,6]],7,[8,9]]

# print("원본 : ", example)
# print("변환 : ",flatten(example))

