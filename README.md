# 🚀 Kuiper Belt Challenger

A classic **arcade-style space shooter** built with **Python and Pygame**.  
Pilot your spaceship through the Kuiper Belt, dodge asteroids, and blast your way to survival!

---

## 🎮 Gameplay Overview
- Control a spaceship using **keyboard arrows** or **mouse movement**.
- Fire bullets to destroy incoming asteroids.
- Each asteroid displays a **hit counter** (followText) showing how many hits are required.
- Explosions and sound effects add immersive feedback.
- Background scrolls continuously to simulate deep space travel.
- Game ends when your ship collides with an asteroid.

---

## ✨ Features
- **Scrolling Galaxy Background** for dynamic space visuals.
- **Spaceship Controls**:
  - Arrow keys for movement (up, down, left, right).
  - Spacebar to fire bullets.
  - Mouse motion support for horizontal movement.
- **Asteroids**:
  - Spawn randomly from top, left, and right.
  - Variable sizes and hit points.
- **Bullets**:
  - Limited ammo system with automatic recharge.
  - Bullet counter displayed on screen.
- **Explosions**:
  - Randomized explosion sprites when objects crash.
- **Sound Effects & Music**:
  - Background soundtrack (`bensound-scifi.wav`).
  - Explosion sounds (`explosion-01.wav`, `explosion-02.wav`).

---

## 🛠️ Tech Stack
- **Python 3**
- **Pygame** (graphics, sprites, sound, events)
- **Object-Oriented Design** (classes for spaceship, asteroids, bullets, explosions, background)

---

## 📂 Project Structure
- `ScrollingBackground` → Handles galaxy background scrolling.
- `playerspaceship` → Player’s ship with firing and crash logic.
- `AsteroidXpos`, `AsteroidYleftpos`, `AsteroidYrightpos` → Different asteroid spawn positions.
- `Bullet` → Bullet mechanics, ammo tracking.
- `Explosion` → Explosion animation when collisions occur.
- `followText` → Displays asteroid hit points.

---

## ▶️ How to Run
1. Install Python 3 and Pygame:
   ```bash
   pip install pygame
