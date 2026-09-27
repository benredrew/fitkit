# Author: Claude (Opus 5)
# Co-Author: Brendan Fennell
"""Parametric fit-test primitives -- printed gauges for measuring real things.

A fit test is a small printed part whose only job is to answer one question
about an object you cannot easily measure: how big is that jar's mouth, what
diameter does this bore actually take, how tight is tight enough. You print
it, you offer it up, and the answer is a fact rather than an estimate.

That makes these primitives a measuring instrument, and they carry the
obligations of one:

- **Every primitive engraves its own critical dimension.** A drawer of
  unlabelled rings is a drawer of rubbish -- you cannot tell 112 from 113 by
  eye, and those two are a fit and a failure. Labels are cut in, never raised:
  a raised boss adds to the diameter it claims to describe.
- **A result is only as good as the record.** The part that fitted is
  evidence; which one it was is the thing people forget. Hence the labels, and
  hence a print log.
- **They are deliberately cheap.** A primitive that takes an hour to print is
  a primitive you will guess instead of printing.

Primitives live one per module and expose a `build()` returning a solid.
"""
__all__ = ["cylinder"]
