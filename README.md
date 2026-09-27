# fitkit

Parametric fit-test primitives — small printed gauges that answer one question
about a real object you can't easily measure.

```bash
fit-test cylinder 112
```

```
part         cylinder OD 112 / ID 108, wall 2, 8 tall
check        1 body, geometry valid, 0 naked edges, 112.0 x 112.0 x 8.0 fits 180x180x180
wrote        output/cylinder_od112_id108_h8.step
slice with   slice-with-preview output/... --printer '...' --filament DogPLA
```

## Why these exist

You cannot caliper the inside of a jar mouth accurately, and a lid cut to a
guess is a lid that drops in the tank. So you print a ring of known diameter,
offer it up, and the answer is a fact. The aquarium project's vessel mouths
were all settled this way — 116 printed loose, 118 fitted "tighter end of
good", and that is why its spec says 118 rather than a caliper reading.

## The rules these follow

- **Every primitive engraves its own critical dimensions.** A drawer of
  unlabelled rings is a drawer of rubbish: 112 and 113 are indistinguishable
  by eye and are the difference between a fit and a failure.
- **Labels are cut in, never raised.** A raised character adds to the diameter
  it claims to describe and subtracts from the bore — corrupting the very fit
  the number reports.
- **A primitive refuses rather than misleads.** Ask for a ring too short to
  carry its own label and you get an error, not an anonymous ring.
- **They are cheap on purpose.** A gauge that takes an hour to print is a
  gauge you will guess instead of printing.

## Primitives

| | |
|---|---|
| `cylinder` | ID/OD ring — for a bore, or over a spigot |

Wall thickness is a parameter because it changes what the ring *measures*: a
thin ring flexes into a bore a rigid part would not enter, and reports a fit
the real part won't reproduce. Compare readings only at the same wall.

## Install

Fitkit brings in the compatible, tagged CadKit release automatically. It does
not need Aquarium, Oil Shelf, or any sibling project checkout:

```bash
git clone https://github.com/benredrew/fitkit.git
cd fitkit
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -e .
```

Then make a gauge:

```bash
.venv/bin/fit-test cylinder 112
```

## Slicing

`fit-test` stops at the STEP file and prints the slicing command rather than
running it. Slicing belongs to `slice-with-preview`, which validates BG-code
checksums and verifies USB copies; wrapping it here would put that logic in
two places.

## Built on

[`cadkit`](https://github.com/benredrew/cadkit) `v0.1.1` — engraving, solid and
printability checks, drawing sheets. The dependency is pinned to that tag so a
Fitkit install is independent of your local projects.
