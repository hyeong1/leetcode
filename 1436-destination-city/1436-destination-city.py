class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        val = {}
        idx = 0
        for a, b in paths:
            if a not in val:
                val[a] = idx
                idx += 1
            if b not in val:
                val[b] = idx
                idx += 1

        link = [False for _ in range(len(val))]
        for a, b in paths:
            link[val[a]] = str(val[b])

        print(link)
        for i in range(len(link)):
            if not link[i]:
                return list(val.keys())[i]