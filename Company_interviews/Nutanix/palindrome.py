#Take a string as input
#You can break (cut) the string into substrings.
#Every substring must be a palindrome.
#Find the minimum number of breaks (cuts) needed to make all the substrings as palindrome


def min_palindrome_cuts(s):
    n = len(s)

    # Helper function to check palindrome
    def is_palindrome(x):
        return x == x[::-1]

    dp = [0] * n

    for i in range(n):
        if is_palindrome(s[:i + 1]):
            dp[i] = 0
        else:
            dp[i] = float('inf')
            for j in range(1, i + 1):
                if is_palindrome(s[j:i + 1]):
                    dp[i] = min(dp[i], dp[j - 1] + 1)

    return dp[-1]


count=min_palindrome_cuts('abcdefgh')
print(count)
