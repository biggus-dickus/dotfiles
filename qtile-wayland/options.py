from libqtile.backend.wayland import InputConfig

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

# In Wayland backend, this can be used to configure input devices.
# https://docs.qtile.org/en/latest/manual/wayland.html#input-device-configuration
wl_input_rules = {
    'type:touchpad': InputConfig(dwt=True, natural_scroll=True, tap=True),
    'type:keyboard': InputConfig(kb_options="compose:ralt"),
}

wmname = "LG3D"
