 
import bpy

# Step 1: Property Registration
def register_properties():
    bpy.types.Scene.my_width = bpy.props.IntProperty(name="Width")
    bpy.types.Scene.my_height = bpy.props.IntProperty(name="Height")
    bpy.types.Scene.my_module = bpy.props.FloatProperty(name="Module")

def unregister_properties():
    del bpy.types.Scene.my_width
    del bpy.types.Scene.my_height
    del bpy.types.Scene.my_module

# Step 2: Panel UI
class SimplePanel(bpy.types.Panel):
    """Creates a Panel in the 3D Viewport UI"""
    bl_label = "Simple Panel"
    bl_idname = "OBJECT_PT_simple"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Arka'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Your existing operator/button
        layout.operator("object.simple_operator")

        # Additional UI elements for width, height, and module
        layout.prop(scene, "my_width", text="Width")
        layout.prop(scene, "my_height", text="Height")
        layout.prop(scene, "my_module", text="Module")

# Assuming you already have a SimpleOperator class or similar for handling the button action

# Register and Unregister Functions
def register():
    bpy.utils.register_class(SimplePanel)
    register_properties()

def unregister():
    bpy.utils.unregister_class(SimplePanel)
    unregister_properties()

if __name__ == "__main__":
    register()