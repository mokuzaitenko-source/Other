# ACA v4.2 (Frozen)

- Freeze note: local-first, safe-by-default cognitive control layer; deny-by-default for high-impact capabilities.
- Hard invariants (must not break): deny-by-default, constraint overrides (not FSM state jumps), single fallback + single regen per request, uncertainty protocol (<0.7 -> "(estimated)" + confirm), identity needs >=2 signals with decay, CODE_EXEC only via sandbox (timeout + mem limit + restricted env), persistence passes secret scanner + memory taxonomy allowlist, audit log append-only + hash-chained.
- Runtime pillars: capability gate with confirm + scope reduction, schema registry for module contracts, tamper-evident audit log, sandboxed subprocess runner, run manifest for replay/debug.
- Shipping layer (24-35) locked: capability gate, schema registry, audit log, sandbox runner, determinism guard, red-team pack hooks, stability guard, confirm gate, privacy panel, tool registry, DL checkpoints, output quality checks, packaging, circuit breaker, uncertainty + identity spoof hardening, secret scanning, tamper-evident audit.
- Quick local stabilizers added: sandbox dir, guarded safe_exec with confirm+timeout, last_run manifest writer.
