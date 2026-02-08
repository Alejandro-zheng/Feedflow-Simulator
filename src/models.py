"""
models.py

Author: Alejandro Zheng
Date: 2025-12-14
Description:
    这是定义用户和视频

"""
from dataclasses import dataclass,field
from typing import List,Dict

@dataclass
class Video:
    """
    视频对象：属性都是不可变的
    """
    video_id: int
    category: str
    duration: int

@dataclass
class User:
    """
    用户对象：模拟抖音用户
    """
    user_id: int
    #用户的兴趣向量，key是类别，value是权重（0.0-1.0）
    interest_vector: Dict[str,float]=field(default_factory=dict)
    #用户看过的视频ID列表
    history:List[int]=field(default_factory=list)
    #是否是新用户 
    is_new: bool = True

if __name__ == "__main__":
    v1 = Video(101,"humor",15)
    u1 = User(1)

    print("--Testing Models---")
    print(v1)
    print(u1)

    u1.history.append(101)
    u1.is_new=False
    print(u1)