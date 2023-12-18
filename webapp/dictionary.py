import justpy as jp
import definition


class Dictionary:
    path = "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes='bg-gray-300 h-screen')
        jp.Div(a=div, text="Instant English Dictionary", classes='text-4xl m2')
        jp.Div(a=div, text="Get the definition of any English word instantly as you type!",
               classes='text-lg')

        input_div = jp.Div(a=div, classes='grid grid-cols-2')

        output_div = jp.Div(a=div, classes='m-2 p-2 text-lg border-2 h-40')

        input_box = jp.Input(a=input_div, placeholder="Type a word here", outputdiv=output_div,
                             classes='m2 bg-gray-100 border-2 border-gray-200 rounded w-64 focus:outline-non '
                                     'focus:border-purple-500 focus:bg-white py-2 px-4')
        input_box.on('click', cls.get_definition)
        return wp

    @staticmethod
    def get_definition(widget, msg):
        defined = definition.Definition(widget.value).get()
        widget.outputdiv.text = " ".join(defined)
