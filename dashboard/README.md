# Preparation Dashboard

The dashboard is a static HTML page with no build step, framework or external runtime dependency. It reads `progress.json`, tracks 30 competencies and four portfolio project checklists, and saves edits in the current browser's local storage.

## Run locally

1. Clone the repository.
2. Open a terminal in the repository root.
3. Run:

```bash
python -m http.server 8000
```

4. Open [http://localhost:8000/dashboard/](http://localhost:8000/dashboard/).

Do not open `index.html` directly as a `file://` URL; browsers block the relative JSON fetch in that mode.

## Publish with GitHub Pages (optional)

The dashboard is static and can be served from the repository root:
1. Open repository **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select branch `main` and folder `/ (root)`, then save.
4. After GitHub Pages publishes the site, open `/dashboard/` under the Pages site URL.

Pages has not been enabled or deployed as part of this repository update.

## Progress persistence

- Skill and project edits are saved to local storage in the browser.
- Use **Export progress** to download a JSON snapshot.
- Review and merge the exported values into `progress.json`, then commit the updated file to sync progress across devices.
- **Reset local edits** returns to the repository baseline and clears this browser's local changes.

The dashboard does not send progress to a server and does not provision cloud resources.
