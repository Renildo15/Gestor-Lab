from django.test import TestCase
from horario_app.forms import HorarioForm

class HorarioFormTestCase(TestCase):

    def test_horario_form_valido(self):
        form = HorarioForm(data={
            'Hora Entrada':'22:22',
            'Hora Saída': '22:22',
            'Turno': 'Tarde',
            'Dia': 'Segunda',
            'Membro': 1,
            
        })

        self.assertTrue(form.errors)

    def test_horario_form_invalido(self):
        form = HorarioForm(data={})
        self.assertFalse(form.is_valid())