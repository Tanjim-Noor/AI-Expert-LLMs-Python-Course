## ✅ Complete Naming Convention Summary

This convention uses numbering prefixes (`XX`) to ensure correct sorting and includes a descriptor letter (`M`, `L`, `A`) for quick identification of the content level.

| Level | Convention | Example Name | Purpose |
| :--- | :--- | :--- | :--- |
| **Repository (Root)** | Title Case, Hyphenated | `AI-Expert-LLMs-Python-Course` | The main container for all course content. |
| **Module Folder** | `M_XX_ModuleName` | `M_01_Introduction_to_AI` | Organizes content by major topic/module. |
| **Lesson Folder** | `L_XX_LessonTitle` | `L_01_Hello_AI_Dev_Setup` | Contains all files/activities for a single lesson. |
| **Activity/Notebook** | `A_XX_ActivityName.ipynb` (or `.py`) | `A_01_Hello_AI_Chatbot.ipynb`, `A_01_TIC_TAC_TOE.py` | The specific code file(s) for a lesson activity. |
| **Documentation** | `README.md` | (Located in Root, Module, and Lesson folders) | Provides context, instructions, and links for its directory. |

---

### 🌳 Example File Path

Here are file path examples using this convention:

- `AI-Expert-LLMs-Python-Course/M_01_Introduction_to_AI/L_01_Hello_AI_Dev_Setup/A_01_Hello_AI_Chatbot.ipynb`
- `AI-Expert-LLMs-Python-Course/M_01_Introduction_to_AI/L_04_AI_in_Games_Building_a_Simple_AI_Opponent/A_01_TIC_TAC_TOE.py`  

Example specifics:

- Activity 01 - "Tic Tac Toe"
- Lesson 04 - "AI in Games: Building a Simple AI Opponent"

This activity uses the file `A_01_TIC_TAC_TOE.py` in `L_04_AI_in_Games_Building_a_Simple_AI_Opponent` under `M_01_Introduction_to_AI`.

---

## 💬 Commit Message Structure

Use this structure for clear and traceable history. It follows the **Conventional Commits** style.

### General Structure

$$\text{Type}(\text{Scope}): \text{Subject}$$

| Component | Convention | Example Value | Description |
| :--- | :--- | :--- | :--- |
| **Type** | Lowercase verb describing the change | `feat`, `fix`, `refactor`, `docs`, `chore` | Indicates the purpose of the commit. |
| **Scope** | Specify the module/lesson location | `M_XX` or `M_XX_L_XX` | Pinpoints the area of the codebase being changed. |
| **Subject** | Imperative, short description | `Complete A_01_Hello_AI_Chatbot solution` | Summarizes the change in under 50 characters. |

### Commit Message Examples

| Action | Example Commit Message |
| :--- | :--- |
| **Completing an activity** | `feat(M_01_L_01): Complete A_01_Hello_AI_Chatbot solution` |
| **Fixing a bug in a lesson's code** | `fix(M_02_L_03): Resolve import error in starter code` |
| **Adding a new lesson structure** | `feat(M_02): Add L_02_Basics_of_Image_Manipulation structure` |
| **Updating the module README** | `docs(M_01): Update module overview with links to L_03` |

### Activity commit pattern (example)

When finishing an activity, use the commit message line followed by a short body listing the specific Activity and Lesson details — this helps reviewers and keeps history consistent.

Example (exact format):

```
feat(M_01_L_04): Complete A_01_TIC_TAC_TOE solution

- Activity 01 - "Tic Tac Toe"
- Lesson 04 - "AI in Games: Building a Simple AI Opponent"
```