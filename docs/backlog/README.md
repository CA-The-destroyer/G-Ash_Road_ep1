# Numbered outstanding work

**30 October 2026 · Journey42 promoted · Journey43 source only**

**127 outstanding primary records**, organized under the existing four workstreams. Existing feature/debug IDs stay stable; newer defects and change requests now have IDs. Numbered sub-items and repeat reports point to one owner record.

[Status and scale](../status/README.md) · [Development log](../../PROJECT_LOG.md) · [Structured register](items.json)

| Tracking category | Outstanding owner records |
| --- | ---: |
| Feature families with remaining scope | 47 |
| Debug/triage records | 62 |
| Change requests and release gates | 18 |
| **Outstanding total** | **127** |

Separate from that total: **8 optional/long-term records**, **3 monitoring records**, **16 scoped closures**, **1 excluded record**, and **1 acceptance rollup**. There are **45 numbered sub-items** within owner records; they are not counted again.

These are tracking records at different levels, not a count of unique finished game features or an effort estimate. A feature family can refer to a separately owned defect/change without owning a duplicate implementation task. Scope is the documented project register and audited intakes; no claim is made about unread chats.

## Current execution order

The existing character-replacement batch remains first. This organization pass does not start the backlog.

| Step | Record | Required outcome |
| --- | --- | --- |
| 1 | [DBG-061](#dbg-061) | Finish focused dressed Rusty/Iron motion, grip/contact review using the corrected cold-verified derivatives; record minor cosmetic gaps and proceed to useful integration. |
| 2 | [F24.01](#f24) | Activate the two checked identities on original actors. |
| 3 | [F24.02](#f24) | Admit the additional fitted melee profile on its real selected slot. |
| 4 | [F24.03](#f24) | Finish the reference-led villager wardrobe through the existing Outfit path. |
| 5 | [CHG-016](#chg-016) | Package the coherent increment and check only changed cooked risks before promotion. |


<!-- execution-guidance:start -->
Owner direction30 October: prioritize useful characters in normal gameplay and a playable build. Accept reasonable playtest-quality grip/surface results, record cosmetic gaps and move on. Retain checks for obvious broken motion, missing bodies, crashes and actual integration; avoid broad repeat verification for minor refinements.
<!-- execution-guidance:end -->

## Workstream index

| Workstream | Outstanding owner records | Queue |
| --- | ---: | --- |
| Campaign, co-op and dungeon (F20) | 16 | [Open records](#f20-workstream) |
| Player systems and interface (F26) | 43 | [Open records](#f26-workstream) |
| Combat, NPC simulation and equipment (F25) | 28 | [Open records](#f25-workstream) |
| World, characters, art and audio (F30) | 40 | [Open records](#f30-workstream) |

## Open records

Each record states the remaining outcome and its closure boundary. `needs-triage` means the exact identity, current recurrence or delivery still needs reconciliation; it does not claim a reproduced current defect. Historical priorities are retained in JSON and do not reorder the active batch.

<a id="f20-workstream"></a>

### Campaign, co-op and dungeon

| ID | Item | State | Remaining outcome |
| --- | --- | --- | --- |
| [CHG-002](#chg-002) | Improve vampire approach, attack and wave contact pacing | backlog | Faster readable running/swings, about three contacting together, faster wave cadence and more woodland entry locations; preserve finite saved roster/rewards. |
| [CHG-007](#chg-007) | Stage Peltsmith hunt offers and require real trophy hand-ins | backlog | Small initial selection then earned quarry unlocks; actual vampire fangs and other canonical trophy quantity handed in atomically, meaningful instructions/audio. |
| [CHG-009](#chg-009) | Implement finite funeral-pyre aftermath quest | backlog | The Last Fire: existing eligible dead bodies picked up/carried/released onto real reachable pyre; modest existing-authority reward and protected story evidence. |
| [CHG-010](#chg-010) | Finish meaningful minor-quest library and higher-level progression | backlog | Remaining64-quest target, configurable1–50 progression, fixed world tiers, relative difficulty, local reputation and controlled repeat rewards; reuse existing12 local jobs and bound native scenes. |
| [CHG-017](#chg-017) | Elin needs a real running escort gait | backlog | Install/review prepared bounded walk/run catch-up with actual Run clip, hysteresis, real corners/heading/footfalls, preserving authoritative rescue/leader/arrival/reward/save. Not a live42 fix. |
| [DBG-001](#dbg-001) | Freestanding crypt doorway / hillside integration | backlog | Actual entrance geometry and normal front/side/back approach. |
| [DBG-031](#dbg-031) | Harrowford closed-house entrapment | backlog | Cooked ordinary ingress/login recovery/restart and all service routes not proven by those sweeps. |
| [DBG-051](#dbg-051) | Crypt stair/inter-floor fall and lower-wall gaps | backlog | Original fall cause, exact owner-save recovery and later screenshot geometry/streaming reports remain open; old traversal pass is not global crypt closure. |
| [DBG-054](#dbg-054) | Oversized Courier's Marker board in trail | backlog | Exact-ID modest supported timber marker, route clearance and clue discoverability. |
| [DBG-058](#dbg-058) | Journal tracks only first quest | backlog | Preserve34 aggregated quest list and36 map/tracking foundations. Remaining GUI/remote breadth and durable selection/history are bounded gaps. Missing Harrowford/Rusk compass markers and uncertain watch-task acceptance are separate intake below, not proof saved quest loss. |
| [DBG-069](#dbg-069) | Tracked Harrowford/Rusk compass target missing | backlog | Identify owner-selected target/range/area, admit prepared marker policy as appropriate, verify actual normal HUD bearings/range including known-site vs live captain binding. No installed or rendered fix found. |
| [DBG-070](#dbg-070) | Watch named-person-in-fort task not recorded | needs-triage | Identify quest and distinguish offer from explicit acceptance; inspect saved fact and aggregated journal presentation. Do not assert lost quest state or reroll owner campaign. |
| [DBG-074](#dbg-074) | Historical slot schema not supported | needs-triage | Retain exact old slot/schema/error identity until compatibility is reconciled; current schema46 save proof does not establish all old-slot support. Do not open/change owner saves during tracking. |
| [F19](#f19) | Persistent Friend Groups and Join Codes | backlog | Finish invite/join-code access, account/roster-change policy and broader actual multiplayer starting-roster quorum acceptance; saved group/quorum foundations are already present. |
| [F20](#f20) | Branching Dialogue and Vampire Quest | backlog | Continue consequential vampire chapters, branching outcomes and clear quest wording. Survivor-wave tuning belongs to CHG-002; ordinary acceptance/tracking faults have their own DBG owners. |
| [F22](#f22) | Campaign Dungeon and Persistent Loot | backlog | Finish dungeon dressing, puzzles/secrets, consequential quest branches, unique boss attacks and balance.18 added rooms/3 lower floors and persistent encounters/loot already ship; stair/fall/wall defects stay separately tracked. |

<a id="chg-002"></a>

#### CHG-002 · Improve vampire approach, attack and wave contact pacing

**Close when:** Actual release/admission/route/contact timing and owner-visible encounter density, not configured counts alone.

**Related owners:** [F20](#f20), [F25](#f25), [F59](#f59).

**Local source pointers:** `docs/future-state-priorities.md`.

<a id="chg-007"></a>

#### CHG-007 · Stage Peltsmith hunt offers and require real trophy hand-ins

**Close when:** Unlock vs acceptance vs progress/reward distinct; preserve old accepted hunts and10/30/70 credit; quarry exists before offer; no counterfeit trophies or duplicate payout.

**Related owners:** [F27](#f27), [F33](#f33).

**Local source pointers:** `docs/hunting-contracts-backlog.md`.

<a id="chg-009"></a>

#### CHG-009 · Implement finite funeral-pyre aftermath quest

**Close when:** Real body/rig/carry/contact/burn, co-op claims and save/reload once-only credit; living actors excluded; pause cleanup during quest handling.

**Related owners:** [F20](#f20), [F28](#f28), [F49](#f49).

**Local source pointers:** `docs/future-state-priorities.md`.

<a id="chg-010"></a>

#### CHG-010 · Finish meaningful minor-quest library and higher-level progression

**Close when:** Only genuinely placed/bound definitions offered; actual consumers/tiers/rewards and persistent progression; no claim64 playable quests or level50 from existing partial libraries.

**Related owners:** [F20](#f20), [F26](#f26), [F33](#f33).

**Local source pointers:** `docs/future-state-priorities.md`.

<a id="chg-017"></a>

#### CHG-017 · Elin needs a real running escort gait

**Close when:** Install/review prepared bounded walk/run catch-up with actual Run clip, hysteresis, real corners/heading/footfalls, preserving authoritative rescue/leader/arrival/reward/save. Not a live42 fix.

**Related owners:** [F20](#f20), [F21](#f21).

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/elin43-run-a01/README.md` (recorded path currently missing); `docs/npc-character-replacement-plan.md`.

<a id="dbg-001"></a>

#### DBG-001 · Freestanding crypt doorway / hillside integration

**Close when:** Resolve or explicitly retire this exact reported scope: Actual entrance geometry and normal front/side/back approach.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-031"></a>

#### DBG-031 · Harrowford closed-house entrapment

**Close when:** Resolve or explicitly retire this exact reported scope: Cooked ordinary ingress/login recovery/restart and all service routes not proven by those sweeps.

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| DBG-031.01 | Stone Rill homes inaccessible — Track exact building/door/entry collision and ordinary ingress/exit. Group related house-access task with DBG031 but retain separate village/subcase; unrelated earlier Harrowford ingress proof does not close it. | backlog | Track exact building/door/entry collision and ordinary ingress/exit. Group related house-access task with DBG031 but retain separate village/subcase; unrelated earlier Harrowford ingress proof does not close it. |

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-051"></a>

#### DBG-051 · Crypt stair/inter-floor fall and lower-wall gaps

**Close when:** Resolve or explicitly retire this exact reported scope: Original fall cause, exact owner-save recovery and later screenshot geometry/streaming reports remain open; old traversal pass is not global crypt closure.

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| DBG-051.01 | Tower stair traversal — User-deferred location; preserve status and exact location/normal route details. Do not newly activate or call closed from Harrowford stairs. | deferred | User-deferred location; preserve status and exact location/normal route details. Do not newly activate or call closed from Harrowford stairs. |

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-054"></a>

#### DBG-054 · Oversized Courier's Marker board in trail

**Close when:** Resolve or explicitly retire this exact reported scope: Exact-ID modest supported timber marker, route clearance and clue discoverability.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-058"></a>

#### DBG-058 · Journal tracks only first quest

**Close when:** Resolve or explicitly retire this exact reported scope: Preserve34 aggregated quest list and36 map/tracking foundations. Remaining GUI/remote breadth and durable selection/history are bounded gaps. Missing Harrowford/Rusk compass markers and uncertain watch-task acceptance are separate intake below, not proof saved quest loss.

**Related owners:** [F20](#f20), [F37](#f37).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| DBG-058.01 | Make acceptance and selected quest tracking durable/discoverable — Correct committed acceptance in journal/chapter with giver/objective/progress/status; persistent chosen main/side/bandit/hunt tracked task and destination guidance. | backlog | Actual guard accept vs Core persisted bounty vs projection reconciled; chosen track survives save/reconnect and new offers don't replace it. |

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`; `docs/future-state-priorities.md`.

<a id="dbg-069"></a>

#### DBG-069 · Tracked Harrowford/Rusk compass target missing

**Close when:** Identify owner-selected target/range/area, admit prepared marker policy as appropriate, verify actual normal HUD bearings/range including known-site vs live captain binding. No installed or rendered fix found.

**Related owners:** [DBG-058](#dbg-058), [F20](#f20).

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/quest-compass40/README.md`.

<a id="dbg-070"></a>

#### DBG-070 · Watch named-person-in-fort task not recorded

**Close when:** Identify quest and distinguish offer from explicit acceptance; inspect saved fact and aggregated journal presentation. Do not assert lost quest state or reroll owner campaign.

**Related owners:** [DBG-058](#dbg-058), [F20](#f20).

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/watch-quest-journal40/README.md`.

<a id="dbg-074"></a>

#### DBG-074 · Historical slot schema not supported

**Close when:** Retain exact old slot/schema/error identity until compatibility is reconciled; current schema46 save proof does not establish all old-slot support. Do not open/change owner saves during tracking.

**Local source pointers:** `docs/debug-triage.md`.

<a id="f19"></a>

#### F19 · Persistent Friend Groups and Join Codes

**Close when:** Finish invite/join-code access, account/roster-change policy and broader actual multiplayer starting-roster quorum acceptance; saved group/quorum foundations are already present.

**Related owners:** [F20](#f20), [F33](#f33), [F51](#f51), [F60](#f60).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| F19.01 | Resolve campaign story-choice and absent-member policy gaps — Explicit authored story-choice resolution, reward catch-up/story recap for absent originals and deliberate starting-roster change policy; distinguish presence quorum from decision voting. | backlog | Document chosen supported policy then implement existing server commit/reward/save authorities with guest/duplicate/reconnect handling; no silent quorum shrink or invented free rewards. |

**Local source pointers:** `docs/campaign-meeting-implementation.md`; `docs/journey-playtest8-delivery.md`; `docs/backlog-status.md`; `docs/future-state-priorities.md`.

<a id="f20"></a>

#### F20 · Branching Dialogue and Vampire Quest

**Close when:** Continue consequential vampire chapters and clearer global quest wording; finish actual survivor-wave pacing/direction/encounter quality and requested vampire presentation. Opening, meeting, Hollow Tithe and bounded run-in/waves are delivered.

**Related owners:** [F03](#f03), [F19](#f19), [F21](#f21), [F22](#f22), [F56](#f56).

**Local source pointers:** `docs/backlog-status.md`; `docs/journey-playtest32-delivery.md`; `docs/future-state-priorities.md`.

<a id="f22"></a>

#### F22 · Campaign Dungeon and Persistent Loot

**Close when:** Finish dungeon dressing, puzzles/secrets, consequential quest branches, unique boss attacks and balance.18 added rooms/3 lower floors and persistent encounters/loot already ship; stair/fall/wall defects stay separately tracked.

**Related owners:** [DBG-051](#dbg-051), [F20](#f20), [F25](#f25).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| F22.01 | Deeper dungeon content and ordinary route acceptance — Finish lower-level dressing/walls, reliable stair/support/pursuit, meaningful puzzles/secrets, bosses and bone-pile awakening. | backlog | Actual ordinary routes/support/awakening and original saved encounter/loot authority; finite lower18rooms are existing foundation. |

**Local source pointers:** `docs/journey-playtest13-delivery.md`; `docs/backlog-status.md`; `docs/backlog-status.md`.

<a id="f26-workstream"></a>

### Player systems and interface

| ID | Item | State | Remaining outcome |
| --- | --- | --- | --- |
| [CHG-001](#chg-001) | Increase player overland travel speed | backlog | Review current travel multipliers and increase overland pace without changing unrelated combat timing or destabilizing authority/collision. |
| [CHG-008](#chg-008) | Add premium paid direct healing service | backlog | Sabeth direct health restoration with shown configurable premium fee/amount, existing living/in-range authority. |
| [CHG-014](#chg-014) | Review cleanup candidates after active delivery | backlog | Measure/classify cold map backup families,92 worktrees, superseded tools, generated output/caches, duplicate runtime assets and stale documentation. |
| [CHG-018](#chg-018) | Cap new ordinary vampire corpse loot to five arrows total | backlog | Apply trusted-context cumulative cap before first new-death commit across canonical arrow types; compile focused prepared tests and native ordinary-death proof; saved loot, fixed rewards/RNG/non-arrow output remain intact. Prepared only. |
| [DBG-010](#dbg-010) | Post-level ability/stat-point allocation | backlog | Durable post-level ability milestone/spend contract and UI; current reviewed reports do not prove it delivered. |
| [DBG-011](#dbg-011) | Level-up sound and full-health reward | backlog | No reviewed receipt establishes health-only durable once-per-gain/replay semantics or complete listening acceptance. |
| [DBG-022](#dbg-022) | Text/frame scaling and low-resolution UI | backlog | All-screen/Options/readability/long-card breadth; old17 creator crop is not unchanged current behavior. |
| [DBG-024](#dbg-024) | Peltsmith recovery should not grant class armor | backlog | No new all-branch native/replay grant proof added by this audit; visual wrong limbs is029. |
| [DBG-025](#dbg-025) | Inventory-moved notification noise | needs-triage | Reviewed queue lacks exact accepted scoped UI delivery; current release recurrence not established. |
| [DBG-038](#dbg-038) | Message separation, scrolling, history and expiry | backlog | Durable across-restart history is not delivered; broad scaling/timed readability remains distinct. |
| [DBG-043](#dbg-043) | Immovable blacksmith props / universal small-object coverage | backlog | Universal new/embedded placements and explicit exceptions; category coverage is not global support or every object's inventory semantics. Distinct crash040 and support049 remain. |
| [DBG-049](#dbg-049) | Off-area loose prop falls through interior support | backlog | Actual off-area support/activation failure remains; fresh dropped-bow hovering and attached-harvestable Save refusal have distinct causes and are not counted as fixes of this support case. |
| [DBG-050](#dbg-050) | Healer wall/shop; newer Harrowford seller discoverability | backlog | The old healer wall/shop defect shipped21; preserve that scoped closure. Remaining later ordinary-goods/seller discoverability report needs the exact attempted vendor/item and normal reachable trade; Herb Gatherer is not Sabeth. |
| [DBG-056](#dbg-056) | Borrowed tunic missing icon | backlog | Accurate tunic art/binding and inventory/card coverage; do not alias unrelated robe. |
| [DBG-062](#dbg-062) | Armor icons include adjacent set fragments | backlog | Admit eight prepared isolated atlas rectangles; repair Ranger/Druid overlap without cropping approved full silhouettes; actual imported/native inventory/loot views must display correct item artwork. Prepared CPU proof is not native acceptance. |
| [DBG-063](#dbg-063) | Iron Shield round model disagrees with kite icon | backlog | Create accurate transparent icon from actual existing round IronShield source using established native capture/import, preserving source UV/materials and item identity. Merge historical silver-shield/icon-correspondence report if same canonical item, otherwise retain distinct unresolved identity. |
| [DBG-067](#dbg-067) | Manual Save refusal due to unsettled loose-object state | needs-triage | Attached-harvestable eligibility correction has source build/menu Save/snapshot/reopen proof. Exact original owner blocker and later packaged inclusion/acceptance are not established by41/42 release summaries. Reconcile source/freeze then identify real outstanding blocker; do not describe known source defect as unfixed or claim universal Save closure. |
| [DBG-068](#dbg-068) | Freshly dropped bow stays floating | backlog | Identify exact dropped actor/item; correct fresh-launch row vs settled-restore initialization with actual gravity/support and saved recovery. No integrated correction established; distinct from off-area support fallthrough. |
| [DBG-073](#dbg-073) | Red container outlines | needs-triage | Historical report lacks exact source/current recurrence or accepted fix. Identify overlay/debug/material cause before modifying all containers. |
| [F04](#f04) | Empty and Poor-Quality Loot | backlog | Add meaningful broken/rotten poor-quality item pools; retain existing saved randomized and empty outcomes. |
| [F08](#f08) | Corpse Containers and Loot All | backlog | Finish an explicitly labeled Loot All action and configurable quick-loot binding with capacity/retry/concurrent-claim behavior; existing corpse/container screens and bounded transfers remain delivered. |
| [F09](#f09) | Lootable Cupboards and Closets | backlog | Bind remaining cupboards/closets/scenery supply containers to suitable persistent contents; resolve the 16 recorded scenery-crate policies. |
| [F10](#f10) | torso Keys and Lockpicking | backlog | Extend access-policy variety and deeper lock interaction where requested; existing keys, DEX authority and illustrated lockpicking are delivered foundations. |
| [F11](#f11) | Realistic Fall Damage | backlog | Finish the explicitly requested landing sound and camera/animation feedback. The real server impact-speed damage/Acrobatics mechanic already shipped6; hypothetical universal verification is not an additional backlog task. |
| [F12](#f12) | Drop Items and Stacks | backlog | Extend selected stack-quantity dropping and supported-item/state coverage; DROP1 bread/books is shipped and canonical gear round-trip expanded28. Preserve rolls, condition, ownership, identity and recovery. |
| [F13](#f13) | Household Loot and Loose Coins | backlog | Finish unresolved ordinary household bindings and extend shared denomination/coin art to tables, barrels and humanoid corpse sources without duplicate grants. Broad useful loot is already shipped28 and purses39. |
| [F16](#f16) | D&D Starting Ability and Skill Points | backlog | Finish explicit manual starting skill-allocation policy and acceptance plus genuine remaining skill consumers; preserve delivered six-ability creation, saved class training and derived effects. Post-level ability allocation is separate DBG-010. |
| [F17](#f17) | Smashable containers and Fragile Contents | backlog | Add destructible loot-container coverage and permanent fragile-content loss with quest safeguards; existing barrel smashing is not universal destruction. |
| [F18](#f18) | Stats for Every Item | backlog | Finish per-item stats, effective-use level policy, rarity and equipment comparison. Numbered sub-items own the specific new requirements; exact icon defects are DBG-062/063. |
| [F23](#f23) | Ledge Climbing and Rigged Traversal | backlog | Implement actual action/jump ledge climbing with fitted rig/IK and replicated traversal; ordinary stair repairs do not deliver climbing. |
| [F26](#f26) | Progression, Class Abilities and Magic | backlog | Finish class/ancestry ability consumers, spellbook breadth, spell presentation and environmental interaction. Campaign XP balance remains F33; initial skill allocation F16; learned-rank audio F15. |
| [F28](#f28) | Movable World Objects and Physics | backlog | Complete actual carrying/dragging, placement-preview and shared movable-object interaction. Household item meaning/binding is F13; unresolved move coverage and support faults are DBG-043/049; floating fresh drops are DBG-068. |
| [F29](#f29) | Stealth, Crime and Faction Systems | backlog | Finish NPC pickpocket runtime admission, guard arrest/fines/jail and coherent broader faction consequences. Crouch/LOS evasion, witnessed theft, stolen provenance and finite Venn fence are already shipped. |
| [F33](#f33) | XP and Leveling Balance | backlog | Balance campaign/party progression, slow earned levels, quest XP, high-level rewards and anti-farming across actual encounters. Current saved talent progression reaches20; historical10-cap text is superseded. |
| [F36](#f36) | Caster Spell Quick Slots | backlog | Extend learned spellbook/loadout selection and wider caster-slot coverage; existing two-slot rebinding, costs/cooldowns and class signatures remain delivered. |
| [F37](#f37) | Clean HUD and Weapon Quick Swap | backlog | Finish the common visual theme, inventory/vendor screen composition and input presentation. Specific low-resolution/card/paging defects belong to DBG-022, durable message history to DBG-038 and quest tracking to DBG-058. |
| [F38](#f38) | Recipe Discovery and Intelligence | backlog | Implement actual experimental/quest/NPC recipe discovery with sensible material tags, known-only recipe UI, bounded loss/Intelligence policy and real supplied ingredients;34 proposals are design data, not installed recipes. |
| [F39](#f39) | Switchable Third-Person View | backlog | Implement supported first/third-person gameplay switching, camera collision, aiming and replication/presentation acceptance; remote models and preview cameras do not establish this feature. |
| [F40](#f40) | Exploration-Based Ore and Mining | backlog | Expand exploration-led mineral/plant/tree gathering and mining/felling art/animations/station quality; existing outcrops, registered-tree harvest and tools already exist. |
| [F43](#f43) | Alchemy, Smithing and Enchanting | backlog | Deepen real ingredient effects, equipment improvement/repair and enchanting/soul-gem consumers;41 current recipes/station transactions are foundations, not the proposed discovery library. |
| [F44](#f44) | Merchant Restocking and Economy Balance | backlog | Finish world-clock merchant purse/stock replenishment, requested price/healer rebalance and exploit-resistant wider economy balance; finite saved shops and actual transactions/fence are delivered. |
| [F45](#f45) | Discovery and Persistent Maps | backlog | Finish persisted map pins, atlas/fog/routefinding and discovery coverage. Personal discovery/pan/zoom already ship. Durable quest selection is DBG-058, missing target marker DBG-069 and faster overland pace CHG-001. |
| [F46](#f46) | Swimming and Water Traversal | backlog | Implement genuine swimming/water movement/depth interaction with appropriate physics/network rules; water appearance and deep-water fall guards do not prove swimming. |

<a id="chg-001"></a>

#### CHG-001 · Increase player overland travel speed

**Close when:** Chosen tuning with measured travel behavior, proper animations, saved/client agreement and no campaign reset.

**Related owners:** [F45](#f45), [F59](#f59).

**Local source pointers:** `docs/future-state-priorities.md`.

<a id="chg-008"></a>

#### CHG-008 · Add premium paid direct healing service

**Close when:** Payment+healing atomic, full health not charged, insufficient funds/retries no heal/debit duplication; preserve finite shop/ledger/story.

**Related owners:** [F27](#f27), [F44](#f44).

**Local source pointers:** `docs/healer21.md`.

<a id="chg-014"></a>

#### CHG-014 · Review cleanup candidates after active delivery

**Close when:** Exact candidate purposes/hashes/recovery value and measured saving reviewed before any removal; source art/UV, unique saves/crashes and useful caches protected.

**Local source pointers:** `docs/cleanup-opportunities.md`.

<a id="chg-018"></a>

#### CHG-018 · Cap new ordinary vampire corpse loot to five arrows total

**Close when:** Apply trusted-context cumulative cap before first new-death commit across canonical arrow types; compile focused prepared tests and native ordinary-death proof; saved loot, fixed rewards/RNG/non-arrow output remain intact. Prepared only.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/loot43-debug-a01/README.md`.

<a id="dbg-010"></a>

#### DBG-010 · Post-level ability/stat-point allocation

**Close when:** Resolve or explicitly retire this exact reported scope: Durable post-level ability milestone/spend contract and UI; current reviewed reports do not prove it delivered.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-011"></a>

#### DBG-011 · Level-up sound and full-health reward

**Close when:** Resolve or explicitly retire this exact reported scope: No reviewed receipt establishes health-only durable once-per-gain/replay semantics or complete listening acceptance.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-022"></a>

#### DBG-022 · Text/frame scaling and low-resolution UI

**Close when:** Resolve or explicitly retire this exact reported scope: All-screen/Options/readability/long-card breadth; old17 creator crop is not unchanged current behavior.

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| DBG-022.01 | Loot card labels and artwork crop against frame — Admit prepared storage-card icon inset/measured-font name box; verify actual font/frame at target and low resolutions and unchanged hit coordinates/stats. Separate from source-atlas bleed. | backlog | Admit prepared storage-card icon inset/measured-font name box; verify actual font/frame at target and low resolutions and unchanged hit coordinates/stats. Separate from source-atlas bleed. |
| DBG-022.02 | Inventory paging historical report — Previously unreproduced; retain historical report and exact reproduction needed. Do not claim currently broken or schedule blanket UI rewrite. | needs-triage | Previously unreproduced; retain historical report and exact reproduction needed. Do not claim currently broken or schedule blanket UI rewrite. |

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`; `tools/prepared/loot43-debug-a01/README.md`.

<a id="dbg-024"></a>

#### DBG-024 · Peltsmith recovery should not grant class armor

**Close when:** Resolve or explicitly retire this exact reported scope: No new all-branch native/replay grant proof added by this audit; visual wrong limbs is029.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-025"></a>

#### DBG-025 · Inventory-moved notification noise

**Close when:** Resolve or explicitly retire this exact reported scope: Reviewed queue lacks exact accepted scoped UI delivery; current release recurrence not established.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-038"></a>

#### DBG-038 · Message separation, scrolling, history and expiry

**Close when:** Resolve or explicitly retire this exact reported scope: Durable across-restart history is not delivered; broad scaling/timed readability remains distinct.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-043"></a>

#### DBG-043 · Immovable blacksmith props / universal small-object coverage

**Close when:** Resolve or explicitly retire this exact reported scope: Universal new/embedded placements and explicit exceptions; category coverage is not global support or every object's inventory semantics. Distinct crash040 and support049 remain.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-049"></a>

#### DBG-049 · Off-area loose prop falls through interior support

**Close when:** Resolve or explicitly retire this exact reported scope: Actual off-area support/activation failure remains; fresh dropped-bow hovering and attached-harvestable Save refusal have distinct causes and are not counted as fixes of this support case.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-050"></a>

#### DBG-050 · Healer wall/shop; newer Harrowford seller discoverability

**Close when:** Resolve or explicitly retire this exact reported scope: The old healer wall/shop defect shipped21; preserve that scoped closure. Remaining later ordinary-goods/seller discoverability report needs the exact attempted vendor/item and normal reachable trade; Herb Gatherer is not Sabeth.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-056"></a>

#### DBG-056 · Borrowed tunic missing icon

**Close when:** Resolve or explicitly retire this exact reported scope: Accurate tunic art/binding and inventory/card coverage; do not alias unrelated robe.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-062"></a>

#### DBG-062 · Armor icons include adjacent set fragments

**Close when:** Admit eight prepared isolated atlas rectangles; repair Ranger/Druid overlap without cropping approved full silhouettes; actual imported/native inventory/loot views must display correct item artwork. Prepared CPU proof is not native acceptance.

**Related owners:** [F18](#f18), [F24](#f24).

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/loot43-debug-a01/README.md`.

<a id="dbg-063"></a>

#### DBG-063 · Iron Shield round model disagrees with kite icon

**Close when:** Create accurate transparent icon from actual existing round IronShield source using established native capture/import, preserving source UV/materials and item identity. Merge historical silver-shield/icon-correspondence report if same canonical item, otherwise retain distinct unresolved identity.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/loot43-debug-a01/README.md`.

<a id="dbg-067"></a>

#### DBG-067 · Manual Save refusal due to unsettled loose-object state

**Close when:** Attached-harvestable eligibility correction has source build/menu Save/snapshot/reopen proof. Exact original owner blocker and later packaged inclusion/acceptance are not established by41/42 release summaries. Reconcile source/freeze then identify real outstanding blocker; do not describe known source defect as unfixed or claim universal Save closure.

**Related owners:** [DBG-049](#dbg-049).

**Local source pointers:** `docs/debug-triage.md`; `PROJECT_LOG.md`; `evidence/unreal/loose-save-attached40-7e51116d88/verification.json`.

<a id="dbg-068"></a>

#### DBG-068 · Freshly dropped bow stays floating

**Close when:** Identify exact dropped actor/item; correct fresh-launch row vs settled-restore initialization with actual gravity/support and saved recovery. No integrated correction established; distinct from off-area support fallthrough.

**Related owners:** [DBG-049](#dbg-049), [F12](#f12).

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/dropped-bow-floating40/README.md`.

<a id="dbg-073"></a>

#### DBG-073 · Red container outlines

**Close when:** Historical report lacks exact source/current recurrence or accepted fix. Identify overlay/debug/material cause before modifying all containers.

**Local source pointers:** `docs/debug-triage.md`.

<a id="f04"></a>

#### F04 · Empty and Poor-Quality Loot

**Close when:** Add meaningful broken/rotten poor-quality item pools; retain existing saved randomized and empty outcomes.

**Related owners:** [F18](#f18).

**Local source pointers:** `docs/encounter-loot.md`; `docs/backlog-status.md`.

<a id="f08"></a>

#### F08 · Corpse Containers and Loot All

**Close when:** Finish an explicitly labeled Loot All action and configurable quick-loot binding with capacity/retry/concurrent-claim behavior; existing corpse/container screens and bounded transfers remain delivered.

**Related owners:** [F02](#f02), [F13](#f13), [F49](#f49).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| F08.01 | Implement contextual right-click looting in UI and world — One RMB press takes from an open loot row or collects/opens a valid world source, universally through existing authority and Take/Steal/access rules. | backlog | No double dispatch/hold-repeat, lock bypass, item consume/equip during take or loss of normal shield block/map/menu/rotation RMB meanings. |

**Local source pointers:** `docs/loot-player-foliage-delivery-0.20.11.md`; `docs/future-state-priorities.md`; `docs/future-state-priorities.md`.

<a id="f09"></a>

#### F09 · Lootable Cupboards and Closets

**Close when:** Bind remaining cupboards/closets/scenery supply containers to suitable persistent contents; resolve the 16 recorded scenery-crate policies.

**Related owners:** [F13](#f13), [F17](#f17), [F28](#f28).

**Local source pointers:** `docs/journey-playtest28-delivery.md`; `docs/backlog-status.md`.

<a id="f10"></a>

#### F10 · torso Keys and Lockpicking

**Close when:** Extend access-policy variety and deeper lock interaction where requested; existing keys, DEX authority and illustrated lockpicking are delivered foundations.

**Related owners:** [F29](#f29).

**Local source pointers:** `docs/backlog-status.md`; `docs/journey-playtest27-delivery.md`.

<a id="f11"></a>

#### F11 · Realistic Fall Damage

**Close when:** Finish the explicitly requested landing sound and camera/animation feedback. The real server impact-speed damage/Acrobatics mechanic already shipped6; hypothetical universal verification is not an additional backlog task.

**Related owners:** [DBG-051](#dbg-051), [F23](#f23), [F46](#f46).

**Local source pointers:** `docs/journey-playtest6-integration.md`; `docs/ash-march-journey-playtest6-results.md`; `docs/class-talent-release8.md`; `docs/fall-damage-acrobatics.md`; `docs/future-state-priorities.md`.

<a id="f12"></a>

#### F12 · Drop Items and Stacks

**Close when:** Extend selected stack-quantity dropping and supported-item/state coverage; DROP1 bread/books is shipped and canonical gear round-trip expanded28. Preserve rolls, condition, ownership, identity and recovery.

**Related owners:** [DBG-049](#dbg-049), [F13](#f13), [F28](#f28).

**Local source pointers:** `docs/ash-march-journey-playtest11.md`; `docs/world-interaction11.md`; `docs/journey-playtest28-delivery.md`.

<a id="f13"></a>

#### F13 · Household Loot and Loose Coins

**Close when:** Finish unresolved ordinary household bindings and extend shared denomination/coin art to tables, barrels and humanoid corpse sources without duplicate grants. Broad useful loot is already shipped28 and purses39.

**Related owners:** [DBG-043](#dbg-043), [F08](#f08), [F09](#f09), [F18](#f18), [F28](#f28), [F29](#f29).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| F13.01 | Extend denomination coin art to tables, barrels and humanoid corpse loot — Use each source's actual saved claim/currency state to render remaining coins and partial depletion. | backlog | No second currency grant/refill; ownership, difficulty/loot tables, concurrent claims and reload preserved. |
| F13.02 | Finish universal portable object loot/physics binding coverage — Remaining loose household/attached/new placements and16 scenery supply crates require explicit canonical item binding or named gap; supports need actual physical collision. | backlog | Normal collection/drop/rest on real supports, ownership/provenance and once-only inventory authority across streamed world; finite eight-map audit is not universal coverage. |

**Local source pointers:** `docs/journey-playtest28-delivery.md`; `docs/journey-playtest39-delivery.md`; `docs/future-state-priorities.md`; `docs/future-state-priorities.md`; `docs/backlog-status.md`.

<a id="f16"></a>

#### F16 · D&D Starting Ability and Skill Points

**Close when:** Finish explicit manual starting skill-allocation policy and acceptance plus genuine remaining skill consumers; preserve delivered six-ability creation, saved class training and derived effects. Post-level ability allocation is separate DBG-010.

**Related owners:** [DBG-010](#dbg-010), [F26](#f26), [F33](#f33).

**Local source pointers:** `docs/stat-progression.md`; `docs/class-talent-release8.md`; `docs/debug-triage.md`.

<a id="f17"></a>

#### F17 · Smashable containers and Fragile Contents

**Close when:** Add destructible loot-container coverage and permanent fragile-content loss with quest safeguards; existing barrel smashing is not universal destruction.

**Related owners:** [F09](#f09), [F18](#f18).

**Local source pointers:** `docs/briarwatch-dungeon-loot.md`; `docs/future-state-priorities.md`.

<a id="f18"></a>

#### F18 · Stats for Every Item

**Close when:** Finish per-instance rare/epic affixes, meaningful level bands/equipment comparison and full item/protection balance;266 canonical useful items already ship.

**Related owners:** [F13](#f13), [F24](#f24), [F33](#f33), [F37](#f37), [F62](#f62), [F64](#f64).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| F18.01 | Implement loot level bands and meaningful effective-use policy — Player-level-aware ordinary drop bands respecting creature/region danger; define boundaries, shared party snapshot, under-level penalties/equip policy and authored exceptions. | backlog | Band-boundary/use tests across vendors, corpse/container/quest/craft/stolen/loose/trade paths; no reroll/reset of persistent items. |
| F18.02 | Show equipped-versus-inventory effective-stat comparison — Compare selected item against actual slot with requirements/effective damage/armor/bonuses/condition/weight/value and signed differences, including two-hand consequences. | backlog | UI values match authoritative character calculations, empty/same-slot/ineligible/two-handed cases and non-color-only explanation. |
| F18.03 | Implement persistent tier rarity/affixes with common-only rusty equipment — D&D5e-inspired adapted real effects; authoritative once-only per-instance weighted rolls, material/tier ranges and explicit story exceptions. | backlog | Shared saved stats/effects visible identically across transfers, inspection races and restart; no rusty rare/epic gear or cosmetic-only promised effects. |
| F18.04 | Iron Shield awarded too early — Choose explicit normal-random-drop restriction/minimum policy and integrate only eligible future rolls; preserve carried-equipment loot, hard/deep rewards as decided, saved shields and canonical identity. User supplied no exact minimum tier. | backlog | Choose explicit normal-random-drop restriction/minimum policy and integrate only eligible future rolls; preserve carried-equipment loot, hard/deep rewards as decided, saved shields and canonical identity. User supplied no exact minimum tier. |

**Local source pointers:** `docs/journey-playtest28-delivery.md`; `docs/loot-level-bands27.md`; `docs/backlog-status.md`; `docs/loot-level-bands27.md`; `docs/loot-level-bands27.md`; `docs/future-state-priorities.md`; `docs/debug-triage.md`; `tools/prepared/loot43-debug-a01/README.md`.

<a id="f23"></a>

#### F23 · Ledge Climbing and Rigged Traversal

**Close when:** Implement actual action/jump ledge climbing with fitted rig/IK and replicated traversal; ordinary stair repairs do not deliver climbing.

**Related owners:** [F11](#f11), [F39](#f39), [F46](#f46).

**Local source pointers:** `docs/stair-traversal.md`; `docs/future-state-priorities.md`.

<a id="f26"></a>

#### F26 · Progression, Class Abilities and Magic

**Close when:** Finish distinct active class/ancestry abilities, high-level consumers, complete spellbooks, bespoke icons/gestures/VFX and campaign balance.216 catalogue nodes and12 class-signature consumers already exist.

**Related owners:** [F16](#f16), [F33](#f33), [F36](#f36), [F43](#f43), [F58](#f58).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| F26.01 | Complete distinct spell effects, free targeting and combustible responses — Distinct cast/travel/impact/voice/gesture signatures per class/spell/NPC; real Lance beam, free casting without hostile target, general trees/grass/wood ignition. | backlog | Actual spell consumers/resource/recovery/interruption and replicated environmental burn/extinguish/persistence rules; define spread/duration before claiming implemented. |

**Local source pointers:** `docs/journey-playtest26-delivery.md`; `docs/journey-playtest30-delivery.md`; `docs/backlog-status.md`; `docs/future-state-priorities.md`.

<a id="f28"></a>

#### F28 · Movable World Objects and Physics

**Close when:** Finish universal portable-object/carry/drag/support/network coverage and explicit bindings/exceptions for new and embedded placements.732 original portable placements and later canonical collection/drop are finite delivered coverage.

**Related owners:** [DBG-043](#dbg-043), [DBG-049](#dbg-049), [F12](#f12), [F13](#f13), [F49](#f49).

**Local source pointers:** `docs/world-interaction12-progress.md`; `docs/journey-playtest28-delivery.md`; `docs/universal-loot.md`; `docs/backlog-status.md`.

<a id="f29"></a>

#### F29 · Stealth, Crime and Faction Systems

**Close when:** Finish NPC pickpocket runtime admission, guard arrest/fines/jail and coherent broader faction consequences. Crouch/LOS evasion, witnessed theft, stolen provenance and finite Venn fence are already shipped.

**Related owners:** [F10](#f10), [F13](#f13), [F44](#f44), [F56](#f56).

**Local source pointers:** `docs/journey-playtest27-delivery.md`; `docs/journey-playtest28-delivery.md`; `docs/backlog-status.md`.

<a id="f33"></a>

#### F33 · XP and Leveling Balance

**Close when:** Balance campaign/party progression, slow earned levels, quest XP, high-level rewards and anti-farming across actual encounters. Current saved talent progression reaches20; historical10-cap text is superseded.

**Related owners:** [DBG-010](#dbg-010), [DBG-011](#dbg-011), [F16](#f16), [F26](#f26), [F32](#f32).

**Local source pointers:** `docs/journey-playtest30-delivery.md`; `docs/backlog-status.md`; `docs/future-state-priorities.md`.

<a id="f36"></a>

#### F36 · Caster Spell Quick Slots

**Close when:** Extend learned spellbook/loadout selection and wider caster-slot coverage; existing two-slot rebinding, costs/cooldowns and class signatures remain delivered.

**Related owners:** [F26](#f26), [F37](#f37).

**Local source pointers:** `docs/combat-vendor-delivery-0.20.8.md`; `docs/journey-playtest26-delivery.md`; `docs/backlog-status.md`.

<a id="f37"></a>

#### F37 · Clean HUD and Weapon Quick Swap

**Close when:** Finish universal readable/low-resolution/long-label UI, durable message history/tracked selection, broader input/remote acceptance and final HUD/inventory/journal polish. Existing controls, weapon swaps and five journal chapters ship.

**Related owners:** [DBG-022](#dbg-022), [DBG-025](#dbg-025), [DBG-038](#dbg-038), [DBG-056](#dbg-056), [DBG-058](#dbg-058), [F05](#f05), [F35](#f35), [F36](#f36), [F45](#f45).

**Local source pointers:** `docs/backlog-status.md`; `docs/journey-playtest34-delivery.md`; `docs/journey-playtest35-delivery.md`.

<a id="f38"></a>

#### F38 · Recipe Discovery and Intelligence

**Close when:** Implement actual experimental/quest/NPC recipe discovery with sensible material tags, known-only recipe UI, bounded loss/Intelligence policy and real supplied ingredients;34 proposals are design data, not installed recipes.

**Related owners:** [F40](#f40), [F43](#f43).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| F38.01 | Hide undiscovered recipes and implement shared discovery/experimentation — Practical starter set, shared campaign knowledge via books/teachers/quests/experiments, ordinary byproducts and2–3-input recipes, Intelligence-based disclosed bounded failure/loss. | backlog | Known recipes consistent across station categories; atomic loss/output/unlock and retry persistence, no unknown-output leak/free rerolls; first-tool path maintained. |

**Local source pointers:** `docs/crafting-discovery-design.md`; `docs/backlog-status.md`; `docs/future-state-priorities.md`.

<a id="f39"></a>

#### F39 · Switchable Third-Person View

**Close when:** Implement supported first/third-person gameplay switching, camera collision, aiming and replication/presentation acceptance; remote models and preview cameras do not establish this feature.

**Related owners:** [F23](#f23), [F37](#f37), [F59](#f59).

**Local source pointers:** `docs/future-state-priorities.md`; `docs/feature-chat-index.json`.

<a id="f40"></a>

#### F40 · Exploration-Based Ore and Mining

**Close when:** Expand exploration-led mineral/plant/tree gathering and mining/felling art/animations/station quality; existing outcrops, registered-tree harvest and tools already exist.

**Related owners:** [F28](#f28), [F31](#f31), [F38](#f38), [F43](#f43), [F61](#f61).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| F40.01 | Make all standing trees visibly fellable through real axe contact — All scenery/resource trees get stable depletion identity, equipped-axe contact swings, wood chips, visible felling and recoverable ground logs. | backlog | Interrupted/simultaneous chopping, slopes/collision, host/client/restart no duplicate yields; ordinary F registered-tree harvest isn't full requested behavior. |

**Local source pointers:** `docs/backlog-status.md`; `docs/future-state-priorities.md`; `docs/future-state-priorities.md`.

<a id="f43"></a>

#### F43 · Alchemy, Smithing and Enchanting

**Close when:** Deepen real ingredient effects, equipment improvement/repair and enchanting/soul-gem consumers;41 current recipes/station transactions are foundations, not the proposed discovery library.

**Related owners:** [F18](#f18), [F38](#f38), [F40](#f40), [F62](#f62).

**Local source pointers:** `docs/backlog-status.md`; `docs/crafting-discovery-design.md`.

<a id="f44"></a>

#### F44 · Merchant Restocking and Economy Balance

**Close when:** Finish world-clock merchant purse/stock replenishment, requested price/healer rebalance and exploit-resistant wider economy balance; finite saved shops and actual transactions/fence are delivered.

**Related owners:** [F18](#f18), [F29](#f29).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| F44.01 | Rebalance vendor prices and complete usable ordinary buyers — Premium service/economy tuning and identifiable/reachable actual town buyers for ordinary catalogue goods, clear shop vs ambient/fence and eligibility feedback. | backlog | Actual attempted trader/item/reach accepted; finite purse/stock/capacity/stolen rules retained. |

**Local source pointers:** `docs/backlog-status.md`; `docs/inventory-loot-design.md`; `docs/future-state-priorities.md`; `docs/backlog-status.md`.

<a id="f45"></a>

#### F45 · Discovery and Persistent Maps

**Close when:** Finish persistent selected pins/tracking, wider atlas/fog/routefinding and discoverable-site coverage. Journey36 already delivers27-entry personal discovery, actual map pan/zoom/recenter, compass bearing/distance; pins are session-local. Marker defects remain separately tracked.

**Related owners:** [DBG-058](#dbg-058), [F37](#f37), [F55](#f55).

**Local source pointers:** `docs/journey-playtest36-delivery.md`; `docs/map-and-compass.md`; `docs/backlog-status.md`.

<a id="f46"></a>

#### F46 · Swimming and Water Traversal

**Close when:** Implement genuine swimming/water movement/depth interaction with appropriate physics/network rules; water appearance and deep-water fall guards do not prove swimming.

**Related owners:** [F11](#f11), [F23](#f23), [F50](#f50).

**Local source pointers:** `docs/world-water-delivery.md`; `docs/fall-damage-acrobatics.md`; `docs/future-state-priorities.md`.

<a id="f25-workstream"></a>

### Combat, NPC simulation and equipment

| ID | Item | State | Remaining outcome |
| --- | --- | --- | --- |
| [CHG-003](#chg-003) | Strengthen spiders and implement real venom/counterplay | backlog | Authored stat tuning across ordinary/roaming/authored paths; server hit-driven poison with bounded cadence/duration/refresh/resistance and cure. |
| [CHG-004](#chg-004) | Rename Shell Pincers and add grouped/huge variants | backlog | Player-facing rename preserving mudcrab IDs; ordinary groups, persisted50% chance of one additional huge cohort member, stronger threat/XP and matching scale/collision/animation. |
| [CHG-005](#chg-005) | Add bounded nearby allied assistance including starter Wood Shrews | backlog | Shared species/faction/pack assist policy covering starter/nest/director/legacy paths, actual local alert and movement without map-wide relay. |
| [CHG-006](#chg-006) | Complete requested wildlife families and ordinary renewable monster supply | backlog | Actual snakes, bears, wildcats and crows in suitable habitats; ordinary vampire/werewolf renewable suppliers for relevant hunts. |
| [CHG-012](#chg-012) | Complete suitable humanoid night lights and handoffs | backlog | Torch/lantern/restrained magic on supported characters at night, body/belt attachment when both hands busy and player extinguishing for stealth. |
| [CHG-013](#chg-013) | Implement bounded arrow recovery and remaining ranged mechanisms | backlog | Implement the requested bounded arrow-recovery path (40% proposal) through once-only projectile/death recovery authority. Remaining weapon-art and ranged draw/reload admission are owned by F24/F21. |
| [DBG-006](#dbg-006) | Shield grip and natural motion | backlog | Fingers/wrist/idle/walk/block/attack acceptance; separate from backward-facing sign defect035. |
| [DBG-007](#dbg-007) | Animal deformation / rig animation | backlog | No universal native/cooked deformation closure; crypt patrol belongs primarily to009, deer cadence to053. |
| [DBG-009](#dbg-009) | NPC/creature jitter and backwards-looking charge | backlog | Identify actual backwards-moving actor, compare travel/mesh forward and actual active clip. The29October distant silhouette is a follow-up here, not a proved new species or a second bug count. Crypt patrol jitter remains a separate subcase within this ID. |
| [DBG-012](#dbg-012) | Hostile camp too close to town/player camp | backlog | Actual occupied-site travel separation, cover and sightline acceptance; definition count is not acceptance. |
| [DBG-017](#dbg-017) | Goblin camp ordinary AI combat contact | backlog | Actual Goblin contact and route/combat behavior in current admitted encounter. |
| [DBG-018](#dbg-018) | Sustained enemy pursuit | backlog | Ordinary all-family/terrain contact and escape acceptance; no omniscient tracking. |
| [DBG-020](#dbg-020) | Messenger running arrival and audible shout | backlog | Other messengers, naturalness/listening and interruption/remote/restart breadth. |
| [DBG-035](#dbg-035) | Shield sometimes held backwards | backlog | Both shields/rigs, FP/preview/all-pose visible closure not established. |
| [DBG-036](#dbg-036) | Hatchet orientation and poor first-person grip | backlog | Current hand/haft geometry, wrist, clearance, ready/strike/TP/FP art; screenshot does not itself prove head upside-down. |
| [DBG-053](#dbg-053) | Deer slow-motion / non-fluid gait | backlog | Preserve shipped genuine fox/deer walks, proportion updates and bounded displacement proof. Natural rendered foot contact, speed/clip phase and owner acceptance remain open; no universal gait closure. |
| [DBG-057](#dbg-057) | Sparse or unseen procedural wildlife/ambushes | backlog | Preserve Journey40 ecology/residency/population work and owner feedback that spawns improved. Remaining region/night visibility, hunt supply for unsupported species and strict failed/deferred grazer/webhunter conditions remain explicit gaps. Definitions alone are not population acceptance. |
| [DBG-061](#dbg-061) | New bandit sword motion regresses from legacy choreography | active-review | Source-frame correction and fresh two-target retargeting pass saved/cold and all40-phase signed RAW/COMPRESSED motion checks. Both corrected attacks also have cold-verified right15-only grasp derivatives. Finish focused dressed Rusty/Iron motion, grip/contact and original-actor admission using those candidates. Earlier backward-lean clips remain held; cosmetic refinements must not delay useful playtest delivery. |
| [F03](#f03) | Unique NPC Conversations | backlog | Extend contextual/branching reactions beyond the bounded existing speaker subset and preserve each exact voice/text binding. |
| [F21](#f21) | Bandit Camps and Party Scaling | backlog | Finish unbound camp scenes, ordinary Rusk completion/payment, ranged role/tactic and faction/reoccupation coverage. The numbered encounter-size sub-item owns new party-count tuning; actor art remains F24. |
| [F25](#f25) | Advanced Enemy AI and Boss Attacks | backlog | Extend perception/stalking/flanking/coordinated tactics and complete readable boss attack sets; preserve existing pursuit/contact, archers, alarms and finite Human support/caster foundations. |
| [F27](#f27) | Roaming NPC Roster and Relationships | backlog | Deliver the habitat-appropriate20-entry roaming character/Roland roster and meaningful persistent relationships; current ambient residents are a separate foundation. |
| [F32](#f32) | Creature Stat Tables and Danger Warnings | backlog | Finish species/threat/stat/XP balancing and any remaining overwhelming-danger skull presentation acceptance; saved stats and removal of creature health bars already exist. |
| [F34](#f34) | Slower Item and Creature Respawns | backlog | Reconcile requested replenishment timing across resource, loot and creature families; retain existing dead-slot/saved-state continuity and116 ordinary habitat supply paths. Do not reroll living survivors or resurrect finite story content. |
| [F48](#f48) | NPC Activity Animations | backlog | Finish convincing NPC cooking/carrying/work/social/sleeping performances and home/pub day-night lifecycle; retain existing watch/walk/rest schedules. |
| [F49](#f49) | Ragdolls, Corpses and Cleanup | backlog | Finish visible material decomposition and protected, persistent corpse cleanup beyond the shipped empty-body lifecycle. Physical settlement is DBG-005; close-range head visibility DBG-052; cast/death replacement F24. |
| [F59](#f59) | Combat Feel and Networked Feedback | backlog | Broader combat presentation acceptance beyond the individually owned motion/grip defects: reactions, readiness/recovery, audible/hit feedback and supported remote feel. The active sword regression is DBG-061; shield and hatchet defects remain DBG-006/035/036. |
| [F62](#f62) | Weapon Deterioration | backlog | Finish general mainhand meaningful-use deterioration, visible consequences and repair balance; condition display and offhand contact wear already ship. |

<a id="chg-003"></a>

#### CHG-003 · Strengthen spiders and implement real venom/counterplay

**Close when:** Actual effect, readable feedback, no duplicate ticks/infinite stacks, stable old living-instance rolls and multiplayer/save behavior.

**Related owners:** [F25](#f25), [F26](#f26), [F32](#f32).

**Local source pointers:** `docs/future-state-priorities.md`.

<a id="chg-004"></a>

#### CHG-004 · Rename Shell Pincers and add grouped/huge variants

**Close when:** Both sizes count once toward same10/30/70 hunt; no reload reroll, reward reset or duplicate variant; tune actual group/scale/stat values.

**Related owners:** [F21](#f21), [F32](#f32).

**Local source pointers:** `docs/future-state-priorities.md`.

<a id="chg-005"></a>

#### CHG-005 · Add bounded nearby allied assistance including starter Wood Shrews

**Close when:** Eligible nearby living allies join; unrelated/dead/blocked/sanctuary actors stay out; no new spawns/credit or infinite chain.

**Related owners:** [F25](#f25).

**Local source pointers:** `docs/future-state-priorities.md`.

<a id="chg-006"></a>

#### CHG-006 · Complete requested wildlife families and ordinary renewable monster supply

**Close when:** Genuine compatible animated art, species audio/faction/director admissions and real hunt supply without resetting finite survivor waves.

**Related owners:** [F27](#f27), [F32](#f32), [F60](#f60).

**Local source pointers:** `docs/future-state-priorities.md`.

<a id="chg-012"></a>

#### CHG-012 · Complete suitable humanoid night lights and handoffs

**Close when:** Actual light/prop transitions and pose/equipment/remote performance; no automatic luminous animals/corpses or unlimited shadows.

**Related owners:** [F27](#f27), [F63](#f63).

**Local source pointers:** `docs/future-state-priorities.md`.

<a id="chg-013"></a>

#### CHG-013 · Implement bounded arrow recovery and remaining ranged mechanisms

**Close when:** Confirm the recovery policy, then real recovered canonical ammo without duplicate yields, item resets or client-owned credit; retain existing typed-arrow damage/draw/fatigue.

**Related owners:** [F18](#f18), [F59](#f59).

**Local source pointers:** `docs/backlog-status.md`.

<a id="dbg-006"></a>

#### DBG-006 · Shield grip and natural motion

**Close when:** Resolve or explicitly retire this exact reported scope: Fingers/wrist/idle/walk/block/attack acceptance; separate from backward-facing sign defect035.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-007"></a>

#### DBG-007 · Animal deformation / rig animation

**Close when:** Resolve or explicitly retire this exact reported scope: No universal native/cooked deformation closure; crypt patrol belongs primarily to009, deer cadence to053.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-009"></a>

#### DBG-009 · NPC/creature jitter and backwards-looking charge

**Close when:** Resolve or explicitly retire this exact reported scope: Identify actual backwards-moving actor, compare travel/mesh forward and actual active clip. The29October distant silhouette is a follow-up here, not a proved new species or a second bug count. Crypt patrol jitter remains a separate subcase within this ID.

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| DBG-009.01 | 29October unknown backwards-running silhouette — Merge as new unconfirmed-identity subcase under existing backwards/jitter DBG009. No global180 mesh flip, reversed clips or forced population. Actual actor/archetype/clip/velocity needed. | backlog | Merge as new unconfirmed-identity subcase under existing backwards/jitter DBG009. No global180 mesh flip, reversed clips or forced population. Actual actor/archetype/clip/velocity needed. |

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`; `tools/prepared/loot43-debug-a01/README.md`.

<a id="dbg-012"></a>

#### DBG-012 · Hostile camp too close to town/player camp

**Close when:** Resolve or explicitly retire this exact reported scope: Actual occupied-site travel separation, cover and sightline acceptance; definition count is not acceptance.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-017"></a>

#### DBG-017 · Goblin camp ordinary AI combat contact

**Close when:** Resolve or explicitly retire this exact reported scope: Actual Goblin contact and route/combat behavior in current admitted encounter.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-018"></a>

#### DBG-018 · Sustained enemy pursuit

**Close when:** Resolve or explicitly retire this exact reported scope: Ordinary all-family/terrain contact and escape acceptance; no omniscient tracking.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-020"></a>

#### DBG-020 · Messenger running arrival and audible shout

**Close when:** Resolve or explicitly retire this exact reported scope: Other messengers, naturalness/listening and interruption/remote/restart breadth.

**Related owners:** [F03](#f03), [F20](#f20), [F48](#f48).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| DBG-020.01 | Stage traveler arrival and camp reactions — Complete actual arriving messenger/traveler running/shouting and camp responses as authored scene with correct dialogue/state. | backlog | Ordinary visible/audible arrival, interaction interruptions and client/restart consistency. |

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`; `docs/future-state-priorities.md`.

<a id="dbg-035"></a>

#### DBG-035 · Shield sometimes held backwards

**Close when:** Resolve or explicitly retire this exact reported scope: Both shields/rigs, FP/preview/all-pose visible closure not established.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-036"></a>

#### DBG-036 · Hatchet orientation and poor first-person grip

**Close when:** Resolve or explicitly retire this exact reported scope: Current hand/haft geometry, wrist, clearance, ready/strike/TP/FP art; screenshot does not itself prove head upside-down.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-053"></a>

#### DBG-053 · Deer slow-motion / non-fluid gait

**Close when:** Resolve or explicitly retire this exact reported scope: Preserve shipped genuine fox/deer walks, proportion updates and bounded displacement proof. Natural rendered foot contact, speed/clip phase and owner acceptance remain open; no universal gait closure.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-057"></a>

#### DBG-057 · Sparse or unseen procedural wildlife/ambushes

**Close when:** Resolve or explicitly retire this exact reported scope: Preserve Journey40 ecology/residency/population work and owner feedback that spawns improved. Remaining region/night visibility, hunt supply for unsupported species and strict failed/deferred grazer/webhunter conditions remain explicit gaps. Definitions alone are not population acceptance.

**Related owners:** [CHG-006](#chg-006), [F21](#f21).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| DBG-057.01 | Dungeon enemy pop-in — Retain as DBG057 activation/visibility subcase with actual dungeon/encounter/rendered appearance gates; no extra unique bug if consolidated. | backlog | Retain as DBG057 activation/visibility subcase with actual dungeon/encounter/rendered appearance gates; no extra unique bug if consolidated. |
| DBG-057.02 | Night life and missing night enemies — Retain as DBG057 night ecology / F27 village routine coverage; bounded three-ID headless observation does not establish all-region night population. | backlog | Retain as DBG057 night ecology / F27 village routine coverage; bounded three-ID headless observation does not establish all-region night population. |

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`; `docs/woodshrew40-progress.md`.

<a id="dbg-061"></a>

#### DBG-061 · New bandit sword motion regresses from legacy choreography

**Close when:** Actual dressed motion, usable Rusty/Iron grasp/contact and original-world admission pass at reasonable playtest quality; record cosmetic gaps and retain checks for broken motion, missing bodies, crashes and real integration.

**Related owners:** [F59](#f59).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| DBG-061.01 | Reuse corrected source frame and verified grasp derivatives — Source correction, two-target signed motion checks and right15 grasp author/cold checks pass. Reuse these results for the remaining dressed/weapon review. | source-verified | Saved/cold source-frame and all40-phase signed motion agreement; actual dressed weapon/contact acceptance remains the parent record's open gate. |

**Local source pointers:** `docs/debug-triage.md`; `CURRENT_WORK.md`; `tools/prepared/legacy-sword43-grip-a01/HANDOFF.md`; `CURRENT_WORK.md`.

<a id="f03"></a>

#### F03 · Unique NPC Conversations

**Close when:** Extend contextual/branching reactions beyond the bounded existing speaker subset and preserve each exact voice/text binding.

**Related owners:** [DBG-042](#dbg-042), [DBG-048](#dbg-048), [F20](#f20), [F27](#f27), [F47](#f47).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| F03.01 | Add automatic proximity greetings and contextual ambient remarks — NPC-specific varied spoken approach remarks/gossip/weather/personality pools and spoilers/context gating. | backlog | Real approach triggers with per-NPC/player cooldown/repeat control and crowd/conversation arbitration on host/client. |

**Local source pointers:** `docs/npc-dialogue-variety.md`; `docs/backlog-status.md`; `docs/future-state-priorities.md`.

<a id="f21"></a>

#### F21 · Bandit Camps and Party Scaling

**Close when:** Complete remaining authored camp quest scenes, ordinary Rusk completion/payment acceptance, crossbows, role/tactical variety, faction/reoccupation behavior and party-scaled natural fights.19 sites and16 templates are not19/16 finished scenes.

**Related owners:** [DBG-012](#dbg-012), [DBG-057](#dbg-057), [F20](#f20), [F25](#f25), [F27](#f27), [F32](#f32), [F34](#f34), [F60](#f60).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| F21.01 | Expand ordinary encounter coverage and modest party group size — A few more enemies per person and overlapping wilderness habitat/interest coverage off main route; preserve budgets, concealment and committed composition. | backlog | Region/route audit and normal solo/party admissions/contact/performance; no visible pops/infinite reinforcements or live join rerolls. |

**Local source pointers:** `docs/backlog-status.md`; `docs/journey-playtest34-delivery.md`; `docs/journey-playtest35-delivery.md`; `docs/future-state-priorities.md`.

<a id="f25"></a>

#### F25 · Advanced Enemy AI and Boss Attacks

**Close when:** Extend perception/stalking/flanking/coordinated tactics and complete readable boss attack sets; preserve existing pursuit/contact, archers, alarms and finite Human support/caster foundations.

**Related owners:** [DBG-007](#dbg-007), [DBG-009](#dbg-009), [DBG-017](#dbg-017), [DBG-018](#dbg-018), [DBG-033](#dbg-033), [DBG-053](#dbg-053), [F21](#f21), [F32](#f32), [F59](#f59).

**Local source pointers:** `docs/backlog-status.md`; `docs/journey-playtest34-delivery.md`.

<a id="f27"></a>

#### F27 · Roaming NPC Roster and Relationships

**Close when:** Deliver the habitat-appropriate20-entry roaming character/Roland roster and meaningful persistent relationships; current ambient residents are a separate foundation.

**Related owners:** [F03](#f03), [F21](#f21), [F48](#f48).

**Local source pointers:** `docs/npc-encounter-roster.md`; `docs/living-npc-world.md`; `docs/backlog-status.md`.

<a id="f32"></a>

#### F32 · Creature Stat Tables and Danger Warnings

**Close when:** Finish species/threat/stat/XP balancing and any remaining overwhelming-danger skull presentation acceptance; saved stats and removal of creature health bars already exist.

**Related owners:** [F21](#f21), [F25](#f25), [F33](#f33).

**Local source pointers:** `docs/enemy-stat-tables.md`; `docs/backlog-status.md`.

<a id="f34"></a>

#### F34 · Slower Item and Creature Respawns

**Close when:** Reconcile requested replenishment timing across resource, loot and creature families; retain existing dead-slot/saved-state continuity and116 ordinary habitat supply paths. Do not reroll living survivors or resurrect finite story content.

**Related owners:** [F21](#f21), [F28](#f28), [F40](#f40), [F49](#f49).

**Local source pointers:** `docs/hunting-replenishment41.md`; `docs/creature-continuity41.md`; `docs/backlog-status.md`.

<a id="f48"></a>

#### F48 · NPC Activity Animations

**Close when:** Finish convincing NPC cooking/carrying/work/social/sleeping performances and home/pub day-night lifecycle; retain existing watch/walk/rest schedules.

**Related owners:** [DBG-020](#dbg-020), [F27](#f27), [F59](#f59).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| F48.01 | Complete villager homes/pub day-night and social/work routines — Real safe indoor routes at night, work/day return and believable interruptible activities/social behavior. | backlog | Actual door traversal/ingress/restart supported; stopping an outdoor route doesn't mean entering a home/pub. |

**Local source pointers:** `docs/living-npc-world.md`; `docs/backlog-status.md`; `docs/future-state-priorities.md`.

<a id="f49"></a>

#### F49 · Ragdolls, Corpses and Cleanup

**Close when:** Finish genuine physical ragdoll falls/terrain support/settlement, corpse collision and persistent cleanup. Distinguish authored terminal aftermath poses from combat-death bodies and head-visibility defects; preserve authoritative loot/death.

**Related owners:** [DBG-005](#dbg-005), [DBG-052](#dbg-052), [F28](#f28), [F54](#f54).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| F49.01 | Finish visible corpse decomposition and modern death handling — Visible material decomposition remains after basic empty-body cleanup; preserve protected/unlooted/in-use bodies and current death/loot state. | backlog | Real decay visuals, rigs/head/garment/physics and replicated saved cleanup no refill; separate DBG-005 ragdoll and DBG-052 head disappearance. |

**Local source pointers:** `docs/backlog-status.md`; `docs/debug-triage.md`; `docs/npc-character-replacement-plan.md`; `docs/future-state-priorities.md`.

<a id="f59"></a>

#### F59 · Combat Feel and Networked Feedback

**Close when:** Correct the actual retarget forward-lean mismatch before new Rusty/Iron grip/contact admission; finish broader weapon/shield ready/strike/recovery poses, reactions, audio and remote feel. Preserve existing server damage/contact/timing and passed body/finger readbacks.

**Related owners:** [DBG-006](#dbg-006), [DBG-009](#dbg-009), [DBG-035](#dbg-035), [DBG-036](#dbg-036), [F21](#f21), [F24](#f24), [F25](#f25), [F49](#f49), [F63](#f63), [F64](#f64).

**Local source pointers:** `CURRENT_WORK.md`; `docs/debug-triage.md`; `docs/npc-character-replacement-plan.md`.

<a id="f62"></a>

#### F62 · Weapon Deterioration

**Close when:** Finish general mainhand meaningful-use deterioration, visible consequences and repair balance; condition display and offhand contact wear already ship.

**Related owners:** [F18](#f18), [F43](#f43), [F64](#f64).

**Local source pointers:** `docs/future-state-priorities.md`; `docs/backlog-status.md`.

<a id="f30-workstream"></a>

### World, characters, art and audio

| ID | Item | State | Remaining outcome |
| --- | --- | --- | --- |
| [CHG-011](#chg-011) | Improve shared fire effects and matching sound | backlog | Torches, camp/cooking fires, braziers, pyres/burning roofs and fire spells need coherent flame shape/motion/embers/smoke/light/flicker/transitions/audio. |
| [CHG-015](#chg-015) | Complete mod-feature reference video review | backlog | Review supplied BIPQhTp7Iik video with verified title/transcript/mod list, timestamp concrete features and primary project links, merge suitable duplicates. |
| [CHG-016](#chg-016) | Package and accept coherent Journey43 cast increment | active-gate | Freeze coherent admitted cast source, complete UAT and promote only after changed cooked risks pass. |
| [DBG-003](#dbg-003) | Stone spear uses sword art | backlog | Exact item art/presenter correspondence; latest physical binding not newly inspected. |
| [DBG-004](#dbg-004) | Torch owner hand/weapon glare | backlog | Accepted optical reduction without losing useful world illumination. |
| [DBG-005](#dbg-005) | Floating/clipping corpses and absent physical ragdoll settlement | backlog | Physical death settlement, corpse/head/garment contacts and saved resting appearance remain open. Journey42 living-resident replacements explicitly restore legacy presentation for dead residents; do not call modern corpse coverage delivered. |
| [DBG-008](#dbg-008) | Camp alchemy table placement | backlog | Support, usable side, path and tent relation. |
| [DBG-013](#dbg-013) | Floating black village-reveal wedge | backlog | Identity and current recurrence; not automatically027 fixed ground or041 moving shovel. |
| [DBG-016](#dbg-016) | Stick/fibre art cannot ground on Landscape | backlog | Queue still lacks dedicated visible/cooked grounding closure; historical model/size approval is a different scope. |
| [DBG-019](#dbg-019) | Natural conversation facing | backlog | Every presenter/turn-in-place/remote/lifetime path is not accepted by source Mara POC. |
| [DBG-027](#dbg-027) | Ground-fixed black trail/bridge triangles | backlog | Original owner-pixel attribution/normal moving view and walk closure not established by queue. |
| [DBG-029](#dbg-029) | Generic armor and missing glove/boot appearance changes | backlog | Retain accepted independent equipment and Journey41/42 item-backed wardrobe coverage. Remaining unsupported item/body/slot presentation and actual source-art fidelity need specific admissions; new Mara garment/production gap is tracked separately and linked. |
| [DBG-030](#dbg-030) | Cape shoulder coverage, floating and inventory follow | backlog | Owner/full rig/pose/wardrobe approval and physical cloth simulation are not established. |
| [DBG-032](#dbg-032) | Detached heads, neck seams and modern human bodies | backlog | Journey42 ships ten resident/five bandit profiles; two genuinely new faces are checked but disabled source assets. Remaining named/player/ancestry/corpse adapters, neck/skin fidelity, actual selected-role binding and supported moving fit remain open. Do not count beard/outfit recipes as distinct faces. |
| [DBG-033](#dbg-033) | Starter shrew fixed seven-metre pursuit radius | backlog | Ordinary chase/contact beyond former radius and genuine sanctuary/return conditions; speed/emergence do not prove all chase acceptance. |
| [DBG-037](#dbg-037) | Landscape PSO precache ensure | backlog | Exact triggering component/workload and remedy. |
| [DBG-039](#dbg-039) | Pale/unconvincing human skin and complexion variety | backlog | New source identities have matching skin and selected face/head settings; Journey42 catalog covers a bounded subset. Preserve intentional undead pallor. Remaining exact actors, hand/head/neck continuity and broad complexion variety require actual presentation acceptance; no all-character closure. |
| [DBG-042](#dbg-042) | Mara robotic voice performance | backlog | Listening/naturalness unapproved. Current fresh-game script/voice mismatch is a separate unnumbered report with a concrete binding diagnosis; new character visual POC fixes neither. |
| [DBG-045](#dbg-045) | Missing distinct tree chop sound | backlog | Listening, actual material/cadence and every-tree coverage. |
| [DBG-046](#dbg-046) | Walking and surface/creature footstep audio | backlog | Actual species/surface sound coverage, stride synchronization and owner listening; deer sound is not gait053. |
| [DBG-047](#dbg-047) | Dialogue versus ambience mix | backlog | Subjective blend/occlusion/listening across contexts. |
| [DBG-048](#dbg-048) | Peltsmith audio coverage | backlog | Every branch/exact final text dispatch and listening acceptance, including newer hunt offers. |
| [DBG-052](#dbg-052) | Corpse head disappears when approaching | backlog | Head-only bounds/LOD/follower/visibility state; not closed by fixed living bandit heads or new character Mara. |
| [DBG-055](#dbg-055) | Oren invisible | backlog | Oren has historical technical modern-asset integration in21, with visible review deferred. No exact later visible/world acceptance was found in41/42 release reports; confirm the actor/path/LOD/bounds and normal visibility rather than claiming the old absence fixed by other residents. |
| [DBG-060](#dbg-060) | Floating authored sideways trees | backlog | Other instances unmeasured; shared box-corner fitting lead across five families is not a proved cause for every tree. |
| [DBG-064](#dbg-064) | Mara remains legacy in actual Journey42 | backlog | Complete real Ranger elbow/fit/LOD/material production admission and actual enabled normal-game dependency/cooked closure.42 lacks specific Blueprint/suit/material roots and enable path; flag-only enabling expensive unapproved prototype is insufficient. Keep original quest/speaker/actor. |
| [DBG-065](#dbg-065) | New character hair disappears near camera or view | backlog | Identify actual groom/component, target mesh, bounds/LOD/visibility route and verify real near/moving views. Living hair loss differs from corpse-head disappearance. |
| [DBG-066](#dbg-066) | Gray geometric patch beneath Barbarian hair | backlog | Attribute actual neck/shoulder patch to component/material/geometry in focused view, repair source and verify fitted native motion without hiding unrelated bodies. Broad previous art views do not close this. |
| [DBG-071](#dbg-071) | Mara first new-character greeting script has wrong or missing voice | backlog | Bind exact short rescue/new-character first greeting wording to matching approved audio and listen through actual normal interaction. Older long clip/visual replacement does not establish script correspondence. |
| [DBG-072](#dbg-072) | Rainbow cutlery material | needs-triage | Historical report lacks matching current acceptance. Identify actual item/material and recurrence before correction; preserve texture-role, UV, tangents and material-slot route. |
| [F02](#f02) | Loot Sounds and Pickup Feedback | backlog | Extend quantity/sound feedback to all supported corpse/container transfers; verify actual listening and remote behavior. |
| [F06](#f06) | Area-Specific Loading Screens | backlog | Author and admit distinct destination-specific town/dungeon/castle loading images; existing themed loading/status already ships. |
| [F07](#f07) | Location-Specific Music | backlog | Provide accepted region/location music with transitions and final listening/mix. The title lute theme is already shipped, not regional music. |
| [F15](#f15) | Action and Ambient Sound Coverage | backlog | Complete creature/surface/contact/action/ambience audio, exact dialogue dispatch, spatial mix and listening acceptance; keep imported subset distinct from universal coverage. |
| [F24](#f24) | Modern Materials and Container Art | active-partial | Finish reference-led armor/character/item production and retained UV/PBR/LOD coverage through the numbered sub-items. Mara's exact production/delivery fault is DBG-064, motion regression is DBG-061, and existing hair/skin/head defects retain their DBG IDs. |
| [F30](#f30) | Original Ash Road World Redesign | backlog | Continue original world/town/interior/site art and the explicit bridge/water/route-art sub-item. Vegetation is F31; shared fires CHG-011; character/armor production F24; expanded connected-region streaming F55. |
| [F31](#f31) | Realistic Grass, Flowers and Trees | backlog | Finish dense tall mixed prairie/herbs, irregular shrub/tree-line cover and biome/tree replacement under measured budgets; preserve actual native foliage/wind and finite grounding fixes. |
| [F47](#f47) | Facial Expressions and Lip Sync | backlog | Complete an actually solved/imported audible speaking face, native expressions/lip-sync and accepted dialogue performance; prepared one-response work and static saved face selection are not delivery. |
| [F50](#f50) | Weather and Climate Polish | backlog | Finish accepted weather pacing, clear starry nights, wet surfaces/splashes/snow/climate response and final wind/fire review. Existing clock/weather/gloom/native foliage wind are foundations. |
| [F55](#f55) | Region Expansion and Streaming | backlog | Expand original connected regions/interiors with persistent identities and actual WorldPartition/remote/late-join acceptance. Existing region, crypt and controlled continuity witnesses are bounded. |

<a id="chg-011"></a>

#### CHG-011 · Improve shared fire effects and matching sound

**Close when:** Inspect/reuse installed owned Unreal/Niagara first; actual native view under8GB budget with readable first-person exposure and unchanged combat/ignition authority.

**Related owners:** [F15](#f15), [F24](#f24), [F26](#f26).

**Local source pointers:** `docs/future-state-priorities.md`.

<a id="chg-015"></a>

#### CHG-015 · Complete mod-feature reference video review

**Close when:** Actual accessible source review; no fabricated mod features or inferred mechanics from failed fetch.

**Local source pointers:** `docs/future-state-priorities.md`.

<a id="chg-016"></a>

#### CHG-016 · Package and accept coherent Journey43 cast increment

**Close when:** Accepted package/cooked checks, clear launcher promotion and N/N-1 retention; no broad repeated campaign tour.

**Depends on:** [DBG-061](#dbg-061), [F24.01](#f24), [F24.02](#f24), [F24.03](#f24).

**Local source pointers:** `CURRENT_WORK.md`.

<a id="dbg-003"></a>

#### DBG-003 · Stone spear uses sword art

**Close when:** Resolve or explicitly retire this exact reported scope: Exact item art/presenter correspondence; latest physical binding not newly inspected.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-004"></a>

#### DBG-004 · Torch owner hand/weapon glare

**Close when:** Resolve or explicitly retire this exact reported scope: Accepted optical reduction without losing useful world illumination.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-005"></a>

#### DBG-005 · Floating/clipping corpses and absent physical ragdoll settlement

**Close when:** Resolve or explicitly retire this exact reported scope: Physical death settlement, corpse/head/garment contacts and saved resting appearance remain open. Journey42 living-resident replacements explicitly restore legacy presentation for dead residents; do not call modern corpse coverage delivered.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`; `docs/journey41-delivery.md`; `docs/journey42-playtest.md`; `docs/npc-character-replacement-plan.md`.

<a id="dbg-008"></a>

#### DBG-008 · Camp alchemy table placement

**Close when:** Resolve or explicitly retire this exact reported scope: Support, usable side, path and tent relation.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-013"></a>

#### DBG-013 · Floating black village-reveal wedge

**Close when:** Resolve or explicitly retire this exact reported scope: Identity and current recurrence; not automatically027 fixed ground or041 moving shovel.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-016"></a>

#### DBG-016 · Stick/fibre art cannot ground on Landscape

**Close when:** Resolve or explicitly retire this exact reported scope: Queue still lacks dedicated visible/cooked grounding closure; historical model/size approval is a different scope.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-019"></a>

#### DBG-019 · Natural conversation facing

**Close when:** Resolve or explicitly retire this exact reported scope: Every presenter/turn-in-place/remote/lifetime path is not accepted by source Mara POC.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-027"></a>

#### DBG-027 · Ground-fixed black trail/bridge triangles

**Close when:** Resolve or explicitly retire this exact reported scope: Original owner-pixel attribution/normal moving view and walk closure not established by queue.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-029"></a>

#### DBG-029 · Generic armor and missing glove/boot appearance changes

**Close when:** Resolve or explicitly retire this exact reported scope: Retain accepted independent equipment and Journey41/42 item-backed wardrobe coverage. Remaining unsupported item/body/slot presentation and actual source-art fidelity need specific admissions; new Mara garment/production gap is tracked separately and linked.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`; `docs/journey41-delivery.md`; `docs/journey42-playtest.md`; `docs/npc-character-replacement-plan.md`.

<a id="dbg-030"></a>

#### DBG-030 · Cape shoulder coverage, floating and inventory follow

**Close when:** Resolve or explicitly retire this exact reported scope: Owner/full rig/pose/wardrobe approval and physical cloth simulation are not established.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-032"></a>

#### DBG-032 · Detached heads, neck seams and modern human bodies

**Close when:** Resolve or explicitly retire this exact reported scope: Journey42 ships ten resident/five bandit profiles; two genuinely new faces are checked but disabled source assets. Remaining named/player/ancestry/corpse adapters, neck/skin fidelity, actual selected-role binding and supported moving fit remain open. Do not count beard/outfit recipes as distinct faces.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`; `docs/journey41-delivery.md`; `docs/journey42-playtest.md`; `docs/npc-character-replacement-plan.md`.

<a id="dbg-033"></a>

#### DBG-033 · Starter shrew fixed seven-metre pursuit radius

**Close when:** Resolve or explicitly retire this exact reported scope: Ordinary chase/contact beyond former radius and genuine sanctuary/return conditions; speed/emergence do not prove all chase acceptance.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`; `docs/woodshrew40-progress.md`.

<a id="dbg-037"></a>

#### DBG-037 · Landscape PSO precache ensure

**Close when:** Resolve or explicitly retire this exact reported scope: Exact triggering component/workload and remedy.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-039"></a>

#### DBG-039 · Pale/unconvincing human skin and complexion variety

**Close when:** Resolve or explicitly retire this exact reported scope: New source identities have matching skin and selected face/head settings; Journey42 catalog covers a bounded subset. Preserve intentional undead pallor. Remaining exact actors, hand/head/neck continuity and broad complexion variety require actual presentation acceptance; no all-character closure.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`; `docs/journey41-delivery.md`; `docs/journey42-playtest.md`; `docs/npc-character-replacement-plan.md`.

<a id="dbg-042"></a>

#### DBG-042 · Mara robotic voice performance

**Close when:** Resolve or explicitly retire this exact reported scope: Listening/naturalness unapproved. Current fresh-game script/voice mismatch is a separate unnumbered report with a concrete binding diagnosis; new character visual POC fixes neither.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-045"></a>

#### DBG-045 · Missing distinct tree chop sound

**Close when:** Resolve or explicitly retire this exact reported scope: Listening, actual material/cadence and every-tree coverage.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-046"></a>

#### DBG-046 · Walking and surface/creature footstep audio

**Close when:** Resolve or explicitly retire this exact reported scope: Actual species/surface sound coverage, stride synchronization and owner listening; deer sound is not gait053.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-047"></a>

#### DBG-047 · Dialogue versus ambience mix

**Close when:** Resolve or explicitly retire this exact reported scope: Subjective blend/occlusion/listening across contexts.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-048"></a>

#### DBG-048 · Peltsmith audio coverage

**Close when:** Resolve or explicitly retire this exact reported scope: Every branch/exact final text dispatch and listening acceptance, including newer hunt offers.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-052"></a>

#### DBG-052 · Corpse head disappears when approaching

**Close when:** Resolve or explicitly retire this exact reported scope: Head-only bounds/LOD/follower/visibility state; not closed by fixed living bandit heads or new character Mara.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-055"></a>

#### DBG-055 · Oren invisible

**Close when:** Resolve or explicitly retire this exact reported scope: Oren has historical technical modern-asset integration in21, with visible review deferred. No exact later visible/world acceptance was found in41/42 release reports; confirm the actor/path/LOD/bounds and normal visibility rather than claiming the old absence fixed by other residents.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`; `docs/journey41-delivery.md`; `docs/journey42-playtest.md`; `docs/npc-character-replacement-plan.md`.

<a id="dbg-060"></a>

#### DBG-060 · Floating authored sideways trees

**Close when:** Resolve or explicitly retire this exact reported scope: Other instances unmeasured; shared box-corner fitting lead across five families is not a proved cause for every tree.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/backlog-rollup25/debug-audit.json`.

<a id="dbg-064"></a>

#### DBG-064 · Mara remains legacy in actual Journey42

**Close when:** Complete real Ranger elbow/fit/LOD/material production admission and actual enabled normal-game dependency/cooked closure.42 lacks specific Blueprint/suit/material roots and enable path; flag-only enabling expensive unapproved prototype is insufficient. Keep original quest/speaker/actor.

**Related owners:** [DBG-029](#dbg-029), [DBG-032](#dbg-032).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| DBG-064.01 | Rejected Mara wardrobe distortion — Merge with actual Mara production/delivery repair; retain fit/elbow/source-art rejection and actual production LOD/material gates rather than create duplicate broad cast issue. | backlog | Merge with actual Mara production/delivery repair; retain fit/elbow/source-art rejection and actual production LOD/material gates rather than create duplicate broad cast issue. |

**Local source pointers:** `docs/debug-triage.md`; `docs/mara43-delivery-gap.md`.

<a id="dbg-065"></a>

#### DBG-065 · New character hair disappears near camera or view

**Close when:** Identify actual groom/component, target mesh, bounds/LOD/visibility route and verify real near/moving views. Living hair loss differs from corpse-head disappearance.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/debug-triage27/barbarian-shoulder-a01/REPORT.md`.

<a id="dbg-066"></a>

#### DBG-066 · Gray geometric patch beneath Barbarian hair

**Close when:** Attribute actual neck/shoulder patch to component/material/geometry in focused view, repair source and verify fitted native motion without hiding unrelated bodies. Broad previous art views do not close this.

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/debug-triage27/barbarian-shoulder-a01/REPORT.md`.

<a id="dbg-071"></a>

#### DBG-071 · Mara first new-character greeting script has wrong or missing voice

**Close when:** Bind exact short rescue/new-character first greeting wording to matching approved audio and listen through actual normal interaction. Older long clip/visual replacement does not establish script correspondence.

**Related owners:** [DBG-042](#dbg-042).

**Local source pointers:** `docs/debug-triage.md`; `tools/prepared/mara-voice-followup40/README.md`.

<a id="dbg-072"></a>

#### DBG-072 · Rainbow cutlery material

**Close when:** Historical report lacks matching current acceptance. Identify actual item/material and recurrence before correction; preserve texture-role, UV, tangents and material-slot route.

**Local source pointers:** `docs/debug-triage.md`.

<a id="f02"></a>

#### F02 · Loot Sounds and Pickup Feedback

**Close when:** Extend quantity/sound feedback to all supported corpse/container transfers; verify actual listening and remote behavior.

**Related owners:** [F08](#f08), [F15](#f15).

**Local source pointers:** `docs/inventory-loot-design.md`; `docs/backlog-status.md`.

<a id="f06"></a>

#### F06 · Area-Specific Loading Screens

**Close when:** Author and admit distinct destination-specific town/dungeon/castle loading images; existing themed loading/status already ships.

**Related owners:** [F50](#f50).

**Local source pointers:** `docs/loading-screen.md`; `docs/backlog-status.md`.

<a id="f07"></a>

#### F07 · Location-Specific Music

**Close when:** Provide accepted region/location music with transitions and final listening/mix. The title lute theme is already shipped, not regional music.

**Related owners:** [F15](#f15).

**Local source pointers:** `docs/journey-playtest16-delivery.md`; `docs/backlog-status.md`.

<a id="f15"></a>

#### F15 · Action and Ambient Sound Coverage

**Close when:** Complete creature/surface/contact/action/ambience audio, exact dialogue dispatch, spatial mix and listening acceptance; keep imported subset distinct from universal coverage.

**Related owners:** [DBG-042](#dbg-042), [DBG-045](#dbg-045), [DBG-046](#dbg-046), [DBG-047](#dbg-047), [DBG-048](#dbg-048), [F02](#f02), [F03](#f03), [F07](#f07), [F26](#f26), [F47](#f47).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| F15.01 | Add distinct once-only learned-rank achievement cue — Fantasy cue only on confirmed newly learned rank using current owner-client purchase feedback. | backlog | Owner audition and confirmation-path check; rejected/duplicate/retry/restored selections never replay, SFX mute respected. |

**Local source pointers:** `docs/backlog-status.md`; `docs/npc-voiceforge-production.md`; `docs/future-state-priorities.md`.

<a id="f24"></a>

#### F24 · Modern Materials and Container Art

**Close when:** Finish reference-faithful character/garment/container/world materials and broader supported item art, retained UV maps/layouts, physical texture scale and native import/LOD acceptance. Preserve approved art and shipped scoped upgrades.

**Related owners:** [DBG-029](#dbg-029), [DBG-030](#dbg-030), [DBG-032](#dbg-032), [DBG-039](#dbg-039), [F16](#f16), [F18](#f18), [F21](#f21), [F27](#f27), [F30](#f30), [F31](#f31), [F48](#f48), [F59](#f59).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| F24.01 | Activate two distinct checked bandit identities — Replace five existing recipes using two genuinely distinct identities through existing operators. Keep saved IDs/equipment and unsupported legacy fallback. | active | Actual original actor alive/death/equipment check and admitted exact weapon mappings before cooked inclusion. |
| F24.02 | Admit the additional fitted melee profile — Complete dressed fit, grasp, original selected-slot world witness and supported equipment for the additional target profile. | active | Real selected original actor and supported new motion/equipment pass; do not reroll saved recipes or count a prepared witness as installed. |
| F24.03 | Finish selected villager wardrobe fidelity — Take actual shirt-derived vest through existing native Outfit path; retain reference construction, weights, UV/material route and physical scale. | active | Selected-reference art and actual native moving fit admitted; prototype fitting alone is insufficient. |
| F24.04 | Complete remaining normal-world character adapters — Named/service/guard roles, player creator and first-person, corpses, actual vampires/undead, Elf/Orc and remaining ancestry/creature/fallback selectors each need intended exact profiles. | backlog | Normal-world actor and motion/equipment/death coverage; no showcase-only replacements, relabeled humans or repeated faces counted as unique. |
| F24.05 | Retire prohibited legacy character dependency closure — After each admitted replacement, retire old selectors/fallbacks and audit hard/soft meshes, materials, textures, animation and physics dependencies. | backlog | Zero unexplained active legacy selectors and zero prohibited character dependencies in current release cook closure. Preserve unrelated assets, licensed provenance and old release/source history. |
| F24.06 | Complete class/family/slot armor production and exact fits — D&D-aligned approved armor for class tiers and actual slots, proportion-aware Human/Dwarf/other supported body fits, all selected references. | backlog | Actual modular clay construction, native moving fit, retained usable UV/layout images/PBR and saved equipment/LOD admission; not multiplied blockouts or uniform-scale fits. |
| F24.07 | Finish creator shape controls and armor deformation support — Runtime creator shape ranges and shared body/armor parameters including build, limb proportions and head size; exact rigs and faces for supported ancestry targets. | backlog | Saved/reopened intended body art and usable sliders, correct motion/equipment fit and supported range admission. |
| F24.08 | Close usable UV and UV-layout image gaps across current asset library — Retain coordinates in every actual model plus corresponding UV layout image alongside source art; generate missing and repair defective mappings while preserving approved art alignment. | backlog | Per-asset coverage/gaps recorded; placement, physical scale and material routing checked on model and export/import. |
| F24.09 | Roll approved metal surface through existing and future actual metal — Apply Style48 nested pitting to actual weapon/ammo/armor/tool/coin/container/architecture metal; retain alloy identity and nonmetal masks, ornament and UVs. | backlog | Per-asset source/output hashes, representative mixed/pure-metal and changed-light/native review; unknown embedded regions explicitly unresolved. |
| F24.10 | Roll worn leather and shared palette through current production assets — Construction-aware worn/grimy finish and approved chestnut palette across actual leather models, hardware separation and current exports/icons. | backlog | Per-asset reviewed successors, actual exportable PBR, model/native view under multiple lights, preserved geometry/UV and original garment choices. |
| F24.11 | Repair continuous straps, wraps and attachment construction — Review existing/new weapon wraps/slings/bindings and relevant armor straps for continuous paths, credible anchors, thickness and moving clearance. | backlog | Actual front/back/side source/model and native-contact evidence; no invented straps on designs that lack them. |
| F24.12 | Admit remaining approved weapon candidates into real canonical equipment — Remaining approved art candidates need geometry budgets/LODs, owner art approval, UV/material/contact/collision and actual item bindings; ranged bows/crossbows require draw/reload rigs. | backlog | Selected real canonical items visible held/loose, correctly animated and cooked with matching stats/icons; no static ranged model marked playable. |
| F24.13 | Place intended camp Barbarian in normal gameplay with approved voice — Persistent successor of existing camp role, reference fit/motion and Austrian-accented voice; retain current role/authority. | backlog | Actual native athletic fit, voice listening approval, original-world binding and cooked inclusion. |

**Local source pointers:** `CURRENT_WORK.md`; `docs/npc-character-replacement-plan.md`; `docs/metal-surface-standard48.md`; `docs/backlog-status.md`; `CURRENT_WORK.md`; `CURRENT_WORK.md`; `CURRENT_WORK.md`; `docs/npc-character-replacement-plan.md`; `docs/npc-character-replacement-plan.md`; `docs/future-state-priorities.md`; `docs/future-state-priorities.md`; `AGENTS.md`; `docs/metal-surface-standard48.md`; `docs/leather-surface-standard26.md`; `docs/future-state-priorities.md`; `docs/future-state-priorities.md`; `docs/future-state-priorities.md`.

<a id="f30"></a>

#### F30 · Original Ash Road World Redesign

**Close when:** Continue original region/town/accessible-interior redesign, bridge/water/fire/site art and the wider atlas without copied landmarks; retain the shipped4.032x6.048km region and two settlements.

**Related owners:** [DBG-001](#dbg-001), [DBG-031](#dbg-031), [DBG-054](#dbg-054), [DBG-060](#dbg-060), [F24](#f24), [F31](#f31), [F50](#f50), [F55](#f55), [F60](#f60).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| F30.01 | Bridge wood, water clarity and bridge/survivor prairie art — Finish named bridge wood quality, appropriately opaque/convincing water and route prairie/brush art; earlier scoped water or single-tree fixes do not close the broader request. Parent may split by acceptance/area. | backlog | Finish named bridge wood quality, appropriately opaque/convincing water and route prairie/brush art; earlier scoped water or single-tree fixes do not close the broader request. Parent may split by acceptance/area. |

**Local source pointers:** `docs/backlog-status.md`; `docs/future-state-priorities.md`; `docs/debug-triage.md`; `docs/environment-brush43.md`.

<a id="f31"></a>

#### F31 · Realistic Grass, Flowers and Trees

**Close when:** Finish dense tall mixed prairie/herbs, irregular shrub/tree-line cover and biome/tree replacement under measured budgets; preserve actual native foliage/wind and finite grounding fixes.

**Related owners:** [DBG-057](#dbg-057), [DBG-060](#dbg-060), [F24](#f24), [F30](#f30), [F40](#f40), [F60](#f60).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| F31.01 | Extend dense layered brush along woodland and field edges — Irregular full leafy clumps connecting prairie/river/bridge direction, using actual installed shrub assets and scalable instancing/culling. | backlog | Before/after same short route, target preset, GPU frame time/VRAM/game-thread/instance data and clear quest/road/fight lanes. |

**Local source pointers:** `docs/environment-brush43.md`; `docs/backlog-status.md`; `docs/future-state-priorities.md`; `docs/environment-brush43.md`.

<a id="f47"></a>

#### F47 · Facial Expressions and Lip Sync

**Close when:** Complete an actually solved/imported audible speaking face, native expressions/lip-sync and accepted dialogue performance; prepared one-response work and static saved face selection are not delivery.

**Related owners:** [DBG-019](#dbg-019), [DBG-042](#dbg-042), [F03](#f03), [F24](#f24).

**Local source pointers:** `docs/backlog-status.md`; `docs/npc-character-art-goal.md`.

<a id="f50"></a>

#### F50 · Weather and Climate Polish

**Close when:** Finish accepted weather pacing, clear starry nights, wet surfaces/splashes/snow/climate response and final wind/fire review. Existing clock/weather/gloom/native foliage wind are foundations.

**Related owners:** [F24](#f24), [F30](#f30), [F31](#f31), [F46](#f46).

| Sub-ID | Scope | State | Close when |
| --- | --- | --- | --- |
| F50.01 | Integrate dry-biased weather and genuinely clear starry nights — Long dry/clear stretches, shorter occasional rain, rare storms and visibly clear/starry/MilkyWay nights; remove conflicting mood clamps in real clear-state path. | backlog | Actual saved weather schedule, host/client and native night views without owner-save reset; launcher label alone insufficient. |

**Local source pointers:** `docs/backlog-status.md`; `docs/future-state-priorities.md`; `docs/future-state-priorities.md`.

<a id="f55"></a>

#### F55 · Region Expansion and Streaming

**Close when:** Expand original connected regions/interiors with persistent identities and actual WorldPartition/remote/late-join acceptance. Existing region, crypt and controlled continuity witnesses are bounded.

**Related owners:** [DBG-014](#dbg-014), [DBG-015](#dbg-015), [DBG-051](#dbg-051), [F30](#f30), [F45](#f45), [F51](#f51), [F60](#f60).

**Local source pointers:** `docs/backlog-status.md`; `docs/creature-continuity41.md`.

## Optional and long-term scope

| ID | Item | State | Boundary |
| --- | --- | --- | --- |
| <a id="f51"></a>F51 | Linux Dedicated Hosting and Campaign Delivery | optional-long-term | Retained long-term scope: packaged Linux Unreal dedicated host, identity/content compatibility and complete campaign backup/restore acceptance. No deployment started or implied. |
| <a id="f52"></a>F52 | Mounts and Mounted Travel | optional-long-term | Retained long-term scope: real owned/persistent mounts and mounted party travel; no accepted mounted system found. |
| <a id="f53"></a>F53 | Housing and Shared Property | optional-long-term | Retained long-term scope: owned homes/furnishing and shared-property persistence/policies; distinguish from existing ordinary storage. |
| <a id="f54"></a>F54 | Wounds, Bleeding and Limb Loss | optional-long-term | Retained long-term scope: general authoritative wounds/bleeding/limb-loss treatment and matching visuals; scripted witness treatment and ordinary death/rescue already exist. |
| <a id="f56"></a>F56 | Broader Faction Campaigns | optional-long-term | Retained longer-term faction/story arcs, meaningful side quests, shared choices and personal consequences; map each to existing vampire/camp/local-quest authorities rather than duplicate campaigns. |
| <a id="f58"></a>F58 | Player Vampirism and Lycanthropy | optional-long-term | Retained long-term player vampirism/lycanthropy progression and transformations; vampire antagonists do not establish playable transformation. |
| <a id="opt-001"></a>OPT-001 | Optional inn upstairs scripted ambience/story idea | optional | Keep recorded idea for possible authored inn event after unsuitable audio audition; no approved scene or scope. |
| <a id="opt-002"></a>OPT-002 | Evaluate optional live NPC voice conversation input | optional | Keep authored/contextual voiced dialogue first; separately evaluate NPCTalk or alternative live conversation input with replaceable voice provider, spatial audio/subtitles, lore/knowledge/spoiler grounding and fallback text. |

## Monitoring and acceptance rollup

| ID | Item | State | Boundary |
| --- | --- | --- | --- |
| <a id="dbg-014"></a>DBG-014 | Source Editor World Partition cell rejected on remote join | monitoring | Historical source World Partition join correction has focused proof. No matching Journey42 recurrence is established. Monitor the exact symptom; broad every-map/late-join testing is not an outstanding fix by itself. |
| <a id="dbg-015"></a>DBG-015 | Pawn capsule blocks floor-readiness ray | monitoring | Historical capsule/self-hit floor-ray correction has focused proof. No matching Journey42 recurrence is established. Monitor exact floor-readiness failure; do not schedule an unchanged global travel suite. |
| <a id="dbg-040"></a>DBG-040 | Recurring fatal D3D12 render crash, including cheese Take | monitoring | Targeted duplicated material-collection-identity repair shipped40 and remains inherited by42. Normal packaged cheese Take20 and cooked metadata/shader checks passed. No post40 matching recurrence is established. Monitor actual recurrences; original sole allocation/free cause/global crash freedom remain unproved, but do not reopen the demonstrated hazard or repeat quiet routes merely for extra samples. |
| <a id="f60"></a>F60 | Treacherous Woods Quality Slice | rollup | Acceptance rollup for the original treacherous-woods slice: route rhythm, fair counterplay and solo/party quality across the linked delivered systems. This is a rollup, not an additional copy of linked implementation work. |

## Closed or excluded scopes

| ID | Item | State | Boundary |
| --- | --- | --- | --- |
| <a id="dbg-002"></a>DBG-002 | Healer's list discoverability | closed | No accepted matching recurrence. Preserve the exact released fix; adjacent broader work remains separately tracked. No current missing-spawn proof; broader unaided discovery remains a usability concern, not a fresh missing-feature claim. |
| <a id="dbg-021"></a>DBG-021 | Fresh messenger launcher exits before connect | closed | No accepted matching recurrence. Preserve the exact released fix; adjacent broader work remains separately tracked. No current matching launcher recurrence established. |
| <a id="dbg-023"></a>DBG-023 | Borrowed wooden axe rendered as sword | closed | No accepted matching recurrence. Preserve the exact released fix; adjacent broader work remains separately tracked. Current grip and pose quality is036, not proof the original fallback returned. |
| <a id="dbg-026"></a>DBG-026 | Inventory Filter/Sort/Character controls | closed | No accepted matching recurrence. Preserve the exact released fix; adjacent broader work remains separately tracked. No current exact recurrence; this is not universal UI acceptance. |
| <a id="dbg-041"></a>DBG-041 | Giant sweeping grave-worker shovel surface | closed | No accepted matching recurrence. Preserve the exact released fix; adjacent broader work remains separately tracked. Original recorded pixels lack frame-exact actor attribution; no global geometry closure. |
| <a id="dbg-044"></a>DBG-044 | Bread icon black background | closed | No accepted matching recurrence. Preserve the exact released fix; adjacent broader work remains separately tracked. No world-space outline cause or separate selected-book cooked view is claimed. |
| <a id="dbg-059"></a>DBG-059 | Starter shrew kills omitted from10/30/70 hunt credit | closed | No accepted matching recurrence. Preserve the exact released fix; adjacent broader work remains separately tracked. Twelve nest definitions are not twelve verified live sites; broader hunt ecology remains057, not a reason to call starter credit absent. |
| <a id="f01"></a>F01 | Loading Tips Expansion | closed | 26 spoiler-free lore/mining/crafting tips. |
| <a id="f05"></a>F05 | Themed Quest Dialogue UI | closed | Themed topic-dialogue/campaign presentation has shipped Journey8 campaign UI and real remote story progression. Preserve that bounded delivery. Current text/resolution issues are DBG-022/F37; no separate dialogue reimplementation task inferred. |
| <a id="f14"></a>F14 | Off-Hand Torch Combat | closed | Rebindable torch strike, directional block and saved contact wear. World ignition is a separate open feature. |
| <a id="f35"></a>F35 | Selected Weapon Ammunition HUD | closed | Selected bow ammo/count follows actual shots and equipment state; future ammo weapons use the same policy. |
| <a id="f41"></a>F41 | Default Builds for Every Class | closed | Valid editable six-ability presets for all twelve supported classes. |
| <a id="f42"></a>F42 | Character Names and Profanity Filter | closed | GUI name entry, inline validation, modest whole-token profanity filtering, cancel/reopen and chosen-name persistence passed in packaged Journey16; retained17 startup proof. |
| <a id="f57"></a>F57 | Removed — Skyrim Shouts | excluded | Excluded by project scope: no Skyrim shouts, dragon-soul progression or Dragonborn story-role system. |
| <a id="f61"></a>F61 | Realistic Ground Resource Pickups | closed | 84cm sticks/50cm fibre verified; sizing closed at user request. Rocks/scatter/physics/felling separate. |
| <a id="f63"></a>F63 | Torch Hand Attachment | closed | Native-fist attachment and walking/guard/strike tested on current rig. Wider rigs and owner-facing glare polish remain separate open work. |
| <a id="f64"></a>F64 | Off-Hand Item Blocking and Wear | closed | Supported current offhand items (torch, dagger, firestarter and two shields) use directional block, differentiated mitigation/stamina and persistent contact wear; packaged0.20.8 remote/rendered proof passes. |

## Numbering and maintenance

Keep F01–F64 and all assigned DBG IDs. DBG-028 and DBG-034 remain unassigned. New defect IDs are DBG-061–074; new change IDs CHG-001–018; optional ideas OPT-001–002. Append future IDs without renumbering existing items or reusing closed IDs. Give repeated reports an alias or a numbered sub-item under the existing outcome; create a new owner only for a distinct outcome.

Every audited newer intake has one owner/sub-item mapping in `intake_to_owner` in the JSON. Closed delivered slices are retained separately in `closed_slices`. Prepared, source-checked, native-accepted, cooked and released remain distinct stages. Preserve current actors, save identities, server authority and approved art/UVs; these standing rules are acceptance constraints, not newly completed tasks.

The detailed evidence pointers name local working documents and prepared reports. Their payloads are not uploaded to this documentation repository. Missing historical pointers remain labeled, rather than presented as newly checked receipts. Existing `CURRENT_WORK.md` remains the live execution authority; this register controls numbered intake/navigation and its audit date is not a live gameplay monitor.

<!-- expanded-history:start -->
**Expanded history:** the [source ledger and combined statistics](../history/README.md) now cover **1,060 source commits across local branches**, including the **612 HEAD subset**, and the separate documentation history. The older table below retains its original audited baseline.
<!-- expanded-history:end -->

## Commits and pull requests

At the audited baseline **2026-10-30T13:03:27.343368+00:00**:

| History | Count | Scope |
| --- | ---: | --- |
| Local source commits | 612 | Reachable from local source HEAD `8051561`; uncommitted work excluded. |
| GitHub commits | 94 | Separate documentation repo at [4a85f01](https://github.com/CA-The-destroyer/G-Ash_Road_ep1/commit/4a85f01208501e9abeceda70b7a80a89489022b6); before this publication. |
| Pull requests | 0 | Open 0; merged 0; closed without merge 0. |

The two commit totals describe different repositories and must not be added. Pull requests do not mean client `git pull` commands. This register publication adds its own documentation commit after the audited baseline.
