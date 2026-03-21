# Catalog - NIQ
Estou construindo um sistema de **Catalog Intelligence** para substituir o seu processo manual de Excel (PROC V e tabelas dinâmicas) por uma automação baseada em Inteligência Artificial. O objetivo central é que a IA aprenda com o seu histórico de dados para **classificar novos produtos automaticamente**, identificando a categoria (CP) e o analista responsável sem a necessidade de intervenção humana constante.

Aqui está o detalhamento do que estou fazendo:

### 1. O que estou tentando fazer
Estou transformando um histórico de cerca de **33 mil registros** em um "cérebro" treinado. Esse sistema será capaz de ler as exportações brutas da sua plataforma e preencher as CPs corretamente, mesmo quando as descrições forem variadas ou inconsistentes, como no caso de "guardanapos" ou "remédios" que antes caíam erroneamente em "OUTRAS".

### 2. Qual função/modelo vamos usar
Utilizaremos o modelo **LinearSVC** da biblioteca `scikit-learn`. Escolhemos este modelo porque ele é superior para lidar com **centenas de categorias (mais de 170 CPs)** e textos curtos, oferecendo uma acurácia que já atingiu cerca de **97%** nos testes realizados. O processo envolve transformar as palavras em números (vetorização TF-IDF) usando bigramas para que a IA entenda expressões como "leite em pó" de forma conjunta.

### 3. Para que serve este projeto (Aplicação prática)
O objetivo final é a **automação total da sua Daily**:
*   **Classificação Automática:** Ao subir um arquivo de produtos novos, a IA preenche a CP e o Analista (Valeria, Julia, etc.) instantaneamente.
*   **Geração de Planilhas:** O script vai gerar automaticamente os arquivos separados que você usa no dia a dia, como **IC, CPS e Semanal**.
*   **Filtro de Confiança:** O modelo indicará um score de certeza; se a IA tiver dúvida (confiança baixa), ela marcará o item para **'REVISAR'**, garantindo que você só olhe para o que realmente for ambíguo.
*   **Aprendizado Contínuo:** Sempre que você corrigir um erro da IA, essa correção será alimentada de volta no histórico, fazendo com que o modelo fique mais inteligente a cada semana.

Em resumo, estou deixando de ser um operador de planilhas para se tornar o gestor de um sistema de IA que **elimina o retrabalho e o erro humano** no seu setor.
