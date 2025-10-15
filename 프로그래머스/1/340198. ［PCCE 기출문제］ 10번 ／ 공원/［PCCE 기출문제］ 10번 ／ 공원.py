def access(mat, park):
    row = len(park)
    col = len(park[0])
    for r in range(row-mat+1):
        for c in range(col-mat+1):
            # 모든 공간이 -1인 경우 
            if all(park[i][j] == '-1' for i in range(r,r+mat) for j in range(c,c+mat)):
                return True
    return False

def solution(mats, park):
    mats.sort(reverse = True)
    for mat in mats:
        if access(mat,park):
            return mat
    return -1