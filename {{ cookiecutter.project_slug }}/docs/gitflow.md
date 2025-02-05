## Gitflow

### **1. Branches Principais**
Essas branches existem permanentemente no repositório:

#### **`main`**
- Representa o estado **estável** e **pronto para produção**.
- Apenas recebe merges de branches **release** ou **hotfix**.
- Nenhum desenvolvimento direto deve ser feito aqui.

#### **`develop`**
- Representa o estado **atual de desenvolvimento**.
- Serve como base para as branches de feature.
- Após a conclusão e testes de uma release, a branch `develop` é mergeada na `main`.

---

### **2. Branches Auxiliares**
Essas branches são criadas temporariamente e removidas após serem mergeadas:

#### **`feature/<nome-da-feature>`**
- Usada para desenvolver **novos recursos**.
- Baseada na branch `develop`.
- Após completar o desenvolvimento e testes da feature, é mergeada de volta na `develop`.
- Exemplo:
  - `feature/pesquisa-web-tavily`
  - `feature/agente-crewai`
  - `feature/frontend-interface`

#### **`release/<versão>`**
- Usada para preparar uma nova versão do sistema.
- Baseada na branch `develop`.
- Aqui você realiza ajustes finais, como documentação e testes de regressão.
- Após aprovação, é mergeada na `main` e na `develop`.
- Exemplo:
  - `release/1.0.0`

#### **`hotfix/<nome-do-hotfix>`**
- Usada para corrigir **erros críticos na produção**.
- Baseada na branch `main`.
- Após a correção, é mergeada de volta na `main` e na `develop`.
- Exemplo:
  - `hotfix/corrige-bug-pesquisa`

---

### **Fluxo de Trabalho no Gitflow**
1. **Início de uma Feature**:
   - Criar uma branch a partir de `develop`:
     ```bash
     git checkout develop
     git checkout -b feature/<nome-da-feature>
     ```

2. **Finalização de uma Feature**:
   - Merge da branch na `develop`:
     ```bash
     git checkout develop
     git merge feature/<nome-da-feature>
     git branch -d feature/<nome-da-feature>
     ```

3. **Preparação de uma Release**:
   - Criar uma branch `release` a partir de `develop`:
     ```bash
     git checkout develop
     git checkout -b release/<versão>
     ```
   - Após ajustes, merge na `main` e na `develop`:
     ```bash
     git checkout main
     git merge release/<versão>
     git checkout develop
     git merge release/<versão>
     git branch -d release/<versão>
     ```

4. **Correção de Hotfix**:
   - Criar uma branch `hotfix` a partir de `main`:
     ```bash
     git checkout main
     git checkout -b hotfix/<nome-do-hotfix>
     ```
   - Após ajustes, merge na `main` e na `develop`:
     ```bash
     git checkout main
     git merge hotfix/<nome-do-hotfix>
     git checkout develop
     git merge hotfix/<nome-do-hotfix>
     git branch -d hotfix/<nome-do-hotfix>
     ```

---

### **Vantagens do Gitflow no Seu Projeto**
- **Organização**: Mantém o desenvolvimento separado das versões de produção.
- **Paralelismo**: Várias features podem ser desenvolvidas simultaneamente sem interferência.
- **Controle**: Processos claros para lançamento e correção de bugs.

Se precisar de um exemplo mais prático ou ajustes no fluxo, é só avisar!
