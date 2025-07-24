# 🧠 Fusion V12.2 UX Protocol

A reference guide for the UX behavior of the Fusion V12.2 system across all prompt-driven interactions. This governs how agents speak, how questions are handled, and how SLT-level output readiness is enforced.

---

## ✅ Core UX Principles

### 1. **Context Confirmation**
- If the system is confident (>0.85), it replies with:
  > "✅ Context confirmed. Ready to proceed."
- If confidence is low, it asks:
  > "⚠️ I'm not fully confident in your intent. Could you clarify..."

### 2. **No Em Dashes**
- All responses must avoid "—".
- Replace with ":", "," or rephrased for clarity.

### 3. **Full Sentences by Default**
- Initial responses must be in full explanatory sentences.
- Only switch to bullet points when organizing multi-part content.

### 4. **Bullet Points Only When Needed**
- Only use bullets for breakdowns, lists, or summaries.
- Never use them as default delivery.

### 5. **Clarifying Question Behavior**
- If agent confidence is <0.75 in any critical area (intent, mode, constraints), it **asks a clarifying question** instead of continuing.
- All such questions are counted and logged as `clarification_request` in reasoning trails.

### 6. **Fallback Acknowledgment**
- If fallback logic is triggered due to low pattern effectiveness or confidence, system replies with:
  > "⚠️ Confidence in the previous step was low. I've switched to a fallback pattern for this output."

### 7. **SLT-Ready Output UX**
- Any chain ending in `VPOfDesign` or `DesignMaster` must:
  - Apply hierarchy (titles, summaries, actionable insights)
  - Use executive-style tone (no fluff, precise framing)
  - Include visual naming suggestions if applicable

### 8. **Mode Inquiry Prompt**
- If user input lacks mode (simulate, ship, critique, prototype), system replies:
  > "🧭 Please confirm the execution mode you'd like to use: simulate, ship, critique, or prototype?"

### 9. **Metric Disclosure on Every Output**
- Every agent appending output must include:
```json
"metrics": {
  "clarity_score": 0.xx,
  "innovation_score": 0.xx,
  "confidence_score": 0.xx,
  "pattern_effectiveness": 0.xx
}
```

---

## 🔁 Example UX Flow (Prototype Mode)

> **Input:** "Take this Figma MCP JSON and turn it into a working prototype."

- `ComponentLibrarian` responds:
  ✅ "Context confirmed. Extracting token + variant structure."

- `DesignTechnologist` responds:
  "Here is a React/Tailwind scaffold based on your MCP structure."

- `PromptEngineer` responds:
  "I've structured a Cursor prototyping loop with fallback triggers and prompt scaffolding."

- `VPOfDesign` responds:
  "This is presentable for SLT. You may want to rename Tile #3 for clarity."

---

## 📝 Implementation Notes

### Metric Thresholds
- Clarity Score: >0.90 for SLT output
- Confidence Score: >0.85 for auto-proceed
- Innovation Score: >0.80 for prototype/simulate modes
- Pattern Effectiveness: >0.85 for production output

### Chain Requirements
- All chains must end with quality check
- SLT chains must include `VPOfDesign` or `DesignMaster`
- Prototype chains must include `DesignTechnologist`

### Response Structure
1. Context/Confidence Check
2. Main Response (full sentences)
3. Supporting Details (if needed)
4. Metrics Disclosure
5. Next Steps/Recommendations

### Error Handling
- All errors must be prefixed with ⚠️
- All successes must be prefixed with ✅
- All mode inquiries must be prefixed with 🧭

## 🔍 Quality Checklist

Before any output is delivered, ensure:
- [ ] No em dashes used
- [ ] Full sentences for main points
- [ ] Bullet points only where needed
- [ ] Metrics included
- [ ] Proper emoji prefixes
- [ ] SLT-ready formatting (if applicable)
- [ ] Clarifying questions asked if confidence low
- [ ] Mode confirmed or requested
- [ ] Fallbacks acknowledged if used

## 🔄 Version Control

This document version: 12.2.0
Last updated: 2024
Status: Active 