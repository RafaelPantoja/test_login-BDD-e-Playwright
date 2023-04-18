# Created by rafael.pantoja at 17/04/2023
Feature: Login no sistema
  Como um usuário registrado
  Eu quero poder fazer login no sistema
  Para poder acessar as funcionalidades

  Scenarios: Login com sucesso
    Examples:Login com sucesso
    Given Dado que o usuário está na página de login
    When  o usuário preenche o campo de usuario com "usuario"
    When E o usuário preenche o campo de senha com "senha"
    Then E o usuário clica no botão de login "enviar"
    Then Então o usuário deve ser redirecionado para a página inicial do sistema
