#有红蓝黄三种颜色的球，其中红球3个，蓝球6个，黄球3个。先将这12个球混合放入一个盒子中
#从中任意找出8个球，编程计算摸出球的各种颜色搭配

for red in range(0,4):
    for yellow in range(0,4):
        for blue in range(2,7):     #blue最少都会有两个
            if red + yellow + blue == 8:
                print("red ball:",red)
                print("yellow ball:",yellow)
                print("blue ball:",blue)
                print("__"*20)