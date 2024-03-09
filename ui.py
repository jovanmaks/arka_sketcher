 
import bpy


element_items = [
    ('BNF', "Wall", "PackingBin.BNF"),
    ('BFF', "Window", "PackingBin.BFF"),
    ('BBF', "Door", "PackingBin.BBF"),
]


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

        layout.separator()


        # Dropdown for mode
        row = layout.row()
        row.prop(context.scene, "element", text="Element")

        layout.separator()
        row = layout.row()
        row.operator("object.evaluate_space")


        layout.separator()
        row = layout.row()
        row.operator("object.import_space")
        row.operator("object.export_space")

# Register and Unregister Functions
def register():
    bpy.utils.register_class(SimplePanel)
    bpy.types.Scene.grid_width = bpy.props.IntProperty(name="Grid Width")
    bpy.types.Scene.grid_height = bpy.props.IntProperty(name="Grid Height")
    bpy.types.Scene.modul = bpy.props.IntProperty(name="Modul")

    bpy.types.Scene.element = bpy.props.EnumProperty(items=element_items)

def unregister():
    bpy.utils.unregister_class(SimplePanel)
    del bpy.types.Scene.grid_width
    del bpy.types.Scene.grid_height
    del bpy.types.Scene.modul

    del bpy.types.Scene.element

if __name__ == "__main__":
    register()