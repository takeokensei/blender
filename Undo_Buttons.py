# 3D NAVIGATION TOOLBAR v1.2 - 3Dview Addon - Blender 2.5x
#
# THIS SCRIPT IS LICENSED UNDER GPL, 
# please read the license block.
#
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK ####

bl_info = {
    "name": "Undo Panel",
    "author": "Takeo, Kensei",
    "version": (1, 0),
    "blender": (2, 6, 0),
    "location": "View3D > Tool Shelf > 3D Nav",
    "description": "Add Undo/Redo/Undo history buttons to the tool shelf",
    "warning": "",
    "wiki_url": ""\
        "Scripts/3D_interaction/3D_Navigation",
    "tracker_url": ""\
	    "",
    "category": "3D View"}


import bpy

class VIEW3D_PT_UndoPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_label = "Undo Panel"

    def draw(self, context):
        layout = self.layout
        view = context.space_data

        col = layout.column(align=True)
        row = col.row()
        row.operator("ed.undo", text="Undo")
        row.operator("ed.redo", text="Redo")
        col.operator("ed.undo_history", text="Undo_history")

# register the class
def register():
    bpy.utils.register_module(__name__)
 
    pass 

def unregister():
    bpy.utils.unregister_module(__name__)
 
    pass 

if __name__ == "__main__": 
    register()
