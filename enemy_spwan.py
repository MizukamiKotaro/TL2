import bpy

#オペレータ カスタムプロパティ['enemy_spwan']追加
class MYADDON_OT_enemy_spwan(bpy.types.Operator):
    bl_idname = "myaddon.myaddon_ot_enemy_spwan"
    bl_label = "エネミースポーン場所 付与"
    bl_description = "['enemy_spwan']カスタムプロパティを追加します"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        #['enemy_spwan']カスタムプロパティを追加
        context.object["enemy_spwan"] = True
        return {"FINISHED"}
    
#パネル エネミースポーン
class OBJECT_PT_enemy_spwan(bpy.types.Panel):
    """オブジェクトのファイルネームパネル"""
    bl_idname = "OBJECT_PT_enemy_spwan"
    bl_label = "enemy_spwan"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    # サブメニューの描画
    def draw(self, context):
        #パネルに項目を追加
        if "enemy_spwan" in context.object:
            #既にプロパティがあれば、プロパティを表示
            self.layout.prop(context.object, '["enemy_spwan"]', text=self.bl_label)
        else:
            #プロパティがなければ、プロパティ追加ボタンを表示
            self.layout.operator(MYADDON_OT_enemy_spwan.bl_idname)
