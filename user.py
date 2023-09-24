class User:
    # construtor de python
    def __init__(self, nome_usuario, sistema_operacional):
        print(f"Seu usuário foi criado {nome_usuario}")
        self.nome_usuario = nome_usuario
        self.sistema_operacional = sistema_operacional
        # atributo setado, não precisa de construtor = óbvio
        self.navegador = "Microsoft Edge"

    def desinstalar_navegador(self):
        if self.navegador == "Microsoft Edge":
            self.navegador = "Windows Chrome"


usuario_02 = User("Jonathan", "Windows10")
print(usuario_02.navegador)
usuario_02.desinstalar_navegador()
print(usuario_02.navegador)
