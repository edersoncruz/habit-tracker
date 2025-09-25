# 🧠 Habit Tracker

Um aplicativo simples para rastrear hábitos diários e ajudar no desenvolvimento pessoal por meio da consistência.

## 🚀 Funcionalidades

- ✅ Adicionar e remover hábitos
- 📅 Marcar hábitos como concluídos por dia
- 📊 Visualizar progresso diário/semanal
- 📈 Gráfico de linha com evolução dos hábitos ao longo do tempo (usando Matplotlib)
- 💾 Salvamento local dos dados via arquivo JSON
- 🌐 Uso de API para salvar e gerenciar os dados

## 🛠️ Tecnologias Utilizadas

- Python 3
- PySide6
- Matplotlib (visualização de dados)

## 📁 Estrutura do Projeto
 ```bash
habit-tracker/
│
├── files/                     # Pasta para arquivos adicionais (ex: logo, JSON de dados)
│   ├── habits.json            # Arquivo JSON para salvar os dados dos hábitos
│   └── logo.png               # Logo do aplicativo
│
├── telas/                     # Módulos das telas da aplicação
│   ├── calendar.py            # Tela/calendário para seleção e visualização das datas
│   ├── habits.py              # Tela para gerenciar hábitos
│   └── grid.py                # Tela com gráfico de hábitos realizados por dia
│
├── utils/                     # Utilitários e funções auxiliares
│   ├── api_connection.py      # API para salvar e carregar dados
│   ├── get_json.py            # Módulo para carregar dados de hábitos em JSON
│   └── variables.py           # Variáveis globais e configurações
│
├── main.py                    # Arquivo principal que inicia a aplicação
├── main_window.py             # Define a janela principal e a navegação entre telas
├── README.md                  # Documentação do projeto
├── LICENSE                    # Licença do projeto
├── requirements.txt           # Dependências do projeto
```

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/edersoncruz/habit-tracker.git
   cd habit-tracker
   ```

2. (Opcional) Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o aplicativo:
   ```bash
   python main.py
   ```

## 📸 Capturas de Tela
<img width="531" height="417" alt="image" src="https://github.com/user-attachments/assets/b04204f6-5e8e-484b-9f74-5e0010accf7b" />
<img width="531" height="417" alt="5" src="https://github.com/user-attachments/assets/efda62be-68f0-4d2c-8842-45ea624e614c" />
<img width="528" height="418" alt="image" src="https://github.com/user-attachments/assets/bb7ffa3d-42f5-4a62-b3bb-e302dda2d688" />
<img width="798" height="469" alt="image" src="https://github.com/user-attachments/assets/8d92779f-054f-43f1-be19-3238fd94bac6" />






## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📄 Licença

Este projeto está licenciado sob a MIT License.
