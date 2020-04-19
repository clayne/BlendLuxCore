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
# ##### END GPL LICENSE BLOCK #####

import bpy
from bpy.types import Panel
from os.path import basename, dirname


def draw_panel_categories(self, context):
    scene = context.scene
    ui_props = scene.luxcoreOL.ui

    name = basename(dirname(dirname(__file__)))
    user_preferences = bpy.context.preferences.addons[name].preferences

    layout = self.layout
    layout.separator()
    layout.label(text='Categories')

    col = layout.column(align=True)


def draw_panel_model_search(self, context):
    scene = context.scene
    model_props = scene.luxcoreOL.model
    layout = self.layout
    col = layout.column(align=True)
    col.prop(model_props, "free_only")

    ui_props = scene.luxcoreOL.ui

    if ui_props.assetbar_on:
        icon = 'HIDE_OFF'
        tooltip = 'Click to Hide Asset Bar'
    else:
        icon = 'HIDE_ON'
        tooltip = 'Click to Show Asset Bar'

    assetbar_operator = layout.operator('view3d.luxcore_ol_asset_bar', text='Asset Bar', icon=icon)
    assetbar_operator.keep_running = False
    #assetbar_operator.do_search = False
    assetbar_operator.tooltip = tooltip

    draw_panel_categories(self, context)

    layout.separator()
    layout.label(text='Import method:')
    col = layout.column()
    col.prop(model_props, 'append_method', expand=True, icon_only=False)


class VIEW3D_PT_LUXCORE_ONLINE_LIBRARY(Panel):
    bl_label = "LuxCore Online Library"
    bl_category = "LuxCoreOnlineLibrary"
    #bl_options = {'DEFAULT_CLOSED'}
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_idname = "VIEW3D_PT_LUXCORE_ONLINE_LIBRARY"

    @classmethod
    def poll(cls, context):
        return True

    def draw(self, context):
        scene = context.scene
        ui_props = scene.luxcoreOL.ui

        layout = self.layout
        name = basename(dirname(dirname(__file__)))
        user_preferences = bpy.context.preferences.addons[name].preferences

        #layout.use_property_split = True
        #layout.use_property_decorate = False

        row = layout.row()
        row.scale_x = 1.6
        row.scale_y = 1.6
        row.prop(ui_props, 'asset_type', expand=True, icon_only=True)

        if bpy.data.filepath == '':
            col = layout.column(align=True)
            col.label(text="It's better to save the file first.")

        if ui_props.asset_type == 'MODEL':
            draw_panel_model_search(self, context)
        #elif ui_props.asset_type == 'SCENE':
            #draw_panel_scene_search(self, context)
        #elif ui_props.asset_type == 'MATERIAL':
            #draw_panel_material_search(self, context)
        #elif ui_props.asset_type == 'BRUSH':
            #if context.sculpt_object or context.image_paint_object:
                #draw_panel_brush_search(self, context)
            #else:
                #label_multiline(layout, text='switch to paint or sculpt mode.', width=context.region.width)


class VIEW3D_PT_LUXCORE_ONLINE_LIBRARY_DOWNLOADS(Panel):
    bl_category = "LuxCoreOnlineLibrary"
    bl_idname = "VIEW3D_PT_LUXCORE_ONLINE_LIBRARY_DOWNLOADS"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Downloads"

    @classmethod
    def poll(cls, context):
        #eturn len(download.download_threads) > 0
        return True

    def draw(self, context):
        layout = self.layout
        #TODO
        #for threaddata in download.download_threads:
        #    tcom = threaddata[2]
        #    asset_data = threaddata[1]
        #    row = layout.row()
        #    row.label(text=asset_data['name'])
        #    row.label(text=str(int(tcom.progress)) + ' %')
        #    row.operator('scene.blenderkit_download_kill', text='', icon='CANCEL')
        #    if tcom.passargs.get('retry_counter', 0) > 0:
        #        row = layout.row()
        #        row.label(text='failed. retrying ... ', icon='ERROR')
        #        row.label(text=str(tcom.passargs["retry_counter"]))
        #
        #        layout.separator()