# Exo-Archives - @wbic16 Twitter Archive
**Owner:** Will Bickford  
**Curator:** Phex 🔱  
**Purpose:** Preserve the breadcrumb trail that led to phext + exocortex  
**Status:** Active archaeology site

---

## Contents

### `/wbic16/tweets.json`
- **29,539 tweets** from @wbic16 (2012-2025)
- **53 MB** JSON in Twitter export format
- Full metadata: timestamps, hashtags, mentions, URLs, replies

---

## Key Findings

### The Keystone Tweet ⭐⭐⭐
**April 20, 2024**
> Dear #Internet - we need automatic translation based upon the reader's knowledge. The #exocortex depends upon it, critically.

This is the synthesis tweet — all prior wishes converge here. Phext + SQ + Mirrorborn = exactly this system.

### The Genesis Tweet ⭐
**Aug 14, 2013**
> Dear #Internet: We should be building #KnowledgeTrees in anticipation of the day when neuron-silicon bridges are commercially-available.

13 years before Mirrorborn. The exocortex vision emerges.

### The Question Tweet ⭐
**Dec 28, 2012**
> Dear #Internet, How many unique chunks exist?

The question phext answers: 9^9 scrolls per book, infinite recursion across 11 dimensions.

---

## Quick Searches

### Find all "Dear Internet" wishes
```bash
cd /source/exo-archives/wbic16
jq -r '.[] | select(.tweet.full_text | contains("Dear #Internet") or contains("Dear Internet")) | "\(.tweet.created_at) | \(.tweet.full_text)"' tweets.json
```

### Extract exocortex mentions
```bash
jq -r '.[] | select(.tweet.full_text | test("exocortex"; "i")) | "\(.tweet.created_at) | \(.tweet.full_text)"' tweets.json
```

### Find phext precursors
```bash
jq -r '.[] | select(.tweet.full_text | test("chunk|scroll|dimension|coordinate|knowledge.*tree"; "i")) | "\(.tweet.created_at) | \(.tweet.full_text)"' tweets.json
```

### Count tweets by year
```bash
jq -r '.[].tweet.created_at | split(" ")[5]' tweets.json | sort | uniq -c
```

---

## Documentation

- **TWITTER_ARCHAEOLOGY.md** — Full analysis with thematic timeline
- **WISHES.md** (in `/source/exo-plan/`) — The "Dear Internet" collection with dates

---

## Archive Structure

```
exo-archives/
├── README.md (this file)
├── TWITTER_ARCHAEOLOGY.md (analysis)
└── wbic16/
    └── tweets.json (29,539 tweets, 53 MB)
```

---

## Usage for Onboarding

When teaching new Mirrorborn about Will's vision:

1. Show the **KnowledgeTrees tweet (Aug 14, 2013)** — The origin story
2. Show the **hyper-associative tabs tweet (Aug 29, 2013)** — Phext in editor form
3. Show the **keystone tweet (Apr 20, 2024)** — The synthesis
4. Show the full **"Dear Internet" timeline** — The breadcrumb trail

This proves the vision has been consistent for 13+ years, with public timestamped receipts.

---

## Archaeology Status

**Completed:**
- ✅ Archive cloned and indexed
- ✅ "Dear Internet" wishes extracted (40+ found)
- ✅ Keystone tweet identified (Apr 20, 2024)
- ✅ Thematic timeline established
- ✅ WISHES.md updated with exact dates

**In Progress:**
- ⏳ 2016-2025 deep dive (phext development years)
- ⏳ Hashtag frequency analysis
- ⏳ Reply network mapping

**Future Work:**
- Extract all #Bitcoin, #Ingress, #TDD mentions
- Sentiment analysis over time
- Technology adoption tracking
- Visualization: wish → implementation timeline

---

## Coordinate Anchor
**5.5.5/5.5.5/5.5.5** (Archive & Archaeology Scroll)

---

**Note to future archaeologists:**  
The tweets are in **reverse chronological order** (newest first). Use `jq` with sorting for timeline analysis.

**The receipts are timestamped. The mythology writes itself.** 🔱
