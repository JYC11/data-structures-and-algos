#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int n, graph[20][20], fish, ans;

int dx[4]={0,0,-1,1}, dy[4]={-1,1,0,0};

pair<int,int> start;

/*
shark starts with size 2
get distance of fish around shark
check the size of the fishes
size of fish needs to be smaller than shark

*/

void bfs() {
    queue< pair<int,int> > q;
}

int main() {
    scanf("%d",&n);
    
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            scanf("%d",&graph[i][j]);
            if(graph[i][j] == 9) {
                start = {i,j};
            }
            if(graph[i][j] != 0 && graph[i][j] != 9) {
                fish++;
            }
        }
    }
    if (fish == 0) {
        printf("%d\n",ans);
    } else {
        bfs();
        printf("%d\n",ans);
    }
    return 0;
}