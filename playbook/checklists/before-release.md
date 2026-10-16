# Before release

For publishing versioned software (applications, packages, libraries, CLIs). See the release workflow and the release checklist template in the ci-cd-and-deployment skill.

- [ ] Commits since the last release are reviewed and classified (breaking, feature, fix).
- [ ] The version number follows semantic versioning and the reason is stated.
- [ ] The changelog and version files are updated; breaking changes include migration steps.
- [ ] The full checks pass on the release commit.
- [ ] The artifact was built from a clean checkout of that commit.
- [ ] The artifact was installed in a clean environment and the quick start works.
- [ ] Dependencies and licenses were reviewed; dependency audit has no unaddressed critical findings.
- [ ] Signing keys, tokens and publishing credentials are available securely (not in the repository).
- [ ] I have authorization to tag and publish, or I will stop before the publish step and give the commands.
- [ ] I know how to roll forward or yank a bad release.
- [ ] After publishing: I fetched or installed the published artifact to verify it, and I recorded the evidence.
