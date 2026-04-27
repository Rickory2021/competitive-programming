"""
Shortest Path Algorithms
────────────────────────
Dijkstra:      O((V+E) log V)  — non-negative weights only
Bellman-Ford:  O(V·E)          — handles negative weights, detects negative cycles
"""

from heapq import heappush, heappop
from math import inf


def dijkstra(adj, start, n):
    """
    adj[u] = [(v, weight), ...]
    Returns dist array from start.
    """
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


def bellman_ford(edges, start, n):
    """
    edges = [(u, v, w), ...]
    Returns (dist, has_negative_cycle).
    """
    dist = [inf] * n
    dist[start] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != inf and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    # check for negative cycle
    neg_cycle = False
    for u, v, w in edges:
        if dist[u] != inf and dist[u] + w < dist[v]:
            neg_cycle = True
            break
    return dist, neg_cycle


# ── Usage ──
# adj = [[] for _ in range(n)]
# for _ in range(m):
#     u, v, w = map(int, input().split())
#     adj[u].append((v, w))
#     adj[v].append((u, w))  # omit for directed
# dist = dijkstra(adj, 0, n)
