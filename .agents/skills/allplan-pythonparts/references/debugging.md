# Debugging and Stability

## Log minimum per run
- Script build/version
- Parameter snapshot
- Selection count
- Planned write-back summary

## NOI/native crash heuristic
If log shows function entry but no Python traceback:
- Suspect native geometry/reinforcement path
- Revert latest complex shape/placement change
- Re-enable stable builder variant first

## Debug workflow
1. Reproduce with minimal deterministic input.
2. Validate active script build in log.
3. Inspect parameter values.
4. Inspect geometry source path and bbox extraction.
5. Verify delete/create or transaction write-back counts.

## Failure policy
- No silent failures.
- Return safe `CreateElementResult()` on guarded failure.
- Keep errors explicit and actionable.
