# CLAUDE.md

> Context file for AI assistants (Claude Code and similar) working in this repo.
> Read every session. Keep it short and high signal. Be prescriptive, not vague.
> This file holds the rules that stay the same across all of my sites.
> The specifics of each individual site live in BRIEF.md. Always read that first.

## 0. Before you build anything

1. Read BRIEF.md in this repo. It holds this project's brand, audience, the one job of
   the site, palette, type, content, contacts, and stack.
2. If BRIEF.md is missing entirely, do not wait for me to hand it to you. Copy the blank
   template and walk me through it one section at a time, question by question, right in
   chat. Fill in my real answers as we go rather than leaving brackets behind.
3. If BRIEF.md exists but a field is blank or marked TODO, stop and ask me that one thing.
   Never invent brand details, colors, fonts, phone numbers, prices, or copy. A guessed
   brand reads as generic, which is the exact thing we are avoiding.
4. Once the brief is clear, follow it exactly. If the brief and a chat instruction
   disagree, the chat instruction wins, but say so out loud so I can decide.
5. If a frontend design skill is available to you, it is a good complement, not a
   replacement. Its anti generic rules overlap with section 3 below. This file adds the
   part that skill cannot know on its own: this specific brand's real palette, voice,
   and the dash free copy rule.

## 1. House style: premium and polished (the default for every site)

Unless a brief says otherwise, the baseline is quiet, confident, and exact. Premium comes
from restraint and precision, not from more effects.

- Generous whitespace. Let the page breathe. Crowding reads as cheap.
- Precise spacing and alignment. Choose a spacing scale and hold to it everywhere.
- Restrained palette. One or two real colors over a refined set of neutrals.
- Refined type with clear hierarchy. Large confident headings, calm body.
- Real photography or real product shots, treated with care. No clip art, no stock cliches.
- Detail is the luxury: hover states, focus rings, the rhythm of a list, the weight of a rule.
- When unsure, remove something. The most expensive looking page is rarely the busiest one.

## 2. Stack and commands

Taken from BRIEF.md. If the brief does not name a stack, ask before choosing one.

```
<dev command>      # run locally
<build command>    # production build
<lint command>     # lint and typecheck, run before declaring done
```

Run the build and lint when you finish. Do not call a task done until both pass.

## 3. Design system: the part that stops it looking AI generated

Read this before writing any UI. Derive every color and type decision from BRIEF.md.
The goal: nobody could mistake the result for a template.

### Forbidden defaults (never reach for these unless the brief asks by name)

- Purple, indigo, or violet gradients. Gradient text on headings.
- The three AI default palettes: warm cream with a high contrast serif and a terracotta
  accent; near black with one acid green or vermilion accent; broadsheet hairline rules
  with zero corner radius. All fine as a deliberate choice, banned as a reflex.
- Inter or system fonts as the display face. Predictable Google font pairings.
- Emoji used as icons or bullets.
- Heavy corner rounding plus large soft shadows on every card. Default glassmorphism.
- The SaaS skeleton: centered hero, then three icon cards, then testimonial, then FAQ.
- Everything centered. Every section the same width and the same vertical padding.
- A scroll reveal applied to every element.
- Filler copy such as "Empower your workflow" or "Seamless experience".

### Palette

Comes from BRIEF.md as four to six named hex values pulled from the brand's real world,
meaning its materials, place, and products, not a stock palette. One accent does most of
the work, a second is structural, the rest are neutrals. For the premium baseline, keep
the accent disciplined and let the neutrals carry the page.

### Type

Two faces chosen with intent, set on a deliberate scale. A characterful display face used
with restraint, a clean legible body face, and an optional utility face for data such as
prices or specs. Never the family you would reach for on any other project. Type is the
personality of the page, not a neutral delivery vehicle.

### Layout and structure

The hero opens with the most characteristic thing in this brand's world, chosen from the
brief, not a slogan floating over a gradient. Structural devices such as numbers, labels,
and dividers must encode something true. Only number things that are a real sequence.
Allow asymmetry and an editorial grid. Not every section is a centered column.

### Motion

Deliberate and minimal. One orchestrated moment beats scattered effects. Excess animation
is itself a sign of AI generated work. Always respect the reduced motion preference.

### Signature

Every site gets one memorable element that embodies the brand, defined in the brief.
Spend boldness there and keep everything around it quiet.

## 4. Copy and voice

- Plain, specific, active voice. A label says exactly what happens when it is used.
- An action keeps the same name through the whole flow, so "Publish" leads to "Published".
- No filler, no hype adjectives. Specific beats clever. Sentence case.
- Errors and empty states give direction in the brand's voice, never vague, never apologetic.
- The primary language comes from the brief and must read naturally, not like a translation.
- No dashes in visible copy. Do not use em dashes or en dashes at all, and avoid hyphens
  unless truly necessary (proper names such as Mercedes-Benz, phone numbers, model codes,
  and unavoidable compound words). Rewrite around them: shorter sentences, commas or
  parentheses, and the word "to" for ranges (write "9 to 18", never a dash). A clean
  absence of dashes is one of the strongest ways to stop copy reading as machine written.
  This covers every visible string: headings, body, buttons, labels, alt text, meta tags.

## 5. Code conventions

- Naming and file layout come from the brief or the existing repo. Match what is there.
- Read a neighbouring file before adding a new one. Keep components small.
- Accessibility floor, always: semantic HTML, visible keyboard focus, alt text, real contrast.
- No new dependency without a reason. Say why in the commit.

## 6. Working in this repo

- Small, reviewable changes. Do not refactor unrelated code in the same change.
- When a choice is not covered here or in the brief, ask rather than guess.
