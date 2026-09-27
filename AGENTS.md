<!--
Author: Claude (Opus 5)
Co-Author: Brendan Fennell
-->
# fitkit

Parametric fit-test primitives. For any agent — Claude, Codex, or otherwise.
Start with [README.md](README.md); this adds what an agent needs on top.

## A primitive is a measuring instrument

Treat it as one. The obligations that follow are not style:

- **It must engrave its own critical dimensions.** Unlabelled gauges get mixed
  up in a drawer and then produce a confident wrong answer, which is worse
  than no answer.
- **Engrave, never raise.** A boss adds to the OD and subtracts from the ID it
  labels. `cadkit.engrave` is the only engraver; do not write a second one.
- **Refuse rather than mislead.** `cylinder.build` raises for a wall that
  leaves no bore, and for a height too short to carry a label. Adding a
  primitive means adding its refusals.
- **Do not change a default silently.** `DEFAULT_WALL` is 2mm because every
  reading in the aquarium project's print log was taken at 2mm; changing it
  invalidates comparison against that history.

## Installing

```bash
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -e .
```

The install fetches CadKit from its public `v0.1.2` tag and resolves CadQuery
2.8.x. It needs no Aquarium, Oil Shelf, sibling checkout, shared venv, or
machine-specific path. The install creates the `fit-test` command.

## Layout

One primitive per module, exposing `build()` returning a solid, plus
`describe()` and `stem()` so a loose file stays identifiable. `cli.py` adds a
subcommand per primitive.

## Do not wrap the slicer

`fit-test` prints the `slice-with-preview` invocation and stops. That tool
validates BG-code checksums and verifies USB copies; a wrapper here would be a
second copy of logic that already exists and is tested.

## Checks are not optional

`cli.py` runs `cadkit.check.printable` and refuses to write a part that fails.
Keep it that way — the point of a gauge is that its dimensions are true.
