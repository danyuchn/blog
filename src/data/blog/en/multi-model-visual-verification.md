---
author: Dustin Yuchen Teng
pubDatetime: 2026-06-05T04:00:00Z
title: "Letting AI Write CAD From an Engineering Drawing: A Single Vision Model Can't Be Trusted to Read Topology"
slug: en/multi-model-visual-verification
featured: false
draft: false
tags:
  - ai-tools
  - case-study
  - model-comparison
description: 'A hands-on lesson: let AI look at an engineering drawing and write CadQuery directly, and a single vision model will confidently get the topology wrong. Two more independent models and a 2:1 veto are what caught it.'
---

I've been trying out a workflow lately: take an engineering drawing, let an AI look at it and write CadQuery directly, and have it spit out STEP/STL. Sounds smooth. The moment I actually ran it, the first wall wasn't the code — it was reading the drawing itself.

## A single model confidently misreads the topology

I started by having a single vision model write it cold. The part in the drawing was a "thickened plate, 20 at the corner / 15 at the edge, plus a Ø100 ring groove and a Ø60 boss." What the model read back was a "flat plate with a solid stepped descent."

Those are very different things. It didn't miss some small detail — it got the whole topology backwards. The groove became a protrusion, the thickened plate became a flat plate. And it wasn't hesitant at all; the code it wrote was confident. That's the dangerous part of a single vision model: it gets it wrong with full confidence, and you can't tell from the output where it went off.

## A 2:1 veto is what forced out the truth

So I added two more independent vision models — Gemini, plus Codex / GPT-5 — and had all three look at the same drawing and describe the topology on their own.

Line the three up and the original reading got vetoed 2:1 immediately. Two models both pointed to the ring groove and the boss, and the "solid step" reading couldn't hold. If I'd trusted only the first model, I'd have carried a structurally wrong part downstream and never noticed.

The lesson is blunt: you can't trust a single model to read topology cold. Either you cross-check across multiple models, or you keep an engineer in the loop for the final sign-off.

## And one coordinate-system trap

Once the model was right, I deployed it to model-viewer and the part stood crooked — at first glance it looked like it wasn't even the same model.

The cause was the coordinate system: GLB / glTF is Y-up, STL is Z-up. trimesh doesn't reorient on export, so the part ends up tipped over inside model-viewer. The fix is to rotate once before exporting, turning Z-up into Y-up:

```python
mesh.apply_transform(trimesh.transformations.rotation_matrix(-pi/2, [1, 0, 0]))
```

Export after that and it stands upright in the viewer.
