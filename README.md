# 👾 Alien Invasion: Armageddon

> A cinematic, adrenaline-fueled 2D space shooter powered by Python and Pygame. Survive wave after wave of multidimensional alien attackers with adaptive AI and elite combat roles.

---

## 🧠 Project Overview

**Alien Invasion: Armageddon** is a high-difficulty, fully object-oriented game designed for **advanced Python developers**, **game enthusiasts**, and **AI simulation hobbyists**. It goes beyond the basics to introduce intelligent enemy behavior, powerups, and a full particle-based visual system. This is not your typical space shooter—this is *Armageddon*.

---

## 🎮 Gameplay Features

- 🚀 **Real-time space combat** in a top-down arena with dynamic movement and friction physics.
- 🧪 **Alien Roles**:
  - **Sinib (Attacker Alien)**: Red circle shaped enemy, standard attacker aliens.
  - **Fardumun (Healer Alien)**: Green circle shaped enemy, emits a green healing pulse that regenerates allies.
  - **Vorgulax (Tank Alien)**: Magenta polygonal shaped enemy, brute with reinforced health.
- 🔫 **Weapon Systems**:
  - Bullet cooldown with adjustable fire rate
  - Powerups: `Multi-shot` & `Rapid-fire`
- ➕ **Healing Visuals**:
  - Unique green "+" signs indicate when a Healer restores enemy HP.
- 💥 **Explosions**:
  - Realistic particle effects that simulate alien deaths and collisions.
- 🎯 **Wave-Based Difficulty Scaling**:
  - Each wave increases enemy count and strength, logged for debugging.
- 🧱 **Powerups**:
  - 💚 Health Recovery
  - ⚡ Rapid Fire (temporary)
  - 🔫 Multi-shot Spread (temporary)
- 🔍 **Status Display**:
  - Score
  - Current wave
  - Health bar
- 🧾 **Logging System**:
  - Automatic logging to `/logs/` directory showing wave progression with timestamps.

---

## 📜 Backstory

> **Year: 2471**  
> A catastrophic quantum experiment tears open a portal to the dimension of the Nezrion.  
> From the breach pour the Horde—intelligent, aggressive, and growing stronger by the second.  
>
> Earth's defense fleet is annihilated in minutes. The last surviving starfighter, **Aegis-X**, piloted by you, is all that remains.  
>
> **Survive the onslaught. Protect the world. Or watch everything burn.**

---

## 🕹️ Controls

| Key          | Action                  |
|--------------|--------------------------|
| `← / →`      | Rotate ship              |
| `↑`          | Apply thrust             |
| `SPACE`      | Fire weapon              |
| `R`          | Restart after defeat     |
| `ESC / QUIT` | Exit game                |

---

## 🔧 Tools & Libraries Used

| Tool / Library     | Version       | Purpose                                                                 |
|--------------------|---------------|-------------------------------------------------------------------------|
| **Python**         | 3.7+          | Core programming language                                               |
| **Pygame**         | ≥ 2.1.0       | 2D game engine used for rendering, input, sound, and main game loop     |
| **logging (builtin)** | -         | Wave tracking and debugging logs saved in `/logs/`                     |
| **math (builtin)** | -             | Trigonometry functions for angles, directions, and vector math         |
| **random (builtin)** | -           | Randomized enemy behavior, spawn locations, power-up selection         |
| **datetime (builtin)** | -        | Timestamped log filenames                                              |
| **os (builtin)**   | -             | Directory creation for logs                                            |
| **sys (builtin)**  | -             | Graceful system exit after quitting the game                           |

---

## 🧰 Installation & Setup

### Prerequisites

- Python 3.7 or newer
- [Pygame](https://www.pygame.org/) library

### Clone and Run

```bash
git clone https://github.com/yourusername/alien-invasion-armageddon.git
cd alien-invasion-armageddon
pip install pygame
python main.py
```
