import bpy

#オペレータ カスタムプロパティ['player_spwan']追加
class MYADDON_OT_player_spwan(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_player_spwan"
    bl_label = "プレイヤースポーン場所 付与"
    bl_description = "['dplayer_spwan']カスタムプロパティを追加します"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        #['player_spwan']カスタムプロパティを追加
        context.object["player_spwan"] = True
        return {"FINISHED"}
    
#パネル プレイヤースポーン
class OBJECT_PT_player_spwan(bpy.types.Panel):
    """オブジェクトのファイルネームパネル"""
    bl_idname = "OBJECT_PT_player_spwan"
    bl_label = "player_spwan"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    # サブメニューの描画
    def draw(self, context):
        #パネルに項目を追加
        if "player_spwan" in context.object:
            #既にプロパティがあれば、プロパティを表示
            self.layout.prop(context.object, '["player_spwan"]', text=self.bl_label)
        else:
            #プロパティがなければ、プロパティ追加ボタンを表示
            self.layout.operator(MYADDON_OT_player_spwan.bl_idname)
