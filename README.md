<h1>🤖 Chatbot Sentimental – SafeSpace</h1>
  <p>Este é um projeto de <strong>chatbot com interface gráfica e backend integrado com a OpenAI</strong>, voltado para <strong>apoio emocional e conversas empáticas</strong>, como se fosse um amigo virtual.</p>

  <h2>🧠 Tecnologias Utilizadas</h2>
  <h3>💻 Frontend</h3>
  <ul>
    <li>HTML5, CSS3 (Tailwind), JavaScript</li>
    <li>Layout responsivo com animações suaves</li>
    <li>Interface de chat moderna e acessível</li>
  </ul>

  <h3>🛠️ Backend</h3>
  <ul>
    <li>Python 3 + Flask</li>
    <li>Integração com OpenAI Chat API (<code>gpt-3.5-turbo</code>)</li>
    <li>Uso de <code>python-dotenv</code> e <code>flask-cors</code> para segurança e comunicação</li>
  </ul>

  <h2>📦 Como Rodar Localmente</h2>
  <h3>Pré-requisitos</h3>
  <ul>
    <li>Python 3.10 ou superior</li>
    <li>Conta na OpenAI com API Key válida</li>
    <li><code>pip</code> instalado</li>
  </ul>

  <h3>1. Clone o projeto</h3>
  <pre><code>git clone https://github.com/livio1212/chatbot.git
cd chatbot/backend</code></pre>

  <h3>2. Instale as dependências</h3>
  <pre><code>pip install -r requirements.txt</code></pre>

  <h3>3. Crie um arquivo <code>.env</code></h3>
  <pre><code>OPENAI_API_KEY=sk-sua-chave-aqui</code></pre>

  <h3>4. Rode o servidor Flask</h3>
  <pre><code>python app.py</code></pre>

  <h3>5. Abra o frontend</h3>
  <p>Abra o arquivo <code>frontend/index.html</code> diretamente no navegador.</p>

  <h2>🌐 Deploy no Fly.io (opcional)</h2>
  <pre><code>curl -L https://fly.io/install.sh | sh
fly auth login
fly launch
fly deploy</code></pre>

  <h3>Atualize o JavaScript</h3>
  <p>Edite o <code>script.js</code> com a URL do backend no Fly.io:</p>
  <pre><code>const BACKEND_URL = "https://seu-app.fly.dev/chat";</code></pre>



  <h2>📌 Funcionalidades</h2>
  <ul>
    <li>Interface agradável com foco no conforto visual</li>
    <li>Comunicação em tempo real com IA da OpenAI</li>
    <li>Deploy pronto para serviços como Fly.io, Render, Railway</li>
    <li>Ideal para portfólio e projetos acadêmicos</li>
  </ul>

  <h2>🙋‍♂️ Autor</h2>
  <p>Desenvolvido com 💙 por <strong>Lívio Costa</strong><br/>
  🔗 <a href="https://devlivio.site" target="_blank">https://devlivio.site</a></p>

  <h2>📃 Licença</h2>
  <p>Este projeto está sob a licença MIT – fique à vontade para usar e modificar.</p>
