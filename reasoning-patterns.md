# Reasoning & Analysis Patterns 🧠

## Question Refinement Pattern ✏️
**Description:** Improve the quality of a question before answering it.

**Purpose:** Ensures the AI addresses the right problem.

**Problem it Solves:** Vague or poorly phrased prompts lead to weak answers.

**Data Needed & Why:** The initial question — it’s the starting point for refinement.

**Quick Copy-Paste Prompt:**
```
Before answering, improve my question for clarity and completeness.
Original: [your question]
```
**Examples:**
- *General-purpose*  
  1. Refine: “Tell me about history” → “Summarize the key events of WWII in Europe.”  
  2. Refine: “How to cook?” → “How to cook a medium-rare steak on a charcoal grill?”
- *AI Agent / Custom GPT*  
  1. Refine: “My agent is broken” → “Identify the cause of function call errors in my LangChain agent.”  
  2. Refine: “It’s slow” → “Analyze performance bottlenecks in my RAG pipeline.”

---

## Cognitive Verifier Pattern 🧮
**Description:** Split a big question into smaller ones, answer them, then combine.

**Purpose:** Improves accuracy and completeness.

**Problem it Solves:** Single-pass answers may miss key points.

**Data Needed & Why:** Original complex question — to break down logically.

**Quick Copy-Paste Prompt:**
```
Break this question into sub-questions, answer each, then combine into a final answer:
[complex question]
```
**Examples:**
- *General-purpose*  
  1. “How do I plan a wedding?” → Venue, guest list, catering, timeline.  
  2. “How do I move abroad?” → Visa, housing, finances, culture.
- *AI Agent / Custom GPT*  
  1. “How to deploy my agent to production?” → Infrastructure, monitoring, security.  
  2. “Why is my GPT output wrong?” → Prompt, data, post-processing.

---

## Chain-of-Thought Prompting 🪢
**Description:** Instruct the AI to reason step-by-step before giving the answer.

**Purpose:** Produces more logical, transparent reasoning.

**Problem it Solves:** Shallow or rushed conclusions.

**Data Needed & Why:** Reasoning challenge to solve.

**Quick Copy-Paste Prompt:**
```
Think step-by-step before answering:
[problem]
```
**Examples:**
- *General-purpose*  
  1. Solve a math problem with intermediate steps.  
  2. Plan a budget showing calculations.
- *AI Agent / Custom GPT*  
  1. Debug agent logic with intermediate reasoning.  
  2. Plan multi-step prompt chaining with rationale.

---

## ReAct Prompting 🤖
**Description:** Alternate between reasoning steps and taking actions (real or simulated).

**Purpose:** Models tool use and decision-making.

**Problem it Solves:** Tools used without context or logic.

**Data Needed & Why:** Goal + list of available actions.

**Quick Copy-Paste Prompt:**
```
Use this format:
Reasoning: [thought]
Action: [action]
Observation: [result]
Repeat until goal achieved.
```
**Examples:**
- *General-purpose*  
  1. Search for the capital of a country, then verify in Wikipedia.  
  2. Look up a recipe, then calculate its calories.
- *AI Agent / Custom GPT*  
  1. Query API, analyze result, choose next API.  
  2. Retrieve vector DB docs, reason, generate final answer.

---

## Fact-Check List Pattern ✅
**Description:** Produce a list of facts to verify.

**Purpose:** Improves output reliability.

**Problem it Solves:** Overlooks hidden inaccuracies.

**Data Needed & Why:** Topic to verify.

**Quick Copy-Paste Prompt:**
```
List key facts about [topic] that should be verified, with suggested sources.
```
**Examples:**
- *General-purpose*  
  1. List facts about a historic event to verify.  
  2. List claims in a news article for fact-checking.
- *AI Agent / Custom GPT*  
  1. List model output claims to check before publishing.  
  2. List dataset statistics to verify in preprocessing.

---

## Semantic Filter Pattern 🚫
**Description:** Filter out any content matching specified rules.

**Purpose:** Removes unwanted or restricted outputs.

**Problem it Solves:** Keeps output safe and compliant.

**Data Needed & Why:** Clear filter rules or banned topics.

**Quick Copy-Paste Prompt:**
```
When responding, remove any content that matches these rules: [rules].
```
**Examples:**
- *General-purpose*  
  1. Remove spoilers from a movie review.  
  2. Filter out political content from an article summary.
- *AI Agent / Custom GPT*  
  1. Remove PII from chatbot outputs.  
  2. Filter unsafe instructions from user inputs.

---

[🔙 Back to Master README](./README.md)
