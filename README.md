# Property KB plugin

Current, dated, referenced facts on Malaysian new property projects for property agents' AIs,
with skills for client matching, price quotes, affordability, mock calls and call reviews.

This repository holds only the installable plugin: manifests and skills. Using the tools needs
a Property KB account: sign in with Google when your AI asks, then wait for approval.

- Website: https://daryl0101.github.io/property-kb-plugin/
- Install instructions (written for your AI to follow): https://property-kb-plugin-64268236583.us-central1.run.app/install
- Claude Code: `claude plugin marketplace add Daryl0101/property-kb-plugin` then
  `claude plugin install property-kb@property-kb`
- Claude or ChatGPT apps: add a connector/app with the MCP address `https://property-kb-plugin-64268236583.us-central1.run.app/mcp`, and the
  folders of `property-kb/skills/` as skills where your app offers them.

Generated from the Property KB code repository (`pkb plugin export`); changes made here are
overwritten.
