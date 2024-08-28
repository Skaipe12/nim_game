# 🎮 Juego de NIM Estéticamente Mejorado

![Juego de NIM](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fi.imgur.com%2F0wiGNRi.png&f=1&nofb=1&ipt=ef4e338949c9b311319ab4dd54baee1dd63d6a0630c00add6de64c122916aeb0&ipo=images)

¡Bienvenido al **Juego de NIM Estéticamente Mejorado**! Este juego implementa la versión clásica del juego de Nim con una interfaz visual mejorada utilizando Python y Pygame.

## 📋 Tabla de Contenidos
- [Introducción](#introducción)
- [Reglas del Juego](#reglas-del-juego)
- [Instrucciones de Instalación](#instrucciones-de-instalación)
- [Cómo Jugar](#cómo-jugar)
- [Dificultades](#dificultades)
- [Funcionalidades](#funcionalidades)
- [Capturas de Pantalla](#capturas-de-pantalla)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Introducción

El **Juego de NIM Estéticamente Mejorado** es una versión gráfica del clásico juego de Nim, donde dos jugadores (uno humano y uno máquina) toman turnos para quitar fósforos de una pirámide. El objetivo del jugador es que quita el último fósforo.

## Reglas del Juego

1. Hay varias pilas de fósforos organizadas en forma de pirámide.
2. En cada turno, un jugador puede quitar uno o más fósforos de una sola pila.
3. El jugador que se vea obligado a quitar el último fósforo pierde el juego.

## Instrucciones de Instalación

### Requisitos Previos

- Python 3.6 o superior
- Pygame

### Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu-usuario/juego-nim-estetico.git
    cd juego-nim-estetico
    ```

2. Instala las dependencias necesarias:

    ```bash
    pip install pygame
    ```

3. Ejecuta el juego:

    ```bash
    python nim_game.py
    ```

## Cómo Jugar

1. Al iniciar el juego, selecciona la dificultad (fácil, media o difícil).
2. En tu turno, selecciona la pila de fósforos de la que deseas quitar fósforos.
3. Puedes quitar tantos fósforos como quieras de la pila seleccionada.
4. Haz clic en el botón "Turno Máquina" para que la máquina haga su movimiento.
5. El juego termina cuando todos los fósforos han sido quitados. ¡Evita ser el último en hacerlo!

## Dificultades

- **Fácil**: La máquina toma decisiones con una búsqueda de profundidad de 1.
- **Media**: La máquina toma decisiones con una búsqueda de profundidad de 3.
- **Difícil**: La máquina toma decisiones con una búsqueda de profundidad de 6 o 7.

## Funcionalidades

- Interfaz gráfica intuitiva y fácil de usar.
- Selección de nivel de dificultad.
- Botón de reinicio para comenzar una nueva partida.
- Puntuaciones en tiempo real para ambos jugadores.
- Algoritmo avanzado de poda alfa-beta para decisiones de la máquina.

## Capturas de Pantalla

![Pantalla Principal](https://ibb.co/0tR8kzz)

*Pantalla principal mostrando la pirámide de fósforos y los botones de control.*

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **Pygame**: Biblioteca para la creación de la interfaz gráfica del juego.
- **Algoritmo Minimax con Poda Alfa-Beta**: Para la toma de decisiones de la máquina.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz un commit (`git commit -am 'Agregar nueva funcionalidad'`).
4. Sube tu rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

¡Gracias por jugar! Esperamos que disfrutes del **Juego de NIM Estéticamente Mejorado** tanto como nosotros disfrutamos creándolo.
