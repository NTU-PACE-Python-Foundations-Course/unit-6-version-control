# Making your repo private + adding the grading bot

1. Click **"Use this template" → "Create a new repository."** On that same
   page, before you click the final **Create repository** button, choose
   **Private** in the visibility selector. This way your repo is never
   public, even briefly.

   (If you already created it without doing this, go to your repo's
   **Settings → General → Danger Zone → Change visibility** and set it to
   Private now.)

2. Go to **Settings → Collaborators and teams → Add people.**

3. Search for and add: **`blueconnectorbot`**

4. Personal GitHub repos don't offer a read-only collaborator role, so this
   adds the bot as a regular (write-access) collaborator — there's no Read
   option to pick. In practice this is fine: the bot is only ever used to
   run your tests and certify your results, it never modifies your code,
   and it has no access to anything else in your account beyond this one
   repo, which only ever holds this unit's learning exercises.

5. That's it on your end. You'll get a confirmation once the invitation is
   accepted (usually within a day) — you don't need to do anything else.

6. Submit your repo URL through the Learning Management System so the
   instructor knows which repo belongs to you.
