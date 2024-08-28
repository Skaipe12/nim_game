import pygame
import sys
from nim_Alpha_Betha import NodeNim, Tree
import random

# Verifica que el juego haya terminado
def check_game_over(piles):
    return all(pile == 0 for pile in piles)


#Selección de la profundidad de búsqueda
def get_search_depth(level):
    if level == 'easy':
        return 2
    elif level == 'medium':
        return 6
    elif level == 'hard':
        return 9 # si lo probamos en otro pc ponerlo en 7
    


# Inicializar Pygame
pygame.init()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_GRAY = (230, 230, 230)
DARK_GRAY = (169, 169, 169)
BUTTON_HOVER = (100, 149, 237)
BUTTON_COLOR = (70, 130, 180)

# Tamaño de la pantalla
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Títulos y fuentes
pygame.display.set_caption('Juego de NIM Estéticamente Mejorado')
font = pygame.font.SysFont('Arial', 45, bold=True)
small_font = pygame.font.SysFont('Arial', 35)

# Cargar imagen de las piezas (fósforos)
match_image = pygame.image.load('match.jpg')
match_image = pygame.transform.scale(match_image, (20, 80))

# Cargar imagen de fondo
background_image = pygame.image.load('background.jpg')

# Definir pilas iniciales y otras variables
piles = [1, 3, 5, 7]
current_pile_index = -1
human_score = 0
machine_score = 0
human_turn = True
game_over = False
turn_started = False # Permite decidir si se ha iniciado un turno
first_move = True # Permite decidir si el humano o la máquina inicia el juego en la primera jugada
difficulty = None  # Dificultad seleccionada

# Posiciones de las pilas para formar la pirámide
pile_positions = [
    (450, 150),
    (410, 250),
    (370, 350),
    (330, 450)
]

# Botones de control y selector de nivel
end_turn_button = pygame.Rect(800, 600, 200, 50)  # Botón más ancho
restart_button = pygame.Rect(800, 500, 200, 50)
difficulty_buttons = {
    'easy': pygame.Rect(400, 200, 200, 50),
    'medium': pygame.Rect(400, 300, 200, 50),
    'hard': pygame.Rect(400, 400, 200, 50)
}


# Dibujar las pilas de fósforos
def draw_piles(piles):
    for i, pile in enumerate(piles):
        x, y = pile_positions[i]
        for j in range(pile):
            screen.blit(match_image, (x + j * 30, y))

# Dibujar botones de dificultad
def draw_buttons():
    screen.fill(LIGHT_GRAY)  # Fondo más claro para la pantalla inicial
    for level, button in difficulty_buttons.items():
        pygame.draw.rect(screen, BUTTON_COLOR, button, border_radius=10)
        text = small_font.render(level.capitalize(), True, WHITE)
        text_rect = text.get_rect(center=(button.x + button.width // 2, button.y + button.height // 2))
        screen.blit(text, text_rect)

# Dibujar el juego
def draw_game(piles, human_score, machine_score):
    screen.blit(background_image, (0, 0))
    draw_piles(piles)
    pygame.draw.rect(screen, RED, end_turn_button, border_radius=10)
    text = small_font.render('Turno Máquina', True, WHITE)
    text_rect = text.get_rect(center=(end_turn_button.x + end_turn_button.width // 2, end_turn_button.y + end_turn_button.height // 2))
    screen.blit(text, text_rect)

    pygame.draw.rect(screen, LIGHT_GRAY, restart_button, border_radius=10)
    text = small_font.render('Reiniciar Juego', True, BLACK)
    text_rect = text.get_rect(center=(restart_button.x + restart_button.width // 2, restart_button.y + restart_button.height // 2))
    screen.blit(text, text_rect)

    for i in range(4):
        button = pygame.Rect(pile_positions[i][0] + (piles[i] * 30) + 50, pile_positions[i][1] + 10, 100, 50)
        pygame.draw.rect(screen, WHITE, button, border_radius=10)
        text = small_font.render(f'Fila {i + 1}', True, BLACK)
        text_rect = text.get_rect(center=(button.x + button.width // 2, button.y + button.height // 2))
        screen.blit(text, text_rect)

    score_text = font.render(f'Humano: {human_score} Máquina: {machine_score}', True, WHITE)
    screen.blit(score_text, (50, 20))

    pygame.display.flip()


# Aqui se hace toda la logica del juego llamando la clase Tree, NodeNim y sus metodos
def main():
    global human_turn, human_score, machine_score, game_over, piles, turn_started, first_move, current_pile_index, difficulty # Variables globales para modificarlas en la función main
    running = True
    selecting_difficulty = True

    while running:
        screen.fill(LIGHT_GRAY)  
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            # Seleccionar la dificultad del juego es una pantalla que aparece por primera vez en la ejecución
            if selecting_difficulty:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for level, button in difficulty_buttons.items():
                        if button.collidepoint(event.pos):
                            difficulty = level
                            selecting_difficulty = False
                            break

            else:
                screen.blit(background_image, (0, 0))  
                # Capturar eventos del mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Reiniciar el juego si se ha terminado o si se presiona el botón de reinicio
                    if restart_button.collidepoint(event.pos):
                        piles = [1, 3, 5, 7]
                        game_over = False
                        first_move = True
                        human_turn = True
                        continue
                    

                    # Lógica para seleccionar la cantidad de fósforos a quitar de una fila siendo el turno del HUMANO
                    if not game_over and human_turn:
                        for i in range(4):
                            button = pygame.Rect(pile_positions[i][0] + (piles[i] * 30) + 50, pile_positions[i][1] + 10, 100, 50)
                            if button.collidepoint(event.pos) and piles[i] > 0:
                                if current_pile_index == -1 or current_pile_index == i:
                                    piles[i] -= 1
                                    turn_started = True
                                    current_pile_index = i


                    # Lógica para finalizar el turno del HUMANO
                        if end_turn_button.collidepoint(event.pos) and (turn_started or first_move):
                            if first_move:
                                first_move = False
                            turn_started = False
                            current_pile_index = -1

                            # Verificar si el juego ha terminado después del turno del humano
                            if check_game_over(piles):
                                game_over = True
                                human_score += 1
                                piles = [1, 3, 5, 7]
                                game_over = False
                                first_move = True
                                human_turn = True
                            else:
                                human_turn = False


                    # Lógica para el turno de la MÁQUINA <Beatriz>
                    if not human_turn and not game_over:
                        #Delay para que el jugador pueda ver el movimiento de la máquina
                        pygame.time.delay(1000)
                        # Crea el estado actual del juego y los operadores posibles
                        current_state = [[f'|' for _ in range(pile)] for pile in piles]
                        operators = [(i, j + 1) for i, fila in enumerate(current_state) for j, valor in enumerate(fila)]
                        
                        # Inicializa el nodo raíz y el árbol de búsqueda
                        nodeInit = NodeNim(False, value="inicio", state=current_state, operators=operators)
                        treeAlphayBeta = Tree(nodeInit, operators)

                        # Se obtiene la jugada de la máquina
                        objectiveA = treeAlphayBeta.alfaYbeta(get_search_depth(difficulty))
                        path, operator_selected = treeAlphayBeta.printPath(objectiveA)
                        # Se actualiza el estado del juego
                        piles[operator_selected[0]] -= operator_selected[1]

                        # Verificar si el juego ha terminado después del turno de la máquina
                        if check_game_over(piles):
                            game_over = True
                            machine_score += 1
                            piles = [1, 3, 5, 7]
                            game_over = False
                            first_move = True
                            human_turn = True
                        else:
                            human_turn = True

            # Cambiar el cursor al pasar sobre los botones
            if event.type == pygame.MOUSEMOTION:
                cursor = pygame.SYSTEM_CURSOR_ARROW
                for i in range(4):
                    button = pygame.Rect(pile_positions[i][0] + (piles[i] * 30) + 50, pile_positions[i][1] + 10, 100, 50)
                    if button.collidepoint(event.pos):
                        cursor = pygame.SYSTEM_CURSOR_HAND
                for button in difficulty_buttons.values():
                    if button.collidepoint(event.pos):
                        cursor = pygame.SYSTEM_CURSOR_HAND
                if end_turn_button.collidepoint(event.pos) and (turn_started or first_move):
                    cursor = pygame.SYSTEM_CURSOR_HAND
                pygame.mouse.set_cursor(cursor)

        if selecting_difficulty:
            draw_buttons()  
        else:
            draw_game(piles, human_score, machine_score)

        pygame.display.flip()  

if __name__ == "__main__":
    main()
