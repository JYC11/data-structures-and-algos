#include <string>
#include <iostream>

using namespace std;

int n, normal, colorblind;
int dx[4]={0,0,-1,1}, dy[4]={-1,1,0,0};
string map[100],map2[100];

void dfs(int x, int y, char color) {
    map[x][y] = 'X';

    for(int i = 0; i < 4; i++) {
        int nx = x + dx[i], ny = y + dy[i];
        if(nx < 0 || nx >= n || ny < 0 || ny >= n || map[nx][ny] != color) {
                continue;
        }
        dfs(nx,ny,color);
    }
    
}

int main() {
    scanf("%d",&n);

    for (int i=0; i<n; i++) {
        cin>>map[i];
        map2[i] = map[i];
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if(map[i][j]!='X') {
                normal++;
                dfs(i,j,map[i][j]);
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            map[i][j] = map2[i][j] == 'B' ? 'B' : 'R';
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if(map[i][j]!='X') {
                colorblind++;
                dfs(i,j,map[i][j]);
            }
        }
    }

    printf("%d %d", normal, colorblind);
    return 0;
}