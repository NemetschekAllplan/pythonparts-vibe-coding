from BaseInteractor import BaseInteractor, BaseInteractorData


def check_allplan_version(_build_ele, version: float) -> bool:
    return float(version) >= 2026.0


def create_interactor(interactor_data: BaseInteractorData) -> "InteractorTemplate":
    return InteractorTemplate(interactor_data)


class InteractorTemplate(BaseInteractor):
    def __init__(self, interactor_data: BaseInteractorData):
        super().__init__(interactor_data)

    def process_mouse_msg(self, mouse_msg, pnt, msg_info):
        del mouse_msg, pnt, msg_info
        return True

    def on_mouse_leave(self):
        return True

    def modify_element_property(self, page, name, value):
        del page, name, value
        return True

    def on_preview_draw(self):
        return True

    def on_value_input_control_enter(self):
        return True

    def on_control_event(self, event_id: int):
        del event_id
        return True

    def on_cancel_function(self):
        return True
