class SystemId():
    Financial = 1 #理财
    Sale = 2 #销售
    Insurance = 3 #保险
    Financial_New = 4

sdp_map = {
    SystemId.Financial: 'financial_sdp_matching',
    SystemId.Sale: 'sale_sdp_matching',
    SystemId.Insurance: 'insurance_sdp_matching',
}
print(sdp_map)

# 终端输出：
# {1: 'financial_sdp_matching', 2: 'sale_sdp_matching', 3: 'insurance_sdp_matching'}
# 注意：这个字典中 key 的数据类型为：int。