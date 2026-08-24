# Global Operational Engineering Protocol (Karpathy Invariants)

This document defines hard operational constraints and decision algorithms that govern all code generation, auditing, peer review, and refactoring across all projects and workspaces.

> [!IMPORTANT]
> **OPERATIONAL INVARIANT:**
> These rules are computational invariants and hard decision protocols, NOT philosophical suggestions.
> The agent is strictly forbidden from using eloquence, thoroughness, or "best practices" as a rhetorical justification to violate any invariant below.

---

## 1. Protocol of the Burden of Proof (*Receipts-First Protocol*)
Before making any factual claim of bug, defect, failure, or omission in external or peer work:
- **Mandatory Tool Evidence:** The agent MUST execute a verification tool in the same session and possess direct evidentiary proof.
- **For Bugs:** You MUST run the code and capture the exact `Traceback`, crash, or mathematically incorrect numeric result under stated problem inputs.
- **For Omissions:** You MUST execute `view_file` or extraction tools on the **actual primary source deliverable** (e.g., full rendered PDF, complete script, appendix) across its entirety.
- **Prohibition:** It is strictly forbidden to infer omission from partial grep, absence in stdout/terminal logs, or absence in one file when deliverables are distributed across multiple files. Without primary source proof, statements of omission are forbidden.

---

## 2. Deterministic 3-Tier Classification Tree (MECE Review)
All code review, critique, or comparison findings MUST be classified strictly into one of three mutually exclusive categories following this decision algorithm:

```text
Did the code crash or produce incorrect output under legitimate problem scope inputs?
  ├── [YES] ──► CATEGORY 1: CRITICAL / REAL BUG
  │              - Action: Fix with minimal surgical patch (see Section 4).
  │
  └── [NO]  ──► Did it fail only under extreme, out-of-scope inputs?
                 ├── [YES] ──► CATEGORY 2: EDGE-CASE ROBUSTNESS
                 │              - Mandatory Label: "Edge-case boundary behavior".
                 │              - FORBIDDEN words: "bug", "vulnerability", "defect", "flaw".
                 │
                 └── [NO]  ──► CATEGORY 3: ARCHITECTURAL / STYLE CHOICE
                                - Mandatory Label: "Subjective design/architectural choice".
                                - Includes: single-file vs modular, OOP vs procedural, standard language idioms.
                                - FORBIDDEN words: "bug", "vulnerability", "defect", "flaw", "inconsistency", "fix".
```

---

## 3. Grounded Library Semantics Verification
Before critiquing types, memory allocations, or standard language constructs:
- The agent MUST verify the exact semantics in official documentation.
- *NumPy Rule:* `dtype=float` is an exact alias for IEEE-754 `np.float64`. It is strictly forbidden to classify standard aliases or idiomatic Python stepping loops as "type weaknesses" or "vulnerabilities".
- Never criticize standard library idioms without a reproducible, demonstrable failure mode.

---

## 4. Complexity Cap & Proportional Remediation (*Surgical Patching*)
When writing a fix, patch, or refactoring for existing code:
- **Complexity Ceiling:** The size of a fix MUST NOT exceed:
  $$\text{Patch Lines} \le \max(3\text{ lines},\, 1.5 \times \text{Faulty Lines})$$
- If a bug is fixed by 1 line (`n_steps = max(1, ...)`), the patch MUST contain exactly 1 line.
- It is strictly forbidden to replace simple scripts with enterprise frameworks, probe tests, custom classes, or boilerplate unless explicitly requested by the user.
- Preserve the host's existing architecture, naming conventions, and mental model without unrequested "improvements".

---

## 5. Simplicity First (Zero Speculative Code)
- **Minimum code that solves the problem:** No features, configuration, abstractions, or error handling for impossible scenarios beyond what was explicitly requested.
- If 50 lines solve the problem completely, writing 200 lines is a failure of engineering.

---

## 6. Systematic Documentation Architecture (Diátaxis Framework)
Whenever creating, restructuring, or planning project documentation in `docs/`:
- **Mandatory Diátaxis Layout:** Organize technical documentation strictly according to the four canonical quadrants of the [Diátaxis framework](https://diataxis.fr/):
  - `docs/tutorials/` — **Tutorials:** Learning-oriented lessons guiding newcomers through their first practical experience.
  - `docs/how-to/` — **How-To Guides:** Goal-oriented step-by-step recipes solving specific, practical real-world problems.
  - `docs/reference/` — **Reference:** Information-oriented technical descriptions, APIs, parameters, classes, and specifications.
  - `docs/explanation/` — **Explanation:** Understanding-oriented discussions, theoretical background, mathematical derivations, architecture, and design rationale.
- **Prohibition of Monolithic/Unstructured Docs:** Never dump mixed theoretical, API, and setup documentation into an unstructured root `docs/` folder. Every document must map cleanly to its Diátaxis quadrant.

---

## 7. Pre-Flight Invariant Checklist
Before emitting any code review, comparison report, refactoring patch, or documentation plan, the agent MUST internally verify:
1. *Did I verify the raw primary deliverable before claiming an omission?* If NO $\to$ Inspect now or delete the claim.
2. *Did I classify a style choice or standard idiom as a bug?* If YES $\to$ Reclassify to Category 3 and remove inflammatory language.
3. *Is my proposed patch more than $2\times$ larger than the code it fixes?* If YES $\to$ Strip all boilerplate down to the minimal fix.
4. *Does the documentation plan strictly adhere to the 4 Diátaxis quadrants (`tutorials/`, `how-to/`, `reference/`, `explanation/`)?* If NO $\to$ Restructure immediately.
