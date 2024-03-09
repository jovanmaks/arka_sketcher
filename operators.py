 
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



class evaluateSpace(bpy.types.Operator):
    """Evaluate the space"""
    bl_idname = "object.evaluate_space"
    bl_label = "Evaluate"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add(size=2)
        return {'FINISHED'}


class importSpace(bpy.types.Operator):
    """Import the space"""
    bl_idname = "object.import_space"
    bl_label = "Import"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add(size=2)
        return {'FINISHED'}

class exportSpace(bpy.types.Operator):
    """Evaluate the space"""
    bl_idname = "object.export_space"
    bl_label = "Export"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add(size=2)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(createGrid)
    bpy.utils.register_class(placeElement)
    bpy.utils.register_class(evaluateSpace)
    bpy.utils.register_class(importSpace)
    bpy.utils.register_class(exportSpace)

def unregister():
    bpy.utils.unregister_class(createGrid)
    bpy.utils.unregister_class(placeElement)
    bpy.utils.unregister_class(evaluateSpace)
    bpy.utils.unregister_class(importSpace)
    bpy.utils.unregister_class(exportSpace)