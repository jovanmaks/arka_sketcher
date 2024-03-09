 
import bpy

class SimplePropertyGroup(bpy.types.PropertyGroup):
    my_string: bpy.props.StringProperty(
        name="Enter Something",
        description=":",
        default="",
        maxlen=1024,
    )
