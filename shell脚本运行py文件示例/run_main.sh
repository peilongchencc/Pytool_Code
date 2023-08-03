# 查看自己正在使用的shell解释器名称(可选)
echo $SHELL

# 添加conda脚本的激活程序，不添加这一步，执行conda指令会显示错误信息
# 
source /opt/anaconda3/etc/profile.d/conda.sh

# 激活nazhi虚拟环境
conda activate nazhi

# 运行测试文件
python main.py