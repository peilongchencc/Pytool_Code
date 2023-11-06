# code_utils
from marking_data_output import refresh_metadata
class Dimension_analy:
    """进行维度分析
    """
    # 定义类属性
    dimension_data = None

    def __init__(self):
        pass

    def handle(self, usr_input):
        """测试类属性是否变化，是否支持动态更新
        """
        res_dict = {"用户数据":usr_input,
                    "维度数据为:": self.dimension_data} # 调用类属性
        return res_dict

    @classmethod
    def modify_class_variable(cls):
        """每次调用更新一次类属性
        """
        cls.dimension_data = refresh_metadata()