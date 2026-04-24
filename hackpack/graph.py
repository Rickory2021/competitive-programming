"""
Graph — BFS, DFS, Toposort, Dijkstra, Bellman-Ford
═══════════════════════════════════════════════════
Always use iterative in Python — recursion limit + overhead kills you.

Adjacency list setup:
  adj = [[] for _ in range(n)]
  for _ in range(m):
      u, v = map(int, input().split())
      adj[u].append(v)
      adj[v].append(u)  # omit for directed
"""
from collections import deque
from heapq import heappush, heappop
from math import inf


# ── BFS ──────────────────────────────────────

def bfs(adj, start):
    """Returns dist array (-1 = unreachable)."""
    n = len(adj)
    dist = [-1] * n
    dist[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


# ── DFS (iterative) ─────────────────────────

def dfs_iterative(adj, start):
    """Returns visited set and parent dict."""
    visited = set()
    parent = {start: -1}
    stack = [start]
    while stack:
        u = stack.pop()
        if u in visited:
            continue
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                parent[v] = u
                stack.append(v)
    return visited, parent


# ── Connected Components ─────────────────────

def connected_components(adj, n):
    """Returns list of components (each a list of nodes)."""
    visited = [False] * n
    comps = []
    for i in range(n):
        if not visited[i]:
            comp = []
            q = deque([i])
            visited[i] = True
            while q:
                u = q.popleft()
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
            comps.append(comp)
    return comps


# ── Topological Sort (Kahn's) ────────────────

def toposort_kahn(adj, n):
    """Returns sorted list or [] if cycle exists."""
    indeg = [0] * n
    for u in range(n):
        for v in adj[u]:
            indeg[v] += 1
    q = deque(u for u in range(n) if indeg[u] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []


# ── Dijkstra ─────────────────────────────────
# adj[u] = [(v, weight), ...]
# O((V+E) log V) — non-negative weights only

def dijkstra(adj, start, n):
    dist = [inf] * n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heappush(pq, (nd, v))
    return dist


# ── Bellman-Ford ─────────────────────────────
# edges = [(u, v, w), ...]
# O(V·E) — handles negative weights, detects negative cycles

def bellman_ford(edges, start, n):
    """Returns (dist, has_negative_cycle)."""
    dist = [inf] * n
    dist[start] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != inf and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    neg_cycle = False
    for u, v, w in edges:
        if dist[u] != inf and dist[u] + w < dist[v]:
            neg_cycle = True
            break
    return dist, neg_cycle
