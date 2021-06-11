#include <bits/stdc++.h>
#define debug(...) fprintf(stderr, __VA_ARGS__)
using namespace std;
using ll = long long;

const int maxn = 505;
const ll inf = 1e18;
int n, m, q;
ll d[maxn][maxn];

int main(){
	scanf("%d %d %d", &n, &m, &q);
	for(int i = 0; i<n; i++) {
		for(int j = 0; j<n; j++) d[i][j] = inf;
		d[i][i] = 0;
	}

	for(int i = 0, u, v, w; i<m; i++) {
		scanf("%d %d %d", &u, &v, &w);
		u -= 1;
		v -= 1;
		d[u][v] = min(d[u][v], (ll)w);
		d[v][u] = min(d[v][u], (ll)w);
	}
	for(int k = 0; k<n; k++)
		for(int i = 0; i<n; i++)
			for(int j = 0; j<n; j++)
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
	
	while(q--){
		int u, v;
		scanf("%d %d", &u, &v);
		--u, --v;
		printf("%lld\n", d[u][v] == inf ? -1ll : d[u][v]);
	}
	


	return 0;
}

