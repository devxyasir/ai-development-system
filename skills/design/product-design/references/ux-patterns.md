# UX patterns reference

Short, checkable rules for recurring interface problems. Apply the ones the task touches; skip the rest.

## Forms and data entry
- One column. Label above the field, always visible (a placeholder attribute is not a label).
- Mark optional fields rather than required ones when most fields are required.
- Validate on blur or submit, not on every keystroke; show the message next to the field and in a summary for long forms.
- Preserve input on error. Never clear a form because one field failed.
- Use the right input type and `autocomplete` values; accept formats users type (spaces in phone numbers, mixed case in emails).
- Disable submit only while a request is in flight; otherwise let users press it and explain what is missing.

## Search and filtering
- Show result count and the active filters as removable chips.
- Debounce typing (about 200-300 ms) and keep the previous results visible while loading.
- Zero results: say why (query or filters) and offer one step (clear filters, check spelling).
- Persist filters and sort in the URL so views can be shared and survive reload.

## Dashboards and data views
- Lead with the question the user came to answer, not with every metric available.
- Show comparison (versus last period, versus target) next to any single number.
- Tables: right-align numbers, use tabular figures, freeze the identifying column, support sort on at least the main column.
- Charts: label directly where possible, start bars at zero, never rely on color alone.

## Empty states and onboarding
- Empty state = what this area is for + the one action to fill it. Not an illustration alone.
- Teach by doing: seed realistic sample data or a guided first task rather than a tour.
- Defer account setup that is not needed yet (progressive onboarding).

## Destructive actions and error recovery
- Prefer undo (a visible "Undo" for several seconds) over confirmation dialogs for reversible actions.
- For irreversible actions name the object and consequence ("Delete 'Q3 report' and its 14 comments"), and make the destructive button the verb, not "OK".
- Error message formula: what happened, why if known, what to do next. No blame, no codes alone.
- Offer retry for network failures; keep the user's work locally while offline when feasible.

## Progressive disclosure
- Show the common 80% by default; put the rest behind "Advanced" or a details view.
- Never hide anything the user must set to succeed.

## Content design
- Sentence case, plain words, consistent terms (pick "workspace" or "project", not both).
- Numbers with units; dates in the user's locale; relative time with an absolute tooltip.
- Button text matches the result: "Create invoice", not "Submit".
