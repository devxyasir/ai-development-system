# Decision trees and examples

Short rules for recurring decisions. They are starting points; project requirements win. Examples are illustrative and contain no measured data.

## Create a new component or reuse one?
- Does an existing component do this job? Yes: reuse it.
- Does it nearly fit, and the missing piece is general (another variant, a slot)? Yes: extend it.
- Is the behavior or structure genuinely different? Yes: create a new component and share primitives.
- Is the markup used once? Keep it local; do not extract yet.

## Local state or shared state?
- Can it be derived from props, state or the URL? Derive it.
- Used by one component only? Local state.
- Needed by siblings? Lift to the nearest common parent.
- Shareable or restorable (filters, tabs)? URL state.
- Data owned by the server? Server cache (query or loader), not a global store.
- Truly cross-cutting UI state (theme, session)? Shared store or context.

## SQL or document database?
- Data has relationships, constraints, multi-record transactions, ad hoc queries? Relational.
- Records are self-contained, hierarchical, read together, with simple access paths? Document store is reasonable.
- Team and operations already run one of them? Prefer it unless a requirement forces otherwise.
- Never choose a database because it is popular.

## Is a monolith enough?
- Single team, one deployable product, unclear boundaries? Yes: modular monolith.
- Different parts need independent scaling, deployment cadence or reliability, and boundaries are stable? Consider services for those parts only.
- The reason to split must be a requirement you can name.

## Do I need a queue?
- Work is slow (more than a few seconds), unreliable, or bursty and the user need not wait? Yes: queue or background job.
- Several independent consumers of the same event? Yes: queue or events.
- Otherwise a direct function call is simpler.

## Direct function call, workflow or agent?
- Rules or code can solve it reliably? Deterministic code.
- One language task with bounded input? Single model call.
- Known sequence of model steps? Workflow.
- Needs your documents or fresh data? Retrieval.
- Cannot predict the steps and evaluation shows a workflow fails? Agent with limits.
- Multiple agents only when one agent demonstrably fails.

## Should I cache?
- Is the result expensive and requested repeatedly? Consider caching.
- Can it tolerate staleness? How stale?
- Can I define invalidation (time-based or event-based) and what happens on a miss storm?
- If any answer is no, fix the slow operation instead.

## Should I add an index?
- Is a real query slow (measured, with its plan)? Look for a missing index on the filter, join or sort columns.
- Does the table receive heavy writes? Weigh the write cost.
- After adding: confirm in the plan that it is used and that timing improved.
- Do not add indexes by guess.

## Does this need an integration test?
- It crosses a boundary (database, queue, HTTP, file system) or wires components together? Yes.
- It is pure logic? A unit test is enough.
- It is a critical user journey? One end-to-end test as well.

## Does this UI need visual regression testing?
- Stable, design-critical, shared component or page where small visual changes matter? Yes, with a small baseline set.
- Frequently changing, content-driven, or in early design? No; use manual visual QA.

## Should I ask a clarifying question?
- Does the answer change the outcome materially? Is it unanswerable from the repository or documentation? Is a wrong guess costly? All yes: ask one focused question.
- Otherwise: state the assumption and proceed.

## When to stop researching
- Can I answer: does it exist, how is it called, what are the limits, what does it cost, what is the risk? Yes: stop and implement.
- Am I reading more without a new question? Stop.

## Does this deployment need a rollback plan?
- Always at least a one-line plan (how to return to the previous version).
- Production, data migrations, or customer-visible changes: a written plan with exact commands and the point of no return.

## Good and bad example: bug fix report
Bad: "Fixed the login bug. Should work now."
Good: "Login failed when the email contained uppercase letters because the lookup was case-sensitive. I normalized the email in `auth/login.py` and added `test_login_is_case_insensitive`. Ran `pytest tests/auth`: 14 passed. Not checked: the mobile client."

## Good and bad example: choosing a dependency
Bad: "Added library X because it is popular."
Good: "The project has no date handling beyond the standard library. Needed time zone conversion; the standard library supports it in the installed version, so no dependency was added."
