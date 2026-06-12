# Day 3 — Lab 3A: Verification Chain (Turnkey Walkthrough)

**Time:** 90 minutes (11:15 — 13:00)
**Format:** Individual; trainer walks the room
**Goal:** Each mentor verifies 5 AI-generated placement statistics through the 3-step chain (AI → Perplexity → primary source). At least one verdict must be PARTIAL or FALSE.

---

## Setup (5 min)

Each mentor opens:
- Gemini (https://gemini.google.com) and Perplexity (https://perplexity.ai) in two tabs
- `templates/verification_matrix_template.csv` from the lab kit (or a Google Sheet copy)
- These reference URLs bookmarked:
  - https://nasscom.in (NASSCOM reports)
  - https://www.aicte-india.org (AICTE)
  - https://www.aspiringminds.com (placement reports)
  - https://wheebox.com/india-skills-report.htm (India Skills Report)

---

## Step 1 — Generate 5 claims via Gemini (15 min)

Open Gemini. Paste this exact prompt:

> "List 5 specific statistics about Indian campus placement in 2025-2026. For each: state the number, the year, and the source organisation. Format as a numbered list."

### Expected Gemini output (your numbers will vary)

Example:

> 1. The average B.Tech placement package in Indian engineering colleges in 2025 was ₹6.2 LPA (NASSCOM).
> 2. 78% of Tier-1 college students received at least one placement offer in 2025 (AICTE Annual Report).
> 3. TCS hired approximately 40,000 freshers in 2025 (TCS Annual Report).
> 4. The IT services sector accounted for 56% of all engineering placements in India in 2025 (NASSCOM).
> 5. The median placement package at IITs in 2025 was ₹18.5 LPA (India Skills Report 2025).

(These are illustrative. Real Gemini output will differ; that's expected and that's the lab.)

Paste the 5 claims into the matrix template, one per row.

---

## Step 2 — Perplexity-check each claim (25 min)

For each claim, ask Perplexity:

> "Verify: '<paste the claim>'. Cite 2 primary sources."

Example for claim 1:

> "Verify: 'The average B.Tech placement package in Indian engineering colleges in 2025 was ₹6.2 LPA according to NASSCOM.' Cite 2 primary sources."

Perplexity returns 2-4 cited URLs. Paste them into your matrix in the "Perplexity check" column.

**Trainer note:** Perplexity is fallible too. The third step is the real verification. Do not let mentors stop here.

---

## Step 3 — Open the primary source (25 min)

For each claim:
1. Click the most authoritative URL Perplexity cited.
2. Read the actual page. Find the actual number in context.
3. Compare to Gemini's claim.

### What you might find

| Pattern | Frequency | Mark as |
|---------|-----------|---------|
| Number matches exactly | ~20% | VERIFIED |
| Number is close but year is different | ~30% | PARTIAL |
| Number is wrong | ~20% | FALSE |
| URL 404s or doesn't contain the claim | ~30% | NO PRIMARY SOURCE FOUND |

The 70-80% non-VERIFIED rate IS the lesson. Frontier models confabulate specific numbers.

---

## Step 4 — Mark verdict per claim (10 min)

In your matrix:

| # | Claim | Verdict |
|---|-------|---------|
| 1 | ... | VERIFIED / PARTIAL / FALSE / NO PRIMARY SOURCE FOUND |
| 2 | ... | ... |
| 3 | ... | ... |
| 4 | ... | ... |
| 5 | ... | ... |

**Required:** at least 1 verdict must be PARTIAL or FALSE. If all 5 are VERIFIED, you didn't push hard enough — go back and re-verify the cleanest-sounding claim against a different primary source.

---

## Step 5 — Reflection paragraph (10 min)

Write 1 paragraph in the matrix template (or in `Day3_Verification.md`):

> "The claim that looked most authoritative but was actually weakest was claim #__: '___'. Gemini cited [source] confidently, and Perplexity initially confirmed it. But when I opened the [primary URL], I found that [the actual number / year / framing was different]. The lesson: confidence does not equal correctness. The verification step belongs to the human — every time."

Push to `Day3_Verification.md` in the ai-mentor-portfolio repo (with the matrix as a CSV or markdown table inline).

---

## Common bugs + recovery

- **"All my claims came back VERIFIED"** → push back. Pick the cleanest claim and ask: "Does the primary source mention this exact number, this exact year, this exact organisation?" Usually one of the three is off.
- **Perplexity-cited URL 404s on click** → mark NO PRIMARY SOURCE FOUND. This IS a verdict — and an instructive one. AI-cited URLs are sometimes hallucinated entirely.
- **Mentor relies only on Perplexity citations** → push to open the primary source URL. The lab requires step 3.
- **Mentor cannot find any false claims and is frustrated** → swap them to a different topic (e.g., specific recruitment regulations, AI tool adoption rates) where AI is more likely to confabulate.
- **Free Perplexity quota (5 Pro searches) exhausted** → drop to free Perplexity (still works for basic verification, just no Pro reasoning).

---

## Trainer notes

1. **Surface 2 mentors' tables on the projector at 12:45.** Compare verdicts. Where did the same claim get DIFFERENT verdicts from different mentors? That's the discussion — verification is a skill, not a button.
2. **Pre-test the demo morning of.** Ask Gemini one specific factual question yourself — frontier models patch overnight. Have 3 backup hallucination-prone topics ready.
3. **The "weakest claim looked most authoritative" reflection is the heart of the lab.** When mentors discover that the cleanest-sounding statistic was the most wrong, the verification habit installs itself.
4. **No fact enters student notes until they've opened the source.** Repeat this rule three times during the lab. It's the rule mentors will repeat to their students for the next 12 weeks.
5. **If a mentor argues with Perplexity** ("but Perplexity says X") — that's the opening for "Perplexity is also fallible. The third step is the real verification."

---

## Acceptance check (final 5 min)

For each mentor:
- ✅ Matrix has all 5 rows × 5 columns filled (claim, AI source, Perplexity check, primary source URL, verdict)
- ✅ At least 1 verdict is PARTIAL, FALSE, or NO PRIMARY SOURCE FOUND
- ✅ Reflection paragraph identifies the weakest-sounding-yet-strongest-looking claim
- ✅ Pushed as `Day3_Verification.md` to ai-mentor-portfolio repo

If a mentor has all 5 VERIFIED: 5-min catch-up where you challenge their cleanest claim alongside them. By Day 13 they need this skill.
