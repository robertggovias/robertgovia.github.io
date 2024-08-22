![portada](https://github.com/user-attachments/assets/470ba61e-31cc-41aa-bcdd-9916306b127a)

# Artigo sobre animações na web em especifico com css.
##Introdução às Animações CSS: O que são e por que são legais?
Você já se perguntou como alguns sites conseguem ter aquelas animações incríveis que deixam tudo mais divertido e interessante? Bem, você está prestes a descobrir! Vamos embarcar em uma aventura emocionante para aprender como criar animações no seu próprio website usando CSS. Não importa se você é novo nisso, vamos começar do básico e, em pouco tempo, você estará fazendo mágica com suas próprias mãos.
##Começando a Aventura: Conhecendo as Animações CSS
Agora que já entendemos o básico das animações CSS, é hora de adicionar um pouco de cor e diversão ao nosso site! Nesta etapa, vamos aprender como mudar as cores e os tamanhos dos elementos de forma suave e interessante.

Mudando Cores Gradualmente
Vamos começar com algo simples: mudar a cor de um botão quando o mouse passa por cima dele. Isso pode fazer com que o botão pareça mais interativo e convidativo.

Exemplo de Código: Mudando a Cor de um Botão
html
Copiar código
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .color-button {
            background-color: #3498db; /* Cor inicial: azul */
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            transition: background-color 0.5s; /* Animação de transição de cor */
        }

        .color-button:hover {
            background-color: #2ecc71; /* Cor final: verde */
        }
    </style>
    <title>Animações CSS - Mudando Cores</title>
</head>
<body>
    <button class="color-button">Passe o mouse aqui!</button>
</body>
</html>
Nesse exemplo, usamos a propriedade transition para suavizar a mudança de cor do botão de azul para verde quando o mouse passa por cima. A transição dura 0,5 segundos.

Ajustando o Tamanho dos Elementos
Além de mudar cores, também podemos criar animações que ajustam o tamanho dos elementos. Isso pode ser útil para destacar algo importante ou criar um efeito divertido quando o usuário interage com o site.

Exemplo de Código: Aumentando o Tamanho de um Botão
html
Copiar código
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .size-button {
            background-color: #e74c3c; /* Cor vermelha */
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            transition: transform 0.3s; /* Animação de transição de tamanho */
        }

        .size-button:hover {
            transform: scale(1.2); /* Aumenta o tamanho do botão em 20% */
        }
    </style>
    <title>Animações CSS - Ajustando Tamanho</title>
</head>
<body>
    <button class="size-button">Passe o mouse aqui!</button>
</body>
</html>
Nesse exemplo, usamos a propriedade transform com a função scale para aumentar o tamanho do botão em 20% quando o mouse passa por cima. A transição dura 0,3 segundos.

Conclusão
Com essas simples animações de cor e tamanho, você já pode tornar seu site muito mais interativo e interessante. Experimente ajustar as cores, tamanhos e durações para ver o que funciona melhor para o seu design. Essas são apenas algumas das muitas possibilidades que as animações CSS oferecem. Continue explorando e experimentando para descobrir novos efeitos e surpreender os visitantes do seu site!
