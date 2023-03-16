import arcade
import random
from dataclasses import dataclass
from math import sqrt

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
          arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]


def distance(x1, y1, x2, y2):
    # calcule la distance entre les points (x1, y1) et (x2, y2)
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


@dataclass
class Cercle:
    # represente un cercle
    # contient toute l'info necessaire pour draw_circle_filled
    rayon: int
    center_x: int
    center_y: int
    color: int

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.rayon, self.color)
        pass


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        # liste de tous les cercles a dessiner
        self.liste_cercles = []

    def setup(self):
        # remplir la liste avec 20 objets de type Cercle
        for _ in range(20):
            # generer les proprietes aleatoirement
            rayon = random.randint(10, 50)
            center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
            center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
            color = random.choice(COLORS)
            self.liste_cercles.append(Cercle(rayon, center_x, center_y, color))

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        # trouver le cercle clique
        for i in range(len(self.liste_cercles)):
            cercle = self.liste_cercles[i]
            # le clic est dans le cercle si la distance au centre est <= rayon
            if distance(x, y, cercle.center_x, cercle.center_y) <= cercle.rayon:
                # si clic gauche, on supprime le cercle de la liste
                if button == arcade.MOUSE_BUTTON_LEFT:
                    del self.liste_cercles[i]
                # si clic droit, on change la couleur
                elif button == arcade.MOUSE_BUTTON_RIGHT:
                    # trouver le nombre associe a la couleur actuelle
                    color_idx = COLORS.index(cercle.color)
                    # trouver la prochaine couleur, avec wrap si ca depasse
                    new_color = (color_idx + 1) % len(COLORS)
                    cercle.color = COLORS[new_color]
                break

    def on_draw(self):
        arcade.start_render()
        # dessiner chaque cercle
        for cercle in self.liste_cercles:
            cercle.draw()


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
