import flet as ft

def main(pagina):

    texto = ft.Text("hashzap")

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):

        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)

        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)


    def enviar_mensagem(evento):
        print("enviar mensagem")
        pagina.pubsub.send_all(f"{nome_usuario.value}: {mensagem.value}")

        mensagem.value = ""

        pagina.update()

    mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([mensagem, botao_enviar])

    def entrar_chat(evento):
        print("entrar no chat")
        popup.open = False

        pagina.remove(botao_inciar)
        pagina.remove(texto)

        pagina.add(chat)
        pagina.add(linha_enviar)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        
        pagina.update()

    titulo_popup = ft.Text("Bem vindo ao site")
    nome_usuario = ft.TextField(label="seu nome")
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    popup = ft.AlertDialog(

        open = False,
        modal= True,
        title= titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]

    )

    def abrir_popup(evento):
        
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_inciar = ft.ElevatedButton("iniciar chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_inciar)
    

ft.app(target=main, view=ft.WEB_BROWSER)


