# AOOT - automatic opening of tokens
A playground project that applies clean architecture and domain-driven design (DDD) to an automatic opening of tokens on a crypto exchange.

---

## Tech Stack
| Tool | Role |
|------|------|
| **Taskiq** | Async task queue & scheduler |
| **PostgreSQL** | Primary relational storage |
| **Dishka** | IoC container |
| **Sqlalchemy** | ORM | 
| **Pytest** | Testing | 

---

## Architecture

The project follows **DDD** with a 3‑layer layout:

| Layer | Eric Evans’ original description\* |
|-------|------------------------------------|
| **Application** | “**Defines the jobs the software is supposed to do and directs the expressive domain objects to work out problems.** … *This layer is kept thin.* It does not contain business rules or knowledge, but only coordinates tasks and delegates work to collaborations of domain objects in the next layer down.”  |
| **Domain / Model** | “**Responsible for representing concepts of the business, information about the business situation, and business rules.** State that reflects the business situation is controlled and used here, even though the technical details of storing it are delegated to the infrastructure. *This layer is the heart of business software.*” |
| **Infrastructure** | “**Provide generic technical capabilities that support the higher layers:** message sending for the application, persistence for the domain, etc.” |
