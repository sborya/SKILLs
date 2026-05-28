# Agent Skills Collection

A collection of [Agent Skills](https://github.com/google-gemini/gemini-cli) compatible with Gemini CLI and Claude Code. These skills follow the open standard for AI agent extensibility.

## Project Structure

This repository is designed to be a central hub for your custom skills. Each skill is contained in its own directory.

```text
.
├── nomad/              # Nomad Vacation Planner Skill
│   ├── SKILL.md        # Core instructions and metadata
│   ├── assets/         # Templates (e.g., profile_template.md)
│   ├── references/     # Detailed procedural workflows
│   └── scripts/        # Supporting logic (e.g., session_manager.py)
└── README.md
```

## How to Install

To use these skills with Gemini CLI, symlink them into your global skills directory:

```bash
# Example for the Nomad skill
ln -s "$(pwd)/nomad" ~/.gemini/skills/nomad
```

For Claude Code:
```bash
ln -s "$(pwd)/nomad" ~/.claude/skills/nomad
```

## Available Skills

### ✈️ Nomad
A sophisticated vacation planner that uses a "Layout then Verify" workflow.
- **Phase 1 (Layout):** High-level trip structure and city selection.
- **Phase 2 (Verify):** Deep search for flights, hotels, and attraction tickets.
- **Review Synthesis:** Automatically vets recommendations by analyzing 5-7 reviews across Google, TripAdvisor, Yelp, and Booking.com.
- **Platform Preferences:** Respects user-preferred booking sites (e.g., Kayak for flights, Booking.com for hotels).
