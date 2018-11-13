# 如何控制实习生用户只能看到自己的记录，但是管理者却可以看到所有的实习生信息
```
<field name="domain">[('user_id','=',uid)]</field>
```
# 获取当前用户的ID
```
current_user = fields.Many2one('res.users','Current User', default=lambda self: self.env.user)
```

#form 表单中加条件，让form表单在某个状态时不可编辑
```
<form string="Listado de Hello" attrs="{edit:'false':[('state','in','confirmed')]}">
```

# 重写model 中的 fields_view_get 方法
fields_view_get 方法会在view视图加载到屏幕上时执行
```
@api.model
def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):

    res = super(Entity, self).fields_view_get(view_id=view_id, view_type=view_type, context=context, toolbar=toolbar, submenu=submenu)
    doc = etree.XML(res['arch'])
    if view_type == 'form' and [some_condition]:
        for node_form in doc.xpath("//form"):

            node_form.set("create", 'false')
            res['arch'] = etree.tostring(doc)
    return res
```
# 根据条件设置 form 表单中的字段 为只读
`<field name="your_field" attrs="{'readonly':[('state ', '!=', 'waiting')]}" />`

```
    <record model="ir.rule" id="user_edit_own_trainee_rule">
            <field name="name">hr.trainee.rule</field>
            <field name="model_id" ref="model_hr_trainee"/>
            <field name="perm_read" eval="False"/>
            <field name="domain_force">[('user_id','=',user.id)]</field>
            <field name="groups" eval="[(4,ref('group_user'))]"/>
   </record>
```

# case 让带教老师能看到自己的实习生信息