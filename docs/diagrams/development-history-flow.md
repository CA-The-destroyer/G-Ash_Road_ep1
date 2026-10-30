# Development history and publication flow

![The Ash Road development history and publication flow](development-history-flow.png)

[History and combined statistics](../history/README.md) · [PNG](development-history-flow.png) · [SVG](development-history-flow.svg) · [Mermaid source](development-history-flow.mmd)

Working source and authoring assets feed both local source commits and reviewed release freezes. A freeze includes its committed base plus reviewed working changes; the current source HEAD alone does not describe every later playable package. Unreal build/cook/archive and focused acceptance determine promotion.

Commit metadata, aggregate statistics and release evidence are published to the separate documentation repository. Its direct commits to main explain the zero pull-request count. Source hashes are recorded in the ledger without implying that their source trees or Git objects are hosted in this repository.

The current HEAD ancestry is a subset of all reachable local source commits. Combined statistics deduplicate the two repository histories by full commit SHA. Unique commit objects are not unique features, accepted releases or independent patches.

```mermaid
flowchart LR
    authorWork["UNREAL / BLENDER / AI authoring"] --> freezeUat["Reviewed freeze and Unreal build / cook / archive"]
    freezeUat --> playableRelease["Journey44 promoted; Journey43 rollback"]
    authorWork -->|"Record commits"| sourceHistory["Local source Git: 1060 all-ref commits; 612 in HEAD ancestry"]
    sourceHistory -->|"Export ledger"| publicMetadata["Reviewed commit metadata and aggregate statistics"]
    freezeUat -->|"Publish evidence"| publicMetadata
    publicMetadata --> docsHistory["GitHub documentation: 102 commits; 0 pull requests"]
    playableRelease -->|"Record status"| docsHistory
    classDef source fill:#DDEFEF,stroke:#478F91,color:#102B32;
    classDef delivery fill:#FFF0D2,stroke:#B98E49,color:#443315;
    classDef released fill:#DDEFE3,stroke:#508965,color:#173625;
    classDef docs fill:#E2EBF7,stroke:#6686B0,color:#172D48;
    class authorWork,sourceHistory source;
    class freezeUat,publicMetadata delivery;
    class playableRelease released;
    class docsHistory docs;
```

[render_history_flow.py](render_history_flow.py) recreates the PNG, SVG and Mermaid from the published history JSON using Python/Pillow and installed Windows Segoe UI fonts. Fonts are not redistributed.
