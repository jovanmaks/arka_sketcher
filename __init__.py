bl_info = {
    "name": "Arka",
    "description": "Plugin for making floorplans",
    "author": "Noah",
    "version": (1, 0),
    "blender": (4, 0, 2),
    "location": "Properties > Render > My Awesome Panel",
    "support": "COMMUNITY",
    "category": "Organization"
}

import bpy
from . import operators, ui, properties

def register():
    operators.register()
    ui.register()
    properties.register()

def unregister():
    operators.unregister()
    ui.unregister()
    properties.unregister()



if __name__ == "__main__":
    register()
