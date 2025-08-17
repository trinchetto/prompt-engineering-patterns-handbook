# Contributing to the Prompt Engineering Patterns Handbook

Thanks for helping expand and improve this collection of prompt patterns!  
We welcome contributions that make the handbook more useful for practitioners building prompts and custom GPTs.

---

## 📂 Repository Structure

```
README.md                  # Master index
interaction-patterns.md    # Group 1: Interaction Patterns
structuring-patterns.md    # Group 2: Structuring Patterns
reasoning-patterns.md      # Group 3: Reasoning & Analysis Patterns
creativity-patterns.md     # Group 4: Creativity & Exploration Patterns
CONTRIBUTING.md            # You are here
```

---

## 🧱 How to Add a New Pattern

1. **Identify the correct group file**  
   Decide whether your pattern belongs to:
   - **Interaction Patterns** 💬
   - **Structuring Patterns** 🏗️
   - **Reasoning & Analysis Patterns** 🧠
   - **Creativity & Exploration Patterns** 🎨

2. **Follow the existing format**  
   Add your pattern as a new section:
   ```markdown
   ## Pattern Name + Emoji
   **Description:** [One or two sentences explaining the pattern.]

   **Purpose:** [What this pattern helps achieve.]

   **Problem it Solves:** [Why you would use it.]

   **Data Needed & Why:** [Required inputs and why they matter.]

   **Quick Copy-Paste Prompt:**
   ```
   [ready-to-use prompt]
   ```

   **Examples:**
   - *General-purpose*  
     1. ...
     2. ...
   - *AI Agent / Custom GPT*  
     1. ...
     2. ...

   ---
   ```

3. **Add it to the master README catalog**  
   In `README.md`, add your pattern to:
   - The **Table of Contents** (link to your section in the group file)
   - The **Pattern Catalog** table in the appropriate group

4. **Keep it witty but professional**  
   Catalog entries should be concise and a touch engaging, but the main section must remain clear and practical.

---

## 🛠️ Style Guidelines

- Use **GitHub-flavored markdown** for compatibility.
- Use emojis in headers and catalog entries for visual scanning.
- Provide **two general-purpose examples** and **two AI agent / custom GPT examples**.
- Keep “Quick Copy-Paste Prompt” concise but functional.

---

## 📥 Submitting Changes

1. Fork the repository.
2. Make your changes in a new branch:
   ```
   git checkout -b add-new-pattern
   ```
3. Commit with a descriptive message:
   ```
   git commit -m "Add [Pattern Name] to [Group]"
   ```
4. Push and open a pull request.

---

## 🔍 Review Process

- We review for **accuracy**, **clarity**, and **consistency**.
- We may suggest edits to examples or prompts for better clarity.
- Approved changes will be merged into the main branch.

---

**Let’s keep building smarter prompts, one pattern at a time!** 🚀
