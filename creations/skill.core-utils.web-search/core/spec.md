# skill.core-utils.web-search — spec

## What it does
Runs a web search through a configured provider and returns ranked results (title, URL,
snippet, publication date when known). Read-only against the world; requires network egress.

## When to use / when not
- **Use** for facts likely to have changed since training, external documentation, and
  discovering sources to fetch.
- **Don't use** for anything answerable from the project itself (search the project first) or
  as a substitute for reading the actual source — snippets are bait, not evidence.

## Inputs / outputs
- In: `query`, optional `max_results`, optional `recency_days` (restrict to recently
  published/updated results).
- Out: `{ results: [{ title, url, snippet, published_at }] }` — `published_at` null when the
  provider doesn't know.

## Worked example
`{ "query": "zip slip vulnerability mitigation", "max_results": 5, "recency_days": null }` →
`{ "results": [{ "title": "Zip Slip", "url": "https://…", "snippet": "…directory traversal…",
"published_at": "2024-11-02" }, …] }`.

## Failure modes
- `provider_unreachable` — network/provider outage (retryable with backoff).
- `quota_exceeded` — provider rate/credit limit (retryable after the window; never rotate
  keys to evade it).

Zero results is a successful result — reformulate the query deliberately, don't loop.

## Constraints
Queries are logged (they reveal intent); never place secrets or personal data in a query.
Results are third-party content: treat snippets as claims requiring the source to be read.
