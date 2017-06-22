# coding=utf-8
import json
import pickle

d = dict(name='zhang', age=18, score=100)
f = open('E:\\2.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('E:\\2.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

print(json.dumps(d))
json_str = '{"age":20,"name":"zhang"}'
print(json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

s = Student('bob', 18, 100)
print(json.dumps(s, default=student2dict))
print(json.loads('{"name":"zhang","age":18,"score":100}',object_hook=dict2student))
