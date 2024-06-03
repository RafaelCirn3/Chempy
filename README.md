# Chempy - Projeto de Aprendizado de Química

---

## Sobre o Projeto:

Chempy é um projeto educacional desenvolvido para ajudar alunos de química a praticarem e aprimorarem seus conhecimentos na disciplina. O projeto inclui uma variedade de ferramentas interativas, incluindo uma calculadora de massa molar, uma lista de elementos da tabela periódica, funções para exibição de informações e um estilo de quiz para testar o conhecimento dos alunos.

---

## Componentes do Projeto:

1. **calculadoraMol.py:** Este arquivo contém o código-fonte para a calculadora de massa molar. Os alunos podem inserir fórmulas químicas e obter a massa molar total do composto, juntamente com a composição percentual de cada elemento.

2. **elements.py:** Uma lista de todos os elementos existentes na tabela periódica. Esta lista é usada pela calculadora de massa molar para calcular a composição de elementos em um composto químico.

3. **funcoes.py:** Contém funções para exibir informações úteis relacionadas à química. Isso pode incluir informações sobre propriedades dos elementos, fórmulas químicas comuns, entre outras.

4. **questoes.py:** Um módulo que implementa um estilo de quiz para os alunos praticarem. Os alunos são apresentados com perguntas de escolha múltipla e devem selecionar a resposta correta entre as opções fornecidas.

---

## Como Utilizar:

1. **Calculadora de Massa Molar:**
   - Execute o arquivo `calculadoraMol.py`.
   - Insira a fórmula química desejada quando solicitado.
   - Obtenha a massa molar total do composto e a composição percentual de cada elemento.

2. **Lista de Elementos:**
   - O arquivo `elements.py` contém uma lista de todos os elementos da tabela periódica. Ele é usado internamente pela calculadora de massa molar.

3. **Funções de Exibição:**
   - No arquivo `funcoes.py`, você encontrará funções para exibir informações úteis relacionadas à química. Execute o arquivo para acessar essas funções.

4. **Quiz:**
   - Execute o arquivo `questoes.py`.
   - Responda às perguntas apresentadas selecionando a opção correta entre 1 e 4.

---

## Requisitos:

Certifique-se de ter todas as bibliotecas necessárias instaladas. Você pode instalar as dependências listadas no arquivo `requirements.txt` executando o seguinte comando:

```bash
pip install -r requirements.txt
