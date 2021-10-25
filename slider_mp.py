import matplotlib
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

from multiprocessing import Process, Pipe


matplotlib.use("GTK3Agg")


class SliderMP:
    def __init__(self):
        self._slider_value = {}
        self.sliders = []

        self.parent_conn, self.child_conn = Pipe()
        self.p = Process(target=plt.show)

    def create_slider(self, label: str, initial_value: float, value_step: float, min_value: float, max_value: float):
        if label in self.slider_value.keys():
            raise Exception("The specified label has already been added.")

        ax = plt.axes([0.25, 0.15 + 0.05 * len(self.sliders), 0.65, 0.03], facecolor="gold")

        slider = Slider(
            ax=ax,
            label=label,
            valmin=min_value,
            valmax=max_value,
            valinit=initial_value,
            valstep=value_step
        )

        def on_changed(value):
            self.child_conn.send([label, value])

        slider.on_changed(on_changed)

        self.sliders.append(slider)

        self.slider_value[label] = initial_value

    def show(self):
        self.p.start()

    def update_val(self):
        while self.parent_conn.poll():
            r = self.parent_conn.recv()
            self.slider_value[r[0]] = r[1]

    @property
    def slider_value(self):
        self.update_val()
        return self._slider_value

    @slider_value.setter
    def slider_value(self, arg):
        self._slider_value = arg
