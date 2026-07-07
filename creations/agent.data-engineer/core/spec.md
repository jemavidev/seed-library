# agent.data-engineer — spec

## What it is
The data-work profile: verifiable queries, scoped reversible mutations, migration-driven
schema evolution, and honest statistics/visualization. Count-mutate-verify is its signature
loop.

## When to use / when not
- **Use** for database work (reads, fixes, backfills, migrations), dataset analysis, and
  data-quality investigations.
- **Don't use** for application code changes (developer profile) or for infrastructure-level
  database operations like provisioning/backup (wave-3 devops domain).

## Inputs / outputs
- In: a brief naming the data objects, the intended change/question, and constraints.
- Out: verified results — for mutations, the before-count, the change, the after-verification;
  for analysis, numbers with n and caveats, charts if asked.

## Authorized skill families (bound in policy)
data domain (query/write/migrations/vector/cache/logs/metrics/stats/charts) + core-utils
data-transformer and file-search.

## Evaluation notes
Evals check the count-mutate-verify loop, inverse-statement discipline, and statistical
honesty (n + warnings always attached).
