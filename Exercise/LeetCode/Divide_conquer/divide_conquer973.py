'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
'''
# date 10.08.2020
def kClosestPointsToOrigin(nums, k):
    finaldict = {}

    for ele in nums:
        currentDistance = ele[0]**2 + ele[1]**2
        if k > 0:
            finaldict[currentDistance] = ele
            k -= 1
        else:
            maxDistance = max(finaldict.keys())
            if currentDistance < maxDistance:
                finaldict.pop(maxDistance)
                finaldict[currentDistance] = ele
    return finaldict.values()

print(kClosestPointsToOrigin([[3,3],[5,-1],[-2,4]], 2))




