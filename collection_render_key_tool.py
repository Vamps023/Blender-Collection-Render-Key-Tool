bl_info = {
    "name": "Collection Render Key Tool",
    "author": "Swapnil",
    "version": (1, 1),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > Render Keys",
    "description": "Set or clear render visibility keys for all objects in a collection",
    "category": "Animation",
}

import bpy


# -------------------------------------------------
# Get objects from selected collection
# -------------------------------------------------
def get_collection_objects(context):
    col = context.scene.key_collection
    if col:
        return col.objects
    return []


# -------------------------------------------------
# Set Render Key
# -------------------------------------------------
class OBJECT_OT_collection_set_key(bpy.types.Operator):
    bl_idname = "object.collection_set_key"
    bl_label = "Set Render Key"
    bl_description = "Add render visibility keyframe to all objects in the collection"

    def execute(self, context):

        objs = get_collection_objects(context)
        frame = context.scene.frame_current

        for obj in objs:
            obj.keyframe_insert(data_path="hide_render", frame=frame)

        self.report({'INFO'}, f"Key added to {len(objs)} objects")

        return {'FINISHED'}


# -------------------------------------------------
# Clear Render Keys
# -------------------------------------------------
class OBJECT_OT_collection_clear_key(bpy.types.Operator):
    bl_idname = "object.collection_clear_key"
    bl_label = "Clear Render Keys"
    bl_description = "Remove render visibility animation from collection objects"

    def execute(self, context):

        objs = get_collection_objects(context)
        removed = 0

        for obj in objs:

            if obj.animation_data and obj.animation_data.action:

                action = obj.animation_data.action

                for fcurve in list(action.fcurves):

                    if fcurve.data_path == "hide_render":
                        action.fcurves.remove(fcurve)
                        removed += 1

        self.report({'INFO'}, f"Removed keys from {removed} objects")

        return {'FINISHED'}


# -------------------------------------------------
# Render Enable
# -------------------------------------------------
class OBJECT_OT_collection_render_on(bpy.types.Operator):
    bl_idname = "object.collection_render_on"
    bl_label = "Render Enable"

    def execute(self, context):

        objs = get_collection_objects(context)

        for obj in objs:
            obj.hide_render = False

        self.report({'INFO'}, "Render enabled")

        return {'FINISHED'}


# -------------------------------------------------
# Render Disable
# -------------------------------------------------
class OBJECT_OT_collection_render_off(bpy.types.Operator):
    bl_idname = "object.collection_render_off"
    bl_label = "Render Disable"

    def execute(self, context):

        objs = get_collection_objects(context)

        for obj in objs:
            obj.hide_render = True

        self.report({'INFO'}, "Render disabled")

        return {'FINISHED'}


# -------------------------------------------------
# UI Panel
# -------------------------------------------------
class VIEW3D_PT_collection_render_keys(bpy.types.Panel):
    bl_label = "Collection Render Tool"
    bl_idname = "VIEW3D_PT_collection_render_keys"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Render Keys"

    def draw(self, context):

        layout = self.layout

        layout.label(text="Select Collection")

        layout.prop(context.scene, "key_collection")

        layout.separator()

        layout.label(text="Keyframe")

        layout.operator("object.collection_set_key", icon='KEY_HLT')
        layout.operator("object.collection_clear_key", icon='TRASH')

        layout.separator()

        layout.label(text="Render Control")

        layout.operator("object.collection_render_on", icon='RESTRICT_RENDER_OFF')
        layout.operator("object.collection_render_off", icon='RESTRICT_RENDER_ON')


# -------------------------------------------------
# Register
# -------------------------------------------------
classes = (
    OBJECT_OT_collection_set_key,
    OBJECT_OT_collection_clear_key,
    OBJECT_OT_collection_render_on,
    OBJECT_OT_collection_render_off,
    VIEW3D_PT_collection_render_keys,
)


def register():

    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.key_collection = bpy.props.PointerProperty(
        name="Collection",
        type=bpy.types.Collection
    )


def unregister():

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.key_collection


if __name__ == "__main__":
    register()