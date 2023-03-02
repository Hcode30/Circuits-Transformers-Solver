from flet import Page, Text, RadioGroup, Radio, ResponsiveRow
from flet import flet, Column, Row, Container, padding, alignment, TextField, MainAxisAlignment, ThemeMode, colors
from flet import Divider, ElevatedButton, ScrollMode, SnackBar, TextAlign, FontWeight, Theme
from math import acos, cos, sin, sqrt, pi
from numpy import angle

"""
    Made By Hazem Ahmed ==> HCode
    Github Link: https://github.com/Hcode30
    Copyrights © 2023 Hcode
"""


def main(page: Page):
    def radtodegree(radians):
        degrees = radians * (180.0 / pi)
        return degrees

    def degreetorad(degrees):
        radians = degrees * (pi / 180.0)
        return radians

    def close(num):
        if type(num) == complex:
            return "%(re).2f + %(im).1fj" % {"re": num.real, "im": num.imag}
        else:
            num = "%.3f" % num
            num = float(num)
            if num - int(num) == 0:
                return int(num)
            else:
                return num

    def close2(num):
        num = "%.2f" % num
        num = float(num)
        if num - int(num) == 0:
            return int(num)
        else:
            return num

    def close1(num):
        if type(num) == complex:
            return "%(re).1f + %(im).1fj" % {"re": num.real, "im": num.imag}
        else:
            num = "%.1f" % num
            num = float(num)
            if num - int(num) == 0:
                return int(num)
            else:
                return num

    page.snack_bar = SnackBar(
        content=Text("Made By HCode \nGithub Link: https://github.com/Hcode30",
                     selectable=True, weight=FontWeight.W_700, text_align='center'),
    )

    page.theme_mode = ThemeMode.DARK

    def change_theme(e):
        if page.theme_mode == ThemeMode.LIGHT:
            page.theme_mode = ThemeMode.DARK
            page.update()
        elif page.theme_mode == ThemeMode.DARK:
            page.theme_mode = ThemeMode.LIGHT
            page.update()

    def show_credits(e):
        page.snack_bar.open = True
        page.update()
    credit = Container(Row([ElevatedButton(
        "Credits", on_click=show_credits, tooltip="Show The Developer's Info", icon='INFO'),
        ElevatedButton("Change Theme", icon='DARK_MODE', tooltip='Switch Between Light And Dark Theme', on_click=change_theme)], alignment='center'))
    page.add(credit)

    def movetonext1(e):
        occ.focus()

    def movetonext2(e):
        nlp.focus()

    def movetonext3(e):
        scc.focus()

    def movetonext4(e):
        scp.focus()

    def movetonext5(e):
        N1.focus()

    def movetonext6(e):
        N2.focus()

    def movetonext7(e):
        flv.focus()

    def movetonext8(e):
        flp.focus()

    def movetonext9(e):
        flt.focus()

    def movetonext10(e):
        xt.focus()

    ####################################################
    ocv = TextField(label="Open Circuit Voltage", text_align=TextAlign.CENTER, suffix_text="V",  col={
                    "sm": 4}, keyboard_type='number', on_submit=movetonext1)
    occ = TextField(label="Open Circuit Current", text_align=TextAlign.CENTER, suffix_text="A",  col={
                    "sm": 4}, keyboard_type='number', on_submit=movetonext2)
    nlp = TextField(label="No Load Power", text_align=TextAlign.CENTER, suffix_text="W",
                    col={"sm": 4})
    ####################################################
    scv = TextField(label="Short Circuit Voltage", text_align=TextAlign.CENTER, suffix_text="V", col={
        "sm": 4}, keyboard_type='number', on_submit=movetonext3)
    scc = TextField(label="Short Circuit Current", text_align=TextAlign.CENTER, suffix_text="A", col={
        "sm": 4}, keyboard_type='number', on_submit=movetonext4)
    scp = TextField(label="Short Circuit Power", text_align=TextAlign.CENTER, suffix_text="W",
                    col={"sm": 4})
    ####################################################

    kva = TextField(label="Transformer kVA", suffix_text="kVA", on_submit=movetonext5,
                    text_align=TextAlign.CENTER, width=150, text_size=21)
    N1 = TextField(text_align=TextAlign.CENTER, on_submit=movetonext6,
                   label='N1', width=100, text_size=20)
    N2 = TextField(text_align=TextAlign.CENTER, on_submit=movetonext7,
                   label='N2', width=100, text_size=20)
    flv = TextField(label="Load Voltage", text_align=TextAlign.CENTER, suffix_text="V", col={
        "sm": 4}, keyboard_type='number', on_submit=movetonext8)
    flp = TextField(label="Power Factor", text_align=TextAlign.CENTER, col={
        "sm": 4}, keyboard_type='number', on_submit=movetonext9)
    flt = TextField(label="Type", on_submit=movetonext10,
                    hint_text="lag or lead or unity", text_align=TextAlign.CENTER, col={"sm": 4})
    xt = TextField(label="X", text_align=TextAlign.CENTER, col={
        "sm": 4}, keyboard_type='number')

    ####################################################
    phy = 0
    page.title = "Transformer Solver"
    page.window_width = 600
    page.window_min_width = 600
    page.window_max_width = 1200
    page.window_height = 800
    page.window_min_height = 600

    def nlb_clicked(g):
        if ocv.value == '':
            ocv.focus()
        elif occ.value == '':
            occ.focus()
        elif nlp.value == '':
            nlp.focus()
        else:
            if ResContainer.content != None:
                page.remove(ResContainer)
                ResContainer.content = None
                col1.controls.clear()
                col2.controls.clear()
                col3.controls.clear()
                col4.controls.clear()
                col5.controls.clear()
            ResContainer.content = ResContainer1
            page.add(ResContainer)
            row = Row([col1, col2])
            row.alignment = MainAxisAlignment.SPACE_EVENLY
            ResContainer1.content = row
            ResContainer1.bgcolor = colors.AMBER
            costheta = float(nlp.value)/(float(ocv.value)*float(occ.value))
            theta = radtodegree(acos(costheta))
            Ic = close(float(occ.value)*costheta)
            Im = close(float(occ.value)*sin((degreetorad(theta))))
            Rc = close((float(ocv.value)/Ic))
            Xm = close((float(ocv.value)/Im))
            col1.controls.append(
                Text(f"cos(α) = {costheta}",
                     size=30, color=colors.BLACK, weight=FontWeight.BOLD, selectable=True),
            )
            col2.controls.append(
                Text(f"α = {close(theta)}°",
                     size=30, color=colors.BLACK, weight=FontWeight.BOLD, selectable=True),
            )
            col1.controls.append(
                Text(f"Ic = {Ic} A",
                     size=30, color=colors.BLACK, weight=FontWeight.BOLD, selectable=True),
            )
            col2.controls.append(
                Text(f"Im = {Im} A",
                     size=30, color=colors.BLACK, weight=FontWeight.BOLD, selectable=True),
            )
            col1.controls.append(
                Text(f"Rc = {Rc} Ω",
                     size=30, color=colors.BLACK, weight=FontWeight.BOLD, selectable=True),
            )
            col2.controls.append(
                Text(f"Xm = {Xm} Ω",
                     size=30, color=colors.BLACK, weight=FontWeight.BOLD, selectable=True),
            )

            page.update()

    def scb_clicked(g):
        if scv.value == '':
            scv.focus()
        elif scc.value == '':
            scc.focus()
        elif scp.value == '':
            scp.focus()
        else:
            if ResContainer.content != None:
                page.remove(ResContainer)
                ResContainer.content = None
                col1.controls.clear()
                col2.controls.clear()
                col3.controls.clear()
                col4.controls.clear()
                col5.controls.clear()
            ResContainer.content = ResContainer2
            page.add(ResContainer)
            row = Row([col3])
            row.alignment = MainAxisAlignment.SPACE_EVENLY
            ResContainer2.content = row
            ResContainer2.bgcolor = colors.GREEN
            Req1 = close(float(scp.value)/(float(scc.value)**2))
            Zeq1 = close(float(scv.value)/(float(scc.value)))
            Xeq1 = close(sqrt((Zeq1)**2-(Req1)**2))

            col3.controls.append(
                Text(f"Req1 = {Req1} Ω",
                     size=30, color=colors.BLACK, weight=FontWeight.BOLD, selectable=True),
            )
            col3.controls.append(
                Text(f"Zeq1 = {Zeq1} Ω",
                     size=30, color=colors.BLACK, weight=FontWeight.BOLD, selectable=True),
            )

            col3.controls.append(
                Text(f"Xeq1 = {Xeq1} Ω",
                     size=30, color=colors.BLACK, weight=FontWeight.BOLD, selectable=True),
            )

            page.update()

    def flb_clicked(g):
        if kva.value == '':
            kva.focus()
        elif N1.value == '':
            N1.focus()
        elif N2.value == '':
            N2.focus()
        elif flv.value == '':
            flv.focus()
        elif flp.value == '':
            flp.focus()
        elif flt.value.lower() not in ['lead', 'lag', 'unity']:
            flt.focus()
        elif xt.value == '':
            xt.focus()
        elif ocv.value == '' or occ.value == '' or nlp.value == '':
            MyRadioGroup.value = 'nlt'
            if UltimateContainer.content != None:
                page.remove(UltimateContainer)
            if ResContainer.content != None:
                page.remove(ResContainer)
                col1.controls.clear()
                col2.controls.clear()
                col3.controls.clear()
                col4.controls.clear()
                col5.controls.clear()
            ResContainer1.bgcolor = colors.TRANSPARENT
            UltimateContainer.content = nltContainer
            page.add(UltimateContainer)
            ResContainer.content = ResContainer3
            ResContainer1.update()
            page.add(ResContainer)
        elif scv.value == '' or scc.value == '' or scp.value == '':
            MyRadioGroup.value = 'sct'
            if UltimateContainer.content != None:
                page.remove(UltimateContainer)
            if ResContainer.content != None:
                page.remove(ResContainer)
                ResContainer.content = None
                col1.controls.clear()
                col2.controls.clear()
                col3.controls.clear()
                col4.controls.clear()
                col5.controls.clear()
            ResContainer2.bgcolor = colors.TRANSPARENT
            UltimateContainer.content = sctContainer
            page.add(UltimateContainer)
            ResContainer.content = ResContainer2
            page.add(ResContainer)
        else:
            if ResContainer.content != None:
                page.remove(ResContainer)
                ResContainer.content = None
                col1.controls.clear()
                col2.controls.clear()
                col3.controls.clear()
                col4.controls.clear()
                col5.controls.clear()
            ResContainer.content = ResContainer3
            page.add(ResContainer)
            row = Row([col4, col5])
            row.alignment = MainAxisAlignment.SPACE_EVENLY
            ResContainer3.content = row
            ResContainer3.bgcolor = colors.CYAN
            ######################################################
            tf = float(kva.value)*1000
            ratio = float(N1.value)/float(N2.value)
            Req1 = float(scp.value)/(float(scc.value)**2)
            Zeq1 = float(scv.value)/(float(scc.value))
            Xeq1 = sqrt((Zeq1)**2-(Req1)**2)
            pf = float(flp.value)
            v2 = float(flv.value)
            X = float(xt.value)
            v2r = v2*ratio
            if flt.value.lower() == 'lag':
                theta = radtodegree(-acos(pf))
            elif flt.value.lower() == 'lead':
                theta = radtodegree(acos(pf))
            elif flt.value.lower() == 'unity':
                theta = 0
            x = close(tf/v2r)
            y = theta
            i2rl = [x*cos(degreetorad(y)), x*sin(degreetorad(y))*1j]
            zeq1l = [Req1, Xeq1*1j]
            i2r = x*cos(degreetorad(y))+x*sin(degreetorad(y))*1j
            zeq1 = Req1 + Xeq1*1j
            v1 = v2r+(i2r*zeq1)
            vangle = close(angle(v1, deg=True))
            vmag = close1(abs(v1))
            vr = (abs(vmag)-abs(v2r))/(abs(v2r))
            pc = float(nlp.value)
            pcu = x**2*Req1
            pout = tf*cos(degreetorad(theta))
            n = ((X*pout)/(X*pout+pc+(X**2)*pcu))*100
            nn = float("%.2f" % float(n))

            ######################################################
            col4.controls.append(
                Text(f"I = {x}∠{close(y)}° A", weight=FontWeight.BOLD, selectable=True,
                     size=30, color=colors.BLACK),
            )
            col4.controls.append(
                Text(f"V1 = {vmag}∠{vangle}° V", weight=FontWeight.BOLD, selectable=True,
                     size=30, color=colors.BLACK),
            )

            col5.controls.append(
                Text(f"%VR= {close(vr*100)}%", weight=FontWeight.BOLD, selectable=True,
                     size=30, color=colors.BLACK),
            )

            col5.controls.append(
                Text(f"%η = {close(nn)}% ", weight=FontWeight.BOLD, selectable=True,
                     size=30, color=colors.BLACK),
            )

            page.update()

    ###############################################
    ResContainer = Container()
    ###############################################
    col1 = Column()
    col2 = Column()
    ResContainer1 = Container(alignment=alignment.center, bgcolor=colors.AMBER,
                              border_radius=30, padding=padding.only(bottom=25, top=25))
    ###############################################
    col3 = Column()
    ResContainer2 = Container(alignment=alignment.center, bgcolor=colors.GREEN,
                              border_radius=30, padding=padding.only(bottom=25, top=25))
    ###############################################
    col4 = Column()
    col5 = Column()
    ResContainer3 = Container(alignment=alignment.center, bgcolor=colors.CYAN,
                              border_radius=30, padding=padding.only(bottom=25, top=25))
    ###############################################
    nlb = ElevatedButton(text="Results",
                         on_click=nlb_clicked, icon='OUTPUT')
    scb = ElevatedButton(text="Results",
                         on_click=scb_clicked, icon='OUTPUT')
    flb = ElevatedButton(text="Results",
                         on_click=flb_clicked, icon='OUTPUT')
    ###############################################

    def radiogroup_changed(s):
        if s.control.value == 'nlt':
            if UltimateContainer.content != None:
                page.remove(UltimateContainer)
            if ResContainer.content != None:
                page.remove(ResContainer)
                col1.controls.clear()
                col2.controls.clear()
                col3.controls.clear()
                col4.controls.clear()
                col5.controls.clear()
            ResContainer1.bgcolor = colors.TRANSPARENT
            UltimateContainer.content = nltContainer
            page.add(UltimateContainer)
            ResContainer.content = ResContainer1
            page.add(ResContainer)
        elif s.control.value == 'sct':
            if UltimateContainer.content != None:
                page.remove(UltimateContainer)
            if ResContainer.content != None:
                page.remove(ResContainer)
                ResContainer.content = None
                col1.controls.clear()
                col2.controls.clear()
                col3.controls.clear()
                col4.controls.clear()
                col5.controls.clear()
            ResContainer2.bgcolor = colors.TRANSPARENT
            UltimateContainer.content = sctContainer
            page.add(UltimateContainer)
            ResContainer.content = ResContainer2
            page.add(ResContainer)
        elif s.control.value == 'flt':
            if UltimateContainer.content != None:
                page.remove(UltimateContainer)
            if ResContainer.content != None:
                page.remove(ResContainer)
                ResContainer.content = None
                col1.controls.clear()
                col2.controls.clear()
                col3.controls.clear()
                col4.controls.clear()
                col5.controls.clear()
            ResContainer3.bgcolor = colors.TRANSPARENT
            UltimateContainer.content = fltContainer
            page.add(UltimateContainer)
            ResContainer.content = ResContainer3
            page.add(ResContainer)
        page.update()

    def page_resize(e):
        page.update()

    nltContainer = Container(Column([ResponsiveRow(
        [
            ocv,
            occ,
            nlp
        ],
        run_spacing={"xs": 10},
    ),
        Divider(height=9, thickness=3), Row([nlb], alignment="center"), Divider(height=9, thickness=3)], spacing=10, scroll=ScrollMode.AUTO, auto_scroll=True,

    ),
    )

    sctContainer = Container(Column([ResponsiveRow(
        [
            scv,
            scc,
            scp
        ],
        run_spacing={"xs": 10},
    ),
        Divider(height=9, thickness=3), Row([scb], alignment="center"), Divider(height=9, thickness=3)], spacing=10, scroll=ScrollMode.AUTO, auto_scroll=True
    ))

    fltContainer = Container(Column([Row(
        [
            kva, Text(value="Voltage Ratio", size=21), N1, Text(value='/', size=26), N2],
        alignment="center",
    ),
        ResponsiveRow(
        [
            flv,
            flp,
        ], run_spacing={"xs": 10}, alignment='center'
    ),
        ResponsiveRow(
        [
            flt,
            xt
        ],
        run_spacing={"xs": 10}, alignment='center'
    ),
        Divider(height=9, thickness=3), Row([flb], alignment="center"), Divider(height=9, thickness=3)], spacing=10, scroll=ScrollMode.AUTO, auto_scroll=True
    ))
    page.on_resize = page_resize
    MyRadios = Container(
        content=Row([
            Radio(value="nlt", label="No Load", width=200, col={"sm": 3}),
            Radio(value="sct", label="Short Circuit",
                  width=200, col={"sm": 3}),
            Radio(value="flt", label="Full Load", width=200, col={"sm": 3})],
            alignment="center"))
    MyRadioGroup = RadioGroup(content=MyRadios,
                              on_change=radiogroup_changed)
    page.add(

        Divider(height=9, thickness=3),
        Container(
            Text(value='Test Types', size=30,
                 weight=FontWeight.W_600),
            alignment=alignment.center,
        ),
        Divider(height=9, thickness=3),
        Container(alignment=alignment.center, content=MyRadioGroup,
                  ), Divider(height=9, thickness=3)
    )

    UltimateContainer = Container()

    page.update()


if __name__ == "__main__":
    flet.app(target=main, assets_dir="assets")
