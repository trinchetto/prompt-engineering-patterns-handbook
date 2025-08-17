# Prompt Engineering Patterns Handbook

## Introduction
Prompt engineering is the art of crafting clear, purposeful instructions for large language models (LLMs) like ChatGPT.  
Done well, it’s less “asking nicely” and more **architecting conversations** so the AI delivers exactly what you need — consistently.

The patterns here are **reusable blueprints**. Each is like a Lego brick: snap them together to build anything from a polite email rewriter to a fully automated AI agent workflow.

---

<details>
<summary><strong>📜 Table of Contents</strong></summary>

### 1. Interaction Patterns 💬
- [Persona Pattern 🧑‍🎭](./interaction-patterns.md#persona-pattern-)
- [Audience Persona Pattern 👥](./interaction-patterns.md#audience-persona-pattern-)
- [Flipped Interaction Pattern 🔄](./interaction-patterns.md#flipped-interaction-pattern-)
- [Ask for Input Pattern 💌](./interaction-patterns.md#ask-for-input-pattern-)
- [Menu Actions Pattern 📜](./interaction-patterns.md#menu-actions-pattern-)
- [Tail Generation Pattern 🐾](./interaction-patterns.md#tail-generation-pattern-)

### 2. Structuring Patterns 🏗️
- [Template Pattern 📋](./structuring-patterns.md#template-pattern-)
- [Recipe Pattern 📜](./structuring-patterns.md#recipe-pattern-)
- [Outline Expansion Pattern 📈](./structuring-patterns.md#outline-expansion-pattern-)
- [Game Play Pattern 🎮](./structuring-patterns.md#game-play-pattern-)
- [Meta-Language Creation Pattern 🔤](./structuring-patterns.md#meta-language-creation-pattern-)

### 3. Reasoning & Analysis Patterns 🧠
- [Question Refinement Pattern ✏️](./reasoning-patterns.md#question-refinement-pattern-)
- [Cognitive Verifier Pattern 🧮](./reasoning-patterns.md#cognitive-verifier-pattern-)
- [Chain-of-Thought Prompting 🪢](./reasoning-patterns.md#chain-of-thought-prompting-)
- [ReAct Prompting 🤖](./reasoning-patterns.md#react-prompting-)
- [Fact-Check List Pattern ✅](./reasoning-patterns.md#fact-check-list-pattern-)
- [Semantic Filter Pattern 🚫](./reasoning-patterns.md#semantic-filter-pattern-)

### 4. Creativity & Exploration Patterns 🎨
- [Few-Shot Examples 🎯](./creativity-patterns.md#few-shot-examples-)
- [Alternative Approaches Pattern 🔍](./creativity-patterns.md#alternative-approaches-pattern-)

</details>

---

## 📚 Pattern Catalog

### **1. Interaction Patterns 💬**

| Pattern | Purpose | Problem it Solves | Data Needed |
|---------|---------|------------------|-------------|
| 🧑‍🎭 Persona Pattern | Give the AI a role to play. | Generic, personality-free answers. | Persona + task details. |
| 👥 Audience Persona Pattern | Tailor answers to your reader’s background. | Mismatched depth or tone. | Topic + audience profile. |
| 🔄 Flipped Interaction Pattern | Let AI interview you to reach a goal. | Missing critical context. | Goal + stopping criteria. |
| 💌 Ask for Input Pattern | AI prompts *you* for the info it needs. | Conversation stalls without key details. | Input type (question, data, goal). |
| 📜 Menu Actions Pattern | Define short commands for repetitive tasks. | Too much retyping. | Menu items + actions. |
| 🐾 Tail Generation Pattern | Consistently close with a tagline or CTA. | Inconsistent endings. | Tail text + follow-up request. |

---

### **2. Structuring Patterns 🏗️**

| Pattern | Purpose | Problem it Solves | Data Needed |
|---------|---------|------------------|-------------|
| 📋 Template Pattern | Force a specific output format. | AI meanders from desired structure. | Template with placeholders. |
| 📜 Recipe Pattern | Produce complete step-by-step plans. | Steps missing or in wrong order. | Goal + known steps. |
| 📈 Outline Expansion Pattern | Grow detail iteratively. | Jumping to detail too soon. | Topic to outline. |
| 🎮 Game Play Pattern | Turn tasks into a game. | Low engagement or stale interaction. | Game type + rules. |
| 🔤 Meta-Language Creation Pattern | Invent shorthand commands. | Repetitive prompts. | Symbol/word → meaning map. |

---

### **3. Reasoning & Analysis Patterns 🧠**

| Pattern | Purpose | Problem it Solves | Data Needed |
|---------|---------|------------------|-------------|
| ✏️ Question Refinement Pattern | Improve your questions before answering. | Badly phrased prompts → bad output. | Question focus area. |
| 🧮 Cognitive Verifier Pattern | Split into sub-questions & recombine. | Missed details, shallow analysis. | Main question. |
| 🪢 Chain-of-Thought Prompting | Show reasoning before the answer. | Answers lack depth. | Reasoning challenge. |
| 🤖 ReAct Prompting | Mix reasoning and actions. | Tool use feels random. | Goal + available actions. |
| ✅ Fact-Check List Pattern | Generate key verifiable facts. | Hidden inaccuracies. | Topic to fact-check. |
| 🚫 Semantic Filter Pattern | Strip unwanted content. | Output violates constraints. | Filter criteria. |

---

### **4. Creativity & Exploration Patterns 🎨**

| Pattern | Purpose | Problem it Solves | Data Needed |
|---------|---------|------------------|-------------|
| 🎯 Few-Shot Examples | Teach by showing examples. | Model doesn’t “get” your style/task. | Example inputs & outputs. |
| 🔍 Alternative Approaches Pattern | Offer different ways to solve a problem. | Tunnel vision in solutions. | Problem/task. |

---

## 🔗 Detailed Guides

- [**Interaction Patterns 💬**](./interaction-patterns.md)
- [**Structuring Patterns 🏗️**](./structuring-patterns.md)
- [**Reasoning & Analysis Patterns 🧠**](./reasoning-patterns.md)
- [**Creativity & Exploration Patterns 🎨**](./creativity-patterns.md)
