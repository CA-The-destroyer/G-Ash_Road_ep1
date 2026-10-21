# The Ash Road — project log

Record a short entry at each meaningful integration, blocker resolution and playable release. State what actually shipped separately from source work. Keep detailed implementation notes in the linked reports.

Publish this log to [CA-The-destroyer/G-Ash_Road_ep1](https://github.com/CA-The-destroyer/G-Ash_Road_ep1) at meaningful build milestones. The repository currently hosts progress records. Licensed assets, saved campaigns, credentials and large build payloads remain local.

## 2026-10-20 — next playable master in progress

### Shipped

- **Journey `0.21.0-preview12-playtest16` remains the current playable release.** Start with `PlayAshMarchJourney.cmd`.
- Runtime `8aaad40`, save schema33. GUI Hero Name, title/menu music and menu focus cues are delivered. Previous campaigns/packages remain retained.
- Storage retention completed: current release plus three previous releases; saved state/diagnostics preserved before cleanup.

### Source work and scoped verification

- Schema35 woodland/outlaw increment; Editor build29 passes. Not yet a new packaged release.
- 48 surveyed wildlife/monster habitats with82 potential inhabitants sharing the existing12 active wilderness actor budget. Four wolf packs plus deer, hares, foxes, spiders, ghouls and Whisper.
- Actual deer wandering/flight/render, natural wolf-pack pursuit and ordinary melee contact with deer, and ghoul roaming/player acquisition passed scoped native checks.
- Wildlife loot/replay/natural-death XP:67 checks. Ecology policy:55 checks. Archer defense against predators:120 policy checks. These are not blanket multiplayer or combat acceptance.
- Six habitat groves saved:192 trees,288 understory patches and18 deadwood pieces. Inner rescue camp saved:14 trees,500 grass patches and50 understory pieces. Existing sampled access/routes preserved.
- Crypt falling-checkpoint safeguard integrated. Two obstructing stair-wall pieces corrected in the map; the original floor/stair meshes remain.

### In progress

- **Next milestone: a playable Journey17 master**, including the bounded woodland/outlaw increment and approved scenery.
- Four open-meadow planting areas have75,050 native terrain/footprint-validated candidates. Saving is held by a foliage-budget check that also counted the existing baseline; no prairie planting has been saved yet. The initial six-area candidate failed its placement coverage gate before saving; forest/building/water conflicts are excluded from the revision.
- Crypt descent passed after the first wall correction; the return walk exposed another narrow corner. Related wall ends are being reviewed together. The original reported fall-through cause remains open.
- Next-version launcher, dependency inspection, freeze, cook and promotion tools are installed/prepared. No17 package or promotion yet.

### Deferred or blocked

- Full first-rescue town return/payment is unaccepted. The complete bandit directive, all16 quest scenes, six equipped bosses, crossbow reloads and full squad/faction behavior remain unfinished.
- Medieval Dungeon is already installed; further expansion follows this playable master.
- Imported open-world foliage provides grass/flowers and cosmetic bending materials. Journey's bending integration is deferred; it does not replace tree harvesting or loot physics.
- Modern face sliders and the separate healer/survivor batch are outside this release scope.

### Detailed local reports

These are local source-workspace reports; they are not published by this log-only update:

- `CURRENT_WORK.md` — exact playable version and work queue.
- `docs/journey-playtest17-mastering.md` — next master scope and gates.
- `docs/woodland-population18.md` — woodland implementation and evidence limits.
- `docs/bandit-camps18-implementation.md` — bandit implementation ledger.
- `docs/backlog-status.md` — backlog index.
- `docs/debug-triage.md` — debug queue.

## Entry format for subsequent milestones

Date and milestone → shipped version → concrete changes → checks and their limits → blockers → next deliverable. Publish source/status after a meaningful milestone; avoid treating prepared files or a successful compile as delivered gameplay.
