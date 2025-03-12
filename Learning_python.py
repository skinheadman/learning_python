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
#이게 왜 돌아가는지 모르겠음음
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