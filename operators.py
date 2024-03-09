 
import bpy

class createGrid(bpy.types.Operator):
    """Create a grid """
    bl_idname = "object.create_grid"
    bl_label = "Grid"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add(size=2)
        return {'FINISHED'}


class placeElement(bpy.types.Operator):
    """Place the element """
    bl_idname = "object.place_element"
    bl_label = "Element"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add(size=2)
        return {'FINISHED'}



def register():
    bpy.utils.register_class(createGrid)
    bpy.utils.register_class(placeElement)

def unregister():
    bpy.utils.unregister_class(createGrid)
    bpy.utils.unregister_class(placeElement)