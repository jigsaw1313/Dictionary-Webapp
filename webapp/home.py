import justpy as jp


class Home:
    path="/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)


        drawer = jp.QDrawer(a=layout, show_if_above=True, v_mode="Left",
                            bordered=True)
        scroller = jp.QScrollArea(a=drawer, classes='fit')
        qlist = jp.QList(a=scroller)
        a_classes = "p-2 m-2 text-lg text-blu-400 hover:text-blue-700"
        jp.A(a=qlist, text="Home", href="/home", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="/dictionary", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes=a_classes)
        jp.Br(a=qlist)


        jp.QBtn(a=toolbar, dense=True, flate=True, round=True, icon='menu',
                click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

        container = jp.QPageContainer(a=layout)

        div = jp.Div(a=container, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text="This is the HOME Page", classes='text-4xl m2')
        jp.Div(a=div, text="Some Text", classes="text-lg")

        return wp

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True

