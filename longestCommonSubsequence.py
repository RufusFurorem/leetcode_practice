def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    
    m = len(text1) + 1
    n = len(text2) + 1
    dp_arr = [[0 for x in range(m)] for x in range(n)]
    
    for i in range(1, n):
        for k in range(1, m):
            if (text1[k-1] == text2[i-1]):
                dp_arr[i][k] += 1 + dp_arr[i-1][k-1]
            else:
                dp_arr[i][k] = max(dp_arr[i-1][k], dp_arr[i][k-1])

    return dp_arr[-1][-1]