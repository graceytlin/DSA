def flood_fill(image, sr, sc, color):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type color: int
    :rtype: List[List[int]]
    """

    curr_col = image[sr][sc]
    height = len(image)
    width = len(image[0])

    result = image

    adjacent = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def dfs(r, c):
        if 0 <= r < height and 0 <= c < width and image[r][c] == curr_col and result[r][c] != color:
            result[r][c] = color

            for adj in adjacent:
                dfs(r + adj[0], c + adj[1])

    dfs(sr, sc)

    return result
