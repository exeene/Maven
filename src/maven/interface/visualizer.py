import matplotlib.pyplot as plt
import numpy as np
from flask import render_template_string

class MarketVisualizer:
    def __init__(self, name: str, mood: str = "neutral"):
        """Initialize market visualizer with character's mood representation."""
        self.name = name
        self.mood = mood
        self.web_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                .waifu-container {{
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    background-color: {{ color }};
                }}
                h2 {{
                    color: white;
                    font-family: Arial, sans-serif;
                }}
            </style>
        </head>
        <body>
            <div class="waifu-container">
                <h2>{{ name }} - {{ mood }}</h2>
                <div class="visual" style="background: {{ color }};"></div>
            </div>
        </body>
        </html>
        """
    
    def web_render(self) -> str:
        """Generate WebGL-compatible output."""
        return render_template_string(
            self.web_template,
            name=self.name,
            mood=self.mood,
            color=self._get_mood_colors().get(self.mood, "#000")
        )
    
    def render_mood(self) -> None:
        """Display a simple visualization of the waifu's mood."""
        color = self._get_mood_colors().get(self.mood, "black")
        fig, ax = plt.subplots()
        circle = plt.Circle((0.5, 0.5), 0.4, color=color)
        ax.add_patch(circle)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(f"{self.name} is feeling {self.mood}")
        plt.show()
    
    def _get_mood_colors(self) -> dict:
        """Internal method to map moods to colors."""
        return {
            "happy": "#00FF00",
            "neutral": "#0000FF",
            "sad": "#808080",
            "angry": "#FF0000"
        }
    
    def animate_mood_transition(self, new_mood: str, steps: int = 10) -> None:
        """Animate transition from the current mood to a new mood."""
        current_color = self._get_mood_colors().get(self.mood, "#000")
        target_color = self._get_mood_colors().get(new_mood, "#000")

        current_rgb = tuple(int(current_color[i:i+2], 16) for i in (1, 3, 5))
        target_rgb = tuple(int(target_color[i:i+2], 16) for i in (1, 3, 5))

        for step in range(steps + 1):
            r = current_rgb[0] + (target_rgb[0] - current_rgb[0]) * step // steps
            g = current_rgb[1] + (target_rgb[1] - current_rgb[1]) * step // steps
            b = current_rgb[2] + (target_rgb[2] - current_rgb[2]) * step // steps
            self.mood = new_mood if step == steps else f"transitioning to {new_mood}"
            self.render_mood()
            plt.pause(0.2)

    def visualize_heatmap(self, portfolio_data: np.ndarray) -> None:
        """Generate a heatmap visualization of portfolio data."""
        plt.imshow(portfolio_data, cmap='coolwarm', aspect='auto')
        plt.colorbar()
        plt.show()