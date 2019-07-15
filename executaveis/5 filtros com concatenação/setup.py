import sys
from cx_Freeze import setup, Executable
import  cv2


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("concat.py", base=base)
]

buildOptions = dict(
        packages = ["numpy"],
        includes = ["cv2"],
        include_files = ["lena_std.tif"],
        excludes = []
)



setup(
    name = "concat",
    version = "1.0",
    description = "Vai aplicar 5 filtros e concatenar as imagens",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
