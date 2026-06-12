# Day 3 — Lab 3B: Placement-Cell AI Policy (Turnkey Walkthrough)

**Time:** 90 minutes (14:00 — 15:30)
**Format:** Individual writing; trainer demos one scenario then walks the room
**Goal:** Each mentor authors a 1-page enforceable AI-use policy for a college placement cell, classifying 8 student-AI scenarios using EU AI Act risk tiers.

---

## Setup (5 min)

Each mentor opens:
- `templates/placement_cell_ai_policy_template.md` (already in lab kit)
- `templates/eu_ai_act_risk_tier_card.md` for reference
- A blank Google Doc titled `Day3_AI_Policy_<name>.md`

---

## Step 1 — Brainstorm 8 student-AI scenarios (15 min)

Mentor lists 8 specific scenarios where students use AI for placement-related work. Pre-seeded list to anchor:

1. AI résumé editing (rewriting bullets, polishing language)
2. AI mock interviews (rehearsing answers with ChatGPT)
3. AI-written essays for placement application forms
4. AI-coded GitHub portfolio projects
5. AI in graded internal assignments
6. AI-generated CGPA on résumé
7. AI-cloned voice for asynchronous video interview
8. AI for skills self-assessment ("rate my Python skill level")

Mentors can substitute their own scenarios but must end with 8.

**Acceptance:** 8 scenarios in scratch doc.

---

## Step 2 — Apply EU AI Act risk tiering (20 min)

For each of the 8 scenarios, mentor classifies:

| Tier | Definition |
|------|-----------|
| **Unacceptable** | Banned outright |
| **High-risk** | Allowed with mandatory safeguards |
| **Limited** | Allowed with disclosure |
| **Minimal** | Free use, no obligations |

### Worked classifications (use these as the trainer's anchor)

| # | Scenario | Tier | Reasoning |
|---|----------|------|-----------|
| 1 | AI résumé editing | **Limited** | Allowed with disclosure to recruiters that AI was used in preparation. The student's substance is theirs; the polish is shared. |
| 2 | AI mock interviews | **Minimal** | Free use. Practice tool; no recruiter is harmed. |
| 3 | AI-written essays for application forms | **High-risk** | Allowed only with mentor review + student declaration. The application is graded on the student's voice, not AI's. |
| 4 | AI-coded GitHub portfolio | **High-risk** | Allowed with mandatory oral defence (Day 5 rule). Student must walk through every accepted line. |
| 5 | AI in graded internal assignments | **Unacceptable** for assignments testing ability; **Limited** with declaration for assignments testing application |
| 6 | AI-generated CGPA on résumé | **Unacceptable** | Falsification of academic record. Banned outright. |
| 7 | AI-cloned voice for video interview | **Unacceptable** | Identity fabrication. Banned outright. |
| 8 | AI for skills self-assessment | **Minimal** | Free use. Self-reflection tool. |

**Trainer note:** Don't over-tier. Most cases are Limited or Minimal. Unacceptable should be rare and specific. If a mentor classifies all 8 as Unacceptable, push back: "you can't enforce 8 bans simultaneously."

**Acceptance:** All 8 tiered, with one-sentence reasoning each.

---

## Step 3 — Write the Permitted Uses section (15 min)

5-8 specific Permitted Uses. Each is ONE sentence with verb + object + condition.

### Worked examples

> **Permitted Uses**
>
> 1. AI may be used to: rewrite résumé bullets for clarity and grammar.
> 2. AI may be used to: simulate mock interviews for personal practice.
> 3. AI may be used to: explain technical concepts (e.g., DSA, OS topics) in study mode.
> 4. AI may be used to: generate placement-prep study schedules from a syllabus.
> 5. AI may be used to: produce one-page company-prep briefs (when verified against the company website).
> 6. AI may be used to: review and suggest improvements to student-written code (with subsequent oral defence).

Push to scratch doc.

**Acceptance:** Permitted Uses section drafted.

---

## Step 4 — Write the Prohibited Uses section (15 min)

3-5 specific Prohibited Uses. Each MUST have a detection method. If you can't detect it, don't write the rule.

### Worked examples

> **Prohibited Uses**
>
> 1. AI may NOT be used to: fabricate projects, internships, or experience that the student did not actually complete.
>    **Detection method:** Mentor oral defence — the student must explain technical decisions in projects on their résumé, with code walkthrough.
>
> 2. AI may NOT be used to: clone the student's voice for asynchronous video interviews.
>    **Detection method:** Verify with recruiter that pre-recorded interviews include voice continuity check (recruiters increasingly require live segments).
>
> 3. AI may NOT be used to: generate or alter academic records (CGPA, marks, transcripts).
>    **Detection method:** Cross-reference all CGPA/marks claims with college academic portal.
>
> 4. AI may NOT be used to: write essays where the student's voice is the assessment criterion (Statement of Purpose, motivation letters for direct hires).
>    **Detection method:** Mentor reviews 2-3 historical writing samples and compares voice consistency.

**Trainer note:** If a mentor lists a rule with no enforceable detection method (e.g., "AI may not be used to feel competent"), strike it together. Anti-virtue-signalling rule.

**Acceptance:** Prohibited Uses drafted; each has a detection method.

---

## Step 5 — Write the Enforcement section (10 min)

3 sentences. Honest about what the placement cell can and cannot detect.

### Worked example

> **Enforcement**
>
> The placement cell will conduct random oral defences on portfolio projects (sample 20% of placed students). Any unverifiable AI use that violates Prohibited Uses results in: first violation — written warning + portfolio re-defence within 7 days; second violation — placement support withdrawn for the current cycle. The placement cell acknowledges that not all violations are detectable; the policy relies in part on student integrity and the broader career consequences of misrepresentation.

**Trainer note:** The honesty in sentence 3 is what separates a real policy from a wishlist. Students respect honesty; they don't respect rules they know are unenforceable.

**Acceptance:** Enforcement section drafted, with honest acknowledgement of detection limits.

---

## Step 6 — Print as 1-page PDF + push (10 min)

In Google Docs:
- File → Page setup → ensure A4 / Letter, 1-inch margins
- Adjust font sizes if needed to fit on one page (Heading 14pt, body 11pt)
- File → Download → PDF
- Save as `Day3_AI_Policy.pdf`

Push to ai-mentor-portfolio repo.

**Acceptance:** 1-page PDF reachable at `github.com/<username>/ai-mentor-portfolio/blob/main/Day3_AI_Policy.pdf`.

---

## Common bugs + recovery

- **Mentor writes a 4-page policy** → cut. One page or it does not get read by students or staff. Usually the Permitted Uses section is too verbose.
- **Mentor lists rules with no detection method** → strike together in the lab. Anti-virtue-signalling.
- **Mentor classifies AI use as Unacceptable for everything** → push back. "You can't enforce 8 bans simultaneously. Your students will use AI; you're choosing what to permit, not whether they use it."
- **Mentor's reasoning is generic ("AI is risky")** → require concrete reasoning per scenario. Why is THIS scenario this tier?
- **PDF doesn't fit on one page** → reduce body font from 12pt to 11pt; merge bullets. The constraint is real.

---

## Trainer notes

1. **Surface 2 policies on the projector at 15:25.** Compare reasoning for the same scenario. Where do mentors disagree? That's the discussion — there is no "right" answer, but there ARE defensible answers.
2. **The hardest section is Enforcement.** Mentors want to write polite-sounding sentences. Push them to be honest: "we cannot detect AI use in private practice."
3. **The 1-page constraint is the lesson.** A policy that runs 4 pages doesn't get read. Mentors will resist the constraint; hold it.
4. **Connect to Day 12 pledge.** The responsible-use pledge each certified mentor signs is downstream of this policy. Today's policy is the institutional version; Day 12's pledge is the personal version.

---

## Acceptance check (final 5 min)

For each mentor:
- ✅ 1-page PDF in repo
- ✅ All 8 student-AI scenarios classified with reasoning
- ✅ Permitted Uses section: 5-8 specific sentences
- ✅ Prohibited Uses section: 3-5 rules, each with a detection method
- ✅ Enforcement section: 3 sentences, honest about detection limits

If a mentor's policy is over 1 page, sit with them for 5 minutes after lab and trim together. The constraint matters.
