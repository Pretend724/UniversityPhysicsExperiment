import math

def angle_diff(a, b):
    diff = abs(a - b)
    return min(diff, 360 - diff)

def round_uncertainty(u):
    if u == 0:
        return 0.0
    exponent = math.floor(math.log10(u))
    factor = 10 ** exponent
    mantissa = u / factor
    rounded_mantissa = round(mantissa, 1)
    return rounded_mantissa * factor

def get_decimal_places(number):
    s = "{:.15f}".format(number).rstrip('0').rstrip('.')
    if '.' in s:
        return len(s.split('.')[1])
    else:
        return 0

# 输入三次测量数据
measurements = []
for i in range(3):
    print(f"\n输入第{i+1}次测量数据：")
    t1_d = int(input("θ1 度： "))
    t1_m = int(input("θ1 分： "))
    t2_d = int(input("θ2 度： "))
    t2_m = int(input("θ2 分： "))
    t1p_d = int(input("θ1' 度： "))
    t1p_m = int(input("θ1' 分： "))
    t2p_d = int(input("θ2' 度： "))
    t2p_m = int(input("θ2' 分： "))
    measurements.append((t1_d, t1_m, t2_d, t2_m, t1p_d, t1p_m, t2p_d, t2p_m))

# 转换为度并计算Φ值
phis = []
for m in measurements:
    t1 = m[0] + m[1] / 60
    t2 = m[2] + m[3] / 60
    t1p = m[4] + m[5] / 60
    t2p = m[6] + m[7] / 60
    diff1 = angle_diff(t1, t1p)
    diff2 = angle_diff(t2, t2p)
    phi_i = (diff1 + diff2) / 2
    phis.append(phi_i)

# 计算平均值和不确定度
phi_avg = sum(phis) / len(phis)
n = len(phis)
sum_sq = sum((phi - phi_avg)**2 for phi in phis)
u_phi = math.sqrt(sum_sq / (n * (n - 1))) if n > 1 else 0.0

# 计算顶角A及其不确定度
A = 180 - phi_avg
u_A = u_phi

# 舍入处理
u_rounded = round_uncertainty(u_A)
decimal_places = get_decimal_places(u_rounded)
A_rounded = round(A, decimal_places)

# 结果输出
print("\n计算结果：")
print(f"Φ的测量值（三次）： {[round(phi, 8) for phi in phis]}")
print(f"Φ的平均值： {phi_avg:.8f}°")
print(f"Φ的A类不确定度： {u_phi:.8f}°")
print(f"顶角A的测量值： {A:.8f}°")
print(f"顶角A的不确定度： {u_A:.8f}°")
print(f"顶角A的结果表示： {A_rounded:.{decimal_places}f}({u_rounded:.{decimal_places}f})")