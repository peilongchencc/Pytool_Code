# nlp_entry.py

from code_utils import Dimension_analy

def create_pipelene(usr_input):
    tmp_dimension = Dimension_analy()
    res_dim = tmp_dimension.handle(usr_input)
    return res_dim