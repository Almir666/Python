from collections import deque
# def sum(list):
#     if list == []:
#         return 0
#     return  list[0] + sum(list[1:])
#
# def count(list):
#     if list == []:
#         return 0
#     return 1 + count(list[1:])
#
# def max(list):
#     if len(list) == 2:
#         return list[0] if list[0] > list[1] else list[1]
#     temp_max = max(list[1:])
#     return list[0] if list[0] > temp_max else temp_max
#
# def quicsort(list):
#     if len(list) < 2:
#         return list
#     else:
#         pivot = list[0]
#         less = [i for i in list[1:] if i < pivot]
#         greater = [i for i in list[1:] if i > pivot]
#         return quicsort(less) + [pivot] + quicsort(greater)
#
# arr = [1,2,10,3]
# print(sum(arr))
# print(count(arr))
# print(max(arr))
# print(quicsort(arr))




graph = {}
graph["You"] = ["Alice", "Claire", "Bob"]
graph["Claire"] = ["Tom", "Johny"]
graph["Alice"] = ["Peggy"]
graph["Bob"] = ["Mango_seller", "Peggy"]
graph["Tom"] = []
graph["Johny"] = []
graph["Peggy"] = []
graph["Mango_seller"] = []

def person_is_seller(name):
    if "Mango_seller" in graph[name].key:
        print("Вот он")
        return True

def search(name):
    search_qeue = deque()
    search_qeue += graph[name]
    searched = []
    while search_qeue:
        person = search_qeue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print("Мы нашли его :3")
                return True
            else:
                search_qeue += graph[person]
                searched.append(person)
        print("Ничего не найдено")
        return False

search("You")

