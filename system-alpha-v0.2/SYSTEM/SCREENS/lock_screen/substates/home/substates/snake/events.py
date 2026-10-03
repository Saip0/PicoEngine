import time
import random

from SYSTEM.DISPLAY import display as DP
from SYSTEM.DISPLAY import txt_ui as TXU
from SYSTEM.DISPLAY import renderer as RD
from SYSTEM.INPUT.buttons import Tc_input


def snake():
    """
        Note:
        This script was generated with AI assistance.
        Review required before major modifications.
    """

    # =========================================================
    # CONFIGURAÇÕES
    # =========================================================

    WIDTH = 320
    HEIGHT = 240

    CELL = 8

    GRID_W = WIDTH // CELL
    GRID_H = HEIGHT // CELL

    FPS = 30

    # Tempo entre movimentos da cobra
    MOVE_INTERVAL = 120  # ms

    SNAKE_COLOR = "BRANCO"
    FOOD_COLOR = "AZUL"
    BG_COLOR = "PRETO"

    # =========================================================
    # OBJETOS
    # =========================================================

    tc = Tc_input()

    # =========================================================
    # TELA INICIAL
    # =========================================================

    DP.init()

    DP.draw_rect(
        0,
        0,
        WIDTH,
        HEIGHT,
        BG_COLOR
    )

    # =========================================================
    # ESTADO INICIAL
    # =========================================================

    center_x = GRID_W // 2
    center_y = GRID_H // 2

    snake_body = [
        (center_x, center_y),
        (center_x - 1, center_y),
        (center_x - 2, center_y)
    ]

    # Direção inicial: direita
    direction = (1, 0)
    next_direction = (1, 0)

    score = 0

    # =========================================================
    # CRIA A PRIMEIRA COMIDA
    # =========================================================

    food = None

    while food is None:

        new_food = (
            random.randint(0, GRID_W - 1),
            random.randint(0, GRID_H - 1)
        )

        if new_food not in snake_body:
            food = new_food

    # =========================================================
    # DESENHA UMA CÉLULA
    # =========================================================

    def draw_cell(position, color):
        DP.draw_rect(
            position[0] * CELL,
            position[1] * CELL,
            CELL,
            CELL,
            color
        )

    # =========================================================
    # DESENHA O PLACAR
    # =========================================================

    def draw_score():

        score_ui = [
            TXU.text_ui(
                "SCORE: " + str(score),
                [0, 0],
                font="8x16",
                cor="BRANCO",
                back_cor="PRETO"
            )
        ]

        RD.render(score_ui)

    # =========================================================
    # DESENHA A COBRA
    # =========================================================

    for part in snake_body:
        draw_cell(part, SNAKE_COLOR)

    # =========================================================
    # DESENHA A COMIDA
    # =========================================================

    draw_cell(food, FOOD_COLOR)

    # =========================================================
    # DESENHA O SCORE
    # =========================================================

    draw_score()

    # =========================================================
    # CONTROLE DE TEMPO
    # =========================================================

    last_move = time.ticks_ms()

    game_over = False

    # =========================================================
    # LOOP PRINCIPAL
    # =========================================================

    while not game_over:

        frame_start = time.ticks_ms()

        # =====================================================
        # INPUT
        # =====================================================

        key = tc.read()

        if key == "2":

            # Não permite ir diretamente para baixo
            if direction != (0, 1):
                next_direction = (0, -1)

        elif key == "8":

            # Não permite ir diretamente para cima
            if direction != (0, -1):
                next_direction = (0, 1)

        elif key == "4":

            # Não permite ir diretamente para direita
            if direction != (1, 0):
                next_direction = (-1, 0)

        elif key == "6":

            # Não permite ir diretamente para esquerda
            if direction != (-1, 0):
                next_direction = (1, 0)

        # =====================================================
        # MOVIMENTO
        # =====================================================

        current_time = time.ticks_ms()

        if time.ticks_diff(
            current_time,
            last_move
        ) >= MOVE_INTERVAL:

            # Aplica a próxima direção
            direction = next_direction

            # -------------------------------------------------
            # CALCULA NOVA CABEÇA
            # -------------------------------------------------

            head = snake_body[0]

            new_head = (
                head[0] + direction[0],
                head[1] + direction[1]
            )

            # -------------------------------------------------
            # COLISÃO COM PAREDE
            # -------------------------------------------------

            if (
                new_head[0] < 0
                or new_head[0] >= GRID_W
                or new_head[1] < 0
                or new_head[1] >= GRID_H
            ):

                game_over = True
                break

            # -------------------------------------------------
            # VERIFICA SE COMEU
            # -------------------------------------------------

            ate_food = new_head == food

            # -------------------------------------------------
            # VERIFICA COLISÃO COM O CORPO
            # -------------------------------------------------

            if ate_food:

                body_to_check = snake_body

            else:

                # O rabo vai sair neste movimento,
                # então não precisamos verificar ele.
                body_to_check = snake_body[:-1]

            if new_head in body_to_check:

                game_over = True
                break

            # -------------------------------------------------
            # GUARDA O RABO ANTIGO
            # -------------------------------------------------

            old_tail = snake_body[-1]

            # -------------------------------------------------
            # ADICIONA A NOVA CABEÇA
            # -------------------------------------------------

            snake_body.insert(0, new_head)

            # -------------------------------------------------
            # SE NÃO COMEU, REMOVE O RABO
            # -------------------------------------------------

            if not ate_food:

                snake_body.pop()

                # Apaga o rabo antigo
                draw_cell(
                    old_tail,
                    BG_COLOR
                )

            # -------------------------------------------------
            # DESENHA A NOVA CABEÇA
            # -------------------------------------------------

            draw_cell(
                new_head,
                SNAKE_COLOR
            )

            # -------------------------------------------------
            # COMIDA
            # -------------------------------------------------

            if ate_food:

                score += 1

                # ---------------------------------------------
                # PROCURA UMA POSIÇÃO LIVRE
                # ---------------------------------------------

                if len(snake_body) >= GRID_W * GRID_H:

                    food = None

                else:

                    food = None

                    while food is None:

                        new_food = (
                            random.randint(
                                0,
                                GRID_W - 1
                            ),
                            random.randint(
                                0,
                                GRID_H - 1
                            )
                        )

                        if new_food not in snake_body:
                            food = new_food

                    # Desenha comida nova
                    draw_cell(
                        food,
                        FOOD_COLOR
                    )

                # ---------------------------------------------
                # ATUALIZA SCORE
                # ---------------------------------------------

                draw_score()

            # Atualiza tempo do último movimento
            last_move = current_time

        # =====================================================
        # CONTROLE DO FPS
        # =====================================================

        elapsed = time.ticks_diff(
            time.ticks_ms(),
            frame_start
        )

        frame_time = int(1000 / FPS)

        remaining = frame_time - elapsed

        if remaining > 0:
            time.sleep_ms(remaining)

    # =========================================================
    # GAME OVER
    # =========================================================

    # Limpa uma área central
    DP.draw_rect(
        60,
        80,
        200,
        80,
        BG_COLOR
    )

    game_over_ui = [

        TXU.text_ui(
            "GAME OVER",
            [104, 85],
            font="16x16",
            cor="BRANCO",
            back_cor="PRETO"
        ),

        TXU.text_ui(
            "SCORE: " + str(score),
            [104, 110],
            font="8x16",
            cor="BRANCO",
            back_cor="PRETO"
        ),

        TXU.text_ui(
            "B = SAIR",
            [104, 130],
            font="8x16",
            cor="BRANCO",
            back_cor="PRETO"
        )
    ]

    RD.render(game_over_ui)

    # =========================================================
    # ESPERA RET
    # =========================================================

    while True:

        key = tc.read()

        if key == "RET":
            break

        time.sleep_ms(20)