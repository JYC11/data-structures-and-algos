#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int n,m,map[8][8],map2[8][8],ans;

int dx[4]={0,0,-1,1}, dy[4]={-1,1,0,0};

vector< pair<int,int> > emptys, virus;

void bfs() {
    queue< pair<int,int> > q;
    int size = virus.size();
    for (int i = 0; i < size; i++) {
        q.push({virus[i].first,virus[i].second});
    }
    while(!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i], ny = y + dy[i];
            if(nx < 0 || nx >= n || ny < 0 || ny >= m) {
                continue;
            }
            if(map2[nx][ny] == 0) {
                map2[nx][ny] = 2;
                q.push({nx,ny});
            }
        }
    }
}

void solve() {
    int size = emptys.size();
    vector<int> p(size,1);
    p[0] = p[1] = p[2] = 0;
    // p [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    // emptys [{i,j},{i,j},{i,j},{i,j},{i,j},{i,j},{i,j},{i,j},{i,j}]
    do {
        for (int i = 0; i < size; i++) {
            if(p[i] == 0) {
                map2[emptys[i].first][emptys[i].second] = 1;
            }
        }
        bfs();
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if(map2[i][j] == 0) {
                    cnt++;
                }
            }
        }
        ans = max(ans,cnt);
        for (int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                map2[i][j] = map[i][j];
            }
        }
    } while (next_permutation(p.begin(),p.end()));
    

}

int main() {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &map[i][j]);
            map2[i][j] = map[i][j];
            if (map[i][j] == 0) {
                emptys.push_back({i,j});
            } else if(map[i][j] == 2) {
                virus.push_back({i,j});
            }
        }
    }
    solve();
    printf("%d\n",ans);
    return 0;
}