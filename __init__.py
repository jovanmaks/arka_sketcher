 
bl_info = {
    "name": "Arka_Sketcher",
    "description": "Plugin for making floorplans",
    "author": "Noah",
    "version": (1, 0),
    "blender": (3, 6, 4),
    "location": "Properties > Render > My Awesome Panel",
    "support": "COMMUNITY",
    "category": "Organization"
}

import bpy
from . import operators, ui, properties

def register():
    bpy.utils.register_class(operators.SimpleOperator)
    bpy.utils.register_class(ui.SimplePanel)
    bpy.utils.register_class(properties.SimplePropertyGroup)
    bpy.types.Scene.my_simple_properties = bpy.props.PointerProperty(type=properties.SimplePropertyGroup)

def unregister():
    bpy.utils.unregister_class(operators.SimpleOperator)
    bpy.utils.unregister_class(ui.SimplePanel)
    bpy.utils.unregister_class(properties.SimplePropertyGroup)
    del bpy.types.Scene.my_simple_properties

if __name__ == "__main__":
    register()
