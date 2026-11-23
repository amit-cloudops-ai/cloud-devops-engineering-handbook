# Linux Foundations — Interview Questions and Troubleshooting Scenarios

> **Scope:** Questions are limited to the Linux topics covered in the current foundations lessons and the user's earlier Foundation notes. Disk/memory deep dives, Linux networking, SSH and full Bash scripting are intentionally excluded until those topics are taught.

## How to practise

For each question:

1. Answer aloud without notes.
2. Define the term in one sentence.
3. Explain how it works.
4. Give a command or example.
5. Connect it to a DevOps task.
6. State one limitation or safety concern.

Score each answer:

| Score | Standard |
|---|---|
| 0 — Unknown | Cannot explain it |
| 1 — Incomplete | Recognises the term but misses key details |
| 2 — Correct | Accurate explanation and a valid example |
| 3 — Strong | Accurate, practical, explains trade-offs and handles a follow-up |

Review scores 0–1 the same day. Re-test weak questions after 24–72 hours.

---

## A. Linux and operating-system foundations

1. What is an operating system, and what problem does it solve?
2. What is Linux? Distinguish the Linux kernel from a Linux distribution.
3. What is a kernel, and what are its main responsibilities?
4. Explain user space and kernel space.
5. What is a system call? Why do applications use system calls?
6. Distinguish a terminal, shell and kernel.
7. What is Bash?
8. What does open source mean? Does open source automatically mean secure?
9. What is a Linux distribution? Name examples and explain what a distribution provides.
10. Explain the high-level Linux boot sequence. What are firmware, GRUB, kernel, initramfs and PID 1?
11. What is WSL, and how is it different from a conventional cloud VM?
12. Explain the client/server model and the role of DNS at a high level.

## B. Filesystem and basic commands

13. What is the Linux root directory? How is it different from the root user's home directory?
14. Explain the purpose of `/home`, `/root`, `/etc`, `/var`, `/var/log`, `/tmp`, `/usr`, `/dev`, `/proc` and `/sys`.
15. What is the difference between an absolute path and a relative path?
16. What do `.`, `..` and `~` mean?
17. Explain `pwd`, `ls -l`, `ls -a` and `ls -lah`.
18. What is the difference between `mkdir` and `mkdir -p`?
19. What does `touch` do? Does it always create a new file?
20. Explain the syntax of `cp SOURCE DESTINATION`. How do you copy a file into a directory under a new name?
21. Explain how `mv` can move a file and rename a file.
22. What is the difference between `rm` and `rmdir`? Why is `rm -rf` dangerous?
23. What does `cat` do? Why is it not a command for listing directory contents?

## C. Reading, searching and text processing

24. When would you use `less` instead of `cat`?
25. What is the difference between `head` and `tail`?
26. What does `tail -f` do, and how do you stop it?
27. Explain `grep` and the options `-i`, `-n`, `-v`, `-c` and `-r`.
28. Explain the difference between `grep` and `find`.
29. What does the pipe operator do? Explain `grep "ERROR" app.log | wc -l`.
30. Why is `sort file | uniq -c` useful? Why might `uniq` alone miss non-adjacent duplicates?
31. What does `cut -d',' -f1` do when used on a simple comma-delimited file?

## D. Users, groups and permissions

32. What is a Linux user? What are UID and GID?
33. What is the root account? Why should administrators avoid using root for every task?
34. What is a group, and why is group-based access useful?
35. What information is stored in `/etc/passwd`? Does it contain password hashes in the normal modern setup?
36. Explain the fields in a typical `/etc/passwd` entry.
37. What is the difference between a primary group and supplementary groups?
38. What does `sudo` do? Explain least privilege.
39. Decode `-rwxr-xr--`. What are the owner, group and others permissions?
40. Explain read, write and execute permissions for a regular file.
41. How does execute/search permission on a directory differ from execute permission on a file?
42. Convert 755 and 644 into symbolic permissions.
43. What does `chmod u+x app.sh` do?
44. What does `chown user:group file` do? What does `-R` mean?
45. Why is `chmod -R 777` a poor default troubleshooting fix?

## E. Processes, jobs and signals

46. What is the difference between a program and a process?
47. What are PID and PPID?
48. Compare `ps`, `ps aux`, `ps -ef` and `top`.
49. Explain process states R, S, D, T and Z.
50. What is a zombie process? Is it actively consuming CPU?
51. What does appending `&` to a command do?
52. What do `jobs`, `fg` and `bg` do?
53. What is a signal?
54. Compare SIGTERM and SIGKILL. Why should SIGTERM normally be tried first?
55. What is the difference between a shell job and an operating-system process?

## F. Services and systemd

56. What is a Linux service? Give examples.
57. What is systemd, and what is its relationship to PID 1 on many modern distributions?
58. What is a systemd unit? What is a `.service` unit?
59. Explain the difference between `start`, `stop`, `restart`, `reload`, `enable` and `disable`.
60. Does `systemctl enable nginx` necessarily start Nginx immediately?
61. What is `journalctl`? How do you filter logs for one service?
62. How would you investigate a service that fails during startup?
63. Why must you check whether systemd is running before relying on systemctl in WSL?

## G. Package management

64. What is a software package? What information can package metadata contain?
65. What is a package manager?
66. What is a repository?
67. What is a dependency? Distinguish direct and transitive dependencies.
68. Why do applications depend on shared libraries and runtimes?
69. What happens at a high level when you run `sudo apt install nginx`?
70. Explain APT vs dpkg.
71. What is the difference between `apt update` and `apt upgrade`?
72. Compare `apt upgrade` and `apt full-upgrade`.
73. Compare `apt remove` and `apt purge`.
74. What does `apt autoremove` do?
75. How would you inspect a package's version, repository source and dependencies?
76. What can cause unmet dependency errors? Which diagnostic commands would you run?

---

## H. Scenario-based troubleshooting

For each scenario, explain the order of investigation. Do not jump straight to a destructive fix.

### Scenario 1 — Application log has errors

A service owner says requests are failing. The application writes to `app.log`, which contains thousands of lines. How do you inspect recent entries and isolate errors?

**Evidence to seek:** Recent log window, matching error lines, line numbers, repeated patterns and surrounding context.

### Scenario 2 — A file cannot be read

An application reports permission denied while opening `/opt/app/config.yaml`. How do you determine whether the problem is the running user, file owner, group or directory traversal permissions?

**Evidence to seek:** Service identity, `id`, `ls -l`, parent directory permissions and the minimum required access.

### Scenario 3 — A deployment script will not execute

A script exists but the shell reports permission denied when you try to execute it. What do you inspect and how might `chmod` help?

**Evidence to seek:** File type, owner, mode, interpreter/shebang and execution context. Do not blindly grant 777.

### Scenario 4 — A process appears stuck

A Python application is unresponsive. How do you identify its PID, inspect its command and decide whether to send SIGTERM or SIGKILL?

**Evidence to seek:** `ps`, `top`, process owner, PID, logs and whether graceful termination is possible.

### Scenario 5 — High CPU on a server

An EC2 instance is reporting high CPU. Which process commands do you use first? What information do you gather before terminating anything?

**Evidence to seek:** Process identity, CPU use over time, command, service criticality and application logs.

### Scenario 6 — Zombie process observed

A process listing shows a process in state Z. Explain what it means, what it does not mean, and why inspecting the parent process is relevant.

**Evidence to seek:** PID, PPID and parent behaviour. Do not assume killing the zombie PID will solve it.

### Scenario 7 — Nginx is inactive

A website is unavailable and `systemctl status nginx` reports a failed service. Describe your investigation.

**Evidence to seek:** Status output, exit code, journal entries, configuration errors, port conflicts and dependencies.

### Scenario 8 — Service starts manually but not after reboot

A service works after `systemctl start` but does not start after reboot. What is the conceptual difference between start and enable, and what would you inspect?

**Evidence to seek:** Enablement state, unit configuration and boot-time dependency/error messages.

### Scenario 9 — Configuration reload vs restart

A configuration file changed. When might reload be preferable to restart, and what must be true for reload to work?

**Evidence to seek:** Whether the service supports reload, configuration validation and whether a restart is actually required.

### Scenario 10 — Package installation reports unmet dependencies

An Ubuntu package fails to install because dependencies cannot be satisfied. What do you inspect before running repair commands?

**Evidence to seek:** Package candidate, configured sources, dependency metadata, version constraints and complete APT error.

### Scenario 11 — A package is installed but the command is not found

What could explain the difference between a package being installed and a command being available in the current shell?

**Evidence to seek:** Package file list, executable path, PATH, package contents and whether the package provides a service rather than a command with the expected name.

### Scenario 12 — Disk is filling with logs (foundations-level)

You suspect a log file is growing quickly. Which commands already covered can help inspect its latest content and identify error repetition? Which deeper disk-capacity commands remain to be learned?

**Evidence to seek:** `tail`, `grep`, `wc`, log patterns. State clearly that `df`/`du` and log rotation are future topics in this curriculum.

### Scenario 13 — Wrong file copied during deployment

A backup operation appears to have overwritten or misplaced a configuration file. Explain how you would reason about `cp SOURCE DESTINATION` and inspect paths before retrying.

**Evidence to seek:** `pwd`, `ls -lah`, absolute paths and source/destination order.

### Scenario 14 — A group member cannot access a shared directory

A developer has been added to a group but still cannot write to a shared directory. What do you inspect?

**Evidence to seek:** Group membership, whether the user session has picked up the new supplementary group, directory owner/group, directory write and execute bits. Do not solve it with 777.

### Scenario 15 — WSL service commands fail

A learner tries `systemctl status nginx` in WSL and gets an error. What should they check before changing configuration?

**Evidence to seek:** PID 1 via `ps -p 1 -o comm=`, whether systemd is enabled in the distro, and whether the expected service manager is available.

---

## Daily revision

Use [Linux Daily Command Practice](../00-foundations/LINUX-DAILY-COMMAND-PRACTICE.md) for the 15–20 minute command routine.

Use [SDLC interview practice](sdlc-interview-questions.md) for the lifecycle topic. Do not mix unstudied Linux topics into this question set until the relevant lessons are complete.

## Interview readiness gate

A topic is not interview-ready until you can:

- [ ] Explain it without reading notes.
- [ ] Give a technically correct example.
- [ ] Run the relevant command in a safe lab.
- [ ] Interpret normal and failure output.
- [ ] Diagnose a realistic scenario.
- [ ] Handle a follow-up question and explain trade-offs.
