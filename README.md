Aqui está o README atualizado, incluindo a área de instituição:

---

# GameHub

## Descrição:

GameHub é uma plataforma de e-commerce de jogos inspirada em serviços como Steam e Nuuvem. O projeto oferece uma experiência completa de compra e descoberta de jogos, com funcionalidades de catálogo, carrinho, lista de desejos e pagamentos integrados via Mercado Pago. Além disso, conta com um app de suporte para usuários e uma área institucional com informações importantes como "Sobre", "Políticas de Privacidade" e "Termos de Uso".

## Índice:

- [Instalação](#instalação)
- [Funcionalidades](#funcionalidades)
- [App de Suporte](#app-de-suporte)
- [Área Institucional](#área-institucional)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## Funcionalidades:

- Catálogo de jogos com filtragem por categorias, desenvolvedoras e plataformas.
- Carrinho de compras e lista de desejos para gerenciar jogos antes de finalizar a compra.
- Integração com a API do Mercado Pago para pagamentos.
- Barra de navegação com dropdowns para filtro dinâmico do catálogo.
- Barra de pesquisa para localizar jogos pelo nome.
- Homepage com sliders e carrosséis destacando jogos em diversas categorias, como mais vendidos, recém-adicionados e destaques aleatórios.

## App de Suporte:

### Funcionalidades:

- Fazer perguntas e dar feedback sobre a plataforma e os jogos.
- Consultar perguntas de outros usuários e suas respectivas respostas.
- Pesquisar por perguntas específicas utilizando palavras-chave.
- Acessar as FAQs organizadas por tópicos, oferecendo respostas rápidas a dúvidas comuns.
- Interface intuitiva para facilitar a navegação e busca de informações de suporte.

## Área Institucional:

- **Sobre**: Uma página que apresenta informações sobre o GameHub, sua missão, visão e objetivos.
- **Políticas de Privacidade**: Informações sobre como os dados dos usuários são coletados, armazenados e utilizados na plataforma.
- **Termos de Uso**: Termos e condições para o uso da plataforma, incluindo direitos e deveres dos usuários e da empresa.

## Visão Geral:

### 1. Homepage:
- Exibição de jogos em destaque por meio de sliders e carrosséis.
- Carrosséis dinâmicos com jogos organizados por temas como "Mais vendidos", "Adicionados recentemente", "Jogos por categoria" e "Jogos por plataforma".
- Destaque de 4 jogos aleatórios na seção principal da homepage.

### 2. Navbar:
- Barra de navegação com dropdowns que filtram jogos por categoria, desenvolvedora ou plataforma.
- Barra de pesquisa para localizar jogos pelo nome inserido pelo usuário.
- Links de login, criação de conta e carrinho de compras.

### 3. Página de Catálogo:
- Exibição dos jogos do site.
- Exibição de jogos em uma grid.
- Opção de como ordenar os jogos (Adicionados Recentemente, Mais Vendidos, Maior Preço, Menor Preço e Lançamentos).
- Aba para fazer uma filtragem nos jogos de acordo com seu preço, categoria, plataforma, tipo, sistema e ativação.

### 4. Página de Detalhes do Jogo:
- Exibição detalhada do jogo selecionado, incluindo preço, descrição, plataformas disponíveis e categoria.
- Botões para adicionar ao carrinho ou à lista de desejos.

### 5. Carrinho e Lista de Desejos:
- Gestão de jogos adicionados ao carrinho ou à lista de desejos.
- Opção de remoção ou compra de jogos.
- Integração com a API do Mercado Pago para realizar pagamentos de forma segura.

### 6. Perfil do Usuário:
- Separado em 4 partes: Perfil, Lista de Desejos, Pedidos e Games.
- 

### 7. Páginas de Edição:
- Editar nome de usuário, email e outras informações de perfil.

## Requisitos:

Os requisitos estão listados no arquivo `requirements.txt`.

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/RatingTax78753/GameHub.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd GameHub
    ```

3. Crie um ambiente virtual:

    ```bash
    python -m venv venv
    ```

4. Ative o ambiente virtual:
    - No Windows:
        ```bash
        venv\Scripts\activate
        ```
    - No macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

5. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

6. Execute as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

7. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

## Uso:

- Acesse o servidor de desenvolvimento no navegador através de `http://127.0.0.1:8000/`.
- Registre-se ou faça login para explorar o catálogo de jogos e realizar compras.
- Utilize o app de suporte para fazer perguntas, enviar feedback ou consultar FAQs.
- Acesse a área institucional para saber mais sobre o projeto, suas políticas de privacidade e termos de uso.

## Contribuição:

Contribuições são bem-vindas! Para contribuir com este projeto:

1. Faça um fork do repositório.
2. Crie uma nova branch:

    ```bash
    git checkout -b minha-nova-funcionalidade
    ```

3. Faça suas alterações e adicione commits:

    ```bash
    git commit -m "Adiciona nova funcionalidade"
    ```

4. Envie para o branch original:

    ```bash
    git push origin minha-nova-funcionalidade
    ```

5. Crie uma pull request.

## Licença:

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais informações.

## Contato:

Email: ruanvr2006@gmail.com
