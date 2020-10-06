# Version Control With Git

This section is a (very) brief and conceptual introduction to the Git version control system. There are many excellent tutorials available for free, of which the following two are independent from the main tool vendors such as Github or Atlassian:

[githowto.com](https://githowto.com/) is a practical hands-on guided tour, while

[Git from the bottom up](https://jwiegley.github.io/git-from-the-bottom-up) provides a more technical explanation of the operation of Git.

## Working Tree, Index, Repository

Git is using three main components to track a project's version history, which all are on the same _local file system_:

The __Working Tree__ is a directory on the local file system that is associated with a _repository_. Snapshots of the state of this working tree are added to the repository using _commits_.

The __Index__ (a.k.a. "Staging Area") contains a snapshot of the working tree before it is definitely added to the official history in the form of a commit. The index is used to interactively compile/curate changes in the working tree into coherent commits.

The __Repository__ contains a tree of commits that represents all the historic snapshots of the working tree. Each commit has a _parent_, which enables a complete lineage of changes back to the project's origin.

Each of these components represents a tree, and the repository can be seen as a tree of trees.

## Commits and References

A __Commit__ contains a snapshot of the working tree and is identified by a SHA1 hash of its contents. When adding the first commit to a repository, the special reference `HEAD` is pointed to this commit. Whenever a new commit is added, the existing commit pointed to by `HEAD` becomes its _parent_ in the tree, and the `HEAD` pointer is advanced to the new commit. There are various Git commands (`reset`, `checkout`) to assign the commit pointed to by `HEAD`.

A __Branch__ is nothing but a custom label that is added to a commit. If `HEAD` points to the same commit as this branch label, we're "on" that branch, and any commits made at this point will progress the branch label together with the `HEAD` reference. Separate branches of developement can be merged using the `merge` or `rebase` commands.

## Syncing Repositories

- Centralized vs. Distributed

## Do's & Dont's

- Always check status
- Always add interactively (`-p`)
- Always add with the intent to commit immediately afterwards
- Create commits with a single purpose
- Commit messages should mainly describe _why_ the change happened
- Commit often, push with caution
- When working on a branch, regularly merge upstream changes to master
- Be consistent with your colleagues re. workflow
- For notebooks: restart kernel (and clear all outputs), save, before adding changes

For easy collaboration:

- Don't commit any code with hardcoded file paths or other configurable items
- Don't add configuration files that are specific for your local development environment
- Don't add (generated) metadata such as compiled code
- Use .gitignore to prevent accidental addition of some of the above

Since a repo contains the whole history of _changes_, and deleting a file doesn't delete it from history:

- Be very cautious adding (potentially sensitive) data
- Never, ever, add passwords, connection strings to databases, etc
