# Personagens
define p = Character(_("Princesa"), color="#f79cc2")
define d = Character(_("Dragão"), color="#ccff99")
define audio.jogomusic = "audio/2.somFundo_250972__luis-audp__celtic-tin-whistle-pennywhistle-in-d.mp3"
define audio.dragaorufo = "audio/5.cena-3_333469__jeffreys2__stohnen"

# Variável para o nível de medo da personagem no início do jogo
default countMedo = 10

# Início do jogo

label start:

    # Inserir uma música fofinha de conto de fadas
    play music jogomusic

    scene bgacordando
    with fade
    pause

    scene bgporta
    with fade
    pause

    scene bgacordando
    with fade

    p "Ouvi o barulho da chuva durante a madrugada, as flores lá fora devem estar lindas hoje."

    play sound dragaorufo
    d "Não estão diferentes de ontem nem da semana passada"

    p "Ah, você estava me ouvindo! Bom dia, Dragão..."

    scene bgtorre

    play sound dragaorufo

    d "Bom dia, minha princesa. Não se esqueça de que hoje é dia de você cantar para mim."

    scene bgacordando

    menu:
        "O que devo fazer agora?"

        "Pentear o cabelo":
            jump pentear

        "Sair pela porta.":
            if countMedo >= 10:
                p "Não posso sair, o dragão está me vigiando."

    label pentear:
        scene bgpenteando
        p "Pentear os cabelos... o que mais me resta fazer?"

    scene bgarmario
    menu:
        "O que devo fazer agora?"

        "Vestir-se":
            jump armario

        "Sair pela porta.":
            if countMedo >= 10:
                p "Não posso sair, o dragão está me vigiando."

    label armario:
        scene bgarmario
        p "Já usei todos esses vestidos por tantas vezes..."

    scene bgbandeja
    with fade

    menu:
        "O que devo fazer agora?"

        "Tomar café":
            jump bandeja

        "Sair pela porta.":
            if countMedo >= 10:
                p "Não posso sair, o dragão está me vigiando."

    label bandeja:
        "A princesa encontra um bilhete misterioso junto ao seu café da manhã. 'Quem está te impedindo de sair por essa porta?'"
        scene bgbandeja

    # Fim da história
    return
