import math

SILENCE_TERMINAL_OUTPUT: bool = True

# *_BORDER_WIDTH is the width INCLUDING the border.

# Stroke settings
STROKE_BORDER_COLOR: str = "#666"
STROKE_BORDER_WIDTH: float = 4.5
STROKE_UNFILLED_COLOR: str = "#eee"
STROKE_UNFILLED_WIDTH: float = 3
STROKE_FILLING_COLOR: str = "#f00"
STROKE_FILLED_COLOR: str = "#000"
STROKE_FILLED_WIDTH: float = 3.1

# Brush settings
SHOW_BRUSH: bool = True
SHOW_BRUSH_FRONT_BORDER: bool = True
BRUSH_COLOR: str = "#f00"
BRUSH_WIDTH: float = 5.5
BRUSH_BORDER_COLOR: str = "#666"
BRUSH_BORDER_WIDTH: float = 7

WAIT_AFTER: float = 1.5

# GIF settings
DELETE_TEMPORARY_FILES: bool = True
GIF_SIZE: int = 150
GIF_FRAME_DURATION: float = 0.04
GIF_BACKGROUND_COLOR: str = "#ddf"
# Set to True to allow transparent background, much bigger file!
GIF_ALLOW_TRANSPARENT: bool = False


def stroke_length_to_duration(length: float) -> float:
    # sqrt, ie. a stroke 4 times the length is drawn
    # at twice the speed, in twice the time.
    return math.sqrt(length) / 8


def time_rescale(interval: float) -> float:
    # global time rescale, let's make animation a bit
    # faster when there are many strokes.
    return math.pow(2 * interval, 2 / 3)


# Possibilities are linear, ease, ease-in, ease-in-out, ease-out,
# see https://developer.mozilla.org/en-US/docs/Web/CSS/timing-function
# for more info.
TIMING_FUNCTION: str = "ease-in-out"
