 
import bpy
import bmesh
import mathutils  # Add this import




class createGrid(bpy.types.Operator):
    """Create a grid of tiles, each with an initial unique black material and a small offset between tiles"""
    bl_idname = "object.create_grid"
    bl_label = "Create Grid"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Clear existing mesh objects
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_by_type(type='MESH')
        bpy.ops.object.delete()

        # Retrieve the grid properties
        grid_width = context.scene.grid_width
        grid_height = context.scene.grid_height
        modul = context.scene.modul
        offset = 0.01  # Offset between tiles in meters

        for x in range(grid_width):
            for y in range(grid_height):
                # Calculate the center position of the tile, including the offset
                x_pos = (x * (modul + offset)) + (modul / 2) - ((grid_width * (modul + offset)) / 2)
                y_pos = (y * (modul + offset)) + (modul / 2) - ((grid_height * (modul + offset)) / 2)

                # Create a new mesh for each tile
                bpy.ops.mesh.primitive_plane_add(size=modul, location=(x_pos, y_pos, 0))

                # Create a new unique black material for each tile
                black_material = bpy.data.materials.new(name=f"BlackMaterial_{x}_{y}")
                black_material.use_nodes = True
                bsdf = black_material.node_tree.nodes.get('Principled BSDF')
                if bsdf is not None:
                    bsdf.inputs['Base Color'].default_value = (0, 0, 0, 1)  # Set the color to black

                # Assign the unique black material to the new tile
                tile_object = bpy.context.object
                tile_object.data.materials.append(black_material)

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