# 👾 Alien Invasion: Armageddon

## 👤 Author

| Name            | Role              | LinkedIn                                      |
|-----------------|-------------------|-----------------------------------------------|
| Jason Emmanuel  | Game Developer    | [linkedin.com/in/jasoneml](https://www.linkedin.com/in/jasoneml/) |

**Alien Invasion: Armageddon** is a high-difficulty, object-oriented 2D space shooter designed for advanced Python developers, game enthusiasts, and AI simulation hobbyists. Built with Pygame, it demonstrates how complex gameplay mechanics, enemy intelligence, and modular code architecture can come together to form a polished and replayable arcade experience.

Unlike beginner-level shooter games, this project features distinct alien behaviors, including healing support units, tank-like enemies with polygonal bodies, and swarm attackers. It incorporates dynamic wave progression, power-up mechanics, and particle-based explosion effects that create a visually engaging and mechanically challenging environment.

The game’s structure is built around clear object-oriented principles, making it easy to expand or customize. With logging tools, a dynamic difficulty curve, and a focus on responsiveness and feedback, *Armageddon* provides both an exciting gameplay experience and a strong foundation for learning advanced game development in Python.

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

**Year: 2471**  
In the heart of the Helion Research Colony, a team of Earth’s most brilliant quantum physicists pushes the boundaries of spacetime. Their objective: unlock interdimensional energy to save a collapsing planet ravaged by centuries of war, pollution, and dwindling resources.

But the experiment goes horribly wrong.

Instead of clean energy, it tears open a rift—a shimmering portal to an alien dimension known as **The Nezrion Expanse**. From it emerge horrifying beings unlike any in recorded history. Creatures of sleek biology and synthetic enhancements, they call themselves the **Nezrion Horde**.

At first, they scout. Then, they swarm.

The Horde descends upon Earth’s defense fleet with merciless precision. Cities fall within hours. Orbital stations go dark. The last bastion of hope, **Fleet Command Omega**, sends out a desperate distress signal. But help will never come.

Amid the ruins, one ship remains: the **Aegis-X**, an experimental starfighter equipped with prototype weapons and maneuvering thrusters. Its systems were offline during the assault—spared by accident, or perhaps fate.

You are the pilot of that ship.

With no reinforcements, no command structure, and no margin for error, you alone must hold the line. Survive wave after wave of increasingly intelligent Nezrion forces—from the standard drones known as **Zarnak**, to the regenerative **Fardumun**, and the armored behemoth **Vorgulax**.

The breach is growing. The Nezrion are learning. And time is running out.

**Survive. Adapt. Overcome.**

Humanity’s fate rests on your trigger finger.

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
