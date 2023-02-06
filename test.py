class wife:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def cooking(self):
        print(self.name+"做饭！")
        print(id(self))
w01=wife("丽",21,"女")
print(id(w01))
w01.cooking()

w02=wife("芳芳",22,"女")
print(id(w02))
w02.cooking()