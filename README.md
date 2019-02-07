# Tibia Autoloot - Python 3.7.x

Ola amigos,
jogo o Tibia no Linux, e como gosto de python resolvi adaptar os scripts que alguns amigos meus utilizavam no windows com AutoHotkey para funcionar na distribuicao que utilizo.

![image](https://user-images.githubusercontent.com/21348986/52380561-67964980-2a55-11e9-90b0-e3406d279c67.png)

# EN
Shift + Right mouse click around character super fast!
Just get the mouse positions around the character using the script  'get_mouse_position.py'  and replace in positions list.

# PT-br
Pra funcionar direitinho, voce vai precisar pegar as posicoes pra simular os cliques do mouse. Na linha #10 do script tem uma lista com as posicoes dos sqm em volta/abaixo do personagem. Provavelmente nao vai funcionar com essas posicoes, pois elas dependem da resolucao do monitor, action bars utilizadas, tamanho do chat, blablabla. Com a sua tela do jogo ajustada, rode o script get_mouse_position.py (ou utilizando o metodo de sua preferencia) e vai pegando de uma em uma a posicao e substituindo na lista. Coloque as na ordem que preferir, recomendo que siga o sentido horario/anti-horario. No final da execucao, o script voltara o mouse pra posicao original.
