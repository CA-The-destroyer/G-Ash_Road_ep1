# The Ash Road

System design and development notes for an original cooperative RPG built with Unreal Engine.

<!-- project-status:start -->
## Project status and scale

![The Ash Road measured status](docs/status/project-status.png)

**Journey52/schema47 promoted; Journey51 rollback.** Modular class equipment integration is active; complete ensembles remain2/24. Cloth routing/runtime proof passes while visible garment fit remains held.

**367.47 GB · 1,271,175 files · 153,507 code-only lines / 1,797 active source files.** Fresh4November metadata/source audit; archived/generated copies included.

[Full status](docs/status/README.md) · [Copy-ready summary](docs/status/teams-summary.txt) · [Data](docs/status/project-scale.json)
<!-- project-status:end -->

<!-- outstanding-register:start -->
## Outstanding work

Last numbered-register audit31October: **125 owner records —47 feature families,61 debug/triage and17 changes/gates**. Later intakes have not been re-audited here. Modular class equipment is the active objective. [Recorded register](docs/backlog/README.md).
<!-- outstanding-register:end -->

<!-- source-history:start -->
## Development history

**1,060 local source commits + 155 documentation commits = 1,215 distinct recorded SHAs.** The 612 HEAD subset is included. Pull requests:0.

[Ledger and method](docs/history/README.md) · [Development flow](docs/diagrams/development-history-flow.md).
<!-- source-history:end -->

## Systems diagrams

The [dedicated systems-diagrams section](docs/diagrams/README.md) contains the architecture and skills graphs, full-size PNGs, text explanations and editable Mermaid graphs.

| Diagram | PNG | Explanation |
| --- | --- | --- |
| Advanced Custom Game Dev System Design | [Systems architecture](docs/diagrams/ash-road-system-design.png) | [Systems and Unreal technology](docs/diagrams/ash-road-system-design.md) |
| Skills and experience | [Skills relationship graph](docs/diagrams/ash-road-system-design-page-2-skills.png) | [Skills and practical experience](docs/diagrams/ash-road-skills-and-experience.md) |

## Development log

Read the [project log](PROJECT_LOG.md) for development milestones, release status and validation limits. Diagrams are dated snapshots; prepared or isolated work is not automatically part of a playable release.

## Production compute

The main workstation uses **NVIDIA RTX4060Ti/CUDA** and **AMD Radeon/HIP** for compatible independent work. An additional **remote RTX4060 Laptop/CUDA** worker has actual production outputs. The owner-recruited **secondary worker PC** remains a separate optional **Blender4.1.1 CPU** lane, limited to **two threads**; its two returned LOD candidates await native admission. Main/Linux CPUs support preparation and build work; hosted image AI uses provider compute. GPU memory is separate. Prefer local NVIDIA when available; owner reservations take priority, with compatible remote NVIDIA, local AMD and CPU fallback. Check actual capacity before dispatch. One coordinator owns Unreal imports, native builds and promotion.

[Compute roles](docs/compute-resources.md).
