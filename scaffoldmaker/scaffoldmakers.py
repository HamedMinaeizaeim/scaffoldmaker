"""
Class for listing and accessing all mesh type scripts supported by scaffoldmaker.
"""

from scaffoldmaker.meshtypes.meshtype_2d_plate1 import MeshType_2d_plate1
from scaffoldmaker.meshtypes.meshtype_2d_plate1 import MeshType_2d_plate1
from scaffoldmaker.meshtypes.meshtype_2d_platehole1 import MeshType_2d_platehole1
from scaffoldmaker.meshtypes.meshtype_2d_sphere1 import MeshType_2d_sphere1
from scaffoldmaker.meshtypes.meshtype_2d_tube1 import MeshType_2d_tube1
from scaffoldmaker.meshtypes.meshtype_3d_box1 import MeshType_3d_box1
from scaffoldmaker.meshtypes.meshtype_3d_boxhole1 import MeshType_3d_boxhole1
from scaffoldmaker.meshtypes.meshtype_3d_heartatria1 import MeshType_3d_heartatria1
from scaffoldmaker.meshtypes.meshtype_3d_heartventricles1 import MeshType_3d_heartventricles1
from scaffoldmaker.meshtypes.meshtype_3d_heartventricles2 import MeshType_3d_heartventricles2
from scaffoldmaker.meshtypes.meshtype_3d_heartventriclesbase1 import MeshType_3d_heartventriclesbase1
from scaffoldmaker.meshtypes.meshtype_3d_heartventriclesbase2 import MeshType_3d_heartventriclesbase2
from scaffoldmaker.meshtypes.meshtype_3d_sphereshell1 import MeshType_3d_sphereshell1
from scaffoldmaker.meshtypes.meshtype_3d_sphereshellseptum1 import MeshType_3d_sphereshellseptum1
from scaffoldmaker.meshtypes.meshtype_3d_tube1 import MeshType_3d_tube1
from scaffoldmaker.meshtypes.meshtype_3d_tubeseptum1 import MeshType_3d_tubeseptum1
from scaffoldmaker.meshtypes.Meshtype_3d_CollabsedBox1 import MeshType_3d_CollabsedBox1

class Scaffoldmaker(object):

    def __init__(self):
        self._allMeshTypes = [
            MeshType_2d_plate1,
            MeshType_2d_platehole1,
            MeshType_2d_sphere1,
            MeshType_2d_tube1,
            MeshType_3d_box1,
            MeshType_3d_CollabsedBox1,
            MeshType_3d_boxhole1,
            MeshType_3d_heartatria1,
            MeshType_3d_heartventricles1,
            MeshType_3d_heartventricles2,
            MeshType_3d_heartventriclesbase1,
            MeshType_3d_heartventriclesbase2,
            MeshType_3d_sphereshell1,
            MeshType_3d_sphereshellseptum1,
            MeshType_3d_tube1,
            MeshType_3d_tubeseptum1
            ]

    def getMeshTypes(self):
        return self._allMeshTypes

    def getDefaultMeshType(self):
        return MeshType_3d_box1
