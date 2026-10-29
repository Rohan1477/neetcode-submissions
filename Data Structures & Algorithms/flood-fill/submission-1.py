class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        og_color = image[sr][sc]

        def dfs(sr, sc, visited):

            if (min(sr, sc) < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != og_color or image[sr][sc] in visited):
                return

            image[sr][sc] = color
            visited.add(image[sr][sc])

            dfs(sr+1, sc, visited)
            dfs(sr-1, sc, visited)
            dfs(sr, sc+1, visited)
            dfs(sr, sc-1, visited)

        visited = set()

        dfs(sr, sc, visited)

        return image


            