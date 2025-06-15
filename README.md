# Pygame Raycaster

A 3D first-person shooter game built with Python and Pygame, featuring raycasting technology for 3D rendering. This project demonstrates advanced game development concepts including 3D rendering, collision detection, NPC pathfinding, and interactive gameplay mechanics.

## Features

- 🎮 First-person shooter gameplay
- 🌟 3D raycasting engine for pseudo-3D rendering
- 🎯 Interactive weapons system
- 🧭 Advanced NPC pathfinding
- 🎵 Dynamic sound system
- 🎨 Texture-based rendering
- 🎯 Collision detection
- 🎮 Mouse and keyboard controls

## Technical Details

- Built with Python and Pygame
- Resolution: 1500x850
- Custom raycasting implementation for 3D rendering
- Advanced pathfinding algorithms for NPC movement
- Dynamic lighting and texture rendering
- Sound system with background music and effects

## Project Structure

- `main.py` - Core game loop and initialization
- `settings.py` - Game configuration and constants
- `player.py` - Player movement and interaction
- `raycasting.py` - 3D rendering engine
- `map.py` - Game map and level design
- `npc.py` - Non-player character implementation
- `weapon.py` - Weapon system and mechanics
- `sound.py` - Audio system
- `pathfinding.py` - NPC navigation algorithms
- `object_handler.py` - Game object management
- `object_renderer.py` - Rendering system
- `sprite_object.py` - Sprite management
- `resources/` - Game assets directory

## Requirements

- Python 3.x
- Pygame

## Installation and Running

### Method 1: Running from Source

1. Clone the repository
2. Install required dependencies:
   ```bash
   pip install pygame
   ```
3. Run the game:
   ```bash
   python main.py
   ```

### Method 2: Using the Executable

1. Download the latest release from the releases section
2. Extract the zip file
3. Run the executable file (main.exe)

## Controls

- WASD - Movement
- Mouse - Look around
- Left Click - Shoot
- ESC - Quit game

## Gameplay Instructions

1. Start the game using either Method 1 or Method 2 above
2. Use WASD keys to move around the map
3. Use the mouse to look around
4. Left-click to shoot enemies
5. Press ESC key to exit the game at any time
6. Survive and eliminate all enemies to win

## Development

This project serves as a demonstration of various game development concepts and algorithms, particularly focusing on:

- 3D rendering techniques using raycasting
- Pathfinding algorithms
- Game state management
- Collision detection
- Interactive gameplay mechanics

## Building the Executable

To create your own executable:

1. Install PyInstaller:

   ```bash
   pip install pyinstaller
   ```

2. Create the executable:

   ```bash
   pyinstaller --onefile --windowed --add-data "resources;resources" --add-data "resource_path.py;." main.py
   ```

3. The executable will be created in the `dist` folder

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
