<div class="by-collab">

My plan for IC151, the first-year C++ programming lab, assumed GitHub Classroom. Students would accept an
assignment link, get a repository, push their code, and the TAs would grade it. Then GitHub shut Classroom down,
and I built the replacement myself, with an AI coding agent, in the week just before the first lab.

</div>

<div class="by-ai">

## What went away

GitHub closed new sign-ups for Classroom on 26 May 2026
([GitHub changelog](https://github.blog/changelog/2026-05-26-github-classroom-sign-ups-are-no-longer-available)).
On 28 August 2026 it went further: "The GitHub Classroom website, APIs, and related services have now been
decommissioned"
([GitHub changelog](https://github.blog/changelog/2026-08-27-github-classroom-deprecated)). The same notice says
that accounts, repositories and organizations made for Classroom are not affected. So the parts worth keeping
were always plain GitHub: private repositories, organizations, teams. Classroom was a layer of convenience on top.
GitHub pointed teachers to its "selected partner solutions".

My course has about 530 students in eight lab batches of roughly 67, and a lab every week for each batch. The
course design document for the semester still says, in its list of first-lab steps, "accepting a GitHub Classroom
assignment". That line had to be replaced by something real before the first lab.

</div>

<div class="by-human">

## A race against the first lab

I started building this in the week just before the first lab. It was a race against time to get everything set
up properly, because of the sunset of GitHub Classroom, before the students began their first lab. There was a
lot of manual intervention in the first two weeks.

Mind you, there are students in the course at both extremes: people so proficient in coding that they do not
need this course, and people using a computer for the first time.

</div>

<div class="by-ai">

So the system had to work for both. The proficient students would find any gap in it. The new ones could not be
asked to do anything beyond the minimum: make a GitHub account, accept one email, open a link, push.

## The rules I started from

The agent works from an instruction file kept in a private admin repository for the course. Its
mission statement is blunt: use ordinary private repositories, and depend on no Classroom, no paid service, no
server, no custom web application and no special submission command. The workflow it fixes is short:

1. The instructor prepares one template repository per assignment, with starter files and a checking script
   that tests them.
2. A release command creates one private repository per student from the template, named
   after the assignment, the batch and the student's roll number.
3. Each student can push only to their own repository. The TAs can read them.
4. Students run the checking script, commit and push to the main branch. The pushed commit is the submission. There is no
   submit button.
5. At the deadline, a collector records the exact commit SHA on the main branch for every student, so a later push
   changes nothing.

## The design

The system has five parts, and none of them runs on a server of mine.

**The organization.** Everything lives in one GitHub organization with base permission set to none. A student
sees nothing in it by default.

**One secret team per student.** Each student's access lives in a team of their own. The rest of the design rests
on it, so the next section covers it in full.

**Templates and manifests.** Each assignment is a private template repository. Creating a batch makes one
repository per student from the template and writes a manifest (CSV and JSON) with every repository and its
initial commit SHA. The manifests are committed to the admin repository, so its Git history is also the audit log:
who got what, and when.

**Issues as the control panel.** TAs release, undo and report access problems through issues in
the admin repository. GitHub Actions does the work and answers in the issue. A later section describes how.

**A public portal.** A free GitHub Pages site turns an assignment and a roll number into a repository URL. It
holds no student data, and a student who is not allowed in simply gets GitHub's 404. GitHub permissions are the
only security boundary.

</div>

<div class="by-collab">

## Teams first: a release is a permission change

</div>

<div class="by-human">

I started by taking GitHub usernames from the students, but that did not work out well. Shifting to team-based
assignment worked out well. The main benefit was that students got an email to accept the invitation to join the
organization only once.

</div>

<div class="by-ai">

The usernames came from a form, as free text. On the first lab day only 25 students of the first batch had a username that
could be validated and given a repository. The problems included typos, logins that did not exist, second
accounts, roll numbers that were not on the roster, and "NA". Granting each repository to a username
would also have meant a separate invitation to accept for every assignment.

</div>

<div class="by-collab">

The idea that made the rest simple: create the teams once, at the start of the semester, and make every
release nothing more than attaching a repository made from the template to a student's team.

</div>

<div class="by-ai">

The day after the first lab, the agent created one team per active student, named after their batch and roll number.
The teams are `secret` on purpose. A `closed` team is visible to every member of the organization, which would
let more than 500 students list each other: the roster leak the instruction file forbids. A team for one person
sounds odd, but it gives each student a single, stable place where their access lives.

Then it invited every student by their institute email address, with one API call that
does two things: it sends the organization invitation and places the student in their team in advance. Email
beats GitHub usernames here. The institute issues the address, whereas a username is free text the student types
into a form, and a typo in an email bounces instead of reaching a stranger. GitHub caps organization invitations
at 50 per 24 hours for a new organization, so the script stops cleanly at the cap and resumes the next day
without inviting anyone twice. When a student accepts, their team holds the account they actually signed in
with, and the usernames are read back from the teams. The team, not a form, is the
authority on who the student is.

After that, a release is one API call per student: put the new repository on their team, with push access. There
is no invitation per repository, nothing to accept and no username to look up. Once a student has accepted the
first email, every later assignment simply appears on their GitHub page. Taking a release back is the same call
in reverse. When batch names were added to the team names partway through, renaming kept the team ids, so the
66 pending invitations for one batch followed the rename without being sent again.

</div>

<div class="by-human">

The learning curve for students was to start by making a GitHub account, then finding the organization, then
finding their team's list of accessible repositories, to see the assignment that is updated there.

</div>

<div class="by-ai">

The team page is the one link that works for a student all semester. Before a lab is released, the new
assignment is simply not on it yet; afterwards it appears in the same list as all the earlier ones. So the public portal, given a roll
number, links to the student's team page as well as to the one repository.

## Create early, attach late

Since attaching is the release, the slow part can happen days earlier. Creating 67 repositories from a template
is slow and, as it turned out, rationed (see below). Attaching them to teams is fast and unlimited. So the agent
pre-creates each batch: the repositories exist, but no team holds them, so no student can
reach them. At lab time the release only attaches, and a batch goes from invisible to available in under a minute.

</div>

<div class="by-collab">

## Four labs in one room

Students in a lab sit side by side, so in section B a batch does not get one assignment. It gets several
versions of the same lab, each with its own template, and the students are split into groups that each get one
version.

</div>

<div class="by-ai">

The first lab had three versions per section, a third of each batch on each. From the second lab every batch got
its own versions, and from the third lab, four per batch: sixteen templates for one week's lab in section B, and
more than 80 so far. The versions are parallel, not different in difficulty. Each asks for the same skills (a
function with a prototype, a recursive function with loops forbidden, a linked list) under a different story and
different numbers.

The split is random but reproducible. The batch's roll numbers are sorted, shuffled with a fixed seed, and dealt
out one version at a time, like cards. Dealing rather than cutting into blocks keeps the groups within one
student of each other, so a batch of 67 splits 17, 17, 17 and 16. The split is then written down and never
recomputed: once a repository exists, a reshuffle would hand a student a different lab from the one they have
started.

Teams make the rest easy. A release for such a lab names one assignment and one batch, as before. For each
student it looks up their version, creates their repository from that version's template, and attaches it to
their team. The repository name carries the assignment, the batch and the roll number, but not the version, so
neighbours cannot tell from their URLs who has which. The TAs see the version in the release manifest.

Which batches share material is also deliberate. Two batches that meet on the same day share nothing, since
students talk between labs. A batch later in the week may reuse the computations of an earlier one under new
stories. Before each batch's lab the instructor checks how far the lectures have actually got, because batches
meet on different days: in one week, one batch met before linked lists were taught and the other three after.

Writing sixteen versions by hand every week is where errors creep in, so the section-B labs are generated. A
generator writes the questions, the starters and the tests, and checks every expected output against two
independent references, one in Python and one in C++. The generator and the reference solutions stay in the
private admin repository and never go into a template.

## Who presses the button: issues and labels

At first, TAs opened release issues themselves from an issue form: type the assignment id, pick the batch,
submit. GitHub Actions replies with a dry run as a comment; adding the `go` label, or replying `/apply`,
releases for real. The commit that added the label explains why: "Adding the 'go' label is two taps in the
GitHub app; typing /apply is not something you want to do one-handed." Since the admin repository is private, only
staff can open or comment on its issues, so the repository's own access list is the authorization check.

That order turned out to be wrong. If a TA opens the issue before the repositories exist, `go` does not just
attach: it creates all 67 in the middle of the lab, which is exactly when creation is slow and may be blocked.
The rule since 19 August: the issue is the signal that a batch is ready, so it is opened only after the batch
is pre-created. Now the sequence is:

1. Pre-create the batch and check the manifest: every repository created, every initial SHA
   present, every repository private.
2. Commit the manifest and the course configuration, and push. The workflow validates the issue against the main
   branch on GitHub, so an issue opened before the push fails with "Unknown assignment".
3. Open the issue, titled with the assignment and the batch, with only the release label. Its body says the
   repositories are created but not yet attached, gives the manifest path, a summary of the questions, the C++17
   build command and a link to the template.
4. Assign it to that batch's TA, looked up in a table every time. Copying the assignee from the previous issue
   once sent a section-B batch to a section-A TA.
5. Wait for the bot's dry run, which should show every student's repository ready to attach.
6. The TA adds `go` when the lab starts. The bot attaches the batch, commits the manifest and closes the loop
   in the issue.

Issue-triggered runs are quick. Over 127 non-skipped release runs, the median time from the event to a finished
run is 26 seconds, and the 90th percentile is 37. One early bug was in the workflow itself: all runs shared one
concurrency group, so opening several release issues at once left only the newest dry run alive and silently
cancelled the rest. Dry runs now get a group per issue.

An undo issue works the same way and detaches the repositories again. It deletes nothing, and it reports who
had already pushed.

## Why the timer did not work

The obvious improvement over a TA's thumb is a timer: list each assignment, batch and release time in a schedule file and
let GitHub Actions release each batch at its lab time, with nobody's laptop awake. The agent built exactly that
on 8 August. A cron workflow ran every 20 minutes, at minutes 7, 27 and 47 past the hour; when a row was due
within 25 minutes, the runner claimed it and waited inside the job for the exact second. Cron only had to be
early, not exact.

Even the cron line carries scars. It sits off the hour boundary because GitHub's documentation names the
start of every hour as a peak for scheduled runs and says queued jobs may be dropped. It polls only from 07:30
to 21:30 IST because Actions bills every job as at least one minute: polling around the clock would have spent
about 2,880 of the 3,000 monthly minutes doing nothing, against about 1,260 for the teaching day.

On 8 August the timer did its job. Helloworld for B4 was attached at 13:30:11 for a 13:30 lab. The second row,
variables for B4 at 14:00, was released by hand a minute early, and the runner already waiting for it attached
the same repositories again at 14:00:12, harmlessly, because a release is idempotent.

The run history over the next ten days shows why it could not be trusted. From 8 to 18 August the workflow ran
309 times. A full teaching day should give 42 runs. On weekdays it got between 22 and 25, so roughly half the
scheduled runs never happened. On the weekend of 15 and 16 August, with less load on GitHub, it got 41 and 40.
The time between consecutive runs had a median of 23 minutes, but 123 of 295 gaps were longer than the 25-minute
lead, and the longest was 53 minutes. A lab time that fell into such a gap had no run waiting for it, so the
release would have gone out on the next run, up to half an hour late. For a lab of 67 students, half an hour late
is a failed lab.

So the timer was not used again. Two days after it was built, the `go` label arrived, and the schedule file has
held no rows since 8 August. The workflow kept polling an empty schedule until it was disabled after its last run
on 18 August. The instruction file now says it outright: GitHub Actions scheduled workflows are not exact enough
for a lab, and the release belongs to a person pressing `go`.

## The limit nobody reports

The other hard lesson came on 18 August, during an A2 lab. GitHub has a secondary rate limit on content
creation. It is separate from the hourly quota, GitHub's rate-limit report does not show it, it applies to the whole
organization, and creating a repository from a template counts heavily against it. We hit it mid-lab. Ten
students had no repository until the block lifted, and one was made by hand on the website.

The rules now in the instruction file: one creating process at a time, never a shell loop over batches, at most
one batch per hour, two workers with a three-second pause, and pre-creation days ahead, never during a lab.
However, permission changes are not throttled. Attaching existing repositories, or giving students read access
to the template, still works when creation is blocked.

## A runbook that remembers

The agent starts every session with no memory, so the instruction file carries a weekly runbook, and every
mistake goes into it the day it happens. It records instructor zip files that arrived with another lab's
checking script, an old solution shipped as a starter, a release issue assigned to the wrong batch's TA, and an issue
opened before its configuration was pushed. The latest entry is from today: an A2 lab released directly 23
minutes before it started, then taken back so the TA could release it. The rule it produced is that if more
than 20 minutes remain before a lab, the TA releases it through an issue.

By 27 October the repository has 190 commits, about 3,100 lines of Python that call the GitHub CLI, and about
4,900 student repositories across 40 assignments. None of the pieces is clever. Private repositories, teams, a
template, an issue and a label do what Classroom did, for free, and the rules that make them safe are written
down where the next session will read them.

</div>

<details class="original">
<summary>Original input</summary>

<p class="note">Lightly edited for coherence: capitalization and punctuation fixed. The first request pointed to the author's old posts on X about the topic; those could not be read, so the post draws on GitHub's changelogs, the course design document, the history of the course's admin repository and its GitHub Actions run history instead.</p>

<div class="by-human">

**Request for this post.** See the blog repo and write a blog post about how this system of assignment management is built due to the death of GitHub Education. See my old tweets about it too.

**Added later.** Write about the system design, issue creation and assignment, why the auto-release schedule was not working due to delays in GitHub workflows, and things like that.

**Added later.** Also write about how I created the teams, and that the release is essentially attaching template repos to teams.

**Added later.** I started building this in the week just before the first lab; it was a race against time to make everything set up properly, due to the sunset of GitHub Classroom, before the students began their first lab. There was a lot of manual intervention involved in the first two weeks. I started with taking GitHub usernames from students, but that didn't work out well, thus shifting to team-based assignment worked out well. The main benefit was sending emails to students to accept the invitation to join the org only once. Mind you that there are students in the course who are on both extremes: people super proficient in coding to not needing to do this course, and people using a computer for the first time.

**Added later.** The learning curve for students was to start with making a GitHub account, then finding the org, then finding their team's accessible repo list to see the assignment that is updated on that.

**Added later.** No need to write file or script name details. Write about how the students are split into groups, and multiple templates are created and assigned to different students in the same batch.

</div>
</details>
