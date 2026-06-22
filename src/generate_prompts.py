from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, StrictUndefined


PROJECT_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = PROJECT_ROOT / "templates"
DATA_FILE = PROJECT_ROOT / "data" / "examples.json"
OUTPUT_DIR = PROJECT_ROOT / "generated_prompts"


def load_examples(path: Path) -> list[dict[str, Any]]:
    """Load and validate the list of example inputs."""
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("The example data must be a JSON list.")

    return data


def create_environment() -> Environment:
    """Create a strict Jinja environment so missing values cause an error."""
    return Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
        autoescape=False,
    )


def render_prompts(examples: list[dict[str, Any]]) -> None:
    """Render one prompt per example and save it as a text file."""
    environment = create_environment()
    template = environment.get_template("npc_prompt.j2")
    OUTPUT_DIR.mkdir(exist_ok=True)

    for example in examples:
        example_id = example.get("id")
        if not example_id:
            raise ValueError("Every example requires a non-empty 'id'.")

        prompt_data = {key: value for key, value in example.items() if key != "id"}
        rendered_prompt = template.render(**prompt_data).strip()

        output_path = OUTPUT_DIR / f"{example_id}.txt"
        output_path.write_text(rendered_prompt + "\n", encoding="utf-8")

        print(f"\n{'=' * 72}")
        print(f"Generated prompt: {example_id}")
        print('=' * 72)
        print(rendered_prompt)


def main() -> None:
    examples = load_examples(DATA_FILE)
    render_prompts(examples)


if __name__ == "__main__":
    main()
