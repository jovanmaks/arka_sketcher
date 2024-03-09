 
import bpy

class SimplePanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Simple Panel"
    bl_idname = "OBJECT_PT_simple"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_simple_properties

        layout.operator("object.simple_operator")
        layout.prop(mytool, "my_string")
