# Montreal Summer School 2025 - Go1 Locomotion Challenge

This repository contains code for the Go1 Locomotion Challenge, which involves training a Go1 robot to walk using reinforcement learning (RL). We will use:
- **Isaac Sim** [(https://github.com/isaac-sim/IsaacSim/)](https://github.com/isaac-sim/IsaacSim/) for simulation
- **Isaac Lab** [(https://github.com/isaac-sim/IsaacLab)](https://github.com/isaac-sim/IsaacLab) for the Go1 robot model
- **RSL RL library** [(https://github.com/leggedrobotics/rsl_rl/)](https://github.com/leggedrobotics/rsl_rl/) for the RL framework

## The Challenge

The core of the competition is to train a robust low-level walking policy in simulation, then perform sim-to-real transfer on an actual Unitree Go1 quadruped robot using the Isaac Lab framework.

Once that works, you'll have the opportunity to code a high-level, vision-based navigation controller to drive your robot autonomously in a simple obstacle race using monocular fisheye camera images. To make this task manageable, we will place AprilTags in the arena.

On Friday, the final challenge will evaluate your walking policy across three tiers of difficulty:

1. **No obstacles, joystick control** - Navigate a straight line to reach the goal as quickly as possible using joystick control.
2. **Obstacles, joystick control** - Same as Tier 1, but with obstacles like walls and uneven terrain in the arena.

## System Requirements

The main requirement is being able to run Isaac Sim and Isaac Lab. If you can successfully install and run these frameworks, your system should be compatible with this project.

**Recommended Operating System:** Ubuntu 22.04 LTS (this is what was used for testing and development)

Your system must meet Isaac Sim's [minimum hardware requirements](https://docs.isaacsim.omniverse.nvidia.com/4.5.0/installation/requirements.html#system-requirements), which include:
- NVIDIA RTX GPU (required for physics simulation)
- Sufficient RAM and storage
- Compatible NVIDIA drivers

Other Linux distributions and Windows may work but are not officially supported.
