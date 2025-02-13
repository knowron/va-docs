# Roles and Permissions

!!! tip "Need more options? Talk to us!"

    ASMPT Virtual Assist's system is designed for maximum modularity for enterprise customers. If you need other roles or a different set of permissions, please let us know - simply contact [us](https://smt.asmpt.com/en/products/software-solutions/virtual-assist).

ASMPT Virtual Assist allows you to choose what features and what access each individual user gets. Some users, such as younger colleagues, will be mostly **consuming** information, while more experienced ones will be **creating and curating** a lot of it.

Every user has a **role**. This role determines what actions they can take and even what features they have access to. Users can currently have one of three roles: 

- [Admin](#admin)
- [Editor](#editor)
- [Contributor](#contributor)
- [Viewer](#viewer)

For every system component, we have **permissions** that determine whether a role can execute a given action. Every one of the roles listed above will have a unique combinations of permissions. See below for more information on each of the roles.

## Roles

### Admin

Admins are **system administrators**. They are often service or engineering managers that are interested in their colleagues doing the best work possible in the most efficient way possible. 

They can read and write everything in the system and can make decisions about what other users can see.

!!! warning "With great power comes great responsibility"

    Admins have access to all the components and potentially sensitive data. Make sure you trust the person you make an admin!


|                       | Create | Edit | Delete | View |
|-----------------------|--------|------|--------|------|
| **Insights Dashboard**    |✅|✅|✅|✅|
| **Search**                |➖|➖|➖|✅|
| **Articles**              |✅|✅|✅|✅|
| **Tutorials**             |✅|✅|✅|✅|
| **Documents**             |✅|✅|✅|✅|
| **Expert Answers**        |✅|✅|✅|✅|
| **Product Lines**         |✅|✅|✅|✅|
| **Machine Inventory**     |✅|✅|✅|✅|
| **Logbook**               |✅|✅|✅|✅|
| **Users**                 |✅|✅|✅|✅|


### Editor

Editors are **content managers**. They are often more first-level support engineers experienced field service engineers that can provide a lot of value with their expertise. They are interested in making sure that their colleagues get the right information at the right time 

They can create, edit and read all **content units** (tutorials, documents and product lines). They can also create feedback loops to make search better.

Editors are **not** entitled to change global settings, or invite other colleagues onto the platform. They also cannot change any other users' settings.


|                       | Create | Edit | Delete | View |
|-----------------------|--------|------|--------|------|
| **Insights Dashboard**    |✅|✅|✅|✅|
| **Search**                |➖|➖|➖|✅|
| **Articles**              |✅|✅|✅|✅|
| **Tutorials**             |✅|✅|✅|✅|
| **Documents**             |✅|✅|✅|✅|
| **Expert Answers**        |✅|✅|✅|✅|
| **Product Lines**         |❌|✅|❌|✅|
| **Machine Inventory**     |✅|✅|✅|✅|
| **Logbook**               |✅|✅|✅|✅|
| **Users**                 |❌|❌|❌|❌|


### Contributor

Contributors are viewer users with **advanced access rights for contetn creation**. They are often production line workers who can upload new tutorial or article drafts which have to be validated by an editor or admin. Only then are these drafts published. 

|                       | Create | Edit | Delete | View |
|-----------------------|--------|------|--------|------|
| **Insights Dashboard**    |❌|❌|❌|❌|
| **Search**                |➖|➖|➖|✅|
| **Articles**              |🟧 (only drafts)|🟧 (only drafts & if owner)|🟧 (only drafts & if owner)|✅|
| **Tutorials**             |🟧 (only drafts)|🟧 (only drafts & if owner)|🟧 (only drafts & if owner)|✅|
| **Documents**             |❌|❌|❌|✅|
| **Expert Answers**        |❌|❌|❌|✅|
| **Product Lines**         |❌|❌|❌|✅|
| **Machine Inventory**     |❌|❌|❌|✅|
| **Logbook**               |✅|✅ (if owner)|✅ (if owner)|✅|
| **Users**                 |❌|❌|❌|❌|



### Viewer

Viewers are **normal users**. They are the bulk of ASMPT Virtual Assist's user base. They are often service engineer and field technicians that need access to information fast. They don't always have the time or the expertise to create or change content, so they are not allowed to.

They can see all **content units** (tutorials, documents and product lines) as well as, of course, search.



|                       | Create | Edit | Delete | View |
|-----------------------|--------|------|--------|------|
| **Insights Dashboard**    |❌|❌|❌|❌|
| **Search**                |➖|➖|➖|✅|
| **Articles**              |❌|❌|❌|✅|
| **Tutorials**             |❌|❌|❌|✅|
| **Documents**             |❌|❌|❌|✅|
| **Expert Answers**        |❌|❌|❌|✅|
| **Product Lines**         |❌|❌|❌|✅|
| **Machine Inventory**     |❌|❌|❌|✅|
| **Logbook**               |✅|✅ (if owner)|✅ (if owner)|✅|
| **Users**                 |❌|❌|❌|❌|



## How to change a users' role

!!! warning "Only Admins can execute this action"

    By default, only admins can change other users' roles. If you are not an admin and require a role change, please contact your manager.

<p align="center"><img src="https://i.imgur.com/CdsfoEC.gif" width="100%"></p>