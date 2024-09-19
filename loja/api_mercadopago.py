import mercadopago
import requests

public_key = "public_key"
token = "token"

def criar_pagamento(itens_pedido, link):
    sdk = mercadopago.SDK(token)
    itens = []
    for item in itens_pedido:
        nome_produto = item.estoque_produto.produto.nome
        preco_unitario = float(item.estoque_produto.produto.preco)
        itens.append({
                "title": nome_produto,
                "quantity": 1,
                "unit_price": preco_unitario,
            })

    preference_data = {
        "items": itens,
        "auto_return": "all",
        "back_urls": {
            "success": link,
            "pending": link,
            "failure": link,
        }
    }

    try:
        resposta = sdk.preference().create(preference_data)
        link_pagamento = resposta["response"]["init_point"]
        id_pagamento = resposta["response"]["id"]
        return link_pagamento, id_pagamento
    except Exception as e:
        return None, None

def info_pedido(id_pagamento):
    sdk = mercadopago.SDK(token)
    
    try:
        pagamento = sdk.payment().get(id_pagamento)
        metodo_pagamento = pagamento["response"].get("payment_method", {}).get("type", "Indefinido")
        preco_final = pagamento['response']['transaction_details']['total_paid_amount']
        return metodo_pagamento, preco_final
    except KeyError as e:
        return "Indefinido", 0