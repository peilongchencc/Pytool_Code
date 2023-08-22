文件运行方式：
1.将 `类套类套类` 型数据写入Redis。<br>
```shell
python classOfclass_to_redis.py
```
2.从Redis中取出写入的 `类套类套类` 型数据。<br>
```shell
python run_redis_function.py
```
运行结果:<br>
```txt
--执行get_redis_function.py文件--
从Redis获取数据成功，类的属性为：
instance_a
instance_b
instance_c
```