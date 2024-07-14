# 1. define yors comfyui nodes here
# ...

# ucase 1.1:
from yors_comfyui_node_as_x_type import * # import all yors comfyui nodes from it

# ucase 1.2:
# from yors_comfyui_node_as_x_type import NodeSetItAsImage # import some yors comfyui nodes from it


# 2. reset yors comfyui nodes category (it will be used set rmb in yors_comfyui_node_setup)
# from yors_comfyui_node_reset_rmb import reset_rmb
# reset_rmb(__name__,"YMC/as_x_type") // danger!

# 3. set nodes category alias
# to set the right mouse menu as your likes.

import yors_comfyui_node_as_x_type as base
from yors_comfyui_node_setup import get_sys_module,set_node_class_category_alias
this_py_module = get_sys_module(__name__)
set_node_class_category_alias(base,this_py_module,"YMC/as_x_type",True)