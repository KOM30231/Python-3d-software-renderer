import pywavefront
from pywavefront import material
import main.py as mn


def cal_projection(scene):



scene = pywavefront.Wavefront('diablo3_pose.obj', collect_faces=True)

for name,mesh in scene.meshes.items():
    print(name,mesh)
    for mat in mesh.materials:
        print(mat)
        # print(mesh.faces)
