import pygame
import random
import math

SCREEN_DIM = (800, 600)

class Vec2d:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        vector = Vec2d(x, y)
        return vector

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        vector = Vec2d(x, y)
        return vector

    def __mul__(self, num):
        x = self.x * num
        y = self.y * num
        vector = Vec2d(x, y)
        return vector

    def __len__(self):
        len = int(math.sqrt(self.x ** 2 + self.y ** 2))
        return len

    def int_pair(self):
        pair = (int(self.x), int(self.y))
        return pair


class Polyline:
    def __init__(self):
        self.points = []
        self.speeds = []

    def add_point(self, x, y):
        point = Vec2d(x, y)
        speed = Vec2d(random.random() * 2, random.random() * 2)

        self.points.append(point)
        self.speeds.append(speed)

    def set_points(self):
        for i in range(len(self.points)):
            point = self.points[i]
            speed = self.speeds[i]

            point_new = point + speed

            if (point_new.x > SCREEN_DIM[0]) or (point_new.x < 0):
                self.speeds[i] = Vec2d(-speed.x, speed.y)
            if (point_new.y > SCREEN_DIM[1]) or (point_new.y < 0):
                self.speeds[i] = Vec2d(speed.x, -speed.y)

            self.points[i] = point_new

    @staticmethod
    def draw_points(display, points, style="points", width=3,
                    color=(255, 255, 255)):
        if style == "line":
            for i in range(-1, len(points) - 1):
                p_cur = points[i]
                p_next = points[i + 1]

                pygame.draw.line(display, color, p_cur.int_pair(),
                                 p_next.int_pair(), width)
        elif style == "points":
            for p in points:
                pygame.draw.circle(display, color, p.int_pair(), width)

    def make_slower(self, perc=5):
        for i, speed in enumerate(self.speeds):
            val = (100 - perc) / 100
            self.speeds[i] = speed * val

    def make_faster(self, perc=5):
        for i, speed in enumerate(self.speeds):
            val = (100 + perc) / 100
            self.speeds[i] = speed * val


class Knot(Polyline):

    def get_knot(self, count):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            p1 = (self.points[i] + self.points[i + 1]) * 0.5
            p2 = self.points[i + 1]
            p3 = (self.points[i + 1] + self.points[i + 2]) * 0.5

            base_points = [p1, p2, p3]

            res.extend(self.get_points(base_points, count))
        return res

    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]

        point = points[deg] * alpha + self.get_point(points, alpha, deg - 1) * \
                (1 - alpha)
        return point

    def get_points(self, base_points, count):
        alpha = 1 / count
        points = []
        for i in range(count):
            point = self.get_point(base_points, i * alpha)
            points.append(point)
        return points


class StartGame:

    def __init__(self):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode(SCREEN_DIM)
        pygame.display.set_caption("MyScreenSaver")

        self.steps = 45
        self.knot = Knot()
        self.working = True
        self.show_help = False
        self.pause = True

        self.hue = 0
        self.color = pygame.Color(0)

    def run(self):
        while self.working:
            for event in pygame.event.get():  # очередь событий
                if event.type == pygame.QUIT:  # отсутствует очередь событий
                    self.working = False
                if event.type == pygame.KEYDOWN:  # получает очередь событий когда нажимается кнопка
                    if event.key == pygame.K_ESCAPE:  # ESC
                        self.working = False
                    if event.key == pygame.K_r:  # R
                        self.knot = Knot()
                    if event.key == pygame.K_p:  # P
                        self.pause = not self.pause
                    if event.key == pygame.K_KP_PLUS:  # +
                        self.steps += 1
                    if event.key == pygame.K_F1:  # F1
                        self.show_help = not self.show_help
                    if event.key == pygame.K_KP_MINUS:  # -
                        self.steps -= 1 if self.steps > 1 else 0
                    if event.key == pygame.K_DOWN:
                        self.knot.make_slower()
                    if event.key == pygame.K_UP:
                        self.knot.make_faster()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self.knot.add_point(x, y)

            self.gameDisplay.fill((0, 0, 0))
            self.hue = (self.hue + 1) % 360
            self.color.hsla = (self.hue, 100, 50, 100)

            self.knot.draw_points(self.gameDisplay, self.knot.points)
            self.knot.draw_points(self.gameDisplay, self.knot.get_knot(self.steps), "line", 3, self.color)
            if not self.pause:
                self.knot.set_points()
            if self.show_help:
                self.draw_help()

            pygame.display.flip()

        pygame.display.quit()
        pygame.quit()
        exit(0)

    def draw_help(self):
        self.gameDisplay.fill((50, 50, 50))
        font1 = pygame.font.SysFont("courier", 24)
        font2 = pygame.font.SysFont("serif", 24)
        data = []
        data.append(["F1", "Show Help"])
        data.append(["R", "Restart"])
        data.append(["P", "Pause/Play"])
        data.append(["Num+", "More points"])
        data.append(["Num-", "Less points"])
        data.append(["", ""])
        data.append([str(self.steps), "Current points"])

        pygame.draw.lines(self.gameDisplay, (255, 50, 50, 255), True, [
            (0, 0), (800, 0), (800, 600), (0, 600)], 5)
        for i, text in enumerate(data):
            self.gameDisplay.blit(font1.render(
                text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
            self.gameDisplay.blit(font2.render(
                text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


if __name__ == '__main__':
    game = StartGame()
    game.run()