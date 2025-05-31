# Space Invaders (PyGame)

Este es un juego tipo "Space Invaders" hecho con Python y la librería PyGame. Fue creado como proyecto práctico para aprender programación de videojuegos, manejo de eventos, estructuras condicionales y multimedia.

## Características

- Movimiento lateral del jugador.
- Disparo con ESPACIO.
- Enemigos que se mueven y disparan.
- Colisiones entre balas y enemigos.
- Puntaje visible con mensajes motivacionales al acertar.
- Efecto de sonido especial en cada múltiplo de 30 puntos.
- Música de fondo.
- Menú principal y pantalla de Game Over.
- Pausa del juego con ESPACIO.

## Sonido y música

- Música de fondo: un archivo music.mp3 que se reproduce en bucle mientras se juega.
- Efectos de sonido:
  - Un archivo bravo.mp3 que se activa al alcanzar cada múltiplo de 30 puntos.
- Todos los archivos deben estar ubicados dentro de la carpeta assets.

## Controles

- Flechas izquierda y derecha: mover al jugador.
- ESPACIO: disparar.
- ENTER: seleccionar opción en los menús.
- ESPACIO (durante el juego): pausar o reanudar el juego.

## Estructura del proyecto

```
space_invaders/
├── assets/
│   ├── player.png
│   ├── enemy.png
│   ├── bullet.png
│   └── music/
│       ├── music.mp3
│       ├── bravo.mp3
├── main.py
├── game.py
├── menu.py
├── utils.py
├── README.md
```

## Requisitos

- Python 3.8 o superior
- PyGame instalado

Para instalar PyGame:

```bash
  pip install pygame
```
## Cómo ejecutar el juego

1. Clona o descarga el proyecto.
2. Asegúrate de tener los archivos en la carpeta assets.
3. Ejecuta:

```bash
  python main.py
```
## Notas

- Puedes reemplazar music.mp3 o bravo.mp3 por otros sonidos.
- Los mensajes motivacionales pueden ser modificados en el archivo game.py.
