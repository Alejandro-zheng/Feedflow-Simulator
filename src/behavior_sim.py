"""
behavior_sim.py

Author: Alejandro Zheng
Date: 2025-12-14
Description:
    这是一个模拟抖音交换界面的模拟器

"""
import random
from typing import Dict
from src.models import User, Video


def simulate_reaction(video: Video,user:User) -> Dict:
    """
    模拟用户观看视频的反应
    """

    #准备一个用户反应子集
    reaction = {
        'like': False,
        'dislike': False,
        'finished': False,
        'watch_time':0,
        'share':False
    }

    #查看用户对这个视频的分类的喜爱程度
    current_interest=user.interest_vector.get(video.category,1.0)

    #模拟看了多久视频
    base_factor=random.uniform(0.2,0.8)
    if current_interest > 1.5:
        base_factor = 0.95

    watch_time = int(video.duration * base_factor)
    reaction['watch_time'] = watch_time

    #模拟用户喜欢一些视频
    if random.random() < 0.3:
        reaction['dislike']=True

    #模拟会不会点赞
    if current_interest > 1.3 and random.random() > 0.6:
        reaction['like']=True

    #模拟：完播率
    if watch_time >= video.duration * 0.9:
        reaction['finished']= True

    return reaction