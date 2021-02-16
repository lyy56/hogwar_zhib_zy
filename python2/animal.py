import os

import yaml


class Animal:
    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def call(self):
        print("会叫")

    def run(self):
        print("会跑")


class Cat(Animal):
    def __init__(self, name, color, age, sex, hair):
        super().__init__(name, color, age, sex)
        self.hair = hair

    def new_call(self):
        print(f"{self.name}短毛")

    def new_work(self):
        print(f"{self.name}会捉老鼠")

    def call(self):
        print(f"{self.name}喵喵叫")


class Dog(Animal):
    def __init__(self, name, color, age, sex):
        super().__init__(name, color, age, sex)

    def dog_call(self):
        print(f"{self.name}长毛")

    def dog_work(self):
        print(f"{self.name}会看家")

    def run(self):
        print(f"{self.name}汪汪叫")


if __name__ == "__main__":
    with open("an.yaml") as f:
        d = yaml.safe_load(f)
    print(d)

    cat = Cat(d['cat'][0]['name'], d['cat'][0]['color'], d['cat'][0]['age'], d['cat'][0]['sex'], d['cat'][0]['hair'])
    cat.new_work()
    dog = Dog(d['dog'][0]['name'], d['dog'][0]['color'], d['dog'][0]['age'], d['dog'][0]['sex'])
    dog.dog_work()
    # print(f'姓名{cat.name},颜色{cat.color},年龄{cat.age},性别{cat.sex},毛发{cat.hair}')
