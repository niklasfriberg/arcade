import arcade
import pyglet

from arcade.math import Mat4


def test_window(window: arcade.Window):
    width = window.width
    height = window.height
    title = "Window Test"
    window.set_caption(title)

    arcade.set_background_color(arcade.color.AMAZON)
    w = arcade.get_window()
    assert w is not None

    # NOTE: Window managers can enforce difference sizes
    # Make sure the arguments get passed to the window
    # assert w.width == width
    # assert w.height == height

    assert w.caption == title
    assert w.resizeable is False
    assert w.current_view is None

    arcade.set_window(w)

    w.background_color = 255, 255, 255, 255
    assert w.background_color == (255, 255, 255, 255)
    w.set_mouse_visible(True)
    w.set_size(width, height)

    p = arcade.get_projection()
    assert isinstance(p, Mat4)

    v = arcade.get_viewport()
    assert v[0] == 0
    assert v[1] == width
    assert v[2] == 0
    assert v[3] == height

    factor = arcade.get_scaling_factor()
    assert factor > 0
    factor = arcade.get_scaling_factor(w)
    assert factor > 0

    arcade.start_render()
    arcade.finish_render()

    def f():
        pass

    arcade.schedule(f, 1/60)
    arcade.pause(0.01)
    arcade.unschedule(f)
    window.test()
