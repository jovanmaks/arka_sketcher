 
import bpy

# Step 1: Property Registration

# Step 2: Panel UI
class SimplePanel(bpy.types.Panel):
    """Creates a Panel in the 3D Viewport UI"""
    bl_label = "Grid Panel"
    bl_idname = "OBJECT_PT_simple"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Arka'

    def draw(self, context):
        layout = self.layout


        row = layout.row()
        row.operator("object.create_grid")

        layout.separator()

        row = layout.row()
        row.prop(context.scene, "grid_width", text="Width (units)")
        row.prop(context.scene, "grid_height", text="Height (units)")
        row.prop(context.scene, "modul", text="Modul")

        layout.separator()

        row = layout.row()
        row.operator("object.place_element")


# Register and Unregister Functions
def register():
    bpy.utils.register_class(SimplePanel)
    bpy.types.Scene.grid_width = bpy.props.IntProperty(name="Grid Width")
    bpy.types.Scene.grid_height = bpy.props.IntProperty(name="Grid Height")
    bpy.types.Scene.modul = bpy.props.IntProperty(name="Modul")

def unregister():
    bpy.utils.unregister_class(SimplePanel)
    del bpy.types.Scene.grid_width
    del bpy.types.Scene.grid_height
    del bpy.types.Scene.modul

if __name__ == "__main__":
    register()