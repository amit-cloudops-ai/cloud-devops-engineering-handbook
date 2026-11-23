# Linux Daily Command Practice — Foundations Check-in

> This is a repeatable 15–20 minute routine for the Linux commands already introduced in the foundations lessons. It is a practice plan, not evidence that the commands have been independently mastered.

## Rules

1. Use your Ubuntu WSL environment or a disposable Linux VM.
2. Work under `~/devops-lab`; do not experiment in `/etc`, `/var`, or another system directory.
3. Before a command that changes or deletes anything, say what it will change.
4. Run the command, inspect the result, and explain it aloud.
5. Never practise destructive commands on important files or production systems.
6. Keep a small record: date, commands run, output understood, error encountered, next review.

## Daily 15–20 minute loop

### Minutes 0–3: Identity and orientation

```bash
whoami
id
groups
pwd
uname -a
cat /etc/os-release
```

Explain the difference between username, UID, GID, kernel and distribution.

### Minutes 3–6: Navigate and manipulate a disposable lab

```bash
mkdir -p ~/devops-lab/daily/logs
cd ~/devops-lab/daily
pwd
touch app.log config.yaml
mkdir backups
cp config.yaml backups/config-backup.yaml
ls -lah
```

Explain source vs destination and why `cp` preserves the original.

### Minutes 6–10: Read and search

```bash
cat app.log
head -n 5 app.log
tail -n 5 app.log
grep -n "ERROR" app.log
grep -c "ERROR" app.log
find . -name "*.log"
wc -l app.log
```

For a useful repeatable test file, create one inside the lab:

```bash
cat > app.log <<'EOF'
INFO Server started
INFO Database connected
WARNING High memory usage
ERROR Database connection failed
INFO Retrying connection
ERROR Connection timeout
EOF
```

Explain the difference between `grep` and `find`, and what the pipe operator does.

### Minutes 10–13: Permissions and process basics

```bash
touch app.sh
chmod 755 app.sh
chmod 644 config.yaml
ls -l
stat app.sh
sleep 60 &
jobs
pgrep -a sleep
ps aux | grep sleep
```

Stop only the test process you just started:

```bash
pkill -TERM -x sleep
```

If you have other intentional `sleep` test processes running, inspect PIDs first and target the correct one instead of using a broad process-name kill.

### Minutes 13–16: Services and package inspection

These are inspection commands; systemd may not be active in every WSL setup.

```bash
ps -p 1 -o comm=
systemctl --version
systemctl list-units --type=service --state=running
apt search nginx
apt show nginx
apt-cache depends nginx
apt-cache policy nginx
```

Do not install, upgrade, purge or autoremove packages as a daily drill. Do those only in a planned lab after reviewing the proposed changes.

### Minutes 16–20: Explain one scenario

Pick one and explain the commands you would run, what each output tells you, and what you would do next:

- A log contains many errors.
- A file cannot be read by an application user.
- A process is consuming high CPU.
- A systemd service will not start.
- A package installation reports unmet dependencies.

## Weekly rotation

| Day | Emphasis | Small challenge |
|---|---|---|
| Monday | Navigation and filesystem | Find a file and explain its absolute and relative paths |
| Tuesday | File operations | Copy, rename and move files inside the lab |
| Wednesday | Text and logs | Extract errors and count them |
| Thursday | Users and permissions | Decode `ls -l` and explain 644 vs 755 |
| Friday | Processes and jobs | Start, inspect and gracefully stop a test process |
| Saturday | Services and packages | Inspect a service and package metadata |
| Sunday | Mixed troubleshooting | Complete one scenario without notes |

## Command recall checklist

- [ ] I can explain `whoami`, `id`, `pwd`, `uname` and `cat /etc/os-release`.
- [ ] I can navigate with `ls`, `cd`, `cd ..`, `cd ~`.
- [ ] I can explain `mkdir`, `touch`, `cp`, `mv`, `rm` and `rmdir`.
- [ ] I can inspect text with `cat`, `less`, `head` and `tail`.
- [ ] I can search with `grep` and `find`.
- [ ] I can explain pipes and use `wc`, `sort`, `uniq` and `cut`.
- [ ] I can inspect users and groups with `id`, `groups`, `/etc/passwd` and `/etc/group`.
- [ ] I can explain and modify basic permissions with `chmod`.
- [ ] I can explain ownership and use `chown` in a safe lab.
- [ ] I can inspect processes with `ps`, `top` and `pgrep`.
- [ ] I understand background jobs and SIGTERM vs SIGKILL.
- [ ] I can inspect services with `systemctl` and `journalctl` where systemd is available.
- [ ] I can explain packages, dependencies, repositories, APT and dpkg.
- [ ] I know `apt update` refreshes indexes; `apt upgrade` upgrades packages.

## Learning log template

Copy this block for each session:

```text
Date:
Environment (Ubuntu WSL / VM / cloud lab):
Commands practised:
What I could explain without notes:
What output surprised me:
Error / troubleshooting performed:
One interview question answered aloud:
Weak point to revisit in 24–72 hours:
```

## Spaced review method

- **Same day:** Re-run the commands and explain them aloud.
- **After 24 hours:** Recall the command from the task, not from the command list.
- **After 72 hours:** Solve a small scenario using several commands together.
- **After one week:** Complete a mixed drill without notes and record mistakes.

A command should be marked as reliable only after repeated correct use and explanation. Do not mark the entire Linux skill as interview-ready based on command recall alone.
