'''
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance
between i and j equals the distance between i and k (the order of the tuple matters).
Find the number of boomerangs.
'''
# date 12.04.2020
import re

# 把输入的字符串转化为坐标list
def trans_input(input_points):
    input_list = []
    pattern = re.compile(r'[[](.*?)[]]', re.S)
    output_list = re.findall(pattern, input_points)
    for ele in output_list:
        point = list(map(int, ele.split(',')))
        input_list.append(point)
    return input_list

#计算两点之间距离
def computeDistance(point1, point2):
    return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2

#计算回回旋镖数量
def findBoomerang(points):
    boomerang = 0
    for i in points:
        # print('------current i is :', i, '---------')
        distance_dic = {}
        for j in points:
            if i == j:
                continue
            distance = computeDistance(i, j)
            # print('the distance of', j, 'to i is : %s' %(distance))
            count = distance_dic.get(distance, 0)
            distance_dic[distance] = count +1 # 这句不要写错！！
        # print('distance_dic :', distance_dic)
        for distance in distance_dic:
            boomerang += distance_dic[distance] * (distance_dic[distance] - 1)
    return boomerang

points = input('please input points :')
input_points = trans_input(points)
# print('the input points are :', input_points)
print('the number of boomerang is :', findBoomerang(input_points))


