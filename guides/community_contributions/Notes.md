# Notes

- [Introduction](#introduction)
  - [What is AI Agents?](#what-is-ai-agents)
  - [What is Agentic AI?](#what-is-agentic-ai)
  - [What are Workflows?](#what-is-workflow)
- [AI APIs & Ollama](#ai-apis--ollama)
- [Workflow Design Patterns](#workflow-design-patterns)
  - [Prompt Chaining](#1-prompt-chaining)
  - [Routing](#routing)
  - [Parallelization](#parallelization)
  - [Orchestrator-Workers](#orchestrator-workers)
  - [Evaluator-Optimizer (or Reflection Pattern)](#evaluator-optimizer-or-reflection-pattern)
  - [Tool Use Pattern](#tool-use-pattern)
  - [Multi-Agent Collaboration](#multi-agent-collaboration)
  - [Lab: Multi Model Orchestration - Creating a system to evaluate AI responses](#lab-multi-model-orchestration---creating-a-system-to-evaluate-ai-responses)
- [Agentic AI Frameworks](#agentic-ai-frameworks)

## Introduction

### What is AI Agents?

An agent in AI is any system that can perceive its environment, reason about it, and take actions to achieve a goal.

or

AI Agents are programs where LLM outputs control the workflow.

In simple terms, an agent is like a software (or robot) that can:

- **Sense/observe** → Get inputs from the environment (e.g., user query, sensor data).
- **Think/plan** → Use reasoning or models to decide what to do next.
- **Act** → Perform actions that affect the environment (e.g., sending an API request, controlling a robot arm).

Formally:

```
Agent = Perception → Reasoning → Action → Feedback → Repeat
```

> Note: LLM ≠ AI Agent

An LLM (Large Language Model) like GPT-4 or Claude is just the "brain" - it's great at understanding and generating text, but by itself it can't take actions in the real world.

An AI Agent uses an LLM as its brain, but also has "hands and feet" to actually do things.

Think of it like this:

**LLM alone:**

- Like a very smart person who can only talk
- Can answer questions, write emails, explain concepts
- But cannot send the email, book flights, or control devices

**AI Agent:**

- Like that same smart person who can also take actions
- Uses the LLM to understand and plan
- Plus has tools to actually execute tasks

### What is Agentic AI?

Agentic AI goes beyond traditional static AI (like a single ChatGPT query-response). It refers to AI systems that act as autonomous agents, meaning they can:

- Take initiative instead of just reacting to prompts.
- Break down tasks into subtasks and execute them.
- Use tools and APIs (e.g., call a weather API, run Python code).
- Remember context over time (short-term and long-term memory).
- Plan multi-step strategies to solve complex goals.
- Collaborate with humans or other agents (multiple LLMs).
- Autonomy

In short: Agentic AI = LLM (like GPT) + memory + reasoning + tools + autonomy.

> Are "AI Agents" and "Agentic AI" the same?  
> They’re closely related, but not exactly the same.  
> Think of it like this:
>
> - AI Agent = the thing itself (the software/robot/assistant that acts).
> - Agentic AI = the capability (the idea of AI having agency — i.e., being autonomous, proactive, and able to act).
>
> So, AI Agents are the entities, while Agentic AI is the concept/approach that powers them.

### What is Workflow?

A workflow is basically a predefined sequence of steps or tasks that an agent (or a set of agents) follows to get something done.

Instead of the agent acting completely “free-form” every time, workflows give structure and repeatability.

So, **Workflows = playbooks for agents**. They don’t replace autonomy, but they give a framework in which autonomy can be applied.

**Example**

**Task:** "Order lunch for the office"
**Workflow steps:**

- Ask how many people need lunch
- Check dietary restrictions
- Search for nearby restaurants
- Compare prices and reviews
- Choose restaurant and menu items
- Place the order
- Confirm delivery time
- Send confirmation to team

**Without workflow:** The agent might do things randomly - maybe place an order before checking how many people, or forget to ask about allergies.

**With workflow:** The agent follows the logical sequence, ensuring nothing is missed and tasks are done in the right order.

Readings:

- [Building effective agents](http://anthropic.com/engineering/building-effective-agents)
- [What Are Agentic Workflows? Patterns, Use Cases, Examples, and More](https://weaviate.io/blog/what-are-agentic-workflows)

## AI APIs & Ollama

Ollama

- [Learn Ollama in 15 Minutes - Run LLM Models Locally for FREE](https://www.youtube.com/watch?v=UtSSMs6ObqY)

Openrouter

- [How to Use OpenRouter: Access Free AI Models & API Keys](https://www.youtube.com/watch?v=a_mpaNqgrGM)

How to choose LLMs: A Developer's guide to LLMs

- [How to choose LLMs: A Developer's guide to LLMs](https://www.youtube.com/watch?v=pYax2rupKEY)

## Workflow Design Patterns

![Workflow Design Patterns](../assets/workflows_design_patterns.png)

### Prompt Chaining

Decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one

**Example:**

- Generate marketing copy → Check if it meets brand guidelines → Translate to different language → Format for social media
- Like an assembly line where each worker adds something to the product

### Routing

Classifies an input and directs it to a specialized followup task. Here, LLM handles the routing.

**Example:**

- Customer query comes in → AI determines if it's "billing," "technical," or "general" → Routes to specialized agent
- Like a hospital receptionist directing patients to the right department

### Parallelization

LLMs can sometimes work simultaneously on a task and have their outputs aggregated **_programmatically_**. This workflow, parallelization, manifests in two key variations:

- Sectioning: Breaking a task into independent subtasks run in parallel.
- Voting: Running the same task multiple times to get diverse outputs.

As mentioned in above image, the coordinator and aggregator are the programs (may be Python or other) which initiates parallelization and process (aggregate) the result respetively.

**Example:**

- Sectioning: Review contract → One agent checks legal terms, another checks financials, third checks dates (all at once)
- Voting: Three agents independently review code for security issues, majority vote decides

### Orchestrator-Workers

A central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results.

As mentioned in above image, orchestrator and synthesizer are your LLMs

**Example:**

- Build a website → Orchestrator decides: "Need designer for layout, developer for code writer for content" → Assigns each worker → Combines results
- Like a project manager delegating to team members

### Evaluator-Optimizer (or Reflection Pattern)

One LLM generates a response while another provides evaluation and feedback in a loop.

**Example:**

- Writer agent creates article → Critic agent reviews and suggests improvements → Writer revises → Repeat until quality threshold met
- Like having a writer and editor working together

### Tool Use Pattern

```mermaid
flowchart TD
    A[User Request] --> B[AI Agent Receives Task]
    B --> C{Analyze Task Requirements}

    C --> D[Identify Needed Tools]
    D --> E{Tool Available?}

    E -->|No| F[Report Missing Tool/Error]
    E -->|Yes| G[Select Appropriate Tool]

    G --> H[Prepare Tool Parameters]
    H --> I[Execute Tool Call]
    I --> J[Receive Tool Response]

    J --> K{Tool Call Successful?}

    K -->|No| L[Handle Error/Retry]
    L --> M{Retry Possible?}
    M -->|Yes| H
    M -->|No| N[Report Tool Failure]

    K -->|Yes| O[Process Tool Results]
    O --> P{Task Complete?}

    P -->|No| Q{Need Additional Tools?}
    Q -->|Yes| D
    Q -->|No| R[Continue with Current Data]

    P -->|Yes| S[Compile Final Response]
    R --> S

    S --> T[Return Results to User]

    F --> U[End - Error State]
    N --> U
    T --> V[End - Success]

    style A fill:#e1f5fe,color:#0d47a1
    style T fill:#c8e6c9,color:#1b5e20
    style U fill:#ffcdd2,color:#b71c1c
    style V fill:#c8e6c9,color:#1b5e20
    style C fill:#fff3e0,color:#e65100
    style E fill:#fff3e0,color:#e65100
    style K fill:#fff3e0,color:#e65100
    style P fill:#fff3e0,color:#e65100
    style Q fill:#fff3e0,color:#e65100
    style M fill:#fff3e0,color:#e65100
```

Agents access external tools and APIs to accomplish tasks.

**Example:**

- Research agent uses Google search → Wikipedia lookup → PDF reader → Database query → Email tool to send findings

### Multi-Agent Collaboration

```mermaid
flowchart TD
    A[User Request] --> B[Coordinator Agent]
    B --> C{Analyze Task Complexity}

    C -->|Simple Task| D[Single Agent Assignment]
    C -->|Complex Task| E[Multi-Agent Required]

    E --> F[Task Decomposition]
    F --> G[Identify Required Expertise]
    G --> H[Select Specialized Agents]

    H --> I[Agent 1<br/>Research/Data]
    H --> J[Agent 2<br/>Analysis/Logic]
    H --> K[Agent 3<br/>Creation/Output]
    H --> L[Agent N<br/>Review/QA]

    I --> M[Execute Task 1]
    J --> N[Execute Task 2]
    K --> O[Execute Task 3]
    L --> P[Execute Task N]

    M --> Q{Task 1 Complete?}
    N --> R{Task 2 Complete?}
    O --> S{Task 3 Complete?}
    P --> T{Task N Complete?}

    Q -->|No| U[Agent 1 Retry/Refine]
    R -->|No| V[Agent 2 Retry/Refine]
    S -->|No| W[Agent 3 Retry/Refine]
    T -->|No| X[Agent N Retry/Refine]

    U --> M
    V --> N
    W --> O
    X --> P

    Q -->|Yes| Y[Result 1]
    R -->|Yes| Z[Result 2]
    S -->|Yes| AA[Result 3]
    T -->|Yes| BB[Result N]

    Y --> CC[Coordinator Agent<br/>Result Integration]
    Z --> CC
    AA --> CC
    BB --> CC

    CC --> DD{Integration Successful?}
    DD -->|No| EE[Request Agent Revisions]
    DD -->|Yes| FF[Quality Check]

    EE --> GG{Which Agents Need Revision?}
    GG --> I
    GG --> J
    GG --> K
    GG --> L

    FF --> HH{Quality Meets Standards?}
    HH -->|No| II[Coordinator Refinement]
    HH -->|Yes| JJ[Final Output Assembly]

    II --> CC
    JJ --> KK[Deliver to User]

    D --> LL[Single Agent Execution]
    LL --> MM{Task Complete?}
    MM -->|No| NN[Agent Retry]
    MM -->|Yes| JJ
    NN --> LL

    KK --> OO[End - Success]

    style A fill:#e1f5fe,color:#0d47a1
    style B fill:#f3e5f5,color:#4a148c
    style CC fill:#f3e5f5,color:#4a148c
    style I fill:#e8f5e8,color:#1b5e20
    style J fill:#fff3e0,color:#e65100
    style K fill:#e3f2fd,color:#0d47a1
    style L fill:#fce4ec,color:#880e4f
    style KK fill:#c8e6c9,color:#1b5e20
    style OO fill:#c8e6c9,color:#1b5e20
    style C fill:#fff3e0,color:#e65100
    style DD fill:#fff3e0,color:#e65100
    style HH fill:#fff3e0,color:#e65100
    style Q fill:#fff3e0,color:#e65100
    style R fill:#fff3e0,color:#e65100
    style S fill:#fff3e0,color:#e65100
    style T fill:#fff3e0,color:#e65100
```

Different specialized agents work together on complex tasks.

**Example:**

- Sales process: Lead qualifier agent → Demo scheduler agent → Proposal writer agent → Follow-up agent

Readings:

- [Building effective agents](http://anthropic.com/engineering/building-effective-agents)
- [7 Practical Design Patterns for Agentic Systems](https://www.mongodb.com/resources/basics/artificial-intelligence/agentic-systems)
- [Zero to One: Learning Agentic Patterns](https://www.philschmid.de/agentic-pattern)

### Lab: Multi Model Orchestration - Creating a system to evaluate AI responses

[LLM Contest](./code/001-week-1/002-llm-contest.py)

## Agentic AI Frameworks

### What Are Agentic AI Frameworks?

Frameworks that provide glue/abstraction code to simplify interacting with LLMs, letting developers focus on business problems rather than low-level API details. The landscape is large and evolving rapidly.

### Framework Complexity Hierarchy

#### Level 1 — No Framework (Direct API)

- Connect directly to LLMs via their APIs
- Full control over prompts and orchestration
- You see exactly what's happening under the hood
- **Anthropic's recommendation**: Their blog post _"Building Effective Agents"_ makes a compelling case for always going direct

##### MCP (Model Context Protocol)

- Created by Anthropic; grouped with "no framework" because it's a **protocol, not a framework**
- Open source standard for connecting models to data sources and tools
- No glue code needed — just conform to the protocol
- Enables elegant, vendor-agnostic stitching of models and providers

#### Level 2 — Lightweight Frameworks

| Framework             | Notes                                                                                                    |
| --------------------- | -------------------------------------------------------------------------------------------------------- |
| **OpenAI Agents SDK** | Very new, lightweight, clean, flexible. API still evolving rapidly.                                      |
| **CrewAI**            | Slightly more mature, easy to use, low-code/YAML-driven configuration, slightly heavier than OpenAI SDK. |

Both frameworks stay out of the way — you still feel like you're just working with LLMs.

#### Level 3 — Heavyweight Frameworks

| Framework     | Notes                                                                                                    |
| ------------- | -------------------------------------------------------------------------------------------------------- |
| **LangGraph** | From the LangChain team. Models agents as a computational graph. Very powerful but steep learning curve. |
| **AutoGen**   | From Microsoft. Also relatively heavy; encompasses multiple concepts/modes.                              |

With these, the **framework ecosystem takes over the project** — it becomes a "LangGraph project" more than an "agentic AI project." Greater power, but greater buy-in required.

### Choosing a Framework

Picking the right framework depends on:

- **Use case** — different platforms suit different business objectives
- **Personal/team preference** — comfort with abstractions and ecosystems
- **Trade-off appetite** — simplicity & flexibility vs. power & structure
