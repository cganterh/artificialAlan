import src


class MixedPanel(src.boiler_ui_module.BoilerUIModule):
    id_ = 'the-mixed-panel'
    classes = {'scrolling-panel', 'teacher-panel',
               'student-panel'}
    name = 'Mixed Panel'

    def render(self):
        return self.render_string(
            '../panels/mixed/mixed.html')
