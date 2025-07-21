from tutor import hooks

hooks.Filters.ENV_TEMPLATE_ROOTS.add(__file__, "templates")

hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("pharmacalogica/build", "edx-platform/themes/pharmacalogica/build"),
        ("pharmacalogica/static", "edx-platform/themes/pharmacalogica/static"),
        ("pharmacalogica/templates", "edx-platform/themes/pharmacalogica/templates"),
    ]
)

@hooks.Actions.LOAD
def _load_pharmacalogica_theme():
    print("tutor-pharmacalogica theme loaded: Teaching Molecular Magic")
