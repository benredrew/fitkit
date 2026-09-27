# Author: Claude (Opus 5)
# Co-Author: Brendan Fennell
"""The ID/OD cylinder: the first and plainest fit-test primitive.

A hollow ring of known outside and inside diameter. Offer the outside to a
bore, or the inside over a spigot, and the answer is a fit or it is not.

## Why both diameters are engraved

Because one ring answers two questions, and a ring you cannot identify answers
neither. 112 and 113 are indistinguishable by eye and are the difference
between a lid that seats and a lid that drops in the tank. The outside
diameter is cut into the outer wall, the inside into the bore, 180 degrees
apart so both fall in one cone of sight when the ring is tipped.

Cut in, never raised. A raised character adds to the diameter it labels and
subtracts from the bore -- corrupting the very fit the number describes.

## Why the wall is a parameter and not a constant

Wall thickness changes what the ring *measures*. A thin ring flexes into a
bore that a rigid part would not enter, and reports a fit that the real part
will not reproduce; a thick one resists and under-reports. 2mm is the default
because it is what this project's vessel mouths were dialled in with, and
comparing a new reading against that history is only valid at the same wall.

## Height

Short, because a fit test is a question, not a part. 8mm is enough to feel
whether the ring is square in a bore and little enough to print in minutes.
Tall enough to engrave: a 5mm cap height needs a wall it can sit on.
"""
import math

import cadquery as cq
from cadkit.engrave import FONT_SIZE, engrave_radial_text

DEFAULT_WALL = 2.0
DEFAULT_HEIGHT = 8.0

# Below this the label has nowhere to go: the text is FONT_SIZE tall and wants
# a little margin at each end of the wall.
MIN_HEIGHT_FOR_LABEL = FONT_SIZE + 2.0


def build(outer_diameter, wall=DEFAULT_WALL, height=DEFAULT_HEIGHT,
          label=True):
    """A labelled ring of `outer_diameter`, `wall` thick, `height` tall.

    Raises rather than producing an unlabelled or impossible ring: a fit test
    you cannot identify afterwards is worse than no fit test, because it
    invites a confident wrong answer.
    """
    inner_diameter = outer_diameter - 2 * wall
    if inner_diameter <= 0:
        raise ValueError(
            f"wall {wall}mm leaves no bore in a {outer_diameter}mm ring")
    if label and height < MIN_HEIGHT_FOR_LABEL:
        raise ValueError(
            f"height {height}mm cannot carry a {FONT_SIZE}mm label; raise it "
            f"to {MIN_HEIGHT_FOR_LABEL}mm or pass label=False -- an unlabelled "
            f"ring cannot be identified once it is in the drawer")

    ring = (cq.Workplane("XY")
            .circle(outer_diameter / 2)
            .circle(inner_diameter / 2)
            .extrude(height))
    if not label:
        return ring

    ring = engrave_radial_text(
        ring, f"{outer_diameter:g}", outer_diameter / 2, +1, height / 2,
        theta0=0.0)
    ring = engrave_radial_text(
        ring, f"{inner_diameter:g}", inner_diameter / 2, -1, height / 2,
        theta0=math.pi)
    return ring


def describe(outer_diameter, wall=DEFAULT_WALL, height=DEFAULT_HEIGHT):
    """One line naming what this ring measures, for a log or a filename."""
    return (f"cylinder OD {outer_diameter:g} / ID "
            f"{outer_diameter - 2 * wall:g}, wall {wall:g}, {height:g} tall")


def stem(outer_diameter, wall=DEFAULT_WALL, height=DEFAULT_HEIGHT):
    """A filename stem carrying the figures, so a loose file is identifiable."""
    return (f"cylinder_od{outer_diameter:g}_id{outer_diameter - 2 * wall:g}"
            f"_h{height:g}")
