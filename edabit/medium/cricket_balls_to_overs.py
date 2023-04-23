def total_overs(balls):
    overs = balls // 6
    remaining_balls = balls % 6

    return overs + (remaining_balls / 10)

print(total_overs(2400))
print(total_overs(164))
print(total_overs(945))
print(total_overs(5))
