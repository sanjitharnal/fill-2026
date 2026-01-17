from pybricks.tools import hub_menu
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button,Color

hub = PrimeHub()

selected = hub_menu("1","2","3","4","5","6")
hub.system.set_stop_button(Button.CENTER)

hub.light.on(Color.BLUE)

if selected == "1":
    import blueside_run1
elif selected == "2":
    import blueside_run2
elif selected == "3":
    import redside_run1
elif selected =="4":
    import redside_run2
elif selected == "5":
    import redside_run3
elif selected == "6":
    import blueside_run3