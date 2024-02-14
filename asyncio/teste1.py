import time
import asyncio


async def calcular_imposto(fatu):
    print('faturamento', fatu *0.1)
    
    
async def calcular_bonus_funcionarios(vendas):
    for funcionario in vendas:
        venda = vendas[funcionario]
        print(funcionario, 'bonus', venda * 0.05)
        await asyncio.sleep(1)

async def fechamento():
    vendas = {
        'lira': 1500,
        'joao': 500,
        'amanda': 5000,
    }


    faturamento =1000
    tarefa1 = asyncio.create_task(calcular_bonus_funcionarios(vendas))
    tarefa2 = asyncio.create_task(calcular_imposto(faturamento))

    await tarefa1
    await tarefa2

    print('finalizou')


asyncio.run(fechamento())
