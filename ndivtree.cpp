#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
const int MAXN = 100 * 1000 + 7;
int tin[MAXN], tout[MAXN];
vector<int> g[MAXN];
bool used[MAXN];
vector<int> divs[MAXN];
int timer = 1;
int p[MAXN][20];
void dfs(int v, int par)
{
 used[v] = true;
 tin[v] = timer;
 timer++;
 p[v][0] = par;
 for (int i = 1; i < 20; i++)
 {
  p[v][i] = p[p[v][i - 1]][i - 1];
 }
 for (int i = 0; i < (int)g[v].size(); i++)
 {
  int to = g[v][i];
  if (!used[to])
  {
   dfs(to, v);
  }
 }
 tout[v] = timer - 1;
}
bool isAncestor(int u, int v)
{
 return tin[u] <= tin[v] && tout[u] >= tout[v];
}
int getUp(int u, int v)
{
 for (int i = 19; i >= 0; i--)
 {
  if (!isAncestor(p[v][i], u))
  {
   v = p[v][i];
  }
 }
 return v;
}
vector<pair<bool, pair<int, int> > >ev[MAXN];
void addRectangle(int x1, int y1, int x2, int y2)
{
 if (x1 > y1)
 {
  swap(x1, y1);
  swap(x2, y2);
 }
 ev[x1].push_back(make_pair(true, make_pair(y1, y2)));
 ev[x2 + 1].push_back(make_pair(false, make_pair(y1, y2)));
}
void addPath(int u, int v, int n)
{
 if (isAncestor(v, u)) swap(u, v);
 if (isAncestor(u, v))
 {
  int uu = getUp(u, v);
  addRectangle(1, tin[v], tin[uu] - 1, tout[v]);
  addRectangle(tout[uu] + 1, tin[v], n, tout[v]);
 }
 else
 {
  addRectangle(tin[u], tin[v], tout[u], tout[v]);
 }
}
struct segmentTree
{
 vector<int> tree;
 vector<int> mod;
 segmentTree(int n)
 {
  tree.resize(4 * n + 17);
  mod.resize(4 * n + 17);
 }
 int getv(int v, int tl, int tr)
 {
  if (mod[v]) return tr - tl + 1;
  return tree[v];
 }
 void change(int v, int tl, int tr, int l, int r, bool add)
 {
  if (r < tl || l > tr) return;
  if (tl >= l && tr <= r)
  {
   if (add)
   {
    mod[v]++;
   }
   else
   {
    mod[v]--;
   }
  }
  else
  {
   int tm = (tl + tr) / 2;
   change(2 * v, tl, tm, l, r, add);
   change(2 * v + 1, tm + 1, tr, l, r, add);
   tree[v] = getv(2 * v, tl, tm) + getv(2 * v + 1, tm + 1, tr);
  }
 }
 int getSum(int v, int tl, int tr, int l, int r)
 {
  if (r < tl || l > tr) return 0;
  if (mod[v]) return min(tr, r) - max(tl, l) + 1;
  if (tl >= l && tr <= r) return tree[v];
  int tm = (tl + tr) / 2;
  return getSum(2 * v, tl, tm, l, r) + getSum(2 * v + 1, tm + 1, tr, l, r);
 }
};
int main()
{
#ifdef LOCAL
 freopen("input.txt", "r", stdin);
#endif
 int n;
 scanf("%d", &n);
 for (int i = 1; i < n; i++)
 {
  int u, v;
  scanf("%d %d", &u, &v);
  g[u].push_back(v);
  g[v].push_back(u);
 }
 dfs(1, 1);
 for (int i = 1; i <= n; i++)
 {
  for (int j = i + i; j <= n; j += i)
  {
   addPath(i, j, n);
  }
 }
 segmentTree st(n + 1);
 ll res = 1LL * n * (n - 1) / 2;
 for (int i = 1; i <= n; i++)
 {
  for (int j = 0; j < (int)ev[i].size(); j++)
  {
   st.change(1, 1, n, ev[i][j].second.first, ev[i][j].second.second, ev[i][j].first);
  }
  res -= st.getSum(1, 1, n, i + 1, n);
 }
 printf("%lld\n", res);
 
}