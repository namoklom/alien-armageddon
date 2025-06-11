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
In the heart of the Helion Research Colony, a team of Earth’s most brilliant quantum physicists pushes the boundaries of spacetime. Their mission is bold: to harness interdimensional energy and save a collapsing Earth, devastated by centuries of war, ecological collapse, and vanishing resources.

But their greatest breakthrough becomes their greatest mistake.

The experiment backfires, tearing open a shimmering portal to an unknown alien dimension: **The Nezrion Expanse**. From this rift emerge creatures never before seen, beings of sleek organic tissue fused with cold, synthetic augmentations. They are not explorers. They are the **Nezrion Horde**.

The invasion begins subtly, covert probes, strange signals, minor disappearances. Then, without warning, the swarm arrives. Earth's orbital defense fleet is wiped out in hours. Metropolises are leveled. Communication with the Moon colonies and Mars outposts ceases. The last known Earth defense station, **Fleet Command Omega**, sends out a final distress beacon before going silent.

Amid the ashes and silence, a single ship reactivates: the **Aegis-X**. A prototype starfighter equipped with experimental weaponry and deep-space maneuvering systems. Its systems had been powered down for diagnostics, sparing it from the EMP storms triggered by the initial attack.

You are its pilot.

With no reinforcements coming and no command structure left, you are Earth's last line of defense. Armed only with your reflexes, your instincts, and an evolving arsenal, you must face wave after wave of increasingly coordinated alien forces.

The Nezrion adapt quickly. From the fast and vicious **Zarnak** drones to the regenerative green **Fardumun** healers and the massive, armor-plated **Vorgulax**, they grow stronger with each wave. The breach is expanding. The enemy is learning. Time is running out.

**Survive. Adapt. Overcome.**  
The future of humanity rests on your trigger finger.

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

| Tool / Library | Purpose                                                                 |
|----------------|-------------------------------------------------------------------------|
| **Python**     | Core programming language                                               |
| **Pygame**     | 2D game engine used for rendering, input, sound, and main game loop     |
| **logging**    | Wave tracking and debugging logs saved in `/logs/`                      |
| **math**       | Trigonometry functions for angles, directions, and vector math          |
| **random**     | Randomized enemy behavior, spawn locations, power-up selection          |
| **datetime**   | Timestamped log filenames                                               |
| **os**         | Directory creation for logs                                             |
| **sys**        | Graceful system exit after quitting the game                            |

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
