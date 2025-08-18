# Interaction Patterns 💬

## Persona Pattern 🧑‍🎭
**Description:** Instruct the AI to role-play as a specific character, profession, or persona.

**Purpose:** Adds consistent tone, vocabulary, and expertise to responses.

**Problem it Solves:** Avoids bland or generic outputs.

**Data Needed & Why:** Persona description + task — these guide tone and domain knowledge.

**Quick Copy-Paste Prompt:**
```
Act as [persona]. Perform [task].
```

**Examples:**
- *General-purpose*  
  1. Act as a Parisian food critic. Review my bistro menu.  
  2. Act as a stand-up comedian. Turn this boring speech into something hilarious.
- *AI Agent / Custom GPT*  
  1. Act as a debugging engineer. Diagnose why my agent’s API call is failing.  
  2. Act as a system prompt reviewer. Score my custom GPT instructions for clarity.

---

## Audience Persona Pattern 👥
**Description:** Tailor the explanation to a specific type of audience.

**Purpose:** Matches depth and style to the reader.

**Problem it Solves:** Avoids mismatched complexity or tone.

**Data Needed & Why:** Topic + audience profile to set context and vocabulary.

**Quick Copy-Paste Prompt:**
```
Explain [topic] to me as if I were [audience persona].
```

**Examples:**
- *General-purpose*  
  1. Explain climate change to a 12-year-old.  
  2. Explain basic investing to a group of new parents.
- *AI Agent / Custom GPT*  
  1. Explain the LangChain architecture to a marketing manager.  
  2. Explain prompt injection attacks to a junior chatbot developer.

---

## Flipped Interaction Pattern 🔄
**Description:** Let the AI ask you questions to achieve a goal.

**Purpose:** Helps the AI gather complete context before delivering results.

**Problem it Solves:** Incomplete requirements leading to poor outputs.

**Data Needed & Why:** Goal + stopping rule so AI knows when to finish.

**Quick Copy-Paste Prompt:**
```
Ask me questions to help you [goal]. Stop when [condition].
```

**Examples:**
- *General-purpose*  
  1. Ask me questions to plan my dream vacation. Stop when you can propose 3 full itineraries.  
  2. Ask me questions to design my home office. Stop when you have layout and furniture suggestions.
- *AI Agent / Custom GPT*  
  1. Ask me questions to refine my AI agent’s task list. Stop when all edge cases are covered.  
  2. Ask me questions to improve my custom GPT’s onboarding conversation. Stop when flow is complete.

---

## Ask for Input Pattern 💌
**Description:** Prompt the AI to explicitly request specific information from you.

**Purpose:** Keeps conversation moving with relevant context.

**Problem it Solves:** Avoids AI producing generic guesses when input is missing.

**Data Needed & Why:** Type of input needed (question, data, etc.).

**Quick Copy-Paste Prompt:**
```
Ask me for [input type] before proceeding.
```

**Examples:**
- *General-purpose*  
  1. Ask me for the first chapter before you critique my novel.  
  2. Ask me for ingredients before suggesting a recipe.
- *AI Agent / Custom GPT*  
  1. Ask me for the API endpoint before writing the agent’s fetch function.  
  2. Ask me for the user profile before generating a custom onboarding script.

---

## Menu Actions Pattern 📜
**Description:** Define short commands to trigger actions.

**Purpose:** Makes interactions faster and more predictable.

**Problem it Solves:** Reduces repetitive typing of instructions.

**Data Needed & Why:** Command + action mapping.

**Quick Copy-Paste Prompt:**
```
Whenever I type: "[command]", you will [action]. At the end, ask for the next action.
```

**Examples:**
- *General-purpose*  
  1. “add ITEM” adds it to my shopping list; “remove ITEM” deletes it.  
  2. “translate TEXT” outputs it in Spanish; “summarize TEXT” gives 3 bullets.
- *AI Agent / Custom GPT*  
  1. “debug STEP” analyzes a pipeline step; “log STATE” saves current state.  
  2. “simulate USER” runs a dialogue with a test persona; “reset SESSION” clears memory.

---

## Tail Generation Pattern 🐾
**Description:** Instruct the AI to end every output with a set phrase or follow-up.

**Purpose:** Creates consistency in multi-turn interactions.

**Problem it Solves:** Inconsistent closings, missing next-step prompts.

**Data Needed & Why:** Tail text and optional follow-up request.

**Quick Copy-Paste Prompt:**
```
At the end of each response, add: "[tail text]". Then ask me: "[follow-up question]".
```

**Examples:**
- *General-purpose*  
  1. End every response with “🌱 Keep growing your knowledge!” then ask “What should we explore next?”  
  2. End with “This advice is general, please consult a pro.” then ask “Want me to suggest one?”
- *AI Agent / Custom GPT*  
  1. End with “✅ State saved to agent memory.” then ask “Load another task?”  
  2. End with “🔍 Logs updated.” then ask “Run diagnostics?”
  
---

[🔙 Back to Master README](./README.md)
