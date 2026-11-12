# BRIEF.md

> Single source of truth for this site. Lines marked TODO are still open with the owner.
> Lines marked (default) were chosen by Claude because the owner had no preference yet.

## 1. The basics

- Brand name: AV Elite Home Renovation LLC
- One line on what it is: home renovation company
- Where it operates: New York and New Jersey
- Primary language: English
- Secondary language, if any: Spanish (Latin American), at /es/
- Live domain, if you have one: avelitehomerenovation.com

## 2. Audience and the one job

- Who visits this site: homeowners in New York and New Jersey, mostly on a phone (default)
- The single most important thing a visitor should do: request a free estimate
- Secondary things that also matter: message on WhatsApp, call
- What success looks like in one sentence: more estimate requests arriving on WhatsApp

## 3. Feeling and references

- Three words for the feeling: premium, exact, hands on (default)
- Sites admired / disliked / must avoid: TODO

## 4. Palette (pulled from the job site) (default, to be revisited once the logo arrives)

- Skim coat #f1f1ee (page), joint compound #fbfbf9 (panels), drywall #dcdbd5 (photo slots)
- Slate tile #1f2428 (text, dark band)
- Painter's tape blue #2c66a8 (the one accent)
- White oak #b98f5f (structural: step numbers, list marks)

## 5. Type (default)

- Display: Big Shoulders Display. Body: Hanken Grotesk. Utility: DM Mono (labels, phone).

## 6. Signature element (default)

- Blue painter's tape: a torn strip labels each section, and tape holds the corners of every photo.

## 7. Content and assets

- Sections: hero, services, recent projects, how it works, free estimate form
- Text: drafted by Claude, owner to confirm (services lists and the four process steps)
- Logo: owner has one, TODO add to assets/ (a type wordmark stands in until then)
- Photos: owner has them, TODO add to assets/photos/ (labeled slots stand in until then)

## 8. Contact and actions

- Phone: +1 (929) 866 9637
- WhatsApp: same number (assumed, TODO confirm)
- Email: TODO (not shown on the site yet)
- Physical address and map: none
- Social links: TODO
- Forms: free estimate form that opens WhatsApp with the details filled in. Nothing is stored.

## 9. Tech and hosting

- Stack: plain HTML, CSS and a little JS. `python3 build.py` generates index.html and
  es/index.html from src/template.html; all copy for both languages lives in build.py.
  Preview: `python3 -m http.server` from the repo root.
- Hosting: Hostinger Web Hosting with Git deploy (plan not bought yet)
- CMS: no

## 10. Constraints

- No licence numbers, years in business, prices or reviews until the owner supplies real ones.
