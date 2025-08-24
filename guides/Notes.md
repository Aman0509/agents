# Notes

- [Introduction](#introduction)
  - [What is AI Agents?](#what-is-ai-agents)
  - [What is Agentic AI?](#what-is-agentic-ai)
  - [What are Workflows?](#what-is-workflow)
- [AI APIs & Ollama](#ai-apis--ollama)

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
