
import pathlib
import toml
from yors_comfyui_node_setup import entry
from yors_pano_ansi_color import info_status,info_step,msg_padd,log_msg

def get_version_from_pyproject(file: pathlib.Path, fallback: str = '1.0.0'):
    """
    get version from pyproject.toml 's project.version

    get_version_from_pyproject(pathlib.Path(__file__).parent / 'pyproject.toml')
    """
    try:
        pyproject_content = file.read_text()
        pyproject = toml.loads(pyproject_content)
        version = pyproject.get('project', {}).get('version', '0.0.0')
    except FileNotFoundError:
        print("pyproject.toml not found, using default version.")
        version = fallback
    except Exception as e:
        print(f"An error occurred while reading pyproject.toml: {e}")
        version = fallback
    return version

__all__,NODE_CLASS_MAPPINGS,NODE_DISPLAY_NAME_MAPPINGS,NODE_MENU_NAMES = entry(__name__,__file__,False)

info_step(f"__all__ + WEB_DIRECTORY")
WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]

# get directory of this file
current_file_path = pathlib.Path(__file__)
name = str(current_file_path.parent)
pyproject_file = current_file_path.parent / 'pyproject.toml'
version= get_version_from_pyproject(pyproject_file)


log_msg(msg_padd("=",60,"="))
log_msg(msg_padd(f'welocme to {name}',60,"="))
log_msg(f'version: {version}')
log_msg(f'node counts:{len(NODE_MENU_NAMES)}')
log_msg(f'node menu names:')
NODE_MENU_NAMES.sort()
for node_name in NODE_MENU_NAMES:
    # log_msg(f'node name:{node_name}')
    info_status(f'{node_name}',0)
log_msg(msg_padd("=",60,"="))