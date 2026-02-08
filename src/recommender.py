"""
recommender.py

Author: Alejandro Zheng
Date: 2025-12-14
Description:
    这是一个模拟抖音算法推荐的机制的文件

"""
import random
from src.models import User,Video
from typing import List

def update_user_interest(user:User,video:Video,reaction:dict):
    """
    根据用户的反应，更新他对视频分类的权重
    """

    #1.获取视频分类
    category= video.category

    #获取用户当前对这个分类的兴趣分。如果没有看过，默认是1.0
    current_weight=user.interest_vector.get(category,1.0)

    #如果用户喜欢这个视频
    if reaction.get('like') == True:
        current_weight = current_weight * 1.5

    #如果用户不感兴趣
    if reaction.get('dislike') == True:
        current_weight = current_weight * 0.7

    #如果用户看完了视频
    if reaction.get('finished') == True:
        current_weight = current_weight * 1.3

    #如果用户观看时间小于一定时间
    if reaction.get('watch_time', 0) < 5:
        current_weight = current_weight * 0.8

    #如果用户观看时间大于一定比例的视频总时长
    if reaction.get('watch_time', 0) > (0.7*video.duration):
        current_weight = current_weight * 1.2
    elif reaction.get('watch_time', 0) > (0.5*video.duration):
        current_weight = current_weight * 1.1

    #存入新的权重
    user.interest_vector[category] = current_weight
    print(f"用户对{category}的兴趣更新为：{current_weight}")

def recommend_next_video(user: User, video_library: List[Video]) -> Video:
    """
    根据用户画像，决定下一个给用户看什么视频
    """

    #查看用户的历史观看记录,观看记录大于5，视为老用户：
    if len(user.history) > 5:
        print(f"用户{user.user_id}视为老用户")
        user.is_new=False

    #如果用户是新用户或者他看过的视频小于5，随机给他推荐视频
    if user.is_new == True or len(user.history) < 5:
        print("冷启动阶段，随机推荐")
        return random.choice(video_library)
    
    #20%的概率推荐新的视频
    if random.random() <0.2:
        print("探索新兴趣")
        return random.choice(video_library)

    #推荐用户喜欢看的视频
    print("投其所好")
    if not user.interest_vector:
        return random.choice(video_library)
    
    #查看用户最喜欢看哪些视频
    fav_category = max(user.interest_vector,key=user.interest_vector.get)
    print(f"用户最喜欢:{fav_category}")

    #找到可以推荐的视频
    candidate_videos = [v for v in video_library if v.category == fav_category]

    #如果可以推荐的视频是空的
    if len (candidate_videos) == 0:
        return random.choice(video_library)

    return random.choice(candidate_videos)

