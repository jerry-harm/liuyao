from kivy.uix.boxlayout import BoxLayout

KV="""
<TimeWidget>
    orientation: 'vertical'
    Label:
        id: time
        text: "时辰"
    Label:
        id: empty
        text: "旬空"
    BoxLayout:
        orientation: 'horizontal'
        TextInput:
            hint_text: 1999/02/01
"""

class TimeWidget(BoxLayout):
    ...