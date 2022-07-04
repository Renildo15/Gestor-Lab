from django.test import TestCase
from evento_app.forms import EventForm

class HorarioFormTestCase(TestCase):

    def test_horario_form_valido(self):
        form = EventForm(data={
            'Hora Entrada':'22:22',
            'Hora Saída': '22:22',
            'Turno': 'Tarde',
            'Dia': 'Segunda',
            'Membro': 1,
            
        })

        self.assertTrue(form.errors)

    def test_pessoa_form_invalido(self):
        form = EventForm(data={})
        self.assertFalse(form.is_valid())