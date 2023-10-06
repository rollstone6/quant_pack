import math


# 定义欧式期权定价函数
def european_option_pricing(S, K, T, r, sigma, n, option_type='call'):
    """
    S: 当前标的资产价格
    K: 期权行权价格
    T: 期权到期时间（年）
    r: 无风险利率
    sigma: 标的资产的波动率
    n: 二叉树的步数
    option_type: 期权类型，'call' 表示看涨期权，'put' 表示看跌期权
    """
    deltaT = T / n
    u = math.exp(sigma * math.sqrt(deltaT))
    d = 1 / u
    discount = math.exp(-r * deltaT)

    option_prices = []

    # 构建二叉树
    for i in range(n + 1):
        spot_price = S * (u ** (n - i)) * (d ** i)
        if option_type == 'call':
            option_price = max(0, spot_price - K)
        else:
            option_price = max(0, K - spot_price)
        option_prices.append(option_price)

    # 反向逐步计算期权价格
    for j in range(n, 0, -1):
        for i in range(j):
            option_prices[i] = (option_prices[i] * p + option_prices[i + 1] * (1 - p)) * discount

    return option_prices[0]


# 示例：计算看涨期权的价格
S = 100  # 当前标的资产价格
K = 100  # 期权行权价格
T = 1.0  # 期权到期时间（年）
r = 0.05  # 无风险利率
sigma = 0.2  # 标的资产的波动率
n = 100  # 二叉树步数

call_option_price = european_option_pricing(S, K, T, r, sigma, n, option_type='call')
print(f"看涨期权的价格为：{call_option_price}")
