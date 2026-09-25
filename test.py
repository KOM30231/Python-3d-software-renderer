import pywavefront
from pywavefront import material
import main as mn
import numpy as np

def cal_projection(scene):
    for name,mat in scene.materials.items():
        s=mat.vertices
        l2=np.array([mn.world_to_screen(s[0])])
    print(l2)

scene = pywavefront.Wavefront('diablo3_pose.obj', collect_faces=True)

# for name,mesh in scene.meshes.items():
#     # print(name,mesh)
#     for mat in mesh.materials:
#         # print(mat)
#         # print(mesh.faces)

cal_projection(scene)
