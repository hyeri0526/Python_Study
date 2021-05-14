def add_many(*args): #매개변수가 몇개인지 모를때. 리스트임
    result = 0
    for i in args:
        result = result + i
    return result

print(add_many(1,2,3,4))
print(add_many(1,2,3,4,5,6,7,8,9,10))


    
