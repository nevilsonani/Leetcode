class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0
        # 使用 defaultdict 构建站点到公交线路的映射
        g = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                g[stop].append(i)

        # 如果 source 或 target 不在站点映射中，返回 -1
        if source not in g or target not in g:
            return -1

        # 初始化队列和访问集合
        q = [(source, 0)]
        vis_bus = set()
        vis_stop = {source}

        # 开始广度优先搜索
        for stop, bus_count in q:
            # 如果当前站点是目标站点，返回所需的公交次数
            if stop == target:
                return bus_count

            # 遍历经过当前站点的所有公交线路
            for bus in g[stop]:
                if bus not in vis_bus:
                    vis_bus.add(bus)

                    # 遍历该线路上的所有站点
                    for next_stop in routes[bus]:
                        if next_stop not in vis_stop:
                            vis_stop.add(next_stop)
                            q.append((next_stop, bus_count + 1))
        return -1 # 如果无法到达目标站点，返回 -1