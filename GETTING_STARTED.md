# Getting Started — Python Fundamentals

> **Python Fundamentals**

This guide walks you through everything you need to do the exercises for this
course — **even if you've never used GitHub, VS Code, or Jupyter notebooks
before.** You don't need to install anything on your own computer. Everything
runs in your web browser using **GitHub Codespaces**.

Read this once before you start Unit 1, and come back to it whenever something
doesn't look right.

---

## 1. What you need

- A free [GitHub](https://github.com) account.
- A modern web browser (Chrome, Edge, or Firefox).
- That's it. No Python install, no software to download.

---

## 2. Opening a unit in Codespaces

Each unit of the course (Unit 1, Unit 2, ...) lives in its own GitHub
repository. To start working on a unit:

1. Open the unit's repository page on GitHub (your trainer will give you the
   link, e.g. `github.com/python-fundamentals-course/unit-1-foundations`).
2. Click the green **`<> Code`** button.
3. Select the **Codespaces** tab.
4. Click **Create codespace on main**.

GitHub will now build your personal coding environment in the cloud. **The
first time you do this for a unit, it can take 1–3 minutes** — you'll see a
progress screen with logs scrolling past. This is normal. It's installing
Python, Jupyter, and all the packages you need (pandas, pytest, etc.).

When it's done, you'll see what looks like a full code editor (this is
**Visual Studio Code**, running in your browser) with a file list on the left.

> **Tip:** Once a Codespace exists, you can come back to it later from the
> same **Codespaces** tab — you don't need to create a new one each session.
> Your files and any saved (committed) work will still be there.

---

## 3. The files in your repo

Each unit repo contains:

| File | What it's for |
|---|---|
| `notebook.ipynb` | The **lesson** — read through this first. It explains the concepts for this unit. |
| `exercises.ipynb` | **Your work goes here.** Practice exercises with `# TODO` markers for you to fill in. |
| `tests/` | Automated checks ("autograder") that test your `exercises.ipynb` answers. You don't need to edit anything in here. |
| `.devcontainer/` | Configuration for your Codespace. You don't need to touch this. |

You'll spend almost all your time in `exercises.ipynb`, after reading
`notebook.ipynb`.

---

## 4. Working with Jupyter notebooks

A notebook (`.ipynb` file) is made of **cells**. There are two kinds:

- **Markdown cells** — formatted text, like the one you're reading now.
  Instructions and explanations live here.
- **Code cells** — actual Python code you can run.

### Opening a notebook

In the file list on the left, click `notebook.ipynb` (or `exercises.ipynb`).
It opens in the main editor area.

### Selecting a kernel (first time only)

The first time you open a notebook, VS Code may show a **"Select Kernel"**
button or prompt in the top-right corner. Click it, then choose:

- **Python Environments** → the one that says something like
  **`Python 3.11.x`** (it's usually the only one available, often labelled
  `/usr/local/bin/python`).

You only need to do this once per Codespace — it will be remembered for every
notebook you open afterwards.

### Running a cell

Click on a code cell, then press **Shift + Enter** (or click the ▶ play
button to its left). This runs the code and shows the output directly below
the cell.

**Run cells from top to bottom, in order.** Later cells often depend on
variables created in earlier cells. If you run cells out of order, you may
get confusing errors — see [Troubleshooting](#7-troubleshooting) below.

### Re-running everything

If things look weird (e.g. a variable seems to have the wrong value, or you
get an error that doesn't make sense), use:

- **Run → Run All Cells** (or the "Restart Kernel and Run All Cells" button at
  the top of the notebook)

This restarts Python from scratch and re-runs every cell in order — a
reliable way to get back to a clean state.

---

## 5. Doing the exercises

1. Read through `notebook.ipynb` first — it covers the concepts you'll need.
2. Open `exercises.ipynb`.
3. Read each markdown cell describing the exercise.
4. In the code cell below it, find the `# TODO:` comments. Write your code
   where indicated, replacing or adding to the `# TODO` lines.
5. Run the cell (**Shift + Enter**) and check the output against what the
   exercise asks for.
6. Move on to the next exercise.

You don't need to delete the `# TODO` comments — they're just there to guide
you. Focus on getting the correct result.

> **Note:** `solutions.ipynb` is **not** included in your repo. This is
> deliberate — it keeps you working things out for yourself. Your trainer can
> walk through solutions in class, and the automated checks (next section)
> tell you whether your answer is correct.

---

## 6. Checking your work (the autograder)

Every unit comes with a set of automated tests that check your
`exercises.ipynb` answers. Running them gives you instant feedback — no need
to wait for your trainer to mark anything.

### Opening a terminal

In VS Code, open a terminal with:

- **Terminal → New Terminal** (from the menu bar), or
- The keyboard shortcut **Ctrl + `** (backtick) — on Mac, **Cmd + `**

A command-line panel opens at the bottom of the screen.

### Running the tests

Type the following and press Enter:

```bash
pytest tests/ -v
```

This runs your `exercises.ipynb` from top to bottom and checks each exercise.
You'll see output like:

```
tests/test_exercises.py::test_exercise_1_variables_and_types PASSED   [ 25%]
tests/test_exercises.py::test_exercise_2_gst_arithmetic PASSED        [ 50%]
tests/test_exercises.py::test_exercise_3_string_manipulation FAILED   [ 75%]
tests/test_exercises.py::test_exercise_4_profile_message FAILED       [100%]
```

- **PASSED** (green) — that exercise is correct. 
- **FAILED** (red) — that exercise still needs work. Scroll up in the output
  for details on what was expected vs. what your code produced.

It's completely normal to see failures while you're still working — that's
the point! Keep editing `exercises.ipynb`, save the file (**Ctrl/Cmd + S**),
and run `pytest tests/ -v` again to re-check.

> A brand-new, unstarted `exercises.ipynb` will show **all tests failing** —
> that's expected, not a bug. As you fill in each `# TODO`, more tests should
> turn green.

---

## 7. Saving your work

Your Codespace keeps your files even if you close the browser tab — but to
make sure your work is permanently saved (and visible to your trainer), you
need to **commit and push** it to GitHub. Do this at the end of every session.

1. Click the **Source Control** icon in the left sidebar (it looks like a
   branching line, and usually shows a number badge for changed files).
2. You'll see a list of changed files (e.g. `exercises.ipynb`).
3. Type a short message describing what you did, e.g. `Completed unit 1
   exercises`, in the **Message** box at the top.
4. Click the **Commit** button (it may say "Commit & Sync" or just "✓").
5. If prompted, click **Sync Changes** (or **Push**) to upload your work to
   GitHub.

> The first time you do this, GitHub may ask you to confirm your identity in
> the browser — follow the on-screen prompts (this is a one-time setup).

Unit 6 covers Git in more depth, including doing this from the command line
with `git add`, `git commit`, and `git push` — but using the Source Control
panel as above is perfectly fine for every unit.

---

## 8. Managing your Codespace

- **Pausing:** You can simply close the browser tab. Your Codespace keeps
  running for a while in the background, then automatically stops itself
  after a period of inactivity. Nothing is lost — just reopen it from the
  **Codespaces** tab on the repo page next time.
- **Stopping manually:** GitHub's free usage allowance is generous, but it's
  good practice to stop a Codespace when you're done for the day. Go to
  [github.com/codespaces](https://github.com/codespaces), find your
  Codespace, click the **`...`** menu, and choose **Stop codespace**.
- **One Codespace per unit:** Each unit repo gets its own Codespace. If you've
  finished Unit 1 and are moving to Unit 2, open a Codespace on the Unit 2
  repo — you don't need to delete the Unit 1 one (though you can, from
  [github.com/codespaces](https://github.com/codespaces), once you're sure
  you've pushed your work).

---

## 9. Troubleshooting

**A "Select Kernel" popup keeps appearing, or my code won't run.**
Click **Select Kernel** → **Python Environments** → the `Python 3.11.x`
option. See [Selecting a kernel](#selecting-a-kernel-first-time-only) above.

**I get `NameError: name '...' is not defined`.**
You probably ran a code cell before running an earlier one that defines that
variable. Use **Run All Cells** to run the whole notebook in order from the
top.

**I get `ModuleNotFoundError: No module named 'pandas'` (or similar).**
The Codespace may still be installing packages. Wait a minute and try again,
or run this in the terminal:
```bash
pip install -r .devcontainer/requirements.txt
```

**My Codespace seems frozen, or the page won't load.**
Refresh the browser tab. If that doesn't help, close the tab, go back to the
repo's **Codespaces** tab on GitHub, and reopen your Codespace.

**I accidentally deleted some code or broke a cell.**
Press **Ctrl/Cmd + Z** to undo. If that doesn't work and you haven't committed
yet, you can also discard changes via the **Source Control** panel — but be
careful, this throws away unsaved work.

**`pytest tests/ -v` says "command not found".**
Make sure you're typing the command into the **terminal** at the bottom of
the screen, not into a notebook cell.

**I closed my Codespace without pushing — did I lose my work?**
Probably not. Reopen the Codespace from the **Codespaces** tab on the repo
page — your files are still there. Push your work (Section 7) as soon as you
can.

---

## 10. Getting help

If something isn't covered here, or still doesn't work after trying the steps
above:

- Take a screenshot of the error/output.
- Ask your trainer, including which unit and exercise you're on.

Good luck, and enjoy the course!
