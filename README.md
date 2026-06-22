# Dynamic NPC Prompt Generator with Jinja

This project demonstrates how Jinja templates can be used to generate structured prompts for an LLM-based NPC dialogue task.

## Task and domain

The domain is dynamic dialogue generation for non-player characters (NPCs) in a video game.  
Each prompt is generated from structured information such as:

- the NPC's name and role;
- personality traits;
- the current world state;
- recent events;
- the requested dialogue mode;
- optional style and safety constraints;
- the desired output format.

The generated prompts could later be sent to an LLM, but this repository focuses only on prompt generation.

## What the Jinja template does

The template dynamically creates different prompts from JSON input data. It uses:

- variables for NPC and world information;
- loops for personality traits and recent events;
- conditional sections for optional context and constraints;
- a reusable macro for bullet lists;
- different instructions for dialogue and quest-hint modes;
- different output requirements for plain text and JSON.

## Why Jinja is appropriate

A simple formatted string would become difficult to maintain because the prompt contains repeated sections, optional fields, loops, and multiple output variants. Jinja keeps the prompt logic in a separate template file and allows the Python script to focus only on loading data and rendering prompts.

The file `data/examples.json` contains three examples:

1. Mira, a suspicious alchemist;
2. Torren, a tired city guard;
3. Elda, a cheerful village baker.

Each example uses different optional fields and output settings to demonstrate why a templating engine is useful.

RUN:
pip install -r requirements.txt
python src/generate_prompts.py

