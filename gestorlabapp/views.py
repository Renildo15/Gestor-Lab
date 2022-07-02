from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from bo.laboratorio import get_laboratorio
from bo.apresentacao import get_apresentacao
from bo.artigo import get_artigo
from bo.evento import get_evento
from bo.membro import get_membro
from bo.pesquisa import get_pesquisa
from bo.projeto import get_projeto
from bo.tcc import get_tcc
from bo.horario import get_horario
from django.views.decorators.http import require_safe


@require_safe
def pagina_inicial(request):
    laboratorio = get_laboratorio()
    apresentacao = get_apresentacao()
    artigo = get_artigo()
    evento = get_evento()
    membro = get_membro()
    pesquisa = get_pesquisa()
    projeto = get_projeto()
    tcc = get_tcc()
    horario = get_horario()

    context = {
        'laboratorio': laboratorio,
        'apresentacao': apresentacao,
        'artigo': artigo,
        'evento': evento,
        'membro': membro,
        'pesquisa': pesquisa,
        'projeto': projeto,
        'tcc': tcc,
        'horario': horario
    }
    return render(request,'PageInicial.html', context)

@require_safe
def sobre(request):
    return render(request, 'sobre.html')