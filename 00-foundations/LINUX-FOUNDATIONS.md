# Linux Foundations for DevOps — Beginner-to-Operational Notes

> **Scope and status:** This chapter documents the Linux concepts taught so far: operating-system and Linux architecture, filesystem navigation and file operations, reading/searching text, users/groups/permissions, processes/jobs/signals, systemd services, and Ubuntu APT package management. The concepts have been explained; practical command execution and independent troubleshooting still need to be verified. Do not interpret this chapter as proof of Linux mastery.

## How to use this chapter

Learn each topic in this order:

1. Understand the idea in plain language.
2. Learn the technical vocabulary.
3. Read the diagram.
4. Run the safe commands in your own Ubuntu/WSL lab.
5. Explain what happened without reading.
6. Solve a troubleshooting scenario.

A command is not mastered because you have seen it. You should be able to predict its effect, run it safely, inspect the result, and explain what the output means.

---

## 1. The operating-system idea

### Explain it like you're five

Imagine a computer is a kitchen. The hardware is the stove, fridge, knives and ingredients. Applications are the people asking the kitchen to cook something. The operating system is the kitchen manager: it decides who can use which equipment, shares resources, and coordinates the work.

A computer's **operating system (OS)** manages hardware and provides common services so applications can run.

Examples of OS families include Linux, Windows, macOS and BSD.

### Technical vocabulary

- **Hardware:** Physical components such as CPU, RAM, disk, network card and keyboard.
- **Operating system:** The software layer that manages hardware and provides services to programs.
- **Application:** A program that performs a user or business task, such as Nginx, PostgreSQL or Python.
- **Process:** A running instance of a program.
- **Resource:** Something programs need, such as CPU time, memory, storage or network access.
- **System call:** A controlled request by a program to the kernel for an operating-system service.
- **User space:** The area where ordinary applications and utilities run with restricted privileges.
- **Kernel space:** The privileged execution area where the kernel manages core system functions.

### Simplified communication path

```text
Human / operator
      |
      v
Application or command-line tool
      |
      | system calls when OS services are needed
      v
Operating-system kernel
      |
      v
CPU / RAM / storage / network devices
```

The application does not normally control hardware directly. It asks the OS to perform work on its behalf.

### Client and server context from the older Foundation notes

Your uploaded notes also recap the client/server model:

- **Client:** A device or program that requests a service. A browser is a client.
- **Server:** A computer or program that provides a service. A web server or database server is an example.
- **Data centre:** A facility containing computing, storage, power, cooling and network infrastructure.
- **ISP (Internet Service Provider):** An organisation that provides internet connectivity.
- **DNS (Domain Name System):** A distributed naming system that helps translate domain names into records such as IP addresses.

A simple request path:

```text
Phone / browser (client)
        |
        | asks for https://example.com
        v
DNS lookup -> obtains an address
        |
        v
Internet / ISP networks / routers
        |
        v
Server infrastructure / data centre
        |
        v
Web server / application / database
        |
        v
Response returns to the client
```

**Accuracy note:** This is a teaching-level path, not a complete packet-level explanation. DNS can be cached, traffic may pass through CDNs, proxies and load balancers, and web servers can reverse-proxy requests to application servers. A web server is not limited to static files; its role depends on configuration and architecture.

---

## 2. What is Linux?

### Plain-language explanation

Linux is the name of an open-source kernel. In everyday conversation, people often say "Linux" to mean a complete operating-system distribution built around that kernel.

A **Linux distribution (distro)** combines the Linux kernel with system utilities, libraries, a package manager, defaults and other software. Examples include Ubuntu, Debian, Fedora, Red Hat Enterprise Linux (RHEL), and Alpine Linux.

### Technical vocabulary

- **Kernel:** The core of the operating system. It manages processes, memory, devices, filesystems and networking.
- **Distribution (distro):** A complete operating-system package built around the Linux kernel.
- **Open source:** Source code is available under a licence that grants defined rights to use, inspect, modify and redistribute it.
- **Unix-like:** An operating system designed around concepts and interfaces associated with Unix. Linux is Unix-like; it is not simply accurate to say "Linux is free Unix and Unix is paid."
- **Multiuser:** The system can distinguish users and apply access controls.
- **Multitasking:** The system can schedule multiple processes so they make progress.
- **Headless server:** A server operated without a local graphical desktop, commonly managed through SSH and command-line tools.

### Why DevOps engineers use Linux

Linux is common in servers, cloud images, containers and infrastructure tooling because it offers automation-friendly interfaces, mature networking and process tools, flexible packaging, broad ecosystem support and strong operational controls.

**Security correction from the old notes:** Linux is not automatically secure and does not make antivirus or security tooling universally unnecessary. Security depends on patching, configuration, identity controls, least privilege, network exposure, monitoring and the workload's threat model.

---

## 3. Linux architecture

### Explain it like you're five

The kernel is the building manager. Applications are tenants. The hardware is the building's equipment. The shell is one way a person can ask the building manager to do something.

### Main layers

```text
+-----------------------------------------------+
| Applications                                  |
| Nginx | Python | Docker CLI | PostgreSQL      |
+-----------------------------------------------+
| Shells and system utilities                   |
| Bash | ls | grep | systemctl | apt             |
+-----------------------------------------------+
| Libraries and system-call interface           |
+-----------------------------------------------+
| Linux kernel                                  |
| processes | memory | devices | filesystems    |
| networking | scheduling | security            |
+-----------------------------------------------+
| Hardware                                      |
| CPU | RAM | SSD | NIC | other devices         |
+-----------------------------------------------+
```

This is a conceptual diagram, not a strict physical stack. Applications can use libraries, runtimes and system calls in different ways.

### Kernel responsibilities

1. **Process management:** Creates, schedules and tracks processes.
2. **Memory management:** Allocates and protects memory, manages virtual memory.
3. **Device management:** Coordinates access to hardware through drivers.
4. **Filesystem management:** Provides interfaces for files, directories and mounted filesystems.
5. **Networking:** Implements core networking functionality and interfaces.
6. **Security and isolation:** Enforces privilege boundaries and access-control mechanisms.
7. **System calls:** Exposes controlled services to user-space programs.

### Shell vs terminal vs kernel

These are different things:

- **Terminal:** The interface/window that displays text input and output.
- **Shell:** The command interpreter, such as Bash, that reads commands, expands variables and launches programs.
- **Kernel:** The privileged OS core that manages resources and provides system services.
- **Command:** An instruction or program invoked from the shell.

Example:

```text
You type: ls -lah
       |
       v
Terminal sends the text to Bash
       |
       v
Bash interprets the command and launches ls
       |
       v
ls requests filesystem information through OS interfaces
       |
       v
Kernel mediates access and returns results
       |
       v
Terminal displays the output
```

### Boot sequence — conceptual overview

Your older notes mention GRUB. The accurate high-level sequence is:

```text
Power on
  -> firmware (BIOS/UEFI)
  -> bootloader (for example, GRUB)
  -> Linux kernel + initramfs
  -> kernel initialises hardware and mounts the real root filesystem
  -> first userspace process (often systemd, PID 1)
  -> services and login environment
```

- **Firmware:** Initial low-level code that starts the machine and selects a boot path.
- **Bootloader:** Loads the kernel and often an initial RAM filesystem.
- **GRUB:** A commonly used Linux bootloader.
- **initramfs:** A temporary early userspace filesystem used during boot to load required drivers and locate/mount the real root filesystem.
- **PID 1:** The first userspace process in a PID namespace. On many Ubuntu systems it is systemd. It is not the bootloader.

WSL has a different boot and integration model from a conventional physical or cloud Linux server.

---

## 4. Your Linux environment: WSL and cloud servers

- **WSL (Windows Subsystem for Linux):** Runs a Linux environment integrated with Windows. WSL 2 uses a lightweight virtualised Linux kernel environment.
- **Virtual machine (VM):** A virtual computer running its own operating system on virtualised hardware.
- **Cloud VM:** A VM provisioned by a cloud provider, such as an AWS EC2 instance.
- **SSH (Secure Shell):** An encrypted protocol commonly used to access and administer remote systems. We will study SSH in the networking section later.

Commands to identify your current environment:

```bash
uname -a
cat /etc/os-release
whoami
pwd
ps -p 1 -o comm=
```

- `uname -a`: kernel and machine information.
- `cat /etc/os-release`: distribution identity and release details.
- `whoami`: current effective username.
- `pwd`: current working directory.
- `ps -p 1 -o comm=`: name of the process with PID 1.

---

## 5. Filesystem hierarchy

### Explain it like you're five

Think of the filesystem as one huge tree of folders. The top of the tree is called the root directory and is written as `/`. Every ordinary file and directory is somewhere underneath it.

Unlike Windows drive letters such as `C:\` and `D:\`, Linux presents storage through one directory tree. Separate disks and filesystems can be attached to that tree using **mount points**.

```text
/
├── home/       personal home directories
│   └── amit/
├── root/       root user's home directory
├── etc/        system and application configuration
├── var/        changing data, often logs and caches
│   └── log/    many system and application logs
├── tmp/        temporary files
├── usr/        many user-space programs and libraries
│   ├── bin/    commands and executables
│   └── lib/    libraries
├── bin/        essential command path; often merged into /usr/bin
├── sbin/       system administration commands; often merged into /usr/sbin
├── dev/        device interfaces
├── proc/       virtual process and kernel information
├── sys/        virtual kernel/device information
└── mnt/        common mount point for temporary mounts
```

### Important directories

| Path | What it is for | Simple mental picture |
|---|---|---|
| `/` | Root of the filesystem tree | The top of the tree |
| `/home` | Regular users' home directories | Personal rooms |
| `/root` | Root administrator's home | Administrator's room |
| `/etc` | System-wide configuration | Settings cupboard |
| `/var` | Variable data that changes during operation | Working records |
| `/var/log` | Many system and application logs | Activity diary |
| `/tmp` | Temporary files | Scratch paper |
| `/usr` | User-space applications, libraries and data | Shared tool shelves |
| `/dev` | Device files/interfaces | Doors to devices |
| `/proc` | Virtual view of process and kernel data | Live status board |
| `/sys` | Kernel/device information | Hardware status board |
| `/mnt` | Common mount location | Attachment point |

**Important nuance:** `/proc` and `/sys` are virtual filesystems. Their contents are exposed by the kernel; they are not ordinary collections of files stored like documents on an SSD. On modern Ubuntu, `/bin` and `/sbin` are commonly symbolic links into `/usr` (the usr-merge layout).

### Path vocabulary

- **Absolute path:** Starts from `/`, for example `/var/log/syslog`.
- **Relative path:** Starts from your current directory, for example `logs/app.log`.
- `.`: Current directory.
- `..`: Parent directory.
- `~`: Current user's home directory.
- **Mount point:** A directory where another filesystem is attached to the directory tree.

---

## 6. Navigation and basic file operations

### Command shape

A common command pattern is:

```text
command [options] [arguments]
```

Example:

```bash
ls -lah /var/log
```

- `ls` is the command.
- `-l`, `-a`, and `-h` are options.
- `/var/log` is the argument (the target directory).

### Navigation commands

| Command | Meaning |
|---|---|
| `pwd` | Print working directory |
| `ls` | List directory entries |
| `ls -l` | Long/detailed listing |
| `ls -a` | Include hidden entries (names beginning with a dot) |
| `ls -h` | Human-readable sizes when used with size-reporting output, commonly `-lh` |
| `ls -lah` | Detailed, hidden entries and human-readable sizes |
| `cd DIR` | Change directory |
| `cd ..` | Move to parent directory |
| `cd ~` | Go to your home directory |
| `cd /` | Go to filesystem root |

### File and directory operations

| Command | Meaning | Example |
|---|---|---|
| `mkdir` | Create a directory | `mkdir logs` |
| `mkdir -p` | Create parent directories as needed | `mkdir -p app/logs/archive` |
| `touch` | Create an empty file if absent; otherwise update timestamps | `touch app.log` |
| `cp` | Copy source to destination | `cp app.log app-backup.log` |
| `mv` | Move or rename source | `mv app-backup.log backups/` |
| `rm` | Remove a file | `rm app.log` |
| `rmdir` | Remove an empty directory | `rmdir empty-dir` |

### Understand cp and mv

```bash
cp SOURCE DESTINATION
mv SOURCE DESTINATION
```

- `cp config.yaml backups/` copies the file into the directory and keeps the original.
- `cp config.yaml backups/config-backup.yaml` copies it with a new destination name.
- `mv app.py backups/` moves it into the directory; it no longer remains at the original path.
- `mv old-name.txt new-name.txt` renames it in the same directory.

When copying multiple source files, the final argument must be a destination directory:

```bash
cp file-a file-b backups/
```

### Deletion safety

- `rmdir directory` only works when the directory is empty.
- `rm -r directory` recursively removes a directory and its contents.
- `rm -rf` combines recursive removal and force behaviour. It can delete large amounts of data without prompting. Never use it casually or with an unverified path.

Practise deletion only inside a disposable lab directory. Always inspect the path with `pwd` and `ls` first.

---

## 7. Reading, searching and processing text

Logs and configuration files are common sources of operational evidence. The goal is to find the useful lines without manually reading thousands of entries.

### Read a file

| Command | Meaning |
|---|---|
| `cat app.log` | Print the whole file |
| `less app.log` | Read interactively, page by page |
| `head app.log` | First 10 lines by default |
| `head -n 3 app.log` | First 3 lines |
| `tail app.log` | Last 10 lines by default |
| `tail -n 20 app.log` | Last 20 lines |
| `tail -f app.log` | Follow new lines as they are appended |

In `less`, common keys include Space (next page), `b` (previous page), `/text` (search), `n` (next match), and `q` (quit). In `tail -f`, press Ctrl+C to stop following.

### grep: search inside file contents

`grep` finds lines matching a pattern.

```bash
grep "ERROR" app.log
grep -i "error" app.log
grep -n "ERROR" app.log
grep -v "INFO" app.log
grep -c "ERROR" app.log
grep -r "database" /var/log/
```

| Option | Meaning |
|---|---|
| `-i` | Ignore case |
| `-n` | Show matching line numbers |
| `-v` | Show lines that do not match |
| `-c` | Count matching lines |
| `-r` | Search recursively in directories |

### find: search for filesystem entries

`find` searches for files and directories by name, type and other criteria.

```bash
find /home -name "app.log"
find /var/log -name "*.log"
find . -type f
find . -type d
```

**Remember:** `grep` searches text inside files; `find` searches the filesystem for entries.

### Other text utilities introduced

| Command | Purpose |
|---|---|
| `wc -l app.log` | Count lines |
| `sort app.log` | Sort lines |
| `uniq app.log` | Collapse adjacent duplicate lines |
| `sort app.log | uniq -c` | Sort first, then count repeated adjacent lines |
| `cut -d',' -f1 data.csv` | Extract the first comma-delimited field |

### Pipes

A pipe (`|`) connects the output of one command to the input of another.

```bash
ps aux | grep nginx
grep "ERROR" app.log | wc -l
```

Read the second example from left to right:

1. `grep "ERROR" app.log` prints matching error lines.
2. The pipe passes those lines onward.
3. `wc -l` counts the lines it receives.

You may see `cat app.log | grep ERROR`; it works, but `grep ERROR app.log` is simpler because grep can read the file directly.

---

## 8. Users and groups

### Explain it like you're five

A Linux server may be shared by many people and services. A **user** is an account with an identity. A **group** is a named collection of users. Groups let an administrator give a team shared access without setting permissions one person at a time.

### Technical vocabulary

- **Username:** Human-readable account name.
- **UID (User ID):** Numeric identity of a user.
- **Group:** Collection of users used for access control.
- **GID (Group ID):** Numeric identity of a group.
- **Primary group:** The main group associated with a user account.
- **Supplementary groups:** Additional groups whose permissions the user can receive.
- **Root:** The superuser account, conventionally UID 0.
- **sudo:** A mechanism that lets an authorised user run a command with another user's privileges, commonly root.
- **Least privilege:** Give an account only the access it needs, for only as long as it needs it.

### Inspect users and groups

```bash
whoami
id
id username
groups
groups username
cat /etc/passwd
cat /etc/group
```

A simplified `/etc/passwd` record:

```text
amit:x:1000:1000:Amit:/home/amit:/bin/bash
  |  |   |    |    |       |          |
  |  |   |    |    |       |          +-- login shell
  |  |   |    |    |       +------------- home directory
  |  |   |    |    +--------------------- comment / GECOS
  |  |   |    +-------------------------- primary GID
  |  |   +------------------------------- UID
  |  +----------------------------------- password placeholder
  +-------------------------------------- username
```

The `x` means password hashes are stored separately, commonly in `/etc/shadow`, which is restricted. Do not publish or casually edit password databases.

### Create a group and user (administrative lab only)

```bash
sudo groupadd developers
sudo useradd -m rahul
sudo passwd rahul
sudo usermod -aG developers rahul
id rahul
groups rahul
```

- `groupadd`: create a group.
- `useradd -m`: create a user and home directory.
- `passwd`: set or change a password.
- `usermod -aG`: append a supplementary group membership.
- `-a` means append. Omitting it with `-G` can replace existing supplementary group memberships.

Only run account-management commands in a lab where you understand the impact. WSL accounts and production server accounts may have different policies.

---

## 9. File permissions and ownership

### Three questions Linux asks

When a user tries to access a file, Linux evaluates identity and permissions. The traditional basic permission model distinguishes:

1. **Owner:** The user that owns the file.
2. **Group:** The file's assigned group.
3. **Others:** Everyone else.

Each category can have read, write and execute permissions.

### Permission letters

| Letter | Name | For a regular file | For a directory |
|---|---|---|---|
| `r` | Read | Read file contents | List directory entries (subject to traversal access) |
| `w` | Write | Modify file contents | Create, remove or rename entries (usually also needs execute/search) |
| `x` | Execute / search | Execute the file if it is a suitable executable | Traverse/search the directory |

A directory's `x` permission is not the same as running a program. It allows traversal/search through that directory.

### Decode ls -l

Example:

```text
-rwxr-xr-- 1 amit developers 1024 Nov 23 app.sh
|---|---|---|      |
 type owner group  owner/group metadata
```

The permission string is:

```text
- | rwx | r-x | r--
    owner group others
```

- First character `-`: regular file. `d` means directory; `l` means symbolic link.
- Owner: `rwx` = read, write, execute.
- Group: `r-x` = read and execute, not write.
- Others: `r--` = read only.

This exact example is numeric mode **754**, not 755.

### Numeric permissions

Values are added:

| Permission | Calculation | Value |
|---|---:|---:|
| `---` | 0 | 0 |
| `--x` | 1 | 1 |
| `-w-` | 2 | 2 |
| `-wx` | 2+1 | 3 |
| `r--` | 4 | 4 |
| `r-x` | 4+1 | 5 |
| `rw-` | 4+2 | 6 |
| `rwx` | 4+2+1 | 7 |

The three digits are owner, group and others:

- `chmod 755 app.sh` -> owner `rwx`, group `r-x`, others `r-x`.
- `chmod 644 config.yaml` -> owner `rw-`, group `r--`, others `r--`.

### chmod: change permissions

Numeric form:

```bash
chmod 755 app.sh
chmod 644 config.yaml
```

Symbolic form:

```bash
chmod u+x app.sh
chmod g-w app.sh
chmod o-r app.sh
```

- `u`: owner/user.
- `g`: group.
- `o`: others.
- `a`: all three classes.
- `+`: add permission.
- `-`: remove permission.
- `=`: set the specified permissions exactly.

### chown: change ownership

```bash
sudo chown amit:developers app.sh
sudo chown -R amit:developers project/
```

- `chown`: change owner.
- `amit:developers`: set owner to amit and group to developers.
- `-R`: recursive; apply through the directory tree.

### Why chmod 777 is usually a bad fix

`chmod -R 777 directory` grants read, write and execute/search to owner, group and others throughout the tree. It may make a symptom disappear while creating a serious security problem. Diagnose the required owner, group and minimum permissions instead.

---

## 10. Processes, PIDs and process states

### Explain it like you're five

A program is a recipe. A process is the cooking job currently being carried out using that recipe. You can have multiple processes running the same program.

### Technical vocabulary

- **Program:** A file or set of instructions stored on disk.
- **Process:** A running instance of a program.
- **PID:** Process ID, a unique identifier within the relevant PID namespace.
- **PPID:** Parent process ID.
- **Foreground process:** A job currently connected to and controlling the terminal.
- **Background process:** A job started without keeping the shell occupied in the same way.
- **Signal:** A notification sent to a process to request or control an action.
- **Zombie:** A process that has exited but whose parent has not yet collected its exit status.
- **Daemon/service:** A background process that provides a continuing system or application function.

### Inspect processes

```bash
ps
ps aux
ps -ef
top
ps aux | grep nginx
pgrep -a sleep
```

- `ps`: process snapshot for the current terminal context.
- `ps aux`: broad process listing with resource and user information.
- `ps -ef`: full-format process listing.
- `top`: live process and resource view.
- `pgrep`: find process IDs by name/pattern; `-a` includes the command line.

### Common process states

| State | Meaning |
|---|---|
| R | Running or runnable |
| S | Interruptible sleep |
| D | Uninterruptible sleep, often waiting on I/O |
| T | Stopped or traced |
| Z | Zombie: exited, awaiting parent reaping |

A zombie is not a normally executing process consuming CPU. A persistent zombie may indicate a parent-process handling problem.

### Background jobs

```bash
sleep 300 &
jobs
```

- `&` asks the shell to start the command as a background job.
- `jobs` lists jobs known to the current shell.

Other job controls:

- `Ctrl+Z`: suspend the foreground job.
- `bg`: resume a stopped job in the background.
- `fg`: bring a job to the foreground.
- `jobs`: show shell-managed jobs.

Shell jobs and operating-system processes are related but not identical concepts. `jobs` only shows jobs managed by the current shell.

### Signals and termination

```bash
kill PID
kill -TERM PID
kill -KILL PID
pkill -TERM -x process-name
```

- `kill PID` sends SIGTERM by default.
- **SIGTERM (15):** Requests graceful termination. The process can handle it and clean up.
- **SIGKILL (9):** Forces termination; the process cannot catch or handle it.
- **SIGSTOP:** Stops a process; it cannot be caught or ignored.
- `pkill`: sends a signal to processes selected by name/pattern.

Use SIGTERM first when appropriate. SIGKILL is a last resort because the process cannot perform normal cleanup. Verify the PID and process identity before signalling anything. Never copy a PID from stale output.

---

## 11. Services and systemd

### What is a service?

A service is a program that provides a continuing function, commonly running in the background. Examples include Nginx, SSH, Docker and PostgreSQL.

### What is systemd?

On many modern Linux distributions, **systemd** is the system and service manager. It commonly runs as PID 1 and starts or supervises system services, handles dependencies and integrates with system logging.

A **unit** is a resource managed by systemd. A service unit commonly ends in `.service`.

### systemctl commands

| Command | What it does |
|---|---|
| `systemctl status nginx` | Show service state and recent status details |
| `sudo systemctl start nginx` | Start it now |
| `sudo systemctl stop nginx` | Stop it now |
| `sudo systemctl restart nginx` | Stop and start it again |
| `sudo systemctl reload nginx` | Ask it to reload configuration if supported |
| `sudo systemctl enable nginx` | Configure automatic start at boot |
| `sudo systemctl disable nginx` | Remove automatic-start configuration |
| `systemctl is-active nginx` | Check whether it is active |
| `systemctl is-enabled nginx` | Check enablement state |

**Start vs enable:**

- `start` changes the current runtime state.
- `enable` configures startup behaviour for future boots.
- Enabling a service does not necessarily start it immediately.
- Disabling a service does not necessarily stop it immediately.

### Inspect services

```bash
systemctl list-units --type=service
systemctl list-units --type=service --state=running
systemctl list-unit-files --type=service
```

### journalctl: inspect systemd journal logs

```bash
sudo journalctl -u nginx
sudo journalctl -u nginx -n 50
sudo journalctl -u nginx -f
sudo journalctl -xeu nginx
```

- `-u nginx`: filter by unit.
- `-n 50`: show the last 50 entries.
- `-f`: follow new entries.
- `-x`: add explanatory help where available.
- `-e`: jump to the end of the journal.

### Troubleshooting flow

```text
Service not working
       |
       v
systemctl status SERVICE
       |
       v
Read the state, exit code and recent messages
       |
       v
journalctl -u SERVICE
       |
       v
Find evidence: bad config? port conflict? permissions?
missing dependency? unavailable resource?
       |
       v
Fix the root cause
       |
       v
Restart/reload if appropriate
       |
       v
Verify status AND application behaviour
```

Do not restart blindly. A restart can hide useful evidence or cause additional disruption.

### WSL note

WSL distributions may or may not have systemd enabled. Check before assuming:

```bash
ps -p 1 -o comm=
systemctl --version
```

If PID 1 is not systemd, systemctl service management may not behave like it does on a conventional Ubuntu server. Do not change WSL boot configuration just to complete a lesson; first inspect the environment.

---

## 12. Ubuntu package management: APT, packages and dependencies

### Explain it like you're five

A package is like a labelled box containing a prepared piece of software and information about it. A package manager is the shopkeeper who finds the box, checks what else is needed, installs it and keeps track of it.

### What is a package?

A **software package** is a structured, distributable unit containing software files and metadata used by a package-management system. Ubuntu commonly distributes packages in the Debian `.deb` format.

A package can include executables, libraries, configuration templates, documentation, service definitions and metadata. Not every package contains every type of file.

### What is a package manager?

A package manager helps discover, install, upgrade, configure and remove software while tracking package state and dependencies.

Key Ubuntu/Debian tools:

- **APT:** High-level package-management tool that uses configured repositories and resolves dependencies.
- **apt-get:** Traditional APT command-line interface, still widely used in scripts and automation.
- **dpkg:** Lower-level Debian package tool that installs, configures, queries and removes individual `.deb` packages.

### What is a dependency?

A **dependency** is another package or component that software requires to work correctly or to provide a particular feature.

Example:

```text
Application A
  |-- requires Library B
  |       |-- requires Runtime D
  |
  |-- requires Library C
```

- A is the package requested by the operator.
- B and C are direct dependencies of A.
- D is a transitive dependency of A because it is required by B.

A dependency can be a library, runtime, command-line utility or another package. A dependency is not necessarily a complete application.

### Why dependencies exist

Software reuses common capabilities instead of reimplementing everything. An application might rely on shared libraries for cryptography, database communication, image processing or system integration.

Package metadata declares relationships such as required dependencies and version constraints. APT uses that information to calculate what must be installed or changed.

### Repository

A **repository** is a configured software source that publishes package metadata and package files. APT refreshes local metadata from configured repositories so it can identify available package versions and download the required packages.

### What happens during apt install?

```text
sudo apt install nginx
       |
       v
APT reads local package indexes and configured sources
       |
       v
Finds candidate package and checks dependency metadata
       |
       v
Calculates packages and version changes required
       |
       v
Downloads required .deb archives
       |
       v
Uses dpkg to unpack/install packages
       |
       v
Runs package configuration steps
       |
       v
Reports result
```

The exact internal sequence can vary, but the key idea is that APT orchestrates repository access and dependency resolution while dpkg performs lower-level package operations.

### APT commands

| Goal | Command | Meaning |
|---|---|---|
| Refresh package indexes | `sudo apt update` | Download current repository metadata |
| Upgrade installed packages | `sudo apt upgrade` | Install available upgrades under normal upgrade rules |
| Search | `apt search nginx` | Search package metadata |
| Inspect package | `apt show nginx` | Show description, version, dependencies and metadata |
| Install | `sudo apt install nginx` | Install package and required dependencies |
| Remove | `sudo apt remove nginx` | Remove package binaries while generally retaining system-wide conffiles |
| Purge | `sudo apt purge nginx` | Remove package and package-managed system configuration files |
| Remove unused auto dependencies | `sudo apt autoremove` | Remove automatically installed packages no longer needed |
| List installed packages | `apt list --installed` | Show installed package records |
| List upgradable packages | `apt list --upgradable` | Show packages with available upgrades |
| Inspect dependencies | `apt-cache depends nginx` | Show dependency relationships |
| Inspect versions and sources | `apt-cache policy nginx` | Show installed/candidate versions and source priorities |

### apt update vs apt upgrade

This distinction is essential:

- `sudo apt update` refreshes the local package index. It does **not** itself upgrade installed software.
- `sudo apt upgrade` uses the refreshed metadata to upgrade installed packages where possible under its rules.

A common sequence is:

```bash
sudo apt update
sudo apt upgrade
```

Review the proposed package changes before confirming, especially on production servers.

### apt upgrade vs full-upgrade

- `apt upgrade` upgrades packages without removing installed packages to satisfy the upgrade.
- `apt full-upgrade` may install or remove packages when required to complete dependency changes.

Neither should be run on production without understanding the proposed changes and maintenance policy.

### apt remove vs purge

- `apt remove PACKAGE` removes the package but generally keeps system-wide configuration files managed as conffiles.
- `apt purge PACKAGE` also removes those package-managed configuration files.

Application data, user-created files and data outside package ownership may remain. Always inspect before assuming purge removes every trace of an application.

### APT vs dpkg

| Capability | APT | dpkg |
|---|---|---|
| Uses configured repositories | Yes | No |
| Downloads repository packages | Yes | No |
| Resolves dependencies from repositories | Yes | No automatic repository resolution |
| Installs local .deb packages | Yes, through dpkg | Yes |
| Low-level Debian package database operations | Coordinates them | Performs them |

Examples:

```bash
sudo apt install nginx
sudo dpkg -i ./example-app.deb
dpkg -l nginx
dpkg -L nginx
dpkg -S /path/to/file
```

If a local `.deb` installed using dpkg has missing dependencies, APT can help resolve repository-available dependencies after inspecting the error.

### Repair commands — understand before running

```bash
sudo dpkg --configure -a
sudo apt --fix-broken install
```

- `dpkg --configure -a` attempts to configure unpacked but not fully configured packages.
- `apt --fix-broken install` asks APT to attempt to repair broken dependency state.

These are recovery tools, not magic commands. Read the error and review the proposed actions first.

### Safe package inspection lab

Start with read-only inspection:

```bash
apt search nginx
apt show nginx
apt-cache depends nginx
apt-cache policy nginx
apt list --upgradable
apt list --installed | head -20
```

Only install software if you intend to practise the lifecycle and understand the environment:

```bash
sudo apt update
sudo apt install nginx
nginx -v
dpkg -l nginx
```

If systemd is available, inspect the service:

```bash
sudo systemctl status nginx
```

For a disposable lab, removal can be practised with `sudo apt remove nginx`. Do not automatically run purge or autoremove; inspect what they propose to remove first.

---

## 13. Operational troubleshooting patterns covered so far

### Find a process using too much CPU

```bash
top
ps aux
ps -ef
```

Identify the process, user, PID and command. Do not kill a process just because its CPU use is high; first establish whether it is expected work, a runaway process or a critical service.

### Find errors in an application log

```bash
tail -n 50 app.log
grep -n "ERROR" app.log
grep -i "timeout" app.log
tail -f app.log
```

Start with a relevant time window, search for error patterns, correlate nearby messages and follow new entries if needed.

### Diagnose a service that will not start

```bash
systemctl status SERVICE
journalctl -u SERVICE -n 50
```

Look for configuration errors, permission problems, port conflicts, missing dependencies and resource failures. Fix the cause and verify the service and the application path.

### Understand a permission-denied error

1. Confirm which user runs the process: `whoami`, `id`, or inspect the service configuration.
2. Inspect the file and parent directory permissions: `ls -l`.
3. Check owner and group.
4. Determine the minimum required access.
5. Correct ownership or permissions deliberately; do not default to 777.

### Understand an installation failure

1. Read the complete APT/dpkg error.
2. Check package availability: `apt-cache policy PACKAGE`.
3. Inspect dependencies: `apt-cache depends PACKAGE`.
4. Check repository metadata and configured sources.
5. Review the proposed repair before confirming.

---

## 14. Technical vocabulary glossary

| Term | Plain-language meaning |
|---|---|
| OS | Software that manages computer hardware and provides services to applications |
| Kernel | Privileged core of the operating system |
| Shell | Command interpreter that reads and launches commands |
| Terminal | Text interface used to interact with a shell |
| CLI | Command-line interface |
| GUI | Graphical user interface |
| Distribution | Complete operating-system package built around a kernel |
| Bootloader | Program that loads the operating-system kernel |
| Firmware | Low-level software that initialises hardware and begins boot |
| System call | A controlled request to the kernel |
| User space | Restricted execution area for ordinary programs |
| Root directory | Top of the Linux filesystem tree, written `/` |
| Home directory | A user's personal directory |
| Absolute path | Path that starts at filesystem root |
| Relative path | Path interpreted from the current directory |
| Mount | Attach a filesystem to a directory in the filesystem tree |
| Log | Recorded event or message useful for diagnosis and audit |
| Standard output | Normal output stream, conventionally file descriptor 1 |
| Standard error | Error output stream, conventionally file descriptor 2 |
| Pipe | Connect one command's output to another command's input |
| UID | Numeric user identity |
| GID | Numeric group identity |
| Root user | Superuser account, conventionally UID 0 |
| Least privilege | Grant only the minimum access needed |
| Permission | Rule controlling an operation on a file or directory |
| Ownership | User and group associated with a filesystem object |
| Process | Running instance of a program |
| PID | Process identifier |
| PPID | Parent process identifier |
| Signal | Notification delivered to a process |
| Zombie | Exited process whose parent has not collected its status |
| Daemon | Background process that provides a continuing service |
| Service unit | systemd unit describing a service |
| Journal | Structured log store managed by systemd-journald |
| Package | Structured software distribution unit |
| Package manager | Tool that installs, upgrades, tracks and removes packages |
| Repository | Configured source of package metadata and package files |
| Dependency | Another package/component required by software |
| Direct dependency | Dependency required directly by the package |
| Transitive dependency | Dependency required through another dependency |
| .deb | Debian package file format |
| APT | High-level Debian/Ubuntu package-management tool |
| dpkg | Low-level Debian package management tool |
| Conffile | Package-managed configuration file with special handling during upgrades/removal |

---

## 15. Command reference — covered so far

### Identity and environment

```bash
whoami
id
groups
uname -a
cat /etc/os-release
pwd
ps -p 1 -o comm=
```

### Navigation and file operations

```bash
ls
ls -lah
cd /path
cd ..
cd ~
mkdir -p path/to/dir
touch file
cp SOURCE DESTINATION
mv SOURCE DESTINATION
rm file
rmdir empty-dir
```

### Reading and searching

```bash
cat file
less file
head -n 10 file
tail -n 10 file
tail -f file
grep "pattern" file
grep -in "pattern" file
find . -name "*.log"
wc -l file
sort file
sort file | uniq -c
cut -d',' -f1 data.csv
```

### Processes and services

```bash
ps aux
ps -ef
top
pgrep -a NAME
jobs
sleep 30 &
fg
bg
kill PID
kill -TERM PID
kill -KILL PID
systemctl status SERVICE
sudo systemctl start SERVICE
sudo systemctl stop SERVICE
sudo systemctl restart SERVICE
sudo systemctl reload SERVICE
sudo systemctl enable SERVICE
sudo systemctl disable SERVICE
journalctl -u SERVICE
```

### Users, permissions and packages

```bash
whoami
id USER
groups USER
cat /etc/passwd
cat /etc/group
sudo groupadd GROUP
sudo useradd -m USER
sudo passwd USER
sudo usermod -aG GROUP USER
ls -l
chmod 755 FILE
chmod 644 FILE
chmod u+x FILE
sudo chown USER:GROUP FILE
apt search PACKAGE
apt show PACKAGE
apt-cache depends PACKAGE
apt-cache policy PACKAGE
sudo apt update
sudo apt upgrade
sudo apt install PACKAGE
sudo apt remove PACKAGE
sudo apt purge PACKAGE
sudo apt autoremove
dpkg -l PACKAGE
dpkg -L PACKAGE
```

---

## 16. What is not completed yet

This chapter deliberately stops at the topics covered so far. The following Linux topics remain for future lessons and must not be marked complete yet:

- Disk capacity, partitions, filesystems, inodes, mounts, `df`, `du`, `lsblk`, `blkid`.
- RAM, swap, virtual memory, OOM killer and deeper CPU/load analysis.
- Log rotation, syslog, persistent journaling, kernel messages and structured application logging.
- Networking: interfaces, IP addresses, routes, DNS, ports, sockets, HTTP/TLS, firewall and SSH.
- Bash scripting: variables, quoting, exit codes, conditions, loops, functions, arrays, traps and safe automation.
- Scheduling with cron and systemd timers.
- Advanced permissions: umask, ACLs, special permission bits and SELinux/AppArmor.
- Practical end-to-end labs, independent troubleshooting and interview validation.

**Exit standard:** Explain the concept, predict command behaviour, run it in a safe lab, interpret output, diagnose a failure and answer follow-up questions without relying on notes.
