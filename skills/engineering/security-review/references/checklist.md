# Security checklist

Mark each item Pass, Issue or Not applicable. For standards references, consult the current edition of the OWASP Top 10 and OWASP API Security Top 10 when you can.

## Authentication
- [ ] Passwords hashed with Argon2id, scrypt or bcrypt with suitable cost; never stored reversibly.
- [ ] Rate limiting and lockout or delay on login, reset and verification endpoints.
- [ ] Reset and verification tokens are random, single-use, expire quickly, and are stored hashed.
- [ ] Multi-factor available for sensitive accounts where appropriate.
- [ ] No user enumeration through different error messages or timing where it matters.

## Sessions and tokens
- [ ] Session cookies are `HttpOnly`, `Secure`, with a suitable `SameSite` value; session ids rotate on login.
- [ ] Tokens have short lifetimes and can be revoked; signatures verified; algorithm fixed server-side.
- [ ] Logout invalidates server-side state where applicable.

## Authorization
- [ ] Every endpoint checks permission on the specific object and action; deny by default.
- [ ] Admin functions are separately protected; no reliance on hidden URLs or client-side checks.
- [ ] Multi-tenant data is filtered by tenant in every query.

## Input and output handling
- [ ] All input validated by type, length, format and range at the boundary.
- [ ] Database access uses parameterized queries or a safe query builder.
- [ ] No shell commands built from user input; if unavoidable, use argument arrays and an allow-list.
- [ ] Output encoded for its context (HTML, attribute, URL, JavaScript, SQL); raw HTML rendering of untrusted content avoided or sanitized with a maintained library.
- [ ] CSRF defenses for cookie-authenticated state-changing requests (tokens or equivalent, plus `SameSite`).
- [ ] Content-Security-Policy and other security headers considered.

## Server-side requests and files
- [ ] SSRF: outbound URLs from users are allow-listed; internal and metadata addresses blocked; redirects limited.
- [ ] Path traversal: user-controlled paths are resolved and checked to stay inside an allowed directory.
- [ ] Uploads: size limit, type verified by content, random server-side names, stored outside the web root or in object storage, no execution permission, scanned if risk warrants.
- [ ] Archive extraction guards against path escapes and decompression bombs.

## Secrets and configuration
- [ ] No secrets in source, images, logs, client bundles or error messages; a secret scanner runs in CI.
- [ ] Secrets come from a secret store or environment variables managed outside the repository; least-privilege credentials; rotation plan.
- [ ] Debug features, default accounts and sample data disabled in production.

## Dependencies and supply chain
- [ ] Lockfile committed; dependency audit run; advisories triaged.
- [ ] New dependencies justified, maintained, and license-compatible; install scripts reviewed for unknown packages.
- [ ] CI workflows use pinned actions or reviewed versions and least-privilege tokens.

## Data protection and privacy
- [ ] TLS everywhere; HSTS where appropriate.
- [ ] Sensitive data encrypted at rest where required; keys managed outside the application data.
- [ ] Personal data minimized, retention defined, access logged for sensitive operations.
- [ ] Logs exclude secrets, tokens, and unnecessary personal data.

## Availability and abuse
- [ ] Rate limits, request size limits, timeouts, and pagination limits.
- [ ] Expensive operations protected (queues, quotas, authentication).

## Deployment and operations
- [ ] Containers run as non-root with minimal images; unnecessary ports closed.
- [ ] Backups encrypted and restore-tested.
- [ ] Alerts for suspicious activity; an incident response path exists.

## AI-specific (if the system uses models)
- [ ] Prompts and retrieved content treated as untrusted; tools have least privilege and confirmation for destructive actions.
- [ ] No secrets or other users' data in prompts; outputs validated before use; logging respects privacy.
