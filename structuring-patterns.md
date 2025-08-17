# Structuring Patterns 🏗️

## Template Pattern 📋
**Description:** Provide the AI with a strict output template to follow.

**Purpose:** Ensures outputs are consistent in structure and easy to parse.

**Problem it Solves:** AI sometimes wanders off-format when left to improvise.

**Data Needed & Why:** Clear template with placeholders — guides formatting and content.

**Quick Copy-Paste Prompt:**
```
Follow this template exactly:

Title: [title]
Summary: [summary]
Steps:
1. [step 1]
2. [step 2]
```
**Examples:**
- *General-purpose*  
  1. Create a meeting note template for my team updates.  
  2. Write a movie review in the format: Plot / Acting / Final Verdict.
- *AI Agent / Custom GPT*  
  1. Output agent run logs in JSON with keys: timestamp, action, result.  
  2. Return function summaries with: Function Name / Purpose / Example Call.

---

## Recipe Pattern 📜
**Description:** Turn a task into a full step-by-step process, like a recipe.

**Purpose:** Breaks complex goals into clear, executable steps.

**Problem it Solves:** Avoids missing steps or presenting them in random order.

**Data Needed & Why:** Final goal + any known constraints or steps.

**Quick Copy-Paste Prompt:**
```
Create a step-by-step process for [goal].
Include preparation, execution, and review steps.
```
**Examples:**
- *General-purpose*  
  1. Make a “recipe” for planning a surprise party.  
  2. Write a step-by-step for assembling IKEA furniture.
- *AI Agent / Custom GPT*  
  1. Create a recipe for building an OpenAI function-calling agent.  
  2. Write a step-by-step for integrating LangChain into a chatbot.

---

## Outline Expansion Pattern 📈
**Description:** Start with a simple outline, then expand each section in stages.

**Purpose:** Keeps writing structured while allowing gradual detail.

**Problem it Solves:** Prevents chaotic information dumps.

**Data Needed & Why:** Topic to outline; expansion requests per section.

**Quick Copy-Paste Prompt:**
```
Create a 5-point outline for [topic]. Then expand each point into a full section.
```
**Examples:**
- *General-purpose*  
  1. Outline a history essay on the Renaissance, then expand each point.  
  2. Outline a marketing plan, then expand with tactics and timelines.
- *AI Agent / Custom GPT*  
  1. Outline a multi-agent system architecture, then expand each module.  
  2. Outline a prompt testing strategy, then expand with sample test cases.

---

## Game Play Pattern 🎮
**Description:** Frame the interaction as a game with rules, roles, and win conditions.

**Purpose:** Boosts engagement and creativity.

**Problem it Solves:** Keeps conversations from becoming monotonous.

**Data Needed & Why:** Game type, rules, and desired outcomes.

**Quick Copy-Paste Prompt:**
```
We will play a game called [game name]. Rules: [rules]. Objective: [objective].
```
**Examples:**
- *General-purpose*  
  1. Play a word-association game where I have to guess your word in 10 tries.  
  2. Play a trivia game where you give me clues, and I guess the answer.
- *AI Agent / Custom GPT*  
  1. Play “Agent Debug Quest” — each round, give me a broken function to fix.  
  2. Play “Prompt Poker” — you give me half a prompt, I complete it to beat your “hand.”

---

## Meta-Language Creation Pattern 🔤
**Description:** Invent a custom shorthand or symbols for recurring instructions.

**Purpose:** Speeds up repeated prompt types.

**Problem it Solves:** Cuts down on typing full instructions every time.

**Data Needed & Why:** List of shorthand commands and their meanings.

**Quick Copy-Paste Prompt:**
```
Whenever I type "[code]", interpret it as "[full instruction]".
```
**Examples:**
- *General-purpose*  
  1. “SUM:” means “Summarize the following text in 3 bullets.”  
  2. “XLT:” means “Translate the following into French.”
- *AI Agent / Custom GPT*  
  1. “DBG:” means “Debug the following code snippet.”  
  2. “SIM:” means “Simulate the given user scenario with the agent.”

---

[🔙 Back to Master README](./README.md)
