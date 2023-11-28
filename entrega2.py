from plyer import notification
from datetime import datetime


def alerta (nivel = 2, 
            base = 'CLIENTES',
            etapa = 'EXTRACAO'):
    
        agora = datetime.now()
        data_atual = agora.strftime('%d/%m/%Y') #vi no google =)
        hora_atual = agora.strftime('%H:%M:%S') #vi no google =)

        mensagem = f'Data: {data_atual}\nHora: {hora_atual}'

        notification.notify(
                title = 'ATENÇÃO : ' + nivel,
                message = 'Falha no carregamento da base {base} na etapa {etapa} \n' + mensagem,
                timeout = 10
                )

alerta('Alerta Medio', 'Clientes', 'Extração')