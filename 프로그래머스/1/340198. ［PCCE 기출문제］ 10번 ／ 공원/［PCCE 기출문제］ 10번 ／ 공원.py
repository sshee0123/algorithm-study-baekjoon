def myfunc(mat,park,r,c):
    for i in range(r, r+mat):
        for j in range(c,c+mat):
            if i<len(park) and j<len(park[0]):
                if park[i][j] != '-1':
                    return False
            else:
                return False
    return True

def solution(mats, park):
    mats.sort(reverse = True) # 크기가 큰 돗자리부터 반복문
    row = len(park)
    col = len(park[0])
    for mat in mats:
        for r in range(row-mat+1):
            for c in range(col-mat+1):
                if myfunc(mat,park,r,c):
                    return mat        
    return -1