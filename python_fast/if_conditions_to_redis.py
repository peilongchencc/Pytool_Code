# 应用场景：将满足不同if条件的值按照顺序存入 redis。
# 代码含义：将20以内满足不同if条件的值按照顺序存入 redis。
import redis
import json
# 连接到Redis
r = redis.Redis(host='localhost', port=6379)

idx =0
for i in range(20):
    if i%3==0:
        print(f'当i为 {i} 时，i%3==0，idx为 {idx}。')
        redis_key = "a_multiple_of_3or5" + "_" + str(idx)   # 3的倍数；
        r.set(redis_key,json.dumps(i))
        idx+=1
    if i%5==0:
        print(f'当i为 {i} 时，i%5==0，idx为 {idx}。')
        redis_key = "a_multiple_of_3or5" + "_" + str(idx)   # 5的倍数；
        r.set(redis_key,json.dumps(i))
        idx+=1
# 输出：
# 当i为 0 时，i%3==0，idx为 0。
# 当i为 0 时，i%5==0，idx为 1。
# 当i为 3 时，i%3==0，idx为 2。
# 当i为 5 时，i%5==0，idx为 3。
# 当i为 6 时，i%3==0，idx为 4。
# 当i为 9 时，i%3==0，idx为 5。
# 当i为 10 时，i%5==0，idx为 6。
# 当i为 12 时，i%3==0，idx为 7。
# 当i为 15 时，i%3==0，idx为 8。
# 当i为 15 时，i%5==0，idx为 9。
# 当i为 18 时，i%3==0，idx为 10。