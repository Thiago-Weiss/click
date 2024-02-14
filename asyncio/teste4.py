import asyncio
import keyboard

async def check_condition():


    while not x:  # Enquanto x for False, continue verificando
        print(x)
        print('Verificando...')
        await asyncio.sleep(1)  # Aguarda por 10 segundos antes de verificar novamente

# Função para alterar x quando a tecla 'q' for pressionada
def on_key_event(event):
    global x
    if event.name == 'q':
        x = True
        print(x)
# Configurando o hook para monitorar as teclas pressionadas
keyboard.on_press(on_key_event)

# Inicializa a variável x
x = False

# Cria e executa o loop assíncronoq
asyncio.run(check_condition())

