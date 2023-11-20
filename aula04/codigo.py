# Passo a passo:
# 1. Botão de iniciar chat
# 2. Popup para entrar no chat
# 3. Quando entrar no chat: (aparece para todo mundo)
    # 3.1 Mensagem que você entrou no chat
    # 3.2 O campo e o botão de enviar mensagem
# 4. A cada mensagem que voce envia: (aparece para todo mundo)
    # 4.1 Nome: Texto da Mensagem

import flet as ft

def main(pagina):
    pagina.title = "Chat em Grupo"
    pagina.vertical_alignment = "center"
    pagina.horizontal_alignment = "center"

    texto = ft.Text("Hashzap")

    chat = ft.Column()

    nome_usuario = ft.TextField(label="Escreva seu nome")

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            usuario_mensagem = mensagem["usuario"]
            texto_mensagem = mensagem["texto"]
            # adicionar a mensagem no chat
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(
                f"{usuario_mensagem} entrou no chat!", 
                size=12, 
                italic=True,
                color=ft.colors.ORANGE_500
            ))
        # atualizar a página
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(e):
        pagina.pubsub.send_all({"texto":campo_mensagem.value, "usuario": nome_usuario.value, "tipo": "mensagem"})
        # limpar o campo de mensagem
        campo_mensagem.value = ""
        # atualizar a página
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite uma mensgem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_popup(e):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        # adicionar o chat
        pagina.add(chat)
        # fechar o popup
        popup.open = False
        # remover o botao iniciar chat
        pagina.remove(botao_iniciar)
        # criar o campo de mensagem do usuario e botão de enviar mensagem do usuário
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem],
        ))
        # atualizar a página
        pagina.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem vindo ao Hashzap!"),
        content=nome_usuario,
        actions=[
            ft.ElevatedButton(
                "Entrar",
                on_click=entrar_popup,
            )
        ],
    )

    def entrar_chat(e):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)    

ft.app(target=main, view=ft.WEB_BROWSER)

# DEPLOY
