import justpy as jp
import definition
from webapp import layout
from webapp import page


class Dictionary(page.Page):
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes='bg-gray-300 h-screen')
        jp.Div(a=div, text="Instant English Dictionary", classes='text-4xl m2')
        jp.Div(a=div, text="Get the definition of any English word instantly as you type!",
               classes='text-lg')

        input_div = jp.Div(a=div, classes='grid grid-cols-2')

        output_div = jp.Div(a=div, classes='m-2 p-2 text-lg border-4 h-60')

        input_box = jp.Input(a=input_div, placeholder="Type a word here", outputdiv=output_div,
                             classes='m2 bg-gray-200 border-2 border-blue-400 rounded w-64 focus:outline-none '
                                     'focus:border-purple-500 focus:bg-white py-2 px-4')
        input_box.on('click', cls.get_definition)
        return wp

    @staticmethod
    def get_definition(widget, msg):
        defined = definition.Definition(widget.value).get()
        widget.outputdiv.text = " ".join(defined)
