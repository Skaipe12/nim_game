# 🎮 **Juego de NIM Estéticamente Mejorado**

![Juego de NIM](https://i.postimg.cc/s1FnzRWv/Fosforos.png)

¡Bienvenido al **Juego de NIM Estéticamente Mejorado**! Esta versión gráfica del clásico juego de Nim se ha mejorado visualmente utilizando **Python** y **Pygame** para una experiencia de juego envolvente.

## 📋 **Tabla de Contenidos**
- [📝 Introducción](#-introducción)
- [📜 Reglas del Juego](#-reglas-del-juego)
- [⚙️ Instrucciones de Instalación](#-instrucciones-de-instalación)
- [🎮 Cómo Jugar](#-cómo-jugar)
- [🧩 Dificultades](#-dificultades)
- [✨ Funcionalidades](#-funcionalidades)
- [📸 Capturas de Pantalla](#-capturas-de-pantalla)
- [💻 Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [🤝 Contribuciones](#-contribuciones)
- [📄 Licencia](#-licencia)

## 📝 **Introducción**

El **Juego de NIM Estéticamente Mejorado** es una versión gráfica del clásico juego de Nim. Dos jugadores (humano vs. máquina) se turnan para quitar fósforos de una pirámide. ¡El objetivo es no ser quien quite el último fósforo!

## 📜 **Reglas del Juego**

1. Hay varias pilas de fósforos organizadas en forma de pirámide.
2. En cada turno, un jugador puede quitar uno o más fósforos de una sola pila.
3. El jugador que tenga que quitar el último fósforo pierde el juego.

## ⚙️ **Instrucciones de Instalación**

### **Requisitos Previos**

- Python 3.6 o superior
- Pygame

### **Instalación**

1. **Clona este repositorio:**

    ```bash
    git clone https://github.com/tu-usuario/juego-nim-estetico.git
    cd juego-nim-estetico
    ```

2. **Instala las dependencias necesarias:**

    ```bash
    pip install pygame
    ```

3. **Ejecuta el juego:**

    ```bash
    python main.py
    ```

## 🎮 **Cómo Jugar**

1. Al iniciar el juego, selecciona la dificultad: **Fácil**, **Media** o **Difícil**.
2. Durante tu turno, selecciona la pila de fósforos de la que deseas quitar.
3. Puedes quitar tantos fósforos como desees de la pila seleccionada.
4. Haz clic en "Turno Máquina" para que la máquina realice su movimiento.
5. ¡El juego termina cuando todos los fósforos han sido quitados! Evita ser el último en quitar uno.

## 🧩 **Dificultades**

- **Fácil**: La máquina toma decisiones con una búsqueda de profundidad de 1.
- **Media**: La máquina toma decisiones con una búsqueda de profundidad de 3.
- **Difícil**: La máquina toma decisiones con una búsqueda de profundidad de 6 o 7.

## ✨ **Funcionalidades**

- Interfaz gráfica intuitiva y amigable.
- Niveles de dificultad ajustables.
- Botón de reinicio para comenzar una nueva partida en cualquier momento.
- Visualización de puntuaciones en tiempo real.
- Algoritmo de toma de decisiones con poda alfa-beta para una experiencia desafiante.

## 📸 **Capturas de Pantalla**

![Pantalla Principal](https://i.postimg.cc/T1jdjTT6/Tablero.png)

*Pantalla principal mostrando la pirámide de fósforos y los controles del juego.*

## 💻 **Tecnologías Utilizadas**

- **Python**: Lenguaje de programación principal para la lógica del juego.
- **Pygame**: Biblioteca utilizada para la creación de la interfaz gráfica.
- **Algoritmo Minimax con Poda Alfa-Beta**: Implementación avanzada para la inteligencia de la máquina.

## 🤝 **Contribuciones**

¡Las contribuciones son bienvenidas! Sigue estos pasos para contribuir:

1. Haz un **fork** del proyecto.
2. Crea una **nueva rama** para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz un **commit** (`git commit -am 'Agregar nueva funcionalidad'`).
4. Sube tu rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un **Pull Request**.

## 📄 **Licencia**

Este proyecto está licenciado bajo la **Licencia MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

**¡Gracias por jugar!** Esperamos que disfrutes del **Juego de NIM Estéticamente Mejorado** tanto como nosotros disfrutamos creándolo. ¡Buena suerte y que gane el mejor!

---
