# Monocloud

## 添加白名单：
以 `processon.com` 为例，`processon.com` 不支持通过代理形式访问，即使 `mode` 设置为规则都不行。正确做法为添加白名单，走国内网络。<br>

1. 点击 `Config`
2. 然后在 `Bypass proxy` 部分添加以下内容即可：
> `*` 表示以 `https://www.processon.com/` 为前缀的网址都走国内网络。

```log
https://www.processon.com/*
```
操作示意图：<br>
![image](https://github.com/peilongchencc/Pytool_Code/assets/89672905/ff453e53-d16a-4ef9-b725-dc349a39ac1d)

网址添加后，点击 `Save&Apply` 即可。此时你就可以正常访问 `processon.com` 了～🥴🥴🥴<br>
