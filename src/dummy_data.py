"""
dummy_data.py

Author: Alejandro Zheng
Date: 2025-12-14
Description:
    这是一个数据集用来给整个程序来进行模拟

"""
import random
from typing import List
from src.models import Video

#定义视频的种类
CATEGORIES = ["News", "Humor", "Pets", "Sports", "Gaming"]

def generate_video_library(count: int = 1000) ->List[Video]:
    """
    随机生成 count 个假视频，返回一个列表
    """

    library=[]

    print(f"正在生成{count}个视频数据")

    for i in range(count):

        #生成视频id
        new_id = count + i

        #生成视频种类
        new_category = random.choice(CATEGORIES)

        #生成视频的时长
        new_duration = random.randint(15,60)

        #生成视频数据
        new_video = Video(video_id=new_id,category=new_category,duration=new_duration)

        #加到视频库里面
        library.append(new_video)

    print(f"视频集生成完毕")

    return library

#测试模块
if __name__ == "__main__":
    test_lib=generate_video_library(5)

    for i in range(5):
        print(test_lib[i])