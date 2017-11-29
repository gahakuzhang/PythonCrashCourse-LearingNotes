#8.5.2 using arbitrary keyword arguments 使用任意数量的关键字实参
#user_profile.py
def build_profile(first,last,**user_info):
    """创建一个字典，包含我们所知道的用户的一切"""
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile
user_profile=build_profile('albert','einstein',
                           location='princeton',
                           field='physics')
print(user_profile)
#返回字典