class solution:
    finalResult=[]
    def bfs (self,matrix,n,visited,str,i,j):
        visited[i][j]=1
        if i==n-1 and j==n-1:
            self.finalResult.append(str)
            visited[i][j]=0
            return
        if j-1>0 and (matrix[i][j-1]==1 and visited[i][j-1]==0) :
            self.bfs(matrix,n,visited,str+"L",i,j-1)
        if j+1<n and (matrix[i][j+1]==1 and visited[i][j+1]==0 ) :
            self.bfs(matrix,n,visited,str+"R",i,j+1)
        if  i-1>0 and (matrix[i-1][j]==1 and visited[i-1][j]==0)  :
            self.bfs(matrix,n,visited,str+"U",i-1,j)
        if i+1<n and (matrix[i+1][j]==1 and visited[i+1][j]==0 ):
            self.bfs(matrix,n,visited,str+"D",i+1,j)
        visited[i][j]=0
        return
    def findpath(self,m,n):
        visited=[[0 for i in range(n)] for j in range(n)]
        #what we need to send
        self.bfs(m,n,visited,"",0,0)
        return self.finalResult






if __name__ == '__main__':
    n = int(input())
    arr=[]
    for i in range(n):
        a = list(map(int, input().strip().split()))
        arr.append(a)
    matrix = [[0 for i in range(n) for j in range(n)]]
    k = 0
    ob = solution()
    result = ob.findpath(arr, n)
    result.sort()
    if len(result) == 0:
        print(-1)
    else:
        for x in result:
            print(x, end=" ")
        print()