 
import bpy

class SimpleOperator(bpy.types.Operator):
    """My Simple Operator"""
    bl_idname = "object.simple_operator"
    bl_label = "Simple Operator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add(size=2)
        return {'FINISHED'}
