"""
    游戏入口
"""

from ui import GameConsoleView

if __name__ == "__main__":
    view = GameConsoleView()
    view.start()
    view.update()

"""
    ２０４８游戏
    规则：
        游戏运行，在４＊４的方格中，出现两个随机的数字．
        产生随机数的策略：10%的概率是４，90%的概率是2.
        用户移动方格（wsad）,方格内的数字按照相应规则进行合并．
        如果地图有变化(数字移动／数字合并)，再产生１个随机数．
        游戏结束：数字不能合并，也没有空白位置．
    架构：
            逻辑处理模块     　　　　　　　　　Controller
            界面视图模块(控制台／pygame/.....)View
            数据模型模块..
            程序入口模块
    步骤：
    　　（一）逻辑处理模块 
             创建游戏核心类GameCoreController
             (1)将核心算法粘贴进来16:32
             (2)将所有参数，改为成员变量．16:50
             (3)产生新数字
             　　　-- 计算所有空白位置(为０的位置).
                   -- 随机选择一个位置
                   -- 根据概率产生数字，存入列表的相应位置．
         （二）界面视图模块
         　　　创建游戏核心类对象
         　　　调用核心类对象的生成数字方法
            　　while True:
                  呈现界面
                  获取用户输入，调用核心类对象的移动方法．　
                  产生随机数
        　(三)如果地图有变化(数字移动／数字合并)，再产生１个随机数．
        　(四)游戏结束：数字不能合并，也没有空白位置．
"""