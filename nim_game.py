import pygame
import sys


class NimGame:
    def __init__(self, piles):
        self.piles = piles  # Lista que representa las pilas de objetos

    def is_game_over(self):
        return all(pile == 0 for pile in self.piles)

    def get_possible_moves(self):
        moves = []
        for i, pile in enumerate(self.piles):
            for j in range(1, pile + 1):
                moves.append((i, j))
        return moves

    def make_move(self, pile_index, num_objects):
        self.piles[pile_index] -= num_objects

    def undo_move(self, pile_index, num_objects):
        self.piles[pile_index] += num_objects

    def print_piles(self):
        print("Pilas actuales:", self.piles)

def nim_sum(piles):
    result = 0
    for pile in piles:
        result ^= pile
    return result

def check_game_over(piles):
    return all(pile == 0 for pile in piles)

def minimize_largest_pile(piles):
    largest_pile = max(piles)
    return -largest_pile  # Retorna el tamaño negativo de la pila más grande

def alpha_beta(game, depth, alpha, beta, is_maximizing, heuristic):
    if game.is_game_over():
        # En la versión Misère, quien haga el último movimiento pierde
        return 1 if is_maximizing else -1  # 1 si es el turno del jugador humano, -1 si es el de la máquina

    if depth == 0:
        # Evaluar el estado del juego según la heurística seleccionada
        if heuristic == 'nim_sum':
            nim_s = nim_sum(game.piles)
            return -1 if nim_s == 0 else 1
        elif heuristic == 'minimize_largest_pile':
            return minimize_largest_pile(game.piles)

    best_value = -float('inf') if is_maximizing else float('inf')
    for pile_index, num_objects in game.get_possible_moves():
        game.make_move(pile_index, num_objects)
        value = alpha_beta(game, depth - 1, alpha, beta, not is_maximizing, heuristic)
        game.undo_move(pile_index, num_objects)

        if is_maximizing:
            best_value = max(best_value, value)
            alpha = max(alpha, value)
        else:
            best_value = min(best_value, value)
            beta = min(beta, value)

        if beta <= alpha:
            break  # Poda

    return best_value

def best_move(game, depth, heuristic):
    best_val = -float('inf')
    move = None
    for pile_index, num_objects in game.get_possible_moves():
        game.make_move(pile_index, num_objects)
        move_val = alpha_beta(game, depth - 1, -float('inf'), float('inf'), False, heuristic)
        game.undo_move(pile_index, num_objects)

        if move_val > best_val:
            best_val = move_val
            move = (pile_index, num_objects)
    return move

def get_search_depth(level):
    if level == 'easy':
        return 2  # Profundidad baja
    elif level == 'medium':
        return 4  # Profundidad media
    elif level == 'hard':
        return 10  # Profundidad alta
    else:
        return 4  # Valor predeterminado
    
# Inicializar Pygame
pygame.init()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)

# Tamaño de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Títulos y fuentes
pygame.display.set_caption('Juego de NIM')
font = pygame.font.SysFont(None, 45)
small_font = pygame.font.SysFont(None, 35)

# Cargar imagen de las piezas
piece_image = pygame.Surface((20, 50))
piece_image.fill(WHITE)

# Definir pilas iniciales y otras variables
piles = [1, 3, 5, 7]
current_pile_index = -1  # Index de la pila actual seleccionada
human_score = 0
machine_score = 0
human_turn = True
game_over = False
turn_started = False  # Indica si se ha iniciado un turno
first_move = True  # Indica si es el primer movimiento del juego

# Posiciones de las pilas para formar la pirámide
pile_positions = [
    (370, 50),  # Primera pila (1 objeto)
    (340, 150),  # Segunda pila (3 objetos)
    (310, 250),  # Tercera pila (5 objetos)
    (280, 350)   # Cuarta pila (7 objetos)
]

# Botón de finalizar turno
end_turn_button = pygame.Rect(600, 500, 150, 50)

def draw_piles(piles):
    for i, pile in enumerate(piles):
        x, y = pile_positions[i]
        for j in range(pile):
            screen.blit(piece_image, (x + j * 30, y))

def draw_game(piles, human_score, machine_score):
    screen.fill(GREEN)
    draw_piles(piles)

    for i in range(4):
        button = pygame.Rect(pile_positions[i][0] + (piles[i] * 30) + 50, pile_positions[i][1] + 10, 100, 50)
        pygame.draw.rect(screen, BROWN, button)
        text = small_font.render(f'Row {i + 1}', True, WHITE)
        screen.blit(text, (button.x + 10, button.y + 10))

    if turn_started or first_move:  # Habilitar el botón si se ha iniciado el turno o es el primer movimiento
        pygame.draw.rect(screen, RED, end_turn_button)
    else:
        pygame.draw.rect(screen, BLACK, end_turn_button)  # Botón deshabilitado visualmente
    text = small_font.render('Finalizar Turno', True, WHITE)
    screen.blit(text, (end_turn_button.x + 10, end_turn_button.y + 10))

    score_text = font.render(f'Humano: {human_score} Máquina: {machine_score}', True, WHITE)
    screen.blit(score_text, (50, 20))

    pygame.display.flip()

def display_winner(winner, human_score, machine_score, last_player):
    screen.fill(GREEN)
    text = font.render(f'{last_player} pierde!', True, WHITE)
    screen.blit(text, (200, 250))
    score_text = font.render(f'Humano: {human_score} Máquina: {machine_score}', True, WHITE)
    screen.blit(score_text, (150, 350))
    pygame.display.flip()
    pygame.time.delay(3000)

def main():
    global human_turn, human_score, machine_score, game_over, piles, turn_started, first_move, current_pile_index
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not game_over and human_turn:  # Asegúrate de que sea el turno del humano para interactuar
                    for i in range(4):
                        button = pygame.Rect(pile_positions[i][0] + (piles[i] * 30) + 50, pile_positions[i][1] + 10, 100, 50)
                        if button.collidepoint(event.pos) and piles[i] > 0:
                            if current_pile_index == -1 or current_pile_index == i:  # Asegurar que se seleccione de una sola pila
                                piles[i] -= 1
                                turn_started = True
                                current_pile_index = i

                    if end_turn_button.collidepoint(event.pos) and (turn_started or first_move):
                        if first_move:
                            first_move = False  # Marcar el primer movimiento como completado
                        turn_started = False
                        current_pile_index = -1  # Resetear selección de pila
                        human_turn = not human_turn  # Cambiar turno

                if not human_turn and not game_over:  # Permitir que la máquina juegue si es su turno
                    pygame.time.delay(1000)  # Pequeña pausa para simular pensamiento
                    pile_index, num_objects = best_move(NimGame(piles), get_search_depth('hard'), 'nim_sum')
                    piles[pile_index] -= num_objects
                    print("Máquina selecciona:", pile_index, num_objects)
                    human_turn = True  # Devolver el turno al jugador humano después de que la máquina juega

                if check_game_over(piles):
                    game_over = True
                    last_player = "Humano" if human_turn else "Máquina"  # Guardar quién hizo la última jugada
                    winner = "Máquina" if human_turn else "Humano"  # Cambia el ganador al jugador que NO tomó el último turno
                    if human_turn:
                        machine_score += 1  # La máquina pierde si el humano fue el último en jugar
                    else:
                        human_score += 1  # El humano pierde si la máquina fue la última en jugar
                    display_winner(winner, human_score, machine_score, last_player)  # Pasar al display_winner
                    piles = [1, 3, 5, 7]  # Restablecer el juego para una nueva partida
                    game_over = False
                    first_move = True  # Permitir que el primer movimiento se pueda finalizar sin acción
                    human_turn = True  # Restablecer a turno humano

            if event.type == pygame.MOUSEMOTION:
                cursor = pygame.SYSTEM_CURSOR_ARROW
                for i in range(4):
                    button = pygame.Rect(pile_positions[i][0] + (piles[i] * 30) + 50, pile_positions[i][1] + 10, 100, 50)
                    if button.collidepoint(event.pos):
                        cursor = pygame.SYSTEM_CURSOR_HAND
                if end_turn_button.collidepoint(event.pos) and (turn_started or first_move):
                    cursor = pygame.SYSTEM_CURSOR_HAND
                pygame.mouse.set_cursor(cursor)

        draw_game(piles, human_score, machine_score)

if __name__ == "__main__":
    main()
