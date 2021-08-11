#!/usr/local/bin/python3.7
# -*- coding:utf-8 -*-

"""
有序列表：
    List： 是一种有序的集合，可以随时添加和删除其中的元素。
    元组：tuple 是一种有序的集合，但是tuple 一旦初始化就不能修改。
"""

# -*- coding: UTF-8 -*-
def print_user_info( name , age , sex = '男' ):
    # 打印用户信息
    print()
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex))
    return



if __name__ == '__main__':

    # 1.一个产品，需要列出产品的用户，这时候就可以使用一个 list 来表示,甩尾王
    # user = ['liangdianshui', 'twowater', '两点水']
    #
    # for dd in user:
    #     print(dd)
    #     del user[len(user)-2]
    #
    # tuple1 = ('两点水','twowter','liangdianshui',123,456)
    # print(tuple1)
    # print(123 in tuple1)
    #
    # for dd in tuple1:
    #     print(dd)

    # dict1={'liangdianshui':'111111' ,'twowater':'222222' ,'两点水':'333333'}
    # print(dict1)
    # # 新增一个键值对
    # dict1['jack']='444444'
    # print(dict1)
    # # 修改键值对
    # dict1['liangdianshui']='555555'
    # print(dict1)
    #
    # # 调用 print_user_info 函数
    # print_user_info('两点水', 18, '女')
    # print_user_info('三点水', 25)

    list1 = list(range(1,31))
    print(list1)
    list2 = [x*x for x in range(1,11) if x%2 ==0]
    print(list2)

    


