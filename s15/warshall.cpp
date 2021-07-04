#include <bits/stdc++.h>
using namespace std;

using ll = long long; // long long = entero de 64 bits

const int maxn = 505;
const ll inf = 1e18;

int n, m, q;
ll d[maxn][maxn];

int main(){
	scanf("%d %d %d", &n, &m, &q);
	for(int i = 0; i<n; i++){
		fill(d[i], d[i]+n, inf);
		d[i][i] = 0;
	}
	for(int i = 0, a, b, c; i<m; i++) {
		scanf("%d %d %d", &a, &b, &c);	
		--a, --b;
		d[a][b] = min(d[a][b], (ll)c);
		d[b][a] = min(d[b][a], (ll)c);
	}

	for(int k = 0; k<n; k++) 
		for(int i = 0; i<n; i++) 
			for(int j = 0; j<n; j++) 
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
	
	while (q--) {
		int a, b;
		scanf("%d %d", &a, &b);
		--a, --b;
		printf("%lld\n", d[a][b] == inf ? -1ll : d[a][b]);

	}
	return 0;
}

