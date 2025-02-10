import bpy
import mathutils

#モジュールのインポート
from .DrawCollider import DrawCollider
from .stretch_vertex import MYADDON_OT_stretch_vertex
from .create_ico_sphere import MYADDON_OT_create_ico_sphere
from .export_scene import MYADDON_OT_export_scene
from .filename import MYADDON_OT_add_filename
from .filename import OBJECT_PT_file_name
from .collider import MYADDON_OT_add_collider
from .collider import OBJECT_PT_collider
from .disabled import MYADDON_OT_disabled
from .disabled import OBJECT_PT_disabled
from .player_spwan import MYADDON_OT_player_spwan
from .player_spwan import OBJECT_PT_player_spwan
from .enemy_spwan import MYADDON_OT_enemy_spwan
from .enemy_spwan import OBJECT_PT_enemy_spwan

#アドオン情報
bl_info = {
    "name": "レベルエディタ",
    "author": "Kotaro Mizukami",
    "version": (1, 0),
    "blender": (3, 3, 1),
    "location": "",
    "description": "レベルエディタ",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object",
}

#トップバーの拡張メニュー
class TOPBAR_MT_my_menu(bpy.types.Menu):
    #Blenderがクラスを識別するための固有の文字列
    bl_idname = "TOPBAR_MT_my_menu"
    #メニューのラベルとして表示される文字列
    bl_label = "MyMenu"
    #著者表示用の文字列
    bl_description = "拡張メニュー by " + bl_info["author"]

    #サブメニューの描画
    def draw(self, context):
        #トップバーの「エディターメニュー」に項目(オペレータ)を追加
        self.layout.operator(MYADDON_OT_export_scene.bl_idname,text=MYADDON_OT_export_scene.bl_label)
        self.layout.operator(MYADDON_OT_stretch_vertex.bl_idname,text=MYADDON_OT_stretch_vertex.bl_label)
        self.layout.operator(MYADDON_OT_create_ico_sphere.bl_idname,text=MYADDON_OT_create_ico_sphere.bl_label)

    #既存のメニューにサブメニューを追加
    def submenu(self, context):
        #ID指定でサブメニューを追加
        self.layout.menu(TOPBAR_MT_my_menu.bl_idname)

#Blenderに登録するクラスリスト
classes = (
    MYADDON_OT_stretch_vertex,
    MYADDON_OT_create_ico_sphere,
    MYADDON_OT_export_scene,
    TOPBAR_MT_my_menu,
    MYADDON_OT_add_filename,
    OBJECT_PT_file_name,
    MYADDON_OT_add_collider,
    OBJECT_PT_collider,
    MYADDON_OT_disabled,
    OBJECT_PT_disabled,
    MYADDON_OT_player_spwan,
    OBJECT_PT_player_spwan,
    MYADDON_OT_enemy_spwan,
    OBJECT_PT_enemy_spwan
)

#Add-On有効化時のコールバック
def register():
    #Blenderにクラス登録
    for cls in classes:
        bpy.utils.register_class(cls)

    #メニューに項目を追加
    bpy.types.TOPBAR_MT_editor_menus.append(TOPBAR_MT_my_menu.submenu)
    #3Dビューに描画関数を追加
    DrawCollider.handle = bpy.types.SpaceView3D.draw_handler_add(DrawCollider.draw_collider, (), "WINDOW", "POST_VIEW")
    
    print("レベルエディタが有効化されました")
    
#Add-On無効化時のコールバック
def unregister():
    #メニューから項目を削除
    bpy.types.TOPBAR_MT_editor_menus.remove(TOPBAR_MT_my_menu.submenu)
    #3Dビューから描画を削除
    bpy.types.SpaceView3D.draw_handler_remove(DrawCollider.handle, "WINDOW")

    #Blenderからクラスを削除
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
    print("レベルエディタが無効化されました")
    
if __name__ == "__main__":
    register()