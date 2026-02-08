"""
main.py

Author: Alejandro Zheng
Date: 2025-12-14
Description:
    整个程序的主循环

"""
import time
import random
from src.models import User
from src.dummy_data import generate_video_library
from src.recommender import recommend_next_video, update_user_interest
from src.behavior_sim import simulate_reaction

def main():
    """
    整个模拟器的主循环
    """

    print("============================")
    print("Tiktok 多巴胺算法模拟器 V1.0 ")
    print("============================")

    #创建数据集
    print("初始化视频集")
    library = generate_video_library(1000)

    #创建用户
    me = User(user_id=1)
    print(f"用户{me.user_id}登录成功")

    print("\n")

    #开始刷视频
    for i in range(1,21):
        print(f"第{i}滑动")

        #推荐视频
        video = recommend_next_video(me,library)
        print(f"推荐视频{video.category},时长:{video.duration}秒")

        #用户观看视频
        my_reaction = simulate_reaction(video,me)
        print(f"用户反馈: 看了{my_reaction['watch_time']}秒，点赞={my_reaction['like']},不感兴趣={my_reaction['dislike']}，完播率={my_reaction['finished']}")

        #记录历史
        me.history.append(video.video_id)

        #更新用户画像
        update_user_interest(me,video,my_reaction)

        #打印内容
        time.sleep(0.5)

        print("\n")

    print("============================")
    print("模拟结束。用户最终画像(Interest_Vector):")
    print(me.interest_vector)
    print("============================")


if __name__ == "__main__":
    main()