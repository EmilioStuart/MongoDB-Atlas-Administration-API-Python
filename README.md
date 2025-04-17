# MongoDB-Atlas-Administration-API-Python

Demonstração de algumas funções para gerenciamento de IPs utilizando a API de administração do MongoDB Atlas em Python 🐍.

## Instalações necessárias

Execute os seguintes comandos no terminal para instalar as dependências:

```bash
pip install requests==2.32.3
pip install python-dotenv==1.1.0
```

## Onde encontrar as informações necessárias?

### Public Key e Private Key  
Para criar sua chave de API, siga os passos abaixo:

1. Vá até **Organization > Access Manager > Application > API Keys**.
2. Clique em **Add New > API Key**.
3. Insira uma descrição e selecione a permissão necessária (recomendo **Organization Owner**, pois ela permite acesso completo).
4. Clique em **Next**, copie a **Public Key** e a **Private Key**, e cole-as no seu arquivo `.env`.

**IMPORTANTE**: não se esqueça de permitir o acesso ao seu IP!  
Na parte inferior da tela, clique em **Add Access List Entry**, insira o seu IP, clique em **Save** e, por fim, em **Done**.

### PROJECT_ID  
1. Vá até a aba **Projects**.
2. Ao lado do projeto desejado, clique nos três pontos e selecione **Copy Project ID**.
3. Cole o ID no seu arquivo `.env`.

**Obs.:** não existe uma forma de atualizar um IP diretamente. Para fazer uma "alteração", é necessário remover o IP atual e adicionar o novo.

## Contribuição

Espero que este projeto tenha te ajudado! Se você achou útil, não esqueça de deixar uma ⭐ no repositório — isso me ajuda bastante!  
Caso algo não esteja funcionando ou esteja desatualizado, sinta-se à vontade para abrir uma *issue* no GitHub para que eu possa corrigir.
