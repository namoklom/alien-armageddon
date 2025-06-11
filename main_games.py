import pygame
import sys
import random
import math
import logging
import os
from datetime import datetime

pygame.init()
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Invasion: Armageddon")
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("Consolas", 18)
WHITE, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, BLACK, ORANGE = (255, 255, 255), (220, 20, 60), (50, 220, 50), (50, 100, 220), (240, 240, 50), (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 140, 0)
BG_COLOR = (5, 5, 25)

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(filename=os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"),
                    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clamp(n, minn, maxn): return max(min(maxn, n), minn)
def angle_to_vector(deg): r = math.radians(deg); return pygame.Vector2(math.cos(r), math.sin(r))

class Particle:
    def __init__(self, pos, vel, life, color):
        self.pos = pygame.Vector2(pos)
        self.vel = pygame.Vector2(vel)
        self.life = life
        self.color = color

    def update(self):
        self.pos += self.vel
        self.life -= 1

    def draw(self, s):
        if self.life > 0:
            pygame.draw.circle(s, self.color, (int(self.pos.x), int(self.pos.y)), 2)

class Explosion:
    def __init__(self, pos):
        self.particles = [Particle(pos, angle_to_vector(a)*random.uniform(2,6), random.randint(20,40), random.choice([RED, YELLOW, MAGENTA])) for a in range(0, 360, 15)]

    def update(self):
        for p in self.particles:
            p.update()

    def draw(self, s):
        for p in self.particles:
            p.draw(s)

    def is_dead(self):
        return all(p.life <= 0 for p in self.particles)

class PowerUp:
    def __init__(self, pos):
        self.pos = pos
        self.type = random.choice(['health', 'rapid', 'multi'])
        self.radius = 10

    def draw(self, s):
        color = {'health': GREEN, 'rapid': YELLOW, 'multi': CYAN}[self.type]
        pygame.draw.circle(s, color, (int(self.pos.x), int(self.pos.y)), self.radius)

    def collide(self, player):
        return (self.pos - player.pos).length() < self.radius + 15

class Player:
    def __init__(self):
        self.pos = pygame.Vector2(WIDTH//2, HEIGHT//2)
        self.vel = pygame.Vector2(0, 0)
        self.angle = 0
        self.health = 100
        self.cooldown = 0
        self.score = 0
        self.rapid_fire = False
        self.multi_shot = False
        self.rapid_timer = 0
        self.multi_timer = 0

    def update(self, keys):
        if keys[pygame.K_LEFT]: self.angle -= 3
        if keys[pygame.K_RIGHT]: self.angle += 3
        if keys[pygame.K_UP]: self.vel += angle_to_vector(self.angle) * 0.4
        self.vel *= 0.96
        self.pos += self.vel
        self.pos.x %= WIDTH
        self.pos.y %= HEIGHT
        if self.cooldown > 0: self.cooldown -= 1
        self.rapid_fire = self.rapid_timer > 0
        self.multi_shot = self.multi_timer > 0
        self.rapid_timer -= 1 if self.rapid_timer > 0 else 0
        self.multi_timer -= 1 if self.multi_timer > 0 else 0

    def shoot(self):
        dir_vec = angle_to_vector(self.angle) * 12
        bullets = [Bullet(self.pos + dir_vec.normalize()*25, dir_vec)]
        if self.multi_shot:
            offset = 15
            for angle in [-offset, offset]:
                vec = angle_to_vector(self.angle + angle) * 12
                bullets.append(Bullet(self.pos + vec.normalize()*25, vec))
        return bullets

    def draw(self, s):
        direction = angle_to_vector(self.angle)
        perp = pygame.Vector2(-direction.y, direction.x)
        points = [
            self.pos + direction * 20,
            self.pos - direction * 12 + perp * 10,
            self.pos - direction * 12 - perp * 10
        ]
        pygame.draw.polygon(s, BLUE, points)
        pygame.draw.rect(s, RED, (self.pos.x-40, self.pos.y+30, 80, 6))
        pygame.draw.rect(s, GREEN, (self.pos.x-40, self.pos.y+30, 80 * self.health / 100, 6))

class Bullet:
    def __init__(self, pos, vel):
        self.pos = pygame.Vector2(pos)
        self.vel = pygame.Vector2(vel)
        self.life = 80

    def update(self):
        self.pos += self.vel
        self.life -= 1

    def draw(self, s):
        pygame.draw.circle(s, YELLOW, (int(self.pos.x), int(self.pos.y)), 4)

    def is_dead(self):
        return self.life <= 0 or not (0 <= self.pos.x <= WIDTH and 0 <= self.pos.y <= HEIGHT)

class Enemy:
    def __init__(self, wave):
        self.pos = pygame.Vector2(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))
        self.vel = pygame.Vector2(random.uniform(-1,1), random.uniform(-1,1))
        self.radius = 20
        self.max_health = self.health = 30 + wave * 10

    def update(self, player):
        if (player.pos - self.pos).length() < 400:
            self.vel = (player.pos - self.pos).normalize() * 1.5
        self.pos += self.vel
        self.pos.x %= WIDTH
        self.pos.y %= HEIGHT

    def draw(self, s):
        pygame.draw.circle(s, RED, (int(self.pos.x), int(self.pos.y)), self.radius)
        pygame.draw.rect(s, RED, (self.pos.x-20, self.pos.y-30, 40, 5))
        pygame.draw.rect(s, GREEN, (self.pos.x-20, self.pos.y-30, 40 * self.health / self.max_health, 5))

    def hit(self, bullet):
        return (self.pos - bullet.pos).length() < self.radius

    def is_dead(self):
        return self.health <= 0

class TankAlien(Enemy):
    def __init__(self, wave):
        super().__init__(wave)
        self.radius = 30
        self.max_health = self.health = 80 + wave * 15

    def draw(self, s):
        points = []
        for i in range(6):
            angle = math.radians(i * 60)
            x = self.pos.x + self.radius * math.cos(angle)
            y = self.pos.y + self.radius * math.sin(angle)
            points.append((x, y))
        pygame.draw.polygon(s, MAGENTA, points)
        pygame.draw.rect(s, RED, (self.pos.x-25, self.pos.y-40, 50, 6))
        pygame.draw.rect(s, GREEN, (self.pos.x-25, self.pos.y-40, 50 * self.health / self.max_health, 6))

class HealerAlien(Enemy):
    def __init__(self, wave):
        super().__init__(wave)
        self.radius = 22
        self.max_health = self.health = 50 + wave * 10
        self.heal_cooldown = 0

    def update(self, player):
        self.heal_cooldown -= 1
        if (player.pos - self.pos).length() < 500:
            self.vel = (player.pos - self.pos).normalize() * 1.2
        self.pos += self.vel
        self.pos.x %= WIDTH
        self.pos.y %= HEIGHT

        if self.heal_cooldown <= 0:
            for e in game.enemies:
                if e != self and (e.pos - self.pos).length() < 100 and e.health < e.max_health:
                    e.health = min(e.max_health, e.health + 10)
                    game.healing_signs.append({'pos': e.pos.copy(), 'timer': 30})
            self.heal_cooldown = 180

    def draw(self, s):
        pygame.draw.circle(s, GREEN, (int(self.pos.x), int(self.pos.y)), self.radius)
        pygame.draw.circle(s, WHITE, (int(self.pos.x), int(self.pos.y)), self.radius, 2)
        pygame.draw.rect(s, RED, (self.pos.x-20, self.pos.y-30, 40, 5))
        pygame.draw.rect(s, GREEN, (self.pos.x-20, self.pos.y-30, 40 * self.health / self.max_health, 5))

class Game:
    def __init__(self):
        self.player = Player()
        self.bullets = []
        self.enemies = []
        self.explosions = []
        self.powerups = []
        self.healing_signs = []
        self.wave = 1
        self.game_over = False
        self.spawn_enemies(self.wave)

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)
        fire_rate = 4 if self.player.rapid_fire else 12
        if keys[pygame.K_SPACE] and self.player.cooldown <= 0:
            self.bullets += self.player.shoot()
            self.player.cooldown = fire_rate

        for b in self.bullets[:]:
            b.update()
            if b.is_dead():
                self.bullets.remove(b)

        for e in self.enemies[:]:
            e.update(self.player)
            for b in self.bullets:
                if e.hit(b):
                    e.health -= 20
                    b.life = 0
                    if e.is_dead():
                        self.player.score += 100
                        self.explosions.append(Explosion(e.pos))
                        self.enemies.remove(e)
                        if random.random() < 0.3:
                            self.powerups.append(PowerUp(e.pos))
                        break
            if (e.pos - self.player.pos).length() < e.radius + 15:
                self.player.health -= 10
                self.explosions.append(Explosion(e.pos))
                self.enemies.remove(e)
                if self.player.health <= 0:
                    self.game_over = True

        for ex in self.explosions[:]:
            ex.update()
            if ex.is_dead():
                self.explosions.remove(ex)

        for pu in self.powerups[:]:
            if pu.collide(self.player):
                if pu.type == 'health':
                    self.player.health = clamp(self.player.health + 20, 0, 100)
                elif pu.type == 'rapid':
                    self.player.rapid_timer = 300
                elif pu.type == 'multi':
                    self.player.multi_timer = 300
                self.powerups.remove(pu)

        for sign in self.healing_signs[:]:
            sign['timer'] -= 1
            if sign['timer'] <= 0:
                self.healing_signs.remove(sign)

        if not self.enemies and not self.game_over:
            self.wave += 1
            self.spawn_enemies(self.wave)
            logging.info(f"Spawned wave {self.wave}")

    def spawn_enemies(self, wave):
        for _ in range(3 + wave):
            enemy_class = random.choices([Enemy, TankAlien, HealerAlien], weights=[0.4, 0.3, 0.3])[0]
            self.enemies.append(enemy_class(wave))

    def draw(self):
        screen.fill(BG_COLOR)
        self.player.draw(screen)
        for b in self.bullets:
            b.draw(screen)
        for e in self.enemies:
            e.draw(screen)
        for ex in self.explosions:
            ex.draw(screen)
        for pu in self.powerups:
            pu.draw(screen)

        for sign in self.healing_signs:
            pygame.draw.line(screen, GREEN, (sign['pos'].x - 5, sign['pos'].y), (sign['pos'].x + 5, sign['pos'].y), 2)
            pygame.draw.line(screen, GREEN, (sign['pos'].x, sign['pos'].y - 5), (sign['pos'].x, sign['pos'].y + 5), 2)

        text = FONT.render(f"Wave: {self.wave}  Score: {self.player.score}", True, WHITE)
        screen.blit(text, (10, 10))
        if self.game_over:
            go = FONT.render("GAME OVER - Press R to Restart", True, RED)
            screen.blit(go, (WIDTH//2 - go.get_width()//2, HEIGHT//2))

    def restart(self):
        self.__init__()

def main():
    global game
    game = Game()
    running = True
    while running:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_r and game.game_over:
                game.restart()
        if not game.game_over:
            game.update()
        game.draw()
        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
