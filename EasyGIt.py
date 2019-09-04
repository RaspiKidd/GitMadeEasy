# Python application to make GitHub easy for children to use
# By RaspiKidd Vesrion 0.00

from guizero import App, Text, PushButton

app = App(title="EasyGit")
intro = Text(app, text="GitHub made easy")
clone = PushButton(app, text='Clone')

app.display()
