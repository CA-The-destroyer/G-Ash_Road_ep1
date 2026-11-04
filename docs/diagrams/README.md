# Systems diagrams

Updated **4 November 2026**. Journey52 is promoted,51 rollback. Architecture, skills and history diagrams now share the current release/compute boundaries; detailed acceptance remains in the [project status](../status/README.md).

| Diagram | PNG | Text / editable source |
| --- | --- | --- |
| Advanced Custom Game Dev System Design | [Systems architecture](ash-road-system-design.png) | [Frameworks and architecture](ash-road-system-design.md) |
| Skills and experience | [Skills graph](ash-road-system-design-page-2-skills.png) | [Skills and experience](ash-road-skills-and-experience.md) |
| Local Git and GitHub publication | [History flow](development-history-flow.png) | [Explanation](development-history-flow.md) · [Mermaid](development-history-flow.mmd) · [SVG](development-history-flow.svg) |

![Systems architecture](ash-road-system-design.png)

![Skills and experience](ash-road-system-design-page-2-skills.png)

![History and publication flow](development-history-flow.png)

Main frameworks: **UNREAL / BLENDER / AI**, with separate local NVIDIA/AMD, additional remote CUDA and owner-recruited secondary CPU worker roles. Hostnames are omitted. [Compute responsibilities](../compute-resources.md).

[render_system_design.py](render_system_design.py) recreates both architecture/skills PNGs. [render_history_flow.py](render_history_flow.py) recreates history PNG/SVG/Mermaid from published metadata. Python/Pillow and installed Windows Segoe UI are used; fonts are not redistributed. Art/source experiments, native integration, packaged proof and final visual acceptance retain their recorded boundaries.
